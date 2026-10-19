```bash

# ==================== 37. 查看进程状态并调整进程优先级 ====================
# 检查先前保存的 CPU 测试进程；只有表头，说明该进程已经结束。
brown@myvis0612:~/linux-lab/unit05-process$ ps -p "$CPU_PID" -o pid,stat,cmd
    PID STAT CMD
# 使用 top 查看系统负载、CPU、内存及进程概况；以下保留主要输出。
brown@myvis0612:~/linux-lab/unit05-process$ top
top - 08:53:43 up 8 days,  2:38,  1 user,  load average: 0.34, 0.67, 0.41
Tasks: 103 total,   1 running, 102 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.4 us,  0.8 sy,  0.0 ni, 98.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1642.9 total,    282.9 free,    445.1 used,   1104.9 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   1197.8 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   1575 brown     20   0   19100   8488   5636 S   0.8   0.5   0:14.29 sshd-session: brown@pts/0
  64830 root      20   0       0      0      0 I   0.8   0.0   0:24.42 [kworker/0:2-events]
  26576 _chrony   20   0   20556   6404   5520 S   0.4   0.4   0:04.30 /usr/sbin/chronyd -n -F 1
      1 root      20   0   25460  16692  11652 S   0.0   1.0   0:47.30 /usr/lib/systemd/systemd --system --deserialize+
# 以 nice 值 10 启动后台 sleep 进程，并查看它的 PID、父 PID 和优先级。
brown@myvis0612:~/linux-lab/unit05-process$ nice -n 10 sleep 300 &
[1] 65097
brown@myvis0612:~/linux-lab/unit05-process$ pgrep -a -x sleep
65097 sleep 300
brown@myvis0612:~/linux-lab/unit05-process$ ps -o pid,ppid,ni,pri,cmd -C sleep
    PID    PPID  NI PRI CMD
  65097    1576  10   9 sleep 300
# 故意对不存在的 PID 24680 执行 renice，观察“No such process”错误。
brown@myvis0612:~/linux-lab/unit05-process$ renice -n 15 -p 24680
renice: failed to get priority for 24680 (process ID): No such process
# 对实际 PID 调整 nice 值，并再次确认；查询不存在的 PID 时仍只显示表头。
brown@myvis0612:~/linux-lab/unit05-process$ renice -n 15 -p 65097
65097 (process ID) old priority 10, new priority 15
brown@myvis0612:~/linux-lab/unit05-process$ ps -o pid,ni,pri,cmd -p 24680
    PID  NI PRI CMD
brown@myvis0612:~/linux-lab/unit05-process$  ps -o pid,ni,pri,cmd -p 65097
    PID  NI PRI CMD
  65097  15   4 sleep 300
brown@myvis0612:~/linux-lab/unit05-process$ ps -o pid,ni,pri,cmd -p 24680
    PID  NI PRI CMD
# 终止后台进程，然后简单查看磁盘设备和根文件系统空间。
brown@myvis0612:~/linux-lab/unit05-process$ kill 65097
brown@myvis0612:~/linux-lab/unit05-process$ lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0   25G  0 disk
├─sda1   8:1    0    1M  0 part
└─sda2   8:2    0   25G  0 part /
sr0     11:0    1 1024M  0 rom
[1]+  Terminated                 nice -n 10 sleep 300
brown@myvis0612:~/linux-lab/unit05-process$ df -h
Filesystem      Size  Used Avail Use% Mounted on
tmpfs           329M  1.1M  328M   1% /run
/dev/sda2        25G  3.8G   20G  17% /
tmpfs           822M     0  822M   0% /dev/shm
tmpfs           822M  8.0K  822M   1% /tmp
none            1.0M     0  1.0M   0% /run/credentials/getty@tty1.service
tmpfs           165M  8.0K  165M   1% /run/user/1000
none            1.0M     0  1.0M   0% /run/credentials/systemd-resolved.service
none            1.0M     0  1.0M   0% /run/credentials/systemd-journald.service

# ==================== 38. 初始化 Unit 06 存储实验并查看系统存储 ====================
# 创建并进入 Unit 06 存储实验目录。
brown@myvis0612:~/linux-lab/unit05-process$ cd ~/linux-lab
brown@myvis0612:~/linux-lab$ mkdir -p unit06-storage
brown@myvis0612:~/linux-lab$ cd unit06-storage
brown@myvis0612:~/linux-lab/unit06-storage$ pwd
/home/brown/linux-lab/unit06-storage
# 使用 lsblk、df、findmnt 和 blkid 从不同角度查看块设备、文件系统与挂载关系。
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0   25G  0 disk
├─sda1   8:1    0    1M  0 part
└─sda2   8:2    0   25G  0 part /
sr0     11:0    1 1024M  0 rom
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -o NAME,PATH,TYPE,SIZE,FSTYPE,FSVER,LABEL,UUID,MOUNTPOINTS,MODEL
NAME   PATH      TYPE  SIZE FSTYPE FSVER LABEL UUID                                 MOUNTPOINTS MODEL
sda    /dev/sda  disk   25G                                                                     VBOX HARDDISK
├─sda1 /dev/sda1 part    1M
└─sda2 /dev/sda2 part   25G ext4   1.0         e5be4de1-6f15-45d6-a223-7812d290a6fe /
sr0    /dev/sr0  rom  1024M                                                                     VBOX CD-ROM
brown@myvis0612:~/linux-lab/unit06-storage$ df -hT
Filesystem     Type   Size  Used Avail Use% Mounted on
tmpfs          tmpfs  329M  1.1M  328M   1% /run
/dev/sda2      ext4    25G  3.8G   20G  17% /
tmpfs          tmpfs  822M     0  822M   0% /dev/shm
tmpfs          tmpfs  822M  8.0K  822M   1% /tmp
none           tmpfs  1.0M     0  1.0M   0% /run/credentials/getty@tty1.service
tmpfs          tmpfs  165M  8.0K  165M   1% /run/user/1000
none           tmpfs  1.0M     0  1.0M   0% /run/credentials/systemd-resolved.service
none           tmpfs  1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
none           tmpfs  1.0M     0  1.0M   0% /run/credentials/systemd-networkd.service
brown@myvis0612:~/linux-lab/unit06-storage$ findmnt
TARGET                         SOURCE   FSTYPE      OPTIONS
/                              /dev/sda2
│                                       ext4        rw,relatime
├─/tmp                         tmpfs    tmpfs       rw,nosuid,nodev,nr_inodes=1048576,inode64,usrquota
├─/run                         tmpfs    tmpfs       rw,nosuid,nodev,size=336476k,nr_inodes=819200,mode=755,inode64
│ ├─/run/credentials/systemd-networkd.service
│ │                            none     tmpfs       ro,nosuid,nodev,noexec,relatime,nosymfollow,size=1024k,nr_inodes=102
│ ├─/run/credentials/getty@tty1.service
│ │                            none     tmpfs       ro,nosuid,nodev,noexec,relatime,nosymfollow,size=1024k,nr_inodes=102
│ ├─/run/user/1000             tmpfs    tmpfs       rw,nosuid,nodev,relatime,size=168236k,nr_inodes=42059,mode=700,uid=1
│ ├─/run/credentials/systemd-resolved.service
│ │                            none     tmpfs       ro,nosuid,nodev,noexec,relatime,nosymfollow,size=1024k,nr_inodes=102
│ └─/run/credentials/systemd-journald.service
│                              none     tmpfs       ro,nosuid,nodev,noexec,relatime,nosymfollow,size=1024k,nr_inodes=102
├─/dev                         devtmpfs devtmpfs    rw,nosuid,size=805656k,nr_inodes=201414,mode=755,inode64
│ ├─/dev/hugepages             hugetlbfs
│ │                                     hugetlbfs   rw,nosuid,nodev,relatime,pagesize=2M
│ ├─/dev/mqueue                mqueue   mqueue      rw,nosuid,nodev,noexec,relatime
│ ├─/dev/shm                   tmpfs    tmpfs       rw,nosuid,nodev,inode64,usrquota
│ └─/dev/pts                   devpts   devpts      rw,nosuid,noexec,relatime,gid=5,mode=600,ptmxmode=000
├─/sys                         sysfs    sysfs       rw,nosuid,nodev,noexec,relatime
│ ├─/sys/kernel/tracing        tracefs  tracefs     rw,nosuid,nodev,noexec,relatime
│ ├─/sys/kernel/debug          debugfs  debugfs     rw,nosuid,nodev,noexec,relatime
│ ├─/sys/fs/fuse/connections   fusectl  fusectl     rw,nosuid,nodev,noexec,relatime
│ ├─/sys/kernel/security       securityfs
│ │                                     securityfs  rw,nosuid,nodev,noexec,relatime
│ ├─/sys/fs/cgroup             cgroup2  cgroup2     rw,nosuid,nodev,noexec,relatime,nsdelegate,memory_recursiveprot,memo
│ ├─/sys/fs/pstore             none     pstore      rw,nosuid,nodev,noexec,relatime
│ ├─/sys/fs/bpf                bpf      bpf         rw,nosuid,nodev,noexec,relatime,mode=700
│ └─/sys/kernel/config         configfs configfs    rw,nosuid,nodev,noexec,relatime
└─/proc                        proc     proc        rw,nosuid,nodev,noexec,relatime
  └─/proc/sys/fs/binfmt_misc   systemd-1
    │                                   autofs      rw,relatime,fd=35,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe
    └─/proc/sys/fs/binfmt_misc binfmt_misc
                                        binfmt_misc rw,nosuid,nodev,noexec,relatime
brown@myvis0612:~/linux-lab/unit06-storage$ findmnt /
TARGET SOURCE    FSTYPE OPTIONS
/      /dev/sda2 ext4   rw,relatime
brown@myvis0612:~/linux-lab/unit06-storage$ sudo blkid
[sudo: authenticate] Password:
# 查看内存和 Swap；当前系统尚未启用 Swap。
brown@myvis0612:~/linux-lab/unit06-storage$ free -h
               total        used        free      shared  buff/cache   available
Mem:           1.6Gi       446Mi       277Mi       1.1Mi       1.1Gi       1.2Gi
Swap:             0B          0B          0B
brown@myvis0612:~/linux-lab/unit06-storage$ cat /proc/swaps
Filename                                Type            Size            Used            Priority
# 继续查看设备文件系统信息、分区表以及根文件系统所在位置。
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -o NAME,PATH,TYPE,SIZE,FSTYPE,LABEL,UUID,MOUNTPOINTS,MODEL
NAME   PATH      TYPE  SIZE FSTYPE LABEL UUID                                 MOUNTPOINTS MODEL
sda    /dev/sda  disk   25G                                                               VBOX HARDDISK
├─sda1 /dev/sda1 part    1M
└─sda2 /dev/sda2 part   25G ext4         e5be4de1-6f15-45d6-a223-7812d290a6fe /
sr0    /dev/sr0  rom  1024M                                                               VBOX CD-ROM
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -f
NAME   FSTYPE FSVER LABEL UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
sda
├─sda1
└─sda2 ext4   1.0         e5be4de1-6f15-45d6-a223-7812d290a6fe   19.4G    15% /
sr0
brown@myvis0612:~/linux-lab/unit06-storage$ sudo fdisk -l
Disk /dev/sda: 25 GiB, 26843545600 bytes, 52428800 sectors
Disk model: VBOX HARDDISK
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 6BCBFAB3-91E3-4F4B-8851-4F70171BC5DF

Device     Start      End  Sectors Size Type
/dev/sda1   2048     4095     2048   1M BIOS boot
/dev/sda2   4096 52426751 52422656  25G Linux filesystem
brown@myvis0612:~/linux-lab/unit06-storage$ findmnt /
TARGET SOURCE    FSTYPE OPTIONS
/      /dev/sda2 ext4   rw,relatime
brown@myvis0612:~/linux-lab/unit06-storage$ df -h ~/linux-lab/unit06-storage
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2        25G  3.8G   20G  17% /

# ==================== 39. 创建稀疏磁盘镜像并关联 Loop 设备 ====================
# 创建一个逻辑大小为 2 GiB 的稀疏镜像；ls 显示逻辑大小，du 显示实际占用为 0。
brown@myvis0612:~/linux-lab/unit06-storage$ cd ~/linux-lab/unit06-storage
brown@myvis0612:~/linux-lab/unit06-storage$ truncate -s 2G disk-lab.img
brown@myvis0612:~/linux-lab/unit06-storage$ ls -lh disk-lab.img
-rw-rw-r-- 1 brown brown 2.0G Oct 15 02:42 disk-lab.img
brown@myvis0612:~/linux-lab/unit06-storage$ du -h disk-lab.img
0       disk-lab.img
brown@myvis0612:~/linux-lab/unit06-storage$ file disk-lab.img
disk-lab.img: data
brown@myvis0612:~/linux-lab/unit06-storage$ sudo losetup --find --show --partscan disk-lab.img
[sudo: authenticate] Password:
/dev/loop0
# 查询镜像已经关联到的 Loop 设备。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo losetup -j "$PWD/disk-lab.img"
[sudo: authenticate] Password:
/dev/loop0: [2050]:262403 (/home/brown/linux-lab/unit06-storage/disk-lab.img)
# 保存镜像和 Loop 设备路径，便于后续命令重复使用。
brown@myvis0612:~/linux-lab/unit06-storage$ IMAGE="$PWD/disk-lab.img"
brown@myvis0612:~/linux-lab/unit06-storage$ LOOP=/dev/loop0
brown@myvis0612:~/linux-lab/unit06-storage$ echo "镜像：$IMAGE"
镜像：/home/brown/linux-lab/unit06-storage/disk-lab.img
brown@myvis0612:~/linux-lab/unit06-storage$ echo "设备：$LOOP"
设备：/dev/loop0
# 查看 Loop 设备容量；此时还没有分区。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo fdisk -l "$LOOP"
[sudo: authenticate] Password:
Disk /dev/loop0: 2 GiB, 2147483648 bytes, 4194304 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk "$LOOP"
NAME  MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
loop0   7:0    0   2G  0 loop

# ==================== 40. 在 fdisk 中练习错误输入并创建 GPT 分区 ====================
# 故意在 Shell 中直接输入 fdisk 子命令 g；它不是独立命令，因此失败。
brown@myvis0612:~/linux-lab/unit06-storage$ g
g: command not found
# 进入 fdisk 后先创建 GPT 分区表；在分区号和扇区提示处故意输入 l、w、+，观察范围错误。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo fdisk "$LOOP"

Welcome to fdisk (util-linux 2.41.3).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS (MBR) disklabel with disk identifier 0x08b7a40b.

Command (m for help): g
Created a new GPT disklabel (GUID: A1FE8098-5B82-420D-9807-774494E34F23).

Command (m for help): n
Partition number (1-128, default 1): l
Value out of range.
Partition number (1-128, default 1): w
Value out of range.
Partition number (1-128, default 1): 1
First sector (2048-4194270, default 2048): l
Value out of range.
First sector (2048-4194270, default 2048): 2048
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-4194270, default 4192255): l
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-4194270, default 4192255): +
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-4194270, default 4192255):
# 重新进入 fdisk，按正确顺序创建覆盖镜像空间的 Linux 文件系统分区并写入分区表。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo fdisk "$LOOP"
[sudo: authenticate] Password:

Welcome to fdisk (util-linux 2.41.3).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): g
Created a new GPT disklabel (GUID: 7D14F990-DB23-42AD-86FC-829D78DB53FD).

Command (m for help): n
Partition number (1-128, default 1): 1
First sector (2048-4194270, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-4194270, default 4192255):

Created a new partition 1 of type 'Linux filesystem' and of size 2 GiB.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.


# ==================== 41. 重新关联镜像并确认分区设备 ====================
# 解除旧 Loop 关联，再通过 --partscan 重新关联，使内核识别新分区。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo losetup -d "$LOOP"
[sudo: authenticate] Password:
brown@myvis0612:~/linux-lab/unit06-storage$ LOOP=$(sudo losetup --find --show --partscan "$IMAGE")
brown@myvis0612:~/linux-lab/unit06-storage$ PART="${LOOP}p1"
brown@myvis0612:~/linux-lab/unit06-storage$ echo "LOOP=$LOOP"
LOOP=/dev/loop0
brown@myvis0612:~/linux-lab/unit06-storage$ echo "PART=$PART"
PART=/dev/loop0p1
# 查看 Loop 设备、分区表，并用 test 确认分区块设备存在。
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -o NAME,PATH,TYPE,SIZE,FSTYPE,LABEL,UUID,MOUNTPOINTS "$LOOP"
NAME      PATH         TYPE SIZE FSTYPE LABEL UUID MOUNTPOINTS
loop0     /dev/loop0   loop   2G
└─loop0p1 /dev/loop0p1 part   2G
brown@myvis0612:~/linux-lab/unit06-storage$ sudo fdisk -l "$LOOP"
Disk /dev/loop0: 2 GiB, 2147483648 bytes, 4194304 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 7D14F990-DB23-42AD-86FC-829D78DB53FD

Device       Start     End Sectors Size Type
/dev/loop0p1  2048 4192255 4190208   2G Linux filesystem
brown@myvis0612:~/linux-lab/unit06-storage$ test -b "$PART" && echo "分区设备存在" || echo "分区设备不存在"
分区设备存在

# ==================== 42. 演示未格式化分区无法挂载 ====================
# 分区刚创建时没有文件系统，因此 blkid 只有 PARTUUID，UUID 和 LABEL 均为空。
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -f "$LOOP"
$PART"NAME      FSTYPE FSVER LABEL UUID FSAVAIL FSUSE% MOUNTPOINTS
loop0
└─loop0p1
brown@myvis0612:~/linux-lab/unit06-storage$ sudo blkid "$PART"
/dev/loop0p1: PARTUUID="d0bf4c87-65fd-42f1-b40c-4653d903b725"
brown@myvis0612:~/linux-lab/unit06-storage$ UUID=$(sudo blkid -s UUID -o value "$PART")
brown@myvis0612:~/linux-lab/unit06-storage$ LABEL=$(sudo blkid -s LABEL -o value "$PART")
brown@myvis0612:~/linux-lab/unit06-storage$ printf 'UUID=%s\n' "$UUID"
UUID=
brown@myvis0612:~/linux-lab/unit06-storage$ printf 'LABEL=%s\n' "$LABEL"
LABEL=
# 故意挂载尚未格式化的分区，保留 wrong fs type 错误。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo mkdir -p /mnt/unit06-data
brown@myvis0612:~/linux-lab/unit06-storage$ sudo mkdir -p /mnt/unit06-data
brown@myvis0612:~/linux-lab/unit06-storage$ sudo mount "$PART" /mnt/unit06-data
mount: /mnt/unit06-data: wrong fs type, bad option, bad superblock on /dev/loop0p1, missing codepage or helper program, or other error.
       dmesg(1) may have more information after failed mount system call.
# findmnt 没有输出；df 因挂载失败而显示挂载点所在的根文件系统。
brown@myvis0612:~/linux-lab/unit06-storage$ findmnt /mnt/unit06-data
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda2      ext4   25G  3.8G   20G  17% /
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -f "$LOOP"
NAME      FSTYPE FSVER LABEL UUID FSAVAIL FSUSE% MOUNTPOINTS
loop0
└─loop0p1

# ==================== 43. 创建 ext4 文件系统并完成挂载 ====================
# 把分区格式化为 ext4，并设置卷标 unit06data。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo mkfs.ext4 -L unit06data "$PART"
mke2fs 1.47.2 (1-Jan-2025)
Discarding device blocks: done
Creating filesystem with 523776 4k blocks and 131072 inodes
Filesystem UUID: 7eaa9ec9-c5d0-4734-b553-010aa0c56345
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912

Allocating group tables: done
Writing inode tables: done
Creating journal (8192 blocks): done
Writing superblocks and filesystem accounting information: done

# 一次漏写右引号导致 Shell 进入续行提示，使用 Ctrl+C 取消；随后重新执行正确命令。
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -f "$LOOP
> sudo blkid "$PART"
> sudo file -s "$PART"
>
>
> ^C
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -f "$LOOP"
NAME      FSTYPE FSVER LABEL      UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
loop0
└─loop0p1 ext4   1.0   unit06data 7eaa9ec9-c5d0-4734-b553-010aa0c56345
brown@myvis0612:~/linux-lab/unit06-storage$ sudo blkid "$PART"
/dev/loop0p1: LABEL="unit06data" UUID="7eaa9ec9-c5d0-4734-b553-010aa0c56345" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="d0bf4c87-65fd-42f1-b40c-4653d903b725"
brown@myvis0612:~/linux-lab/unit06-storage$ sudo file -s "$PART"
/dev/loop0p1: Linux rev 1.0 ext4 filesystem data, UUID=7eaa9ec9-c5d0-4734-b553-010aa0c56345, volume name "unit06data" (extents) (64bit) (large files) (huge files)
# 创建挂载点并挂载，随后使用 findmnt、df 和 lsblk 验证。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo mkdir -p /mnt/unit06-data
brown@myvis0612:~/linux-lab/unit06-storage$ sudo mount "$PART" /mnt/unit06-data
brown@myvis0612:~/linux-lab/unit06-storage$ findmnt /mnt/unit06-data
TARGET           SOURCE       FSTYPE OPTIONS
/mnt/unit06-data /dev/loop0p1 ext4   rw,relatime
brown@myvis0612:~/linux-lab/unit06-storage$ df -hT /mnt/unit06-data
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/loop0p1   ext4  2.0G  532K  1.9G   1% /mnt/unit06-data
brown@myvis0612:~/linux-lab/unit06-storage$ lsblk -f "$LOOP"
NAME      FSTYPE FSVER LABEL      UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
loop0
└─loop0p1 ext4   1.0   unit06data 7eaa9ec9-c5d0-4734-b553-010aa0c56345    1.8G     0% /mnt/unit06-data

# ==================== 44. 在新文件系统中创建文件并查看 inode ====================
# 修改挂载点所有者，创建 docs、backup 目录并写入两个文本文件。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo chown brown:brown /mnt/unit06-data
brown@myvis0612:~/linux-lab/unit06-storage$ mkdir -p /mnt/unit06-data/docs
brown@myvis0612:~/linux-lab/unit06-storage$ mkdir -p /mnt/unit06-data/backup
brown@myvis0612:~/linux-lab/unit06-storage$ printf 'Linux storage lab\n' > /mnt/unit06-data/docs/readme.txt
brown@myvis0612:~/linux-lab/unit06-storage$ printf 'First line\n' > /mnt/unit06-data/docs/notes.txt
brown@myvis0612:~/linux-lab/unit06-storage$ printf 'Second line\n' >> /mnt/unit06-data/docs/notes.txt
brown@myvis0612:~/linux-lab/unit06-storage$ cat /mnt/unit06-data/docs/readme.txt
Linux storage lab
brown@myvis0612:~/linux-lab/unit06-storage$ cat /mnt/unit06-data/docs/notes.txt
First line
Second line
# 递归列出目录时，普通用户不能进入 root 所有的 lost+found；这是预期的权限失败。
brown@myvis0612:~/linux-lab/unit06-storage$ ls -lR /mnt/unit06-data
/mnt/unit06-data:
total 24
drwxrwxr-x 2 brown brown  4096 Oct 16 02:32 backup
drwxrwxr-x 2 brown brown  4096 Oct 16 02:33 docs
drwx------ 2 root  root  16384 Oct 16 02:17 lost+found
ls: cannot open directory '/mnt/unit06-data/lost+found': Permission denied

/mnt/unit06-data/backup:
total 0

/mnt/unit06-data/docs:
total 8
-rw-rw-r-- 1 brown brown 23 Oct 16 02:33 notes.txt
-rw-rw-r-- 1 brown brown 18 Oct 16 02:33 readme.txt
# 查看文件系统容量、inode 使用情况和文件详细元数据。
brown@myvis0612:~/linux-lab/unit06-storage$ df -hT /mnt/unit06-data
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/loop0p1   ext4  2.0G  548K  1.9G   1% /mnt/unit06-data
-data/docs/readme.txtbrown@myvis0612:~/linux-lab/unit06-storage$ df -i /mnt/unit06-data
Filesystem     Inodes IUsed  IFree IUse% Mounted on
/dev/loop0p1   131072    16 131056    1% /mnt/unit06-data
brown@myvis0612:~/linux-lab/unit06-storage$ stat /mnt/unit06-data/docs/readme.txt
  File: /mnt/unit06-data/docs/readme.txt
  size: 18              Blocks: 8          IO Block: 4096   regular file
Device: 259,0   Inode: 14          Links: 1
Access: (0664/-rw-rw-r--)  Uid: ( 1000/   brown)   Gid: ( 1000/   brown)
Access: 2026-10-16 02:33:22.301972465 +0000
Modify: 2026-10-16 02:33:08.017602869 +0000
Change: 2026-10-16 02:33:08.017602869 +0000
 Birth: 2026-10-16 02:33:08.017602869 +0000

# ==================== 45. 练习硬链接、软链接和悬空链接 ====================
# 创建硬链接；两个名称的 inode 相同，链接计数都变为 2。
brown@myvis0612:~/linux-lab/unit06-storage$ cd /mnt/unit06-data/docs
brown@myvis0612:/mnt/unit06-data/docs$ ln readme.txt readme-hard.txt
brown@myvis0612:/mnt/unit06-data/docs$ ls -li readme.txt readme-hard.txt
rd.txt14 -rw-rw-r-- 2 brown brown 18 Oct 16 02:33 readme-hard.txt
14 -rw-rw-r-- 2 brown brown 18 Oct 16 02:33 readme.txt
brown@myvis0612:/mnt/unit06-data/docs$ stat readme.txt
  File: readme.txt
  size: 18              Blocks: 8          IO Block: 4096   regular file
Device: 259,0   Inode: 14          Links: 2
Access: (0664/-rw-rw-r--)  Uid: ( 1000/   brown)   Gid: ( 1000/   brown)
Access: 2026-10-16 02:33:22.301972465 +0000
Modify: 2026-10-16 02:33:08.017602869 +0000
Change: 2026-10-19 03:19:26.759820730 +0000
 Birth: 2026-10-16 02:33:08.017602869 +0000
brown@myvis0612:/mnt/unit06-data/docs$ stat readme-hard.txt
  File: readme-hard.txt
  size: 18              Blocks: 8          IO Block: 4096   regular file
Device: 259,0   Inode: 14          Links: 2
Access: (0664/-rw-rw-r--)  Uid: ( 1000/   brown)   Gid: ( 1000/   brown)
Access: 2026-10-16 02:33:22.301972465 +0000
Modify: 2026-10-16 02:33:08.017602869 +0000
Change: 2026-10-19 03:19:26.759820730 +0000
 Birth: 2026-10-16 02:33:08.017602869 +0000
# 通过硬链接追加内容后，两个名称读到相同数据；删除原名后数据仍可访问。
brown@myvis0612:/mnt/unit06-data/docs$ printf 'Added through hard link\n' >> readme-hard.txt
brown@myvis0612:/mnt/unit06-data/docs$ cat readme.txt
Linux storage lab
Added through hard link
brown@myvis0612:/mnt/unit06-data/docs$ cat readme-hard.txt
Linux storage lab
Added through hard link
brown@myvis0612:/mnt/unit06-data/docs$ rm readme.txt
brown@myvis0612:/mnt/unit06-data/docs$ cat readme-hard.txt
Linux storage lab
Added through hard link
brown@myvis0612:/mnt/unit06-data/docs$ ls -li readme-hard.txt
14 -rw-rw-r-- 1 brown brown 42 Oct 19 03:34 readme-hard.txt
brown@myvis0612:/mnt/unit06-data/docs$ ln -s readme-hard.txt readme-soft.txt
brown@myvis0612:/mnt/unit06-data/docs$ ls -l readme-soft.txt
lrwxrwxrwx 1 brown brown 15 Oct 19 03:36 readme-soft.txt -> readme-hard.txt
brown@myvis0612:/mnt/unit06-data/docs$ readlink readme-soft.txt
readme-hard.txt
brown@myvis0612:/mnt/unit06-data/docs$ stat -c '%N | inode=%i | type=%F' readme-hard.txt
 '%N | inode=%i | type=%F' readme-soft.txt'readme-hard.txt' | inode=14 | type=regular file
brown@myvis0612:/mnt/unit06-data/docs$ stat -c '%N | inode=%i | type=%F' readme-soft.txt
'readme-soft.txt' -> 'readme-hard.txt' | inode=16 | type=symbolic link
# 创建指向不存在目标的软链接；-L 为真但 -e 为假，说明链接本身存在而目标不存在。
brown@myvis0612:/mnt/unit06-data/docs$ ln -s missing.txt dangling-link.txt
brown@myvis0612:/mnt/unit06-data/docs$ ls -l dangling-link.txt
lrwxrwxrwx 1 brown brown 11 Oct 19 03:52 dangling-link.txt -> missing.txt
brown@myvis0612:/mnt/unit06-data/docs$ test -L dangling-link.txt && echo "软链接本身存在"
g-link.txt && echo "目标存在" || echo "目标不存在"软链接本身存在
brown@myvis0612:/mnt/unit06-data/docs$ test -e dangling-link.txt && echo "目标存在" || echo "目标不存在"
目标不存在
brown@myvis0612:/mnt/unit06-data/docs$ rm dangling-link.txt
brown@myvis0612:/mnt/unit06-data/docs$ rm readme-soft.txt

# ==================== 46. 通过 UUID 挂载并写入 fstab ====================
# 查看分区标识，并再次确认卷标。
brown@myvis0612:/mnt/unit06-data/docs$ sudo blkid "$PART"
[sudo: authenticate] Password:
/dev/loop0p1: LABEL="unit06data" UUID="7eaa9ec9-c5d0-4734-b553-010aa0c56345" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="d0bf4c87-65fd-42f1-b40c-4653d903b725"
brown@myvis0612:/mnt/unit06-data/docs$ lsblk -o NAME,PATH,FSTYPE,LABEL,UUID,MOUNTPOINTS "$LOOP"
NAME      PATH         FSTYPE LABEL      UUID                                 MOUNTPOINTS
loop0     /dev/loop0
└─loop0p1 /dev/loop0p1 ext4   unit06data 7eaa9ec9-c5d0-4734-b553-010aa0c56345 /mnt/unit06-data
brown@myvis0612:/mnt/unit06-data/docs$ sudo e2label "$PART" unit06data
brown@myvis0612:/mnt/unit06-data/docs$ sudo blkid "$PART"
/dev/loop0p1: LABEL="unit06data" UUID="7eaa9ec9-c5d0-4734-b553-010aa0c56345" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="d0bf4c87-65fd-42f1-b40c-4653d903b725"
# 获取 UUID，并通过 UUID 把同一文件系统挂载到第二个挂载点。
brown@myvis0612:/mnt/unit06-data/docs$ UUID=$(sudo blkid -s UUID -o value "$PART")
brown@myvis0612:/mnt/unit06-data/docs$ echo $UUID
7eaa9ec9-c5d0-4734-b553-010aa0c56345
brown@myvis0612:/mnt/unit06-data/docs$ sudo mkdir -p /mnt/unit06-uuid
brown@myvis0612:/mnt/unit06-data/docs$ sudo mount "UUID=$UUID" /mnt/unit06-uuid
brown@myvis0612:/mnt/unit06-data/docs$ findmnt /mnt/unit06-uuid
TARGET           SOURCE       FSTYPE OPTIONS
/mnt/unit06-uuid /dev/loop0p1 ext4   rw,relatime
brown@myvis0612:/mnt/unit06-data/docs$ df -hT /mnt/unit06-uuid
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/loop0p1   ext4  2.0G  548K  1.9G   1% /mnt/unit06-uuid
brown@myvis0612:/mnt/unit06-data/docs$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0    2G  0 loop
└─loop0p1 259:0    0    2G  0 part /mnt/unit06-uuid
                                   /mnt/unit06-data
sda         8:0    0   25G  0 disk
├─sda1      8:1    0    1M  0 part
└─sda2      8:2    0   25G  0 part /
sr0        11:0    1 1024M  0 rom
# 备份 fstab，再以 UUID 添加 nofail 持久挂载项。
brown@myvis0612:/mnt/unit06-data/docs$ cd ~
brown@myvis0612:~$ sudo cp -a /etc/fstab /etc/fstab.unit06-backup
[sudo: authenticate] Password:
brown@myvis0612:~$ UUID=$(sudo blkid -s UUID -o value "$PART")
brown@myvis0612:~$ printf '%s\n' "$UUID"
7eaa9ec9-c5d0-4734-b553-010aa0c56345
brown@myvis0612:~$ if ! grep -Fq '# unit06-storage-lab' /etc/fstab; then
>     printf 'UUID=%s /mnt/unit06-data ext4 defaults,nofail 0 2 # unit06-storage-lab\n' "$UUID" \
>     | sudo tee -a /etc/fstab
> fi
UUID=7eaa9ec9-c5d0-4734-b553-010aa0c56345 /mnt/unit06-data ext4 defaults,nofail 0 2 # unit06-storage-lab
brown@myvis0612:~$ tail -n 8 /etc/fstab
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda2 during curtin installation
/dev/disk/by-uuid/e5be4de1-6f15-45d6-a223-7812d290a6fe / ext4 defaults 0 1
UUID=7eaa9ec9-c5d0-4734-b553-010aa0c56345 /mnt/unit06-data ext4 defaults,nofail 0 2 # unit06-storage-lab
# 校验 fstab；没有解析错误，但 systemd 提示配置已修改，需要 daemon-reload。
brown@myvis0612:~$ sudo findmnt --verify --verbose
/
   [ ] target exists
   [ ] source /dev/disk/by-uuid/e5be4de1-6f15-45d6-a223-7812d290a6fe exists
   [ ] FS type is ext4
/mnt/unit06-data
   [ ] target exists
   [ ] userspace options: nofail
   [ ] UUID=7eaa9ec9-c5d0-4734-b553-010aa0c56345 translated to /dev/loop0p1
   [ ] source /dev/loop0p1 exists
   [ ] FS type is ext4
   [W] your fstab has been modified, but systemd still uses the old version;
       use 'systemctl daemon-reload' to reload

0 parse errors, 0 errors, 1 warning
# 卸载主挂载点后执行 mount -a，按提示重载 systemd 再验证自动挂载。
brown@myvis0612:~$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0    2G  0 loop
└─loop0p1 259:0    0    2G  0 part /mnt/unit06-uuid
                                   /mnt/unit06-data
sda         8:0    0   25G  0 disk
├─sda1      8:1    0    1M  0 part
└─sda2      8:2    0   25G  0 part /
sr0        11:0    1 1024M  0 rom
brown@myvis0612:~$ sudo umount /mnt/unit06-data
brown@myvis0612:~$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0    2G  0 loop
└─loop0p1 259:0    0    2G  0 part /mnt/unit06-uuid
sda         8:0    0   25G  0 disk
├─sda1      8:1    0    1M  0 part
└─sda2      8:2    0   25G  0 part /
sr0        11:0    1 1024M  0 rom
brown@myvis0612:~$ sudo mount -a
mount: (hint) your fstab has been modified, but systemd still uses
       the old version; use 'systemctl daemon-reload' to reload.
brown@myvis0612:~$ sudo systemctl daemon-reload
brown@myvis0612:~$ sudo mount -a
brown@myvis0612:~$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0    2G  0 loop
└─loop0p1 259:0    0    2G  0 part /mnt/unit06-data
                                   /mnt/unit06-uuid
sda         8:0    0   25G  0 disk
├─sda1      8:1    0    1M  0 part
└─sda2      8:2    0   25G  0 part /
sr0        11:0    1 1024M  0 rom
brown@myvis0612:~$ findmnt /mnt/unit06-data
TARGET           SOURCE       FSTYPE OPTIONS
/mnt/unit06-data /dev/loop0p1 ext4   rw,relatime
brown@myvis0612:~$ df -hT /mnt/unit06-data
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/loop0p1   ext4  2.0G  548K  1.9G   1% /mnt/unit06-data

# ==================== 47. 练习只读和 noexec 等挂载选项 ====================
# 重新挂载为只读后，故意创建文件，得到 Read-only file system 错误。
brown@myvis0612:~$ sudo mount -o remount,ro /mnt/unit06-data
[sudo: authenticate] Password:
brown@myvis0612:~$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS /mnt/unit06-data
TARGET           SOURCE       FSTYPE OPTIONS
/mnt/unit06-data /dev/loop0p1 ext4   ro,relatime
brown@myvis0612:~$ sudo touch /mnt/unit06-data/readonly-test.txt
touch: cannot touch '/mnt/unit06-data/readonly-test.txt': Read-only file system
# 恢复读写后可以创建并删除测试文件。
brown@myvis0612:~$ sudo mount -o remount,rw /mnt/unit06-data
brown@myvis0612:~$ sudo touch /mnt/unit06-data/readonly-test.txt
brown@myvis0612:~$ ls -l /mnt/unit06-data/readonly-test.txt
-rw-r--r-- 1 root root 0 Oct 19 09:14 /mnt/unit06-data/readonly-test.txt
brown@myvis0612:~$ sudo rm /mnt/unit06-data/readonly-test.txt
# 创建可执行脚本并确认能够直接运行。
brown@myvis0612:~$ cat > /mnt/unit06-data/docs/test-script.sh <<'EOF'
> #!/bin/sh
> echo "Script executed"
> EOF
brown@myvis0612:~$ chmod +x /mnt/unit06-data/docs/test-script.sh
brown@myvis0612:~$ /mnt/unit06-data/docs/test-script.sh
Script executed
# 加入 noexec、nosuid、nodev 后，脚本无法直接执行；恢复默认选项后再次成功。
brown@myvis0612:~$ sudo mount -o remount,rw,noexec,nosuid,nodev /mnt/unit06-data
brown@myvis0612:~$ findmnt -o TARGET,OPTIONS /mnt/unit06-data
TARGET           OPTIONS
/mnt/unit06-data rw,nosuid,nodev,noexec,relatime
brown@myvis0612:~$ /mnt/unit06-data/docs/test-script.sh
-bash: /mnt/unit06-data/docs/test-script.sh: Permission denied
brown@myvis0612:~$ sudo mount -o remount,defaults /mnt/unit06-data
brown@myvis0612:~$ findmnt -o TARGET,OPTIONS /mnt/unit06-data
TARGET           OPTIONS
/mnt/unit06-data rw,relatime
brown@myvis0612:~$ /mnt/unit06-data/docs/test-script.sh
Script executed

# ==================== 48. 创建、启用并关闭 Swap 文件 ====================
# 确认系统当前没有 Swap。
brown@myvis0612:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           1.6Gi       447Mi       346Mi       1.1Mi       1.0Gi       1.2Gi
Swap:             0B          0B          0B
swapon --show
cat /proc/swapsbrown@myvis0612:~$ swapon --show
brown@myvis0612:~$ cat /proc/swaps
Filename                                Type            Size            Used            Priority
# 创建 256 MiB Swap 文件并限制权限为 600。
brown@myvis0612:~/linux-lab/unit06-storage$ cd ~/linux-lab/unit06-storage
brown@myvis0612:~/linux-lab/unit06-storage$ sudo fallocate -l 256M swap-labfile
brown@myvis0612:~/linux-lab/unit06-storage$ sudo chmod 600 swap-labfile
brown@myvis0612:~/linux-lab/unit06-storage$ ls -lh swap-labfile
-rw------- 1 root root 256M Oct 19 09:16 swap-labfile
brown@myvis0612:~/linux-lab/unit06-storage$ ls -l swap-labfile
-rw------- 1 root root 268435456 Oct 19 09:16 swap-labfile
# 格式化并启用 Swap，分别通过 swapon、free 和 /proc/swaps 验证。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo mkswap swap-labfile
Setting up swapspace version 1, size = 256 MiB (268431360 bytes)
no label, UUID=6d1cc9f1-f7cc-4b9e-b22d-1b31944566f1
brown@myvis0612:~/linux-lab/unit06-storage$ sudo swapon swap-labfile
brown@myvis0612:~/linux-lab/unit06-storage$ swapon --show
NAME                                              TYPE SIZE USED PRIO
/home/brown/linux-lab/unit06-storage/swap-labfile file 256M   0B   -1
brown@myvis0612:~/linux-lab/unit06-storage$ free -h
               total        used        free      shared  buff/cache   available
Mem:           1.6Gi       446Mi       346Mi       1.1Mi       1.0Gi       1.2Gi
Swap:          255Mi          0B       255Mi
brown@myvis0612:~/linux-lab/unit06-storage$ cat /proc/swaps
Filename                                Type            Size            Used            Priority
/home/brown/linux-lab/unit06-storage/swap-labfile file          262140          0               -1
# 关闭 Swap 后再次确认容量恢复为 0。
brown@myvis0612:~/linux-lab/unit06-storage$ sudo swapoff swap-labfile
brown@myvis0612:~/linux-lab/unit06-storage$ swapon --show
brown@myvis0612:~/linux-lab/unit06-storage$ free -h
               total        used        free      shared  buff/cache   available
Mem:           1.6Gi       446Mi       346Mi       1.1Mi       1.0Gi       1.2Gi
Swap:             0B          0B          0B

# ==================== 49. 处理 target is busy 并卸载文件系统 ====================
# 当前 Shell 位于挂载点内部，卸载时故意触发 target is busy。
brown@myvis0612:~/linux-lab/unit06-storage$ cd /mnt/unit06-data/docs
brown@myvis0612:/mnt/unit06-data/docs$ pwd
/mnt/unit06-data/docs
brown@myvis0612:/mnt/unit06-data/docs$ sudo umount /mnt/unit06-data
[sudo: authenticate] Password:
umount: /mnt/unit06-data: target is busy.
# 切换到挂载点之外后卸载成功；另一个 UUID 挂载点仍然存在。
brown@myvis0612:/mnt/unit06-data/docs$ cd /
brown@myvis0612:/$ sudo umount /mnt/unit06-data
brown@myvis0612:/$ findmnt /mnt/unit06-data
brown@myvis0612:/$ lsblk
NAME      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
loop0       7:0    0    2G  0 loop
└─loop0p1 259:0    0    2G  0 part /mnt/unit06-uuid
sda         8:0    0   25G  0 disk
├─sda1      8:1    0    1M  0 part
└─sda2      8:2    0   25G  0 part /
sr0        11:0    1 1024M  0 rom
```
