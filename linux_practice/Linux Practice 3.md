# 创建

> mkdir (Make Directory)

作用： 用来“开辟空间”。它不能创建文件，只能创建用来存放文件的容器（目录）。

用法： mkdir my_folder。如果你想一次性创建多级目录，还可以加 -p 参数：mkdir -p project/src/data。

> touch

作用： 用来“标记存在”。它是创建一个空的文件对象。

用法： touch note.txt。

> echo

作用： 用来“生成内容”。它本身是一个打印工具，把字符打印在屏幕上。但配合重定向符号 >，它就变成了“写入工具”。

用法： echo "Hello World" > hello.txt。这会创建一个名为 hello.txt 的文件，并将内容填进去。

> 这三个命令的区分，体现了 Unix 哲学中的“单一职责原则”：

# mkdir 处理的是结构：它是在文件系统的“树状结构”中添加一个新节点。

# touch 处理的是元数据（MetaData）：它不关心文件内容，只关心文件本身“存在”这个事实以及它的“时间记录”。

# echo 处理的是数据流：它的核心是把一段数据（字符串）从一个地方（内存）搬运到另一个地方（文件）。

当你理解了这三者的分工，你就能非常灵活地组合它们：

1. mkdir work (建房)

2. cd work (进房)

3. touch list.txt (放纸)

4. echo "todo item" > list.txt (写字)

```bash
brown@brown-vm:~$ pwd
/home/brown
brown@brown-vm:~$ ls
file1.txt  mlops  test.txt
brown@brown-vm:~$ mkdir linux_practice
brown@brown-vm:~$ ls
file1.txt  linux_practice  mlops  test.txt
brown@brown-vm:~$ cd linux_practice
brown@brown-vm:~/linux_practice$ pwd
/home/brown/linux_practice
brown@brown-vm:~/linux_practice$ mkdir project
brown@brown-vm:~/linux_practice$ ls
project
brown@brown-vm:~/linux_practice$ cd project
brown@brown-vm:~/linux_practice/project$ mkdir docs
brown@brown-vm:~/linux_practice/project$ mkdir backup
brown@brown-vm:~/linux_practice/project$ mkdir archive
brown@brown-vm:~/linux_practice/project$ mkdir docs

```
# 读写

```bash
brown@brown-vm:~/linux_practice/project$ cd docs
brown@brown-vm:~/linux_practice/project/docs$ pwd
/home/brown/linux_practice/project/docs
brown@brown-vm:~/linux_practice/project/docs$ touch readme.txt
brown@brown-vm:~/linux_practice/project/docs$ touch notes.txt
brown@brown-vm:~/linux_practice/project/docs$ ls
notes.txt  readme.txt
brown@brown-vm:~/linux_practice/project/docs$ echo 'linux is powerful' > readme.txt
brown@brown-vm:~/linux_practice/project/docs$ echo 'I am learing linux command' >notes.txt
brown@brown-vm:~/linux_practice/project/docs$ cat readme.txt
linux is powerful
brown@brown-vm:~/linux_practice/project/docs$ cat notes.txt
I am learing linux command
brown@brown-vm:~/linux_practice/project/docs$
```

# seq 是单词 Sequence（序列）的缩写。你在后面给了它两个参数 1 和 100，它底层的 C 语言循环体就会瞬间在内存里数数，从 1 一直数到 100，并在每个数字后面加一个换行符 \n。              如果后面什么都不加，它会把 1 2 3 ... 100 直接打印在你的终端屏幕上。

# less 文本分页查看器（Pager），终端屏幕有几行就看几行
1. 视轨移动控制
j 或 方向键下：将屏幕向下物理滚动 1 行。

k 或 方向键上：将屏幕向上物理滚动 1 行（这是旧版 more 命令绝对无法做到的反向回滚）。

Space (空格键) 或 PageDown：向下翻 1 整页。

b (Back) 或 PageUp：向上回翻 1 整页。

g (小写)：瞬间将指针物理重置到文件的 最开头第一行。

G (大写)：瞬间将指针物理空降到文件的 最末尾最后一行。

2. 内存文本指纹动态检索（极速定位）
在 less 的只读状态下，你不需要退出，可以直接在最左下方敲入检索符号，物理激活流式过滤引擎：

/keyword：从当前位置向后（向下）搜寻指定的关键字（例如输入 /88 寻找含有 88 的数字行）。

?keyword：从当前位置向前（向上）反向搜寻关键字。

n (Next)：沿用上一次的搜索方向（如果你用的是 / 就是向下，用的是 ? 就是向上），继续寻找下一个指纹。
N (Shift + n)：违背上一次的搜索方向，强行反向寻找上一个指纹。
如果之前用 / 向下找，按 N 就会向上调头回溯。

3. 终结与安全退场
q (Quit)：物理终结 less 状态机，关闭文件句柄，将终端控制权干净无污染地交还给原生的用户 Shell。


```bash
brown@brown-vm:~/linux_practice/project/docs$ rm readme.txt
brown@brown-vm:~/linux_practice/project/docs$ seq 1 100 > readme.txt
brown@brown-vm:~/linux_practice/project/docs$ cat readme.txt
1
2
3
4
5
.......(省略)
99
100

brown@brown-vm:~/linux_practice/project/docs$ less readme.txt
```
# 查找

```bash
brown@brown-vm:~/linux_practice/project/docs$ grep 50 readme.txt
50

brown@brown-vm:~/linux_practice/project/docs$ grep learning notes.txt
brown@brown-vm:~/linux_practice/project/docs$ cat notes.txt
I am learing linux command
brown@brown-vm:~/linux_practice/project/docs$ sed -i 's/learing/learning/g' notes.txt
brown@brown-vm:~/linux_practice/project/docs$ grep learning notes.txt
I am learning linux command

```
> i (Ignore case) 忽略大小写
> 's/learing/learning/g' ── 替换算子逻辑流

s：代表 Substitute（替换） 动作，激活替换状态机。

/learing/：这是你的目标搜索指纹（你之前打错的字）。
/learning/：这是你的目标修正指纹（你想改成的正确拼写）。

g：代表 Global（全局）。如果你的 notes.txt 的某一行里同时出现了好几次 learing，加上 g 就会把这一行里所有的错误全部洗掉；如果不加 g，它在底层遇到每一行的第一个错字后就会停止扫描、直接跳到下一行。

g的位置也可以改为数字n：sed -i 's/path/dir/2' paths.txt  （如果一行里有多个 path，只改第二个，其余的完好保留）
指定第 N 次命中才触发。强行指定一个计数器（Counter），只有当某一行里第 N 次出现该指纹时，才执行物理修改。


# Linux 里面有两个完全不同的 i
1. 作为命令参数的 -i ─── 它是“就地落盘（In-place）”
它所在的位置：紧跟在 sed 动词的屁股后面，带有减号（-i）。
本质：控制系统 I/O 管道的流向。
敲了 -i：改完的代码直接重写砸进硬盘。
不敲 -i：改完的代码只喷在屏幕上给你看。
英文字根：In-place（在原地）。

2. 作为算子尾缀的 i ─── 它是“忽略大小写（Ignore Case）”
它所在的位置：被死死关在单引号 's/旧/新/gi' 的最末尾。
本质：控制内存比对引擎的匹配严苛度。
加了尾缀 i：内存扫描时把 ERROR 和 error 当成同一个字。
不加尾缀 i：严格比对 ASCII 码，错一个大小写就绝对不匹配。
英文字根：Ignore Case（忽略大小写）。


```bash
brown@brown-vm:~$ echo "ERROR_INFO" > test_two_i.txt
brown@brown-vm:~$ sed 's/error_info/SUCCESS/i' test_two_i.txt
SUCCESS
brown@brown-vm:~$ cat test_two_i.txt
ERROR_INFO
```
在默认状态下，sed 被设计为一个“只读过滤器”，它绝对不会轻易去触碰或污染你的原始磁盘资产（test_two_i.txt）。它的物理执行逻辑是这样的：

[磁盘文件: test_two_i.txt] (内容: ERROR_INFO)
         |
         | 1. 读取一行到内存
         v
[内存缓冲区: Pattern Space] (内容: ERROR_INFO)
         |
         | 2. 匹配成功，在内存中被替换
         v
[内存缓冲区: Pattern Space] (内容: SUCCESS)
         |
         | 3. 默认物理流向：标准输出 (stdout)
         v
[你的屏幕终端] ---> 打印出 SUCCESS (但磁盘文件根本没变！)

读取到内存：sed 从磁盘中把 test_two_i.txt 的内容 ERROR_INFO 复制一份，放进内存里一块叫 模式空间（Pattern Space） 的区域。

在内存中修改：因为你加了 i，匹配引擎在内存中把 ERROR_INFO 成功替换成了 SUCCESS。

定向到屏幕：替换完成后，sed 把内存中改好的 SUCCESS 发送到了标准输出（stdout，也就是你的屏幕），你在屏幕上看到了替换成功的结果。

释放内存：命令结束，内存缓冲区被清空释放。而自始至终，磁盘上的 test_two_i.txt 文件完全没有被重新写入过。 所以当你再次运行 cat 去读取磁盘时，拿到的依然是最初的 ERROR_INFO。

<!-- 
Pattern Space：模式空间（sed 在内存中开辟的一块临时缓冲区，用来处理文本，不影响磁盘文件）。

Standard Output (stdout)：标准输出（Linux 默认将处理完的结果直接打印到屏幕上展示，不写回磁盘）。

In-place Editing：原位修改（通过特定的物理参数，强行命令 sed 把内存中的改动覆盖写回原文件的操作）。 -->


```bash
brown@brown-vm:~$ sed -i 's/error_info/SUCCESS/i' test_two_i.txt
brown@brown-vm:~$ cat test_two_i.txt
SUCCESS
```

# '>'（覆盖模式）与 '>>'（追加模式）

## '>' 符号本身只负责“开辟通道并强制清空目标”，但它能不能拿到数据去写入，完全取决于前面那个命令（如 sed、cat、echo）在它的运行逻辑里，到底有没有向“标准输出（stdout）”这个管道里喷射字节。  如果前面的命令在运行时发生了逻辑熔断、错误、或者数据被 -i 这样的黑洞内部截留，那么 > 就什么也拿不到，最终导致目标文件变成 0字节的完全空白.

## 由于 > 具有冷酷的“第一步先清空文件”的特性，在线上生产环境中使用它极其危险。如果你想在文件末尾接着写、不破坏原资产，必须使用双大于号 >>：

```bash
brown@brown-vm:~$ echo "NEW_LOG" >> test_output.txt
brown@brown-vm:~$ cat test_output.txt
NEW_LOG
```

系统级别区别：>> 在底层调用的是 open(..., O_APPEND)。它在第一步时绝对不会清空目标文件，而是把文件指针物理锁死在现有文件的末尾最后一个字节之后，实现安全的追加。


# 身份切換 su

```bash
brown@brown-vm:~$ sudo passwd root
[sudo: authenticate] Password:
New password:
Retype new password:
passwd: password updated successfully
brown@brown-vm:~$ su -
Password:
root@brown-vm:~#
root@brown-vm:~# su - brown
brown@brown-vm:~$
# 注意：减号 - 和 用户名 brown 之间，必须狠狠敲一下空格键！
```

 <!-- 注意提示符变化：
符号	身份
$	普通用户
#	root -->

> 只能在root用户修改时钟和显示bios clock  （修改系统时间属于系统管理行为 普通用户没有权限）
```bash
root@brown-vm:~# hwclock
2026-06-06 02:33:07.663017+00:00
root@brown-vm:~#
```

系统有两个时钟：
1. 系统时钟 Kernel Time
查看： date


2. 硬件时钟 BIOS Clock
查看： hwclock

<!-- hwclock -w   把系统时间同步到 BIOS。

-w意思：write
写入硬件时钟

 -->


# 环境变量（Environment Variables）
PATH
HOME
USER
SHELL
LANG
EDITOR
JAVA_HOME
...

# locale 查看当前正在使用的语系配置
```bash
brown@brown-vm:~$ locale
LANG=en_US.UTF-8                  #默认语系
LANGUAGE=                         #用于翻译程序信息,比如 LANGUAGE=zh_CN
LC_CTYPE="en_US.UTF-8"            #控制：字符分类、字符编码、大小写转换   grep awk sed 识别字符时都会参考它。
LC_NUMERIC="en_US.UTF-8"          #控制：数字格式  很多金融软件会读取这个设置
LC_TIME="en_US.UTF-8"             #控制：时间格式 月份名称 星期名称
LC_COLLATE="en_US.UTF-8"          #控制：排序规则  ls  sort 排序时会参考它。
LC_MONETARY="en_US.UTF-8"         #货币格式
LC_MESSAGES="en_US.UTF-8"         #错误信息 帮助信息
LC_PAPER="en_US.UTF-8"            #纸张尺寸 美国：8.5 × 11 inch  中、欧：A4
LC_NAME="en_US.UTF-8"             #姓名格式
LC_ADDRESS="en_US.UTF-8"          #地址格式 美国：Street/City/State/ZIP
LC_TELEPHONE="en_US.UTF-8"        #电话号码格式
LC_MEASUREMENT="en_US.UTF-8"      #度量单位 美国：英寸/英尺/磅/华氏度  国际：厘米/米/公斤/摄氏度
LC_IDENTIFICATION="en_US.UTF-8"   #只是 locale 元数据 平时基本不会碰。
LC_ALL=                           #权限最高
```

> Linux 优先级：

LC_ALL
↓
LC_XXX
↓
LANG

# locale -a 列出系统已经安装并支持的所有语系
```bash
brown@brown-vm:~$ locale -a
C
C.utf8
en_US.utf8
POSIX
```

# 快捷键
> Tab 补全： 开头+tab+tab
> Ctrl+A   跳到行首
> Ctrl+E   跳到行尾
> Ctrl+L   清屏
> Ctrl+R   搜索历史命令
> Ctrl+D   退出Shell


# '|' 管线（Pipe）就是把前一个命令的输出，当成后一个命令的输入。

```bash
brown@myvis0612:~$ echo "365*24*60*60" | bc      #bc 任意精度计算器语言
31536000
```

```bash
brown@myvis0612:~$ ip addr | grep "inet " | grep -v 127.0.0.1
    inet 10.0.2.15/24 metric 100 brd 10.0.2.255 scope global dynamic enp0s3
```

```bash
ls -l /etc | more
ls -l /etc | less
```

less功能更强：

Space   下一页
b       上一页
g       第一页
G       最后一页
/关键字 搜索
n       下一个结果
N       上一个结果
q       离开


> ls -l（水平切面读取）：

底层行为：它只调用了系统内核的 readdir() 系统调用。它是一个非递归的、局部的水平切面读取工具。

执行逻辑：当你输入 ls -l 时，它只会读取你当前所在的那个目录文件（Directory File）的索引块，把该目录下的第一层子文件和子目录的元数据（Metadata）以列表形式吐出来。它不会主动钻取到子目录的内部去寻找文件。

> find（垂直深度遍历）：

底层行为：它在底层不断地循环调用 stat()、lstat() 和 readdir()，在文件系统的目录树上执行经典的深度优先搜索（DFS, Depth-First Search）算法。

执行逻辑：它是一个全局性的、检索型的垂直深度遍历工具。你给它一个起点（如 find / -name "*.py"），它就会像八爪鱼一样，把该路径下所有的子目录、孙子目录翻个底朝天，直到把所有符合条件的文件路径全部捕获为止。

② 匹配维度的区别：无差别列表 vs 多维特征过滤
> ls -l：无法进行复杂的条件过滤。它只能无差别地列出所有文件，或者通过 Shell 的通配符（Wildcard，如 *.log）做简单的文件名过滤。

> find：具备极其强大且多维度的特征过滤引擎。它可以根据文件的绝对物理特征进行精准检索：

时间维度：-mtime -1（过去24小时内修改过的文件）。

大小维度：-size +100M（大于100MB的文件）。

权限与属主：-perm 644 或 -user root。

类型维度：-type f（普通文件）或 -type d（目录）。




# 目录

/	文件系统起点（根目录）
~	当前用户家目录
.	当前目录
..	上一级目录
-	上一次所在目录



> cp -r 与 cp -a 磁盘物理行为

                 [ 物理源文件：属主为 admin, 权限为 755, 时间为 2024年 ]
                                      │
           ┌──────────────────────────┴──────────────────────────┐
           ▼                                                     ▼
【 选型一：cp -r (只认骨架，洗白属性) 】                 【 选型二：cp -a (时间冻结，属性平移) 】
           │                                                     │
           ▼ (元数据重写)                                         ▼ (元数据克隆)
 1. 深度优先递归克隆整个目录树结构。                   1. 深度优先递归克隆整个目录树结构。
 2. 目标路径新文件的属主变成【当前执行命令的用户】。     2. 保持原文件属主 admin 不变 (保持 UID/GID)。
 3. 文件的历史时间戳全自动刷新为【当前这一秒】。         3. 历史时间戳完美“冰冻”平移，保持 2024年。
 4. 软链接会被物理拆解并复制一份真实实体文件。           4. 软链接（Symlink）保持原样克隆，不发生膨胀。