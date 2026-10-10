```bash
# ==================== 24. 初始化 Unit 04 权限实验目录 ====================
# 回到实验根目录，并重新建立权限实验所需的目录结构。
brown@myvis0612:~/linux-lab$ rm -rf unit04-permission
brown@myvis0612:~/linux-lab$ mkdir -p unit04-permission/{files,dirs,users,shared}
brown@myvis0612:~/linux-lab$ cd unit04-permission

# 确认当前路径及两层以内的目录结构。
brown@myvis0612:~/linux-lab/unit04-permission$ pwd
/home/brown/linux-lab/unit04-permission
brown@myvis0612:~/linux-lab/unit04-permission$ find . -maxdepth 2 -type d | sort
.
./dirs
./files
./shared
./users

# ==================== 25. 创建不同类型的文件并查看权限 ====================
# 创建普通文件、目录和指向普通文件的符号链接。
brown@myvis0612:~/linux-lab/unit04-permission$ cd files
brown@myvis0612:~/linux-lab/unit04-permission/files$ touch normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ mkdir directory
brown@myvis0612:~/linux-lab/unit04-permission/files$ ln -s normal.txt symlink.txt

# 长格式输出的首字符用于区分类型：d 表示目录，- 表示普通文件，l 表示符号链接。
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l
total 4
drwxrwxr-x 2 brown brown 4096 Oct  8 03:06 directory
-rw-rw-r-- 1 brown brown    0 Oct  8 03:06 normal.txt
lrwxrwxrwx 1 brown brown   10 Oct  8 03:06 symlink.txt -> normal.txt

# 分别查看三个对象本身，而不是列出目录内容。
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -ld normal.txt directory symlink.txt
-rw-rw-r-- 1 brown brown    0 Oct  8 03:06 normal.txt
drwxrwxr-x 2 brown brown 4096 Oct  8 03:06 directory
lrwxrwxrwx 1 brown brown   10 Oct  8 03:06 symlink.txt -> normal.txt

# ==================== 26. 使用数字方式修改文件权限 ====================
# 权限数字依次表示所有者、所属组和其他人；r=4、w=2、x=1。
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod 640 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rw-r----- 1 brown brown 0 Oct  8 03:06 normal.txt

# 依次练习几种常见权限组合，并观察 rwx 字符串的变化。
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod 644 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rw-r--r-- 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod 755 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxr-xr-x 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod 700 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwx------ 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod 750 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxr-x--- 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod 777 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxrwxrwx 1 brown brown 0 Oct  8 03:06 normal.txt

# 将文件恢复为实验后续使用的 640 权限。
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod 640 normal.txt

# ==================== 27. 使用符号方式增删和设定权限 ====================
# u、g、o 分别代表所有者、所属组和其他人；+ 添加权限，- 删除权限，= 精确设定权限。
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod u+x normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxr----- 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod g+w normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxrw---- 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod o+r normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxrw-r-- 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod o-r normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxrw---- 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod u=rwx,g=r,o= normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rwxr----- 1 brown brown 0 Oct  8 03:06 normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ chmod u-x,g-r,o+r normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rw----r-- 1 brown brown 0 Oct  8 03:06 normal.txt

# ==================== 28. 观察目录读、写、执行权限 ====================
# 建立测试目录和其中的文件。
brown@myvis0612:~/linux-lab/unit04-permission/files$ cd ../dirs
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ mkdir testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ touch testdir/file.txt
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ ls -ld testdir
drwxrwxr-x 2 brown brown 4096 Oct  8 06:51 testdir

# 对目录分别保留 r+x、仅 r、w+x 和仅 x，观察权限字符串。
# 目录的 r 控制列出名称，w 控制增删目录项，x 控制进入和按名称访问。
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ chmod 500 testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ ls -ld testdir
dr-x------ 2 brown brown 4096 Oct  8 06:51 testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ chmod 400 testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ ls -ld testdir
dr-------- 2 brown brown 4096 Oct  8 06:51 testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ chmod 300 testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ ls -ld testdir
d-wx------ 2 brown brown 4096 Oct  8 06:51 testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ chmod 100 testdir
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ ls -ld testdir
d--x------ 2 brown brown 4096 Oct  8 06:51 testdir

# 恢复为常用的 755 权限，避免影响后续实验。
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ chmod 755 testdir

# ==================== 29. 安装并练习 ACL ====================
# 系统最初没有 getfacl；安装 acl 软件包后可使用 getfacl 和 setfacl。
brown@myvis0612:~/linux-lab/unit04-permission/dirs$ cd ../files
brown@myvis0612:~/linux-lab/unit04-permission/files$ getfacl normal.txt
Command 'getfacl' not found, but can be installed with:
sudo apt install acl
brown@myvis0612:~/linux-lab/unit04-permission/files$ sudo apt install acl
...
Setting up acl (2.3.2-2)…

# 查看文件当前的基础 ACL。
brown@myvis0612:~/linux-lab/unit04-permission/files$ getfacl normal.txt
# file: normal.txt
# owner: brown
# group: brown
user::rw-
group::---
other::r--

# 给 brown 组添加读写 ACL；mask 表示命名用户和组类条目的最大有效权限。
brown@myvis0612:~/linux-lab/unit04-permission/files$ setfacl -m g:brown:rw- normal.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ getfacl normal.txt
# file: normal.txt
# owner: brown
# group: brown
user::rw-
group::---
group:brown:rw-
mask::rw-
other::r--

# 权限字符串末尾的 + 表示文件存在扩展 ACL。
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l normal.txt
-rw-rw-r--+ 1 brown brown 0 Oct  8 03:06 normal.txt

# ==================== 30. 修改文件时间戳并汇总对象类型 ====================
# touch -t 的时间格式为 [[CC]YY]MMDDhhmm[.ss]。
brown@myvis0612:~/linux-lab/unit04-permission/files$ touch timestamp.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ touch -t 202610011230 timestamp.txt
brown@myvis0612:~/linux-lab/unit04-permission/files$ ls -l timestamp.txt
-rw-rw-r-- 1 brown brown 0 Oct  1 12:30 timestamp.txt

# 分别查找并显示目录、普通文件和符号链接。
brown@myvis0612:~/linux-lab/unit04-permission/files$ cd ..
brown@myvis0612:~/linux-lab/unit04-permission$ find . -type d -exec ls -ld {} \;
drwxrwxr-x 6 brown brown 4096 Oct  8 03:05 .
drwxr-xr-x 2 brown brown 4096 Oct  8 06:51 ./dirs/testdir
drwxrwxr-x 2 brown brown 4096 Oct  8 03:05 ./shared
drwxrwxr-x 3 brown brown 4096 Oct  9 01:45 ./files
brown@myvis0612:~/linux-lab/unit04-permission$ find . -type f -exec ls -l {} \;
-rw-rw-r-- 1 brown brown 0 Oct  8 06:51 ./dirs/testdir/file.txt
-rw-rw-r--+ 1 brown brown 0 Oct  8 03:06 ./files/normal.txt
-rw-rw-r-- 1 brown brown 0 Oct  1 12:30 ./files/timestamp.txt
brown@myvis0612:~/linux-lab/unit04-permission$ find . -type l -exec ls -l {} \;
lrwxrwxrwx+ 1 brown brown 10 Oct  8 03:06 ./files/symlink.txt -> normal.txt

# ==================== 31. 创建实验用户和用户组 ====================
# 创建 labgroup，并按需创建两个实验用户；-m 同时建立用户主目录。
brown@myvis0612:~/linux-lab/unit04-permission$ getent group labgroup >/dev/null || sudo groupadd labgroup
brown@myvis0612:~/linux-lab/unit04-permission$ id labuser1 >/dev/null 2>&1 || sudo useradd -m labuser1
brown@myvis0612:~/linux-lab/unit04-permission$ id labuser2 >/dev/null 2>&1 || sudo useradd -m labuser2

# 使用 -aG 追加附加组；缺少 -a 时会替换原有附加组列表。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo usermod -aG labgroup labuser1
brown@myvis0612:~/linux-lab/unit04-permission$ sudo usermod -aG labgroup labuser2
brown@myvis0612:~/linux-lab/unit04-permission$ id labuser1
uid=1001(labuser1) gid=1002(labuser1) groups=1002(labuser1),1001(labgroup)
brown@myvis0612:~/linux-lab/unit04-permission$ id labuser2
uid=1002(labuser2) gid=1003(labuser2) groups=1003(labuser2),1001(labgroup)
brown@myvis0612:~/linux-lab/unit04-permission$ getent group labgroup
labgroup:x:1001:labuser2,labuser1

# ==================== 32. 使用 chown 和 chgrp 修改归属 ====================
# 创建所有权实验文件和目录。
brown@myvis0612:~/linux-lab/unit04-permission$ mkdir -p ownership/project
brown@myvis0612:~/linux-lab/unit04-permission$ printf 'owner test\n' > ownership/owner-test.txt
brown@myvis0612:~/linux-lab/unit04-permission$ printf 'group test\n' > ownership/group-test.txt
brown@myvis0612:~/linux-lab/unit04-permission$ printf 'project source\n' > ownership/project/main.txt
brown@myvis0612:~/linux-lab/unit04-permission$ cd ownership

# 只修改文件所有者，再用 stat 同时查看符号权限、数字权限、属主和属组。
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ sudo chown labuser1 owner-test.txt
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ stat -c '%A %a %U %G %n' owner-test.txt
-rw-rw-r-- 664 labuser1 brown owner-test.txt

# 同时修改所有者与所属组。
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ sudo chown labuser2:labgroup owner-test.txt
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ stat -c '%A %a %U %G %n' owner-test.txt
-rw-rw-r-- 664 labuser2 labgroup owner-test.txt

# “用户:”会将组设为该用户的登录组；chgrp 只修改所属组；“:组”也可只改组。
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ sudo chown labuser1: owner-test.txt
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ sudo chgrp labgroup group-test.txt
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ stat -c '%A %a %U %G %n' owner-test.txt group-test.txt
-rw-rw-r-- 664 labuser1 labuser1 owner-test.txt
-rw-rw-r-- 664 brown labgroup group-test.txt
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ sudo chown :brown group-test.txt

# -R 递归修改目录及其所有后代对象的归属。
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ sudo chown -R labuser1:labgroup project
brown@myvis0612:~/linux-lab/unit04-permission/ownership$ stat -c '%U %G %n' project project/main.txt
labuser1 labgroup project
labuser1 labgroup project/main.txt

# ==================== 33. 创建、设置密码并删除用户 ====================
# 创建 labuser3 并确认其 UID、主组、主目录和登录 Shell。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo useradd -m labuser3
brown@myvis0612:~/linux-lab/unit04-permission$ id labuser3
uid=1003(labuser3) gid=1004(labuser3) groups=1004(labuser3)
brown@myvis0612:~/linux-lab/unit04-permission$ getent passwd labuser3
labuser3:x:1003:1004::/home/labuser3:/bin/sh
brown@myvis0612:~/linux-lab/unit04-permission$ ls -ld /home/labuser3
drwxr-x--- 2 labuser3 labuser3 4096 Oct 10 03:35 /home/labuser3

# 设置密码并查询密码状态；P 表示已设置可用密码。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo passwd labuser3
passwd: password updated successfully
brown@myvis0612:~/linux-lab/unit04-permission$ sudo passwd -S labuser3
labuser3 P 2026-10-10 0 99999 7 -1

# 以 labuser3 身份创建文件，然后使用 userdel（未加 -r）删除账户。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser3 touch /home/labuser3/keep-test.txt
brown@myvis0612:~/linux-lab/unit04-permission$ sudo userdel labuser3
brown@myvis0612:~/linux-lab/unit04-permission$ id labuser3
id: 'labuser3': no such user

# 未使用 userdel -r，因此主目录仍在；原 UID/GID 已无法解析，只显示数字。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo ls -l /home/labuser3
total 0
-rw-r--r-- 1 1003 1004 0 Oct 10 06:40 keep-test.txt

# ==================== 34. 建立共享组目录并验证访问权限 ====================
# 创建独立的 devteam 组并把两个实验用户加入其中。
brown@myvis0612:~/linux-lab/unit04-permission$ getent group devteam >/dev/null || sudo groupadd devteam
brown@myvis0612:~/linux-lab/unit04-permission$ sudo usermod -aG devteam labuser1
brown@myvis0612:~/linux-lab/unit04-permission$ sudo usermod -aG devteam labuser2

# 创建共享目录。此时目录仍为 root:root 且权限为 755，组成员不能写入。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo mkdir -p /tmp/unit04-final/shared
brown@myvis0612:~/linux-lab/unit04-permission$ ls -ld /tmp/unit04-final/shared
drwxr-xr-x 2 root root 40 Oct 10 08:05 /tmp/unit04-final/shared

# 这是有意义的失败实验：labuser1 没有目录写权限，因此无法新建文件。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser1 bash -c 'echo "created by labuser1" > /tmp/unit04-final/shared/user1-data.txt'
bash: line 1: /tmp/unit04-final/shared/user1-data.txt: Permission denied

# 把目录所属组改为 labgroup，并赋予所有者和组完整权限。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo chown root:labgroup /tmp/unit04-final/shared
brown@myvis0612:~/linux-lab/unit04-permission$ sudo chmod 770 /tmp/unit04-final/shared
brown@myvis0612:~/linux-lab/unit04-permission$ ls -ld /tmp/unit04-final/shared
drwxrwx--- 2 root labgroup 40 Oct 10 08:05 /tmp/unit04-final/shared

# 两个组成员现在都可以创建文件，并能读取对方具有读取权限的文件。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser1 touch /tmp/unit04-final/shared/user1.txt
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser2 touch /tmp/unit04-final/shared/user2.txt
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser1 bash -c 'echo "created by labuser1" > /tmp/unit04-final/shared/user1.txt'
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser2 cat /tmp/unit04-final/shared/user1.txt
created by labuser1

# brown 不属于 labgroup，所以不借助 sudo 无法列出 770 的共享目录。
brown@myvis0612:~/linux-lab/unit04-permission$ ls -l /tmp/unit04-final/shared
ls: cannot open directory '/tmp/unit04-final/shared': Permission denied

# ==================== 35. 使用 setgid 继承共享目录的所属组 ====================
# 2770 中的首位 2 为 setgid；新文件会继承目录的所属组 labgroup。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo chmod 2770 /tmp/unit04-final/shared
brown@myvis0612:~/linux-lab/unit04-permission$ ls -ld /tmp/unit04-final/shared
drwxrws--- 2 root labgroup 80 Oct 10 08:26 /tmp/unit04-final/shared
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser1 touch /tmp/unit04-final/shared/user1-setgid.txt
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser2 touch /tmp/unit04-final/shared/user2-setgid.txt
brown@myvis0612:~/linux-lab/unit04-permission$ sudo ls -l /tmp/unit04-final/shared
total 4
-rw-r--r-- 1 labuser1 labgroup  0 Oct 10 08:48 user1-setgid.txt
-rw-r--r-- 1 labuser2 labgroup  0 Oct 10 08:48 user2-setgid.txt

# 非成员 nobody 没有任何目录权限，不能列出目录内容。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u nobody ls /tmp/unit04-final/shared
ls: cannot open directory '/tmp/unit04-final/shared': Permission denied

# ==================== 36. 结合 umask 验证组写权限 ====================
# 当前交互用户的 umask 为 0002；但 sudo -u 启动的进程可能使用不同环境和 umask。
brown@myvis0612:~/linux-lab/unit04-permission$ umask
0002

# labuser1 创建的文件实际为 644，因此同组的 labuser2 可以读但不能追加写入。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser1 bash -c 'echo "line from user1" > /tmp/unit04-final/shared/permission-test.txt'
brown@myvis0612:~/linux-lab/unit04-permission$ sudo ls -l /tmp/unit04-final/shared/permission-test.txt
-rw-r--r-- 1 labuser1 labgroup 16 Oct 10 09:21 /tmp/unit04-final/shared/permission-test.txt
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser2 bash -c 'echo "line from user2" >> /tmp/unit04-final/shared/permission-test.txt'
bash: line 1: /tmp/unit04-final/shared/permission-test.txt: Permission denied

# 给所有者和所属组读写权限后，labuser2 可以成功追加内容。
brown@myvis0612:~/linux-lab/unit04-permission$ sudo chmod 660 /tmp/unit04-final/shared/permission-test.txt
brown@myvis0612:~/linux-lab/unit04-permission$ sudo -u labuser2 bash -c 'echo "line from user2" >> /tmp/unit04-final/shared/permission-test.txt'
brown@myvis0612:~/linux-lab/unit04-permission$ sudo cat /tmp/unit04-final/shared/permission-test.txt
line from user1
line from user2
```
