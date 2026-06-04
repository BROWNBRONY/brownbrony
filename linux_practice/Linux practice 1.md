```bash
w

```

```text
 09:39:57 up 2 days,  1:10,  2 users,  load average: 0.25, 0.29, 0.13
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
brown    pts/0    10.0.2.2         Sat09    0.00s  3.16s   ?    w
brown    tty1     -                Sat08    2days  0.19s  0.19s -bash
```

# 注释：


up 2 days, 1:10	运行时间 (系统已连续运行2天1小时10分钟)
 TTY终端类型 (Teletypewriter / 进程关联的控制终端)
FROM来源 IP 地址 (用户连接到此服务器的客户端主机 IP)

LOGIN@	登录时间 (用户会话建立的初始时间)
IDLE	空闲时间 (用户自上一次与终端交互以来的停顿时间)
JCPU / PCPU	核心 CPU 耗时 (Job CPU: 该终端所有进程耗时 / Process CPU: 当前 WHAT 进程耗时)
WHAT	当前执行命令 (用户当前正在运行的进程或命令) 

```bash 
ip a
```

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 08:00:27:ad:53:70 brd ff:ff:ff:ff:ff:ff
    altname enx080027ad5370
    inet 10.0.2.15/24 metric 100 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 75403sec preferred_lft 75403sec
    inet6 fd17:625c:f037:2:a00:27ff:fead:5370/64 scope global dynamic mngtmpaddr noprefixroute
       valid_lft 86294sec preferred_lft 14294sec
    inet6 fe80::a00:27ff:fead:5370/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever
3: tailscale0: <POINTOPOINT,MULTICAST,NOARP,UP,LOWER_UP> mtu 1280 qdisc fq_codel state UNKNOWN group default qlen 500
    link/none
    inet 100.117.183.100/32 scope global tailscale0
       valid_lft forever preferred_lft forever
    inet6 fd7a:115c:a1e0::9338:b764/128 scope global
       valid_lft forever preferred_lft forever
    inet6 fe80::402d:73be:e3f1:6671/64 scope link stable-privacy proto kernel_ll
       valid_lft forever preferred_lft forever
```
# lo（本地回环接口）
# enp0s3（真正联网网卡）  mtu 1500： 标准以太网 MTU 互联网最常见。
MTU：

Maximum Transmission Unit

最大传输单元。

意思：

一次最多发送多大的网络包。
# tailscale0（重点）

这是：

Tailscale VPN 虚拟网卡

说明：

你已经成功安装并连接 Tailscale。

# 网络结构：

你的 Linux
│
├── lo
│   └── 127.0.0.1（本机）
│
├── enp0s3
│   └── 10.0.2.15（局域网）
│
└── tailscale0
    └── 100.117.183.100（Tailscale VPN）



```bash
ping -c 3 8.8.8.8
```

    #-c 3 (Count)	发送次数参数 (指定只发送 3 个探测数据包后自动停止)
    
```text
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=64 time=36.3 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=64 time=37.1 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=64 time=38.6 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2001ms
rtt min/avg/max/mdev = 36.298/37.306/38.559/0.939 ms
```
# TTL (Time To Live)	生存时间值 (数据包在网络中允许经过的路由器最大跳数)

# 上述的ping -c 3 8.8.8.8底层原理与网络交互设计逻辑

当你输入 ping -c 3 8.8.8.8 并按下回车时，操作系统的网络子系统在后台执行了以下标准的三步流转逻辑：

+-------------------+                      +-------------------+
|   本地计算机      |                      |  谷歌 DNS 服务器  |
|  (Local Host)     |                      |     (8.8.8.8)     |
+-------------------+                      +-------------------+
          |                                          |
          |  1. ICMP Echo Request (seq=1)            |
          |----------------------------------------->|
          |                                          |
          |  2. ICMP Echo Reply (seq=1)              |
          |<-----------------------------------------|  (计算 RTT = 延迟时间)
          |                                          |
          |  3. [重复上述过程，直到发满 3 次]        |
          | - - - - - - - - - - - - - - - - - - - - -|
          |                                          |
          v                                          v

> 构造并发送 ICMP 报文（无状态探测）：
ping 工具不会像 HTTP 或 SSH 那样去建立复杂的 TCP 三次握手连接。它直接在网络层（Network Layer）组装一个 ICMP（Internet Control Message Protocol，网际控制报文协议） 数据包，其类型字段被设置为 8（代表 Echo Request，回显请求），并打上序列号（如 seq=1），然后通过物理网卡发射出去。

目标响应与内核自动回复：
当这个数据包跨越千山万水到达谷歌位于全球各地的边缘机房（通过 Anycast 任播技术）时，内核网络栈在硬件层识别到这是一个标准 ICMP 请求，会绕过用户空间的应用层程序，直接由内核在底层自动封装一个 ICMP 类型为 0（代表 Echo Reply，回显应答）的报文，原路返回给你的计算机。

计算时间戳与丢包率：
本地计算机收到应答包后，用“当前接收时间”减去“当初发送该包时记录的时间戳”，就得到了一个核心指标：RTT（Round-Trip Time，往返时延），单位是毫秒（ms）。 


```bash
top
```

 top 相当于 Linux 的：
任务管理器（Windows Task Manager）

```
top - 09:30:51 up 3 days,  1:01,  2 users,  load average: 0.01, 0.00, 0.
Tasks: 124 total,   1 running, 123 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.2 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.0 si,
MiB Mem :   3398.8 total,   1963.2 free,    497.9 used,   1181.5 buff/ca
MiB Swap:   3910.0 total,   3910.0 free,      0.0 used.   2900.9 avail M

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+
  33477 brown     20   0   10816   6336   4176 R   0.7   0.2   0:00.98
     40 root      20   0       0      0      0 S   0.3   0.0   0:21.60
  33460 root      20   0       0      0      0 I   0.3   0.0   0:00.11
      1 root      20   0   25684  16840  11544 S   0.0   0.5   0:36.26
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.21
      3 root      20   0       0      0      0 S   0.0   0.0   0:00.00
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00
      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00
      7 root       0 -20       0      0      0 I   0.0   0.0   0:00.00
      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00
     10 root       0 -20       0      0      0 I   0.0   0.0   0:00.25
     12 root      20   0       0      0      0 I   0.0   0.0   0:00.00
     13 root       0 -20       0      0      0 I   0.0   0.0   0:00.00
     14 root      20   0       0      0      0 S   0.0   0.0   0:01.20
     15 root      20   0       0      0      0 I   0.0   0.0   0:11.80
     16 root      20   0       0      0      0 S   0.0   0.0   0:00.00
     17 root      20   0       0      0      0 S   0.0   0.0   0:00.06
     18 root      rt   0       0      0      0 S   0.0   0.0   0:05.57
     19 root      20   0       0      0      0 S   0.0   0.0   0:00.00
     20 root     -51   0       0      0      0 S   0.0   0.0   0:00.00
     21 root      20   0       0      0      0 S   0.0   0.0   0:00.00
     22 root      20   0       0      0      0 S   0.0   0.0   0:00.00
     23 root     -51   0       0      0      0 S   0.0   0.0   0:00.00
     24 root      rt   0       0      0      0 S   0.0   0.0   0:10.14
     25 root      20   0       0      0      0 S   0.0   0.0   0:01.75
     27 root       0 -20       0      0      0 I   0.0   0.0   0:01.08
     30 root      20   0       0      0      0 S   0.0   0.0   0:00.00
     31 root       0 -20       0      0      0 I   0.0   0.0   0:00.00
     32 root      20   0       0      0      0 I   0.0   0.0   0:00.00
     33 root      20   0       0      0      0 I   0.0   0.0   0:00.00
     34 root      20   0       0      0      0 S   0.0   0.0   0:00.00
     35 root      20   0       0      0      0 S   0.0   0.0   0:00.15
     36 root      20   0       0      0      0 S   0.0   0.0   0:00.00
     39 root       0 -20       0      0      0 I   0.0   0.0   0:00.00

```

``` text

进程列表:PID USER PR NI VIRT RES SHR S %CPU %MEM
PID
1
2
3

进程ID。像身份证。

USER
root

谁运行的。

PR   (Priority)优先级
默认：20

NI  Nice值 -20~19
越小：优先级越高 

VIRT 虚拟内存
25684
进程申请的总空间。

RES 实际占用内存

Resident Memory
16840

实际使用。

SHR 共享内存

S 状态：

  R 运行

  S 睡眠

  I 空闲内核线程

  Z  僵尸

你大量：

S
I

正常。

%CPU

CPU占用率。

%MEM

内存占用率。

TIME+
0:36.25

累计CPU时间。

不是系统时间。

表示：

这个进程总共用CPU：

36秒
你的机器当前一句话总结
运行3天
CPU几乎空闲
内存充足
没有Swap
没有僵尸进程
123个后台进程
系统健康

对于一个 Linux 虚拟机来说，这状态非常正常。


``` 
# ls 的用法
[ / ] (根目录: 整个文件系统的最高绝对起点)
       │
       ├─ [ /home ] (用户数据区: 存放普通用户的私人数据与配置文件)
       ├─ [ /etc ]  (系统配置区: 存放全系统所有软件与核心服务的静态文本配置文件)
       └─ [ /var ]  (动态数据区: 存放系统日志、缓存、队列等频繁变动的数据)



# ls -la（ls -al）     (--long --all)这是复合写法同时输出ls -l和 -a复合结果 
# 范围最大化 + 细节最大化

```bash
brown@brown-vm:~$ ls -la
total 48
drwxr-x--- 6 brown brown 4096 May 19 09:27 .
drwxr-xr-x 3 root  root  4096 May 13 09:58 ..
-rw------- 1 brown brown  292 May 18 08:23 .bash_history
-rw-r--r-- 1 brown brown  220 Feb 13 12:16 .bash_logout
-rw-r--r-- 1 brown brown 3771 Feb 13 12:16 .bashrc
drwx------ 2 brown brown 4096 May 14 02:40 .cache
drwx------ 3 brown brown 4096 May 19 09:27 .config
-rw-r--r-- 1 brown brown  807 Feb 13 12:16 .profile
drwx------ 2 brown brown 4096 May 16 09:27 .ssh
-rw-r----- 1 brown brown    6 May 16 08:50 .vboxclient-clipboard-tty1-control.pid
drwxrwxr-x 3 brown brown 4096 May 16 09:34 mlops
-rw-rw-r-- 1 brown brown   46 May 18 08:31 test.txt
```

# ls -lh (--long --human-readable) 不扩大范围,只增加细节并格式化体积
如果不带 -h，普通的 ls -l 打印一个 40GB 的模型文件，体积那一列会显示为极其反人类的一长串数字：42949672960（字节）。你的大脑需要花好几秒去数到底有几个零。-h 的底层数学逻辑：
当加上 -h 时，工具在输出体积前，会自动在内存里执行一段进位逻辑：

显示数值= 原始字节数 (Bytes)➗1024^3

它发现超过了 1024^3 字节，就会自动换算成物理计量的 GB，并在屏幕上干净利落地打印出 40G。这能瞬间释放你作为 INTP 的视觉带宽。致命局限：因为没加 -a，所以当前目录下的隐藏环境变量配置文件（如 .env）在这个命令下完全隐形。

```bash
brown@brown-vm:~$ ls -lh
total 8.0K
drwxrwxr-x 3 brown brown 4.0K May 16 09:34 mlops
-rw-rw-r-- 1 brown brown   46 May 18 08:31 test.txt
```

# ls -a (--all) —— 只扩大范围，不增加细节
内部行为：系统调用读取目录文件。当它扫描到 .env 或者 .git 时，因为 -a 开关为真，它不会跳过它们，而是把它们的名字一起拉出来。

屏幕表现：屏幕上喷出一堆名字，密密麻麻。你看不到谁大谁小，也看不到谁有执行权限。

```bash
brown@brown-vm:~$ ls -a
.   .bash_history  .bashrc  .config   .ssh                                    mlops
..  .bash_logout   .cache   .profile  .vboxclient-clipboard-tty1-control.pid  test.txt

```

# --help 说明书
几乎绝大多数别的 Linux 命令、开源工具甚至你未来在 MLOps 里要用的所有高级云端 CLI 工具，全部可以写 help。

```bash
ls --help

```

*** 
Linux 的标准语法铁律公式是：
命令 (Command) + 选项 (Options) + 参数 (Arguments)
***

1. 隐含的主语 ── 【你（User）/ 操作系统内核（Kernel）】
在命令行里，主语永远是被省略的。

当你在终端敲下命令时，隐含的主语就是 “你（操作者）” 或者是 “操作系统内核”。

2. 谓语（动词） ── 【命令 (Command)】 —— 执行什么动作？
这是这一行指令的灵魂起点，必须放在第一位。它代表你想召唤哪个二进制可执行程序。

例子：ls（列出资产）、cd（切换空间坐标）、ping（发射无状态探测包）、rm（物理抹除文件）。

底层本质：你敲下这个动词，系统就会去磁盘的 /bin 或 /usr/bin 路径下找到同名的物理文件，并把它拉进内存变成一个运行中的进程。

3. 状语（修饰副词） ── 【选项 (Options)】 —— 动作的姿态是什么？
用来调整、修饰这个动词的执行方式。它通常用单减号 -（短别名）或双减号 --（长全称）引导。

例子：在 ls -lh 里，-l（详细列表姿态）和 -h（人类可读体积进位姿态）就是状语。它们不改变“列出文件”这个核心动词，但极大地修饰了输出结果长什么样。

4. 宾语（受动实体） ── 【参数 (Arguments)】 —— 动作施加在谁身上？
命令最终要物理作用、支配、或修改的具体资产目标。它通常是一个物理路径、一个文件名、或者一个网络 IP 地址。

例子：/etc（配置中心绝对路径）、test.txt（纯文本文件）、8.8.8.8（谷歌远程服务器）。

