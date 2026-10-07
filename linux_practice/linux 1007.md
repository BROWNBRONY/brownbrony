

```bash
# ==================== 1. 登录 Linux 与查看基础环境 ====================
# 从 Windows PowerShell 通过 2222 端口登录本机 Linux SSH 服务。
PS C:\Users\Administrator> ssh brown@127.0.0.1 -p 2222
brown@127.0.0.1's password:
Welcome to Ubuntu 26.04 LTS (GNU/Linux 7.0.0-22-generic x86_64)
# 显示当前登录用户名。
brown@myvis0612:~$ whoami
brown
# 显示当前所在目录的绝对路径。
brown@myvis0612:~$ pwd
/home/brown
# 列出当前目录中的文件和目录。
brown@myvis0612:~$ ls
s
# 以长格式列出全部内容，包括隐藏文件。
brown@myvis0612:~$ ls -la
total 44
drwxr-x--- 4 brown brown  4096 Jun 17 06:51 .
drwxr-xr-x 3 root  root   4096 Jun 12 09:48 ..
-rw-r--r-- 1 brown brown   220 Feb 13  2026 .bash_logout
-rw-r--r-- 1 brown brown  3771 Feb 13  2026 .bashrc
drwx------ 2 brown brown  4096 Jun 13 01:25 .cache
-rw------- 1 brown brown    44 Jun 17 06:51 .lesshst
-rw-r--r-- 1 brown brown   807 Feb 13  2026 .profile
drwx------ 2 brown brown  4096 Jun 12 09:52 .ssh
-rw-r--r-- 1 brown brown 11295 Jun 17 06:49 s
# 切换到当前用户的主目录。
brown@myvis0612:~$ cd ~
# 以长格式列出全部内容，包括隐藏文件。
brown@myvis0612:~$ ls -la
total 44
drwxr-x--- 4 brown brown  4096 Jun 17 06:51 .
drwxr-xr-x 3 root  root   4096 Jun 12 09:48 ..
-rw-r--r-- 1 brown brown   220 Feb 13  2026 .bash_logout
-rw-r--r-- 1 brown brown  3771 Feb 13  2026 .bashrc
drwx------ 2 brown brown  4096 Jun 13 01:25 .cache
-rw------- 1 brown brown    44 Jun 17 06:51 .lesshst
-rw-r--r-- 1 brown brown   807 Feb 13  2026 .profile
drwx------ 2 brown brown  4096 Jun 12 09:52 .ssh
-rw-r--r-- 1 brown brown 11295 Jun 17 06:49 s
# 切换到当前用户的主目录。
brown@myvis0612:~$ cd ~

# ==================== 2. 建立 Linux 实验工作区 ====================
# 创建目录：linux-lab。
brown@myvis0612:~$ mkdir linux-lab
# 切换到目录：linux-lab。
brown@myvis0612:~$ cd linux-lab
# 显示当前所在目录的绝对路径。
brown@myvis0612:~/linux-lab$ pwd
/home/brown/linux-lab
# 创建目录：files dirs backup work。
brown@myvis0612:~/linux-lab$ mkdir files dirs backup work
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab$ ls -l
total 16
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 backup
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 dirs
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 files
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 work
# 以长格式查看目录或路径本身：files dirs backup work。
brown@myvis0612:~/linux-lab$ ls -ld files dirs backup work
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 backup
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 dirs
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 files
drwxrwxr-x 2 brown brown 4096 Oct  6 06:22 work

# ==================== 3. 创建普通目录和多级目录 ====================
# 切换到目录：~/linux-lab/dirs。
brown@myvis0612:~/linux-lab$ cd ~/linux-lab/dirs
# 创建目录：test1。
brown@myvis0612:~/linux-lab/dirs$ mkdir test1
# 创建目录：test2。
brown@myvis0612:~/linux-lab/dirs$ mkdir test2
# 创建目录：test3。
brown@myvis0612:~/linux-lab/dirs$ mkdir test3
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/dirs$ ls -l
total 12
drwxrwxr-x 2 brown brown 4096 Oct  6 06:28 test1
drwxrwxr-x 2 brown brown 4096 Oct  6 06:28 test2
drwxrwxr-x 2 brown brown 4096 Oct  6 06:28 test3
# 创建目录：test1/sub1。
brown@myvis0612:~/linux-lab/dirs$ mkdir test1/sub1
# 创建目录：test2/sub2。
brown@myvis0612:~/linux-lab/dirs$ mkdir test2/sub2
# 创建目录：test3/sub3。
brown@myvis0612:~/linux-lab/dirs$ mkdir test3/sub3
# 创建目录：test3/sub4。
brown@myvis0612:~/linux-lab/dirs$ mkdir test3/sub4
# 列出与模式匹配的内容：-R。
brown@myvis0612:~/linux-lab/dirs$ ls -R
.:
test1  test2  test3

./test1:
sub1

./test1/sub1:

./test2:
sub2

./test2/sub2:

./test3:
sub3  sub4

./test3/sub3:

./test3/sub4:
# 切换到目录：~/linux-lab/dirs。
brown@myvis0612:~/linux-lab/dirs$ cd ~/linux-lab/dirs
# 递归创建目录，缺失的父目录一并创建：project/src/java。
brown@myvis0612:~/linux-lab/dirs$ mkdir -p project/src/java
# 递归创建目录，缺失的父目录一并创建：project/src/python。
brown@myvis0612:~/linux-lab/dirs$ mkdir -p project/src/python
# 递归创建目录，缺失的父目录一并创建：project/docs/manual。
brown@myvis0612:~/linux-lab/dirs$ mkdir -p project/docs/manual
# 递归创建目录，缺失的父目录一并创建：project/config/database。
brown@myvis0612:~/linux-lab/dirs$ mkdir -p project/config/database
# 列出与模式匹配的内容：-R project。
brown@myvis0612:~/linux-lab/dirs$ ls -R project
project:
config  docs  src

project/config:
database

project/config/database:

project/docs:
manual

project/docs/manual:

project/src:
java  python

project/src/java:

project/src/python:
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/dirs$ ls -l
total 16
drwxrwxr-x 5 brown brown 4096 Oct  6 06:33 project
drwxrwxr-x 3 brown brown 4096 Oct  6 06:33 test1
drwxrwxr-x 3 brown brown 4096 Oct  6 06:33 test2
drwxrwxr-x 4 brown brown 4096 Oct  6 06:33 test3
# 以长格式查看目录或路径本身：project。
brown@myvis0612:~/linux-lab/dirs$ ls -ld project
drwxrwxr-x 5 brown brown 4096 Oct  6 06:33 project
# 以长格式查看匹配项或目录内容：project。
brown@myvis0612:~/linux-lab/dirs$ ls -l project
total 12
drwxrwxr-x 3 brown brown 4096 Oct  6 06:33 config
drwxrwxr-x 3 brown brown 4096 Oct  6 06:33 docs
drwxrwxr-x 4 brown brown 4096 Oct  6 06:33 src
# 切换到目录：~/linux-lab/dirs。
brown@myvis0612:~/linux-lab/dirs$ cd ~/linux-lab/dirs

# ==================== 4. 练习删除空目录和文件 ====================
# 创建目录：empty1。
brown@myvis0612:~/linux-lab/dirs$ mkdir empty1
# 删除空目录：empty1。
brown@myvis0612:~/linux-lab/dirs$ rmdir empty1
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/dirs$ ls -l
total 16
drwxrwxr-x 5 brown brown 4096 Oct  6 06:33 project
drwxrwxr-x 3 brown brown 4096 Oct  6 06:33 test1
drwxrwxr-x 3 brown brown 4096 Oct  6 06:33 test2
drwxrwxr-x 4 brown brown 4096 Oct  6 06:33 test3
# 创建目录：nonempty。
brown@myvis0612:~/linux-lab/dirs$ mkdir nonempty
# 创建空文件；已存在时更新其时间戳：nonempty/test.txt。
brown@myvis0612:~/linux-lab/dirs$ touch nonempty/test.txt
# 以长格式查看匹配项或目录内容：nonempty。
brown@myvis0612:~/linux-lab/dirs$ ls -l nonempty
total 0
-rw-rw-r-- 1 brown brown 0 Oct  6 06:37 test.txt
# 删除文件：nonempty/test.txt。
brown@myvis0612:~/linux-lab/dirs$ rm nonempty/test.txt
# 以长格式查看匹配项或目录内容：nonempty。
brown@myvis0612:~/linux-lab/dirs$ ls -l nonempty
total 0
# 切换到目录：~/linux-lab。
brown@myvis0612:~/linux-lab/dirs$ cd ~/linux-lab

# ==================== 5. 区分查看目录内容与目录本身 ====================
# 创建目录：example。
brown@myvis0612:~/linux-lab$ mkdir example
# 创建空文件；已存在时更新其时间戳：example/file.txt。
brown@myvis0612:~/linux-lab$ touch example/file.txt
# 以长格式查看匹配项或目录内容：example。
brown@myvis0612:~/linux-lab$ ls -l example
total 0
-rw-rw-r-- 1 brown brown 0 Oct  6 06:39 file.txt
# 以长格式查看目录或路径本身：example。
brown@myvis0612:~/linux-lab$ ls -ld example
drwxrwxr-x 2 brown brown 4096 Oct  6 06:39 example
# 列出与模式匹配的内容：-la example。
brown@myvis0612:~/linux-lab$ ls -la example
total 8
drwxrwxr-x 2 brown brown 4096 Oct  6 06:39 .
drwxrwxr-x 7 brown brown 4096 Oct  6 06:39 ..
-rw-rw-r-- 1 brown brown    0 Oct  6 06:39 file.txt
# 以长格式查看目录本身及隐藏属性：example。
brown@myvis0612:~/linux-lab$ ls -lad example
drwxrwxr-x 2 brown brown 4096 Oct  6 06:39 example
# 切换到目录：~/linux-lab/files。
brown@myvis0612:~/linux-lab$ cd ~/linux-lab/files

# ==================== 6. 创建通配符练习文件 ====================
# 创建空文件；已存在时更新其时间戳：a.txt。
brown@myvis0612:~/linux-lab/files$ touch a.txt
# 创建空文件；已存在时更新其时间戳：b.txt。
brown@myvis0612:~/linux-lab/files$ touch b.txt
# 创建空文件；已存在时更新其时间戳：c.txt。
brown@myvis0612:~/linux-lab/files$ touch c.txt
# 创建空文件；已存在时更新其时间戳：aa.txt。
brown@myvis0612:~/linux-lab/files$ touch aa.txt
# 创建空文件；已存在时更新其时间戳：ab.txt。
brown@myvis0612:~/linux-lab/files$ touch ab.txt
# 创建空文件；已存在时更新其时间戳：ac.txt。
brown@myvis0612:~/linux-lab/files$ touch ac.txt
# 创建空文件；已存在时更新其时间戳：aaa.txt。
brown@myvis0612:~/linux-lab/files$ touch aaa.txt
# 创建空文件；已存在时更新其时间戳：abc.txt。
brown@myvis0612:~/linux-lab/files$ touch abc.txt
# 创建空文件；已存在时更新其时间戳：a1.txt。
brown@myvis0612:~/linux-lab/files$ touch a1.txt
# 创建空文件；已存在时更新其时间戳：a2.txt。
brown@myvis0612:~/linux-lab/files$ touch a2.txt
# 创建空文件；已存在时更新其时间戳：a3.txt。
brown@myvis0612:~/linux-lab/files$ touch a3.txt
# 创建空文件；已存在时更新其时间戳：b1.txt。
brown@myvis0612:~/linux-lab/files$ touch b1.txt
# 创建空文件；已存在时更新其时间戳：b2.txt。
brown@myvis0612:~/linux-lab/files$ touch b2.txt
# 创建空文件；已存在时更新其时间戳：b3.txt。
brown@myvis0612:~/linux-lab/files$ touch b3.txt
# 创建空文件；已存在时更新其时间戳：file1.txt。
brown@myvis0612:~/linux-lab/files$ touch file1.txt
# 创建空文件；已存在时更新其时间戳：file2.txt。
brown@myvis0612:~/linux-lab/files$ touch file2.txt
# 创建空文件；已存在时更新其时间戳：file3.txt。
brown@myvis0612:~/linux-lab/files$ touch file3.txt
# 创建空文件；已存在时更新其时间戳：file10.txt。
brown@myvis0612:~/linux-lab/files$ touch file10.txt
# 创建空文件；已存在时更新其时间戳：file20.txt。
brown@myvis0612:~/linux-lab/files$ touch file20.txt
# 列出与模式匹配的内容：-1。
brown@myvis0612:~/linux-lab/files$ ls -1
a.txt
a1.txt
a2.txt
a3.txt
aa.txt
aaa.txt
ab.txt
abc.txt
ac.txt
b.txt
b1.txt
b2.txt
b3.txt
c.txt
file1.txt
file10.txt
file2.txt
file20.txt
file3.txt
# 切换到目录：~/linux-lab/files。
brown@myvis0612:~/linux-lab/files$ cd ~/linux-lab/files
# 列出与模式匹配的内容：-1。
brown@myvis0612:~/linux-lab/files$ ls -1
a.txt
a1.txt
a2.txt
a3.txt
aa.txt
aaa.txt
ab.txt
abc.txt
ac.txt
b.txt
b1.txt
b2.txt
b3.txt
c.txt
file1.txt
file10.txt
file2.txt
file20.txt
file3.txt
# 切换到目录：~/linux-lab/files。
brown@myvis0612:~/linux-lab/files$ cd ~/linux-lab/files

# ==================== 7. 使用 Shell 通配符筛选文件 ====================
# 每行一个名称，列出匹配项：*.txt。
brown@myvis0612:~/linux-lab/files$ ls -1 *.txt
a.txt
a1.txt
a2.txt
a3.txt
aa.txt
aaa.txt
ab.txt
abc.txt
ac.txt
b.txt
b1.txt
b2.txt
b3.txt
c.txt
file1.txt
file10.txt
file2.txt
file20.txt
file3.txt
# 以长格式查看匹配项或目录内容：a*。
brown@myvis0612:~/linux-lab/files$ ls -l a*
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aaa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ab.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 abc.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ac.txt
# 以长格式查看匹配项或目录内容：ab*。
brown@myvis0612:~/linux-lab/files$ ls -l ab*
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ab.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 abc.txt
# 以长格式查看匹配项或目录内容：*1.txt。
brown@myvis0612:~/linux-lab/files$ ls -l *1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file1.txt
# 以长格式查看匹配项或目录内容：file*。
brown@myvis0612:~/linux-lab/files$ ls -l file*
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file10.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file20.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file3.txt
# 以长格式查看匹配项或目录内容：?.txt。
brown@myvis0612:~/linux-lab/files$ ls -l ?.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 c.txt
# 以长格式查看匹配项或目录内容：??.txt。
brown@myvis0612:~/linux-lab/files$ ls -l ??.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ab.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ac.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b3.txt
# 以长格式查看匹配项或目录内容：a?.txt。
brown@myvis0612:~/linux-lab/files$ ls -l a?.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ab.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ac.txt
# 以长格式查看匹配项或目录内容：[abc].txt。
brown@myvis0612:~/linux-lab/files$ ls -l [abc].txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 c.txt
# 以长格式查看匹配项或目录内容：[abc][abc].txt。
brown@myvis0612:~/linux-lab/files$ ls -l [abc][abc].txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ab.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ac.txt
# 以长格式查看匹配项或目录内容：[abc]*.txt。
brown@myvis0612:~/linux-lab/files$ ls -l [abc]*.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aaa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ab.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 abc.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ac.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 b3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 c.txt
# 以长格式查看匹配项或目录内容：a[1-9].txt。
brown@myvis0612:~/linux-lab/files$ ls -l a[1-9].txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a3.txt
# 以长格式查看匹配项或目录内容：file[0-9].txt。
brown@myvis0612:~/linux-lab/files$ ls -l file[0-9].txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 file3.txt
# 每行一个名称，列出匹配项：[^ab].txt。
brown@myvis0612:~/linux-lab/files$ ls -1 [^ab].txt
c.txt
# 每行一个名称，列出匹配项：[^a].txt。
brown@myvis0612:~/linux-lab/files$ ls -1 [^a].txt
b.txt
c.txt
# 以长格式查看匹配项或目录内容：a[^1].txt。
brown@myvis0612:~/linux-lab/files$ ls -l a[^1].txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 a3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 aa.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ab.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 07:04 ac.txt
# 切换到目录：~/linux-lab。
brown@myvis0612:~/linux-lab/files$ cd ~/linux-lab

# ==================== 8. 使用通配符批量复制文件 ====================
# 递归创建目录，缺失的父目录一并创建：work/glob-source。
brown@myvis0612:~/linux-lab$ mkdir -p work/glob-source
# 递归创建目录，缺失的父目录一并创建：work/glob-backup。
brown@myvis0612:~/linux-lab$ mkdir -p work/glob-backup
# 复制文件或匹配到的文件：从 ~/linux-lab/files/*.txt 到 ~/linux-lab/work/glob-source/。
brown@myvis0612:~/linux-lab$ cp ~/linux-lab/files/*.txt ~/linux-lab/work/glob-source/
# 每行一个名称，列出匹配项：~/linux-lab/work/glob-source。
brown@myvis0612:~/linux-lab$ ls -1 ~/linux-lab/work/glob-source
a.txt
a1.txt
a2.txt
a3.txt
aa.txt
aaa.txt
ab.txt
abc.txt
ac.txt
b.txt
b1.txt
b2.txt
b3.txt
c.txt
file1.txt
file10.txt
file2.txt
file20.txt
file3.txt
# 复制文件或匹配到的文件：从 ~/linux-lab/files/a*.txt 到 ~/linux-lab/work/glob-backup/。
brown@myvis0612:~/linux-lab$ cp ~/linux-lab/files/a*.txt ~/linux-lab/work/glob-backup/
# 每行一个名称，列出匹配项：~/linux-lab/work/glob-backup。
brown@myvis0612:~/linux-lab$ ls -1 ~/linux-lab/work/glob-backup
a.txt
a1.txt
a2.txt
a3.txt
aa.txt
aaa.txt
ab.txt
abc.txt
ac.txt
# 切换到目录：~/linux-lab/work。
brown@myvis0612:~/linux-lab$ cd ~/linux-lab/work

# ==================== 9. 文件写入、追加与复制 ====================
# 把内容覆盖写入文件 original.txt。
brown@myvis0612:~/linux-lab/work$ echo "original file" > original.txt
# 显示文件内容：original.txt。
brown@myvis0612:~/linux-lab/work$ cat original.txt
original file
# 复制文件或匹配到的文件：从 original.txt 到 ../backup/copy.txt。
brown@myvis0612:~/linux-lab/work$ cp original.txt ../backup/copy.txt
# 以长格式查看匹配项或目录内容：../backup/。
brown@myvis0612:~/linux-lab/work$ ls -l ../backup/
total 4
-rw-rw-r-- 1 brown brown 14 Oct  6 07:29 copy.txt
# 显示文件内容：../backup/copy.txt。
brown@myvis0612:~/linux-lab/work$ cat ../backup/copy.txt
original file
# 把内容追加写入文件 original.txt。
brown@myvis0612:~/linux-lab/work$ echo "second line" >> original.txt
# 显示文件内容：original.txt。
brown@myvis0612:~/linux-lab/work$ cat original.txt
original file
second line
# 显示文件内容：../backup/copy.txt。
brown@myvis0612:~/linux-lab/work$ cat ../backup/copy.txt
original file
# 切换到目录：~/linux-lab/work。
brown@myvis0612:~/linux-lab/work$ cd ~/linux-lab/work

# ==================== 10. 建立项目结构并使用 find 查找 ====================
# 递归创建目录，缺失的父目录一并创建：project/src。
brown@myvis0612:~/linux-lab/work$ mkdir -p project/src
# 递归创建目录，缺失的父目录一并创建：project/docs。
brown@myvis0612:~/linux-lab/work$ mkdir -p project/docs
# 递归创建目录，缺失的父目录一并创建：project/config。
brown@myvis0612:~/linux-lab/work$ mkdir -p project/config
# 把内容覆盖写入文件 project/src/main.txt。
brown@myvis0612:~/linux-lab/work$ echo "main source" > project/src/main.txt
# 把内容覆盖写入文件 project/docs/readme.txt。
brown@myvis0612:~/linux-lab/work$ echo "documentation" > project/docs/readme.txt
# 把内容覆盖写入文件 project/config/app.conf。
brown@myvis0612:~/linux-lab/work$ echo "configuration" > project/config/app.conf
# 查找指定路径下的全部普通文件：project。
brown@myvis0612:~/linux-lab/work$ find project -type f
project/config/app.conf
project/src/main.txt
project/docs/readme.txt
# 查找指定路径下的全部目录：project。
brown@myvis0612:~/linux-lab/work$ find project -type d
project
project/config
project/src
project/docs
# 查找指定路径下的全部符号链接：project。
brown@myvis0612:~/linux-lab/work$ find project -type l
# 查找指定路径下的全部普通文件：project。
brown@myvis0612:~/linux-lab/work$ find project -type f
project/config/app.conf
project/src/main.txt
project/docs/readme.txt
# 切换到目录：~/linux-lab/work。
brown@myvis0612:~/linux-lab/work$ cd ~/linux-lab/work

# ==================== 11. 使用 cp -a 备份目录 ====================
# 创建目录：archive-test。
brown@myvis0612:~/linux-lab/work$ mkdir archive-test
# 把内容覆盖写入文件 archive-test/test.txt。
brown@myvis0612:~/linux-lab/work$ echo "archive test" > archive-test/test.txt
# 切换到目录：~/linux-lab/work。
brown@myvis0612:~/linux-lab/work$ cd ~/linux-lab/work
# 递归复制并尽量保留属性：从 archive-test 到 ../backup/。
brown@myvis0612:~/linux-lab/work$ cp -a archive-test ../backup/
# 查找指定路径下的全部普通文件：../backup/archive-test。
brown@myvis0612:~/linux-lab/work$ find ../backup/archive-test -type f
../backup/archive-test/test.txt
# 显示文件内容：../backup/archive-test/test.txt。
brown@myvis0612:~/linux-lab/work$ cat ../backup/archive-test/test.txt
archive test

# ==================== 12. 创建并递归删除目录树 ====================
# 递归创建目录，缺失的父目录一并创建：delete-test/sub1/sub2。
brown@myvis0612:~/linux-lab/work$ mkdir -p delete-test/sub1/sub2
# 创建空文件；已存在时更新其时间戳：delete-test/a.txt。
brown@myvis0612:~/linux-lab/work$ touch delete-test/a.txt
# 创建空文件；已存在时更新其时间戳：delete-test/sub1/b.txt。
brown@myvis0612:~/linux-lab/work$ touch delete-test/sub1/b.txt
# 创建空文件；已存在时更新其时间戳：delete-test/sub1/sub2/c.txt。
brown@myvis0612:~/linux-lab/work$ touch delete-test/sub1/sub2/c.txt
# 递归打印路径下的全部条目：delete-test。
brown@myvis0612:~/linux-lab/work$ find delete-test -print
delete-test
delete-test/sub1
delete-test/sub1/b.txt
delete-test/sub1/sub2
delete-test/sub1/sub2/c.txt
delete-test/a.txt
# 递归删除目录树：delete-test。
# 注意：这是递归删除操作，执行前必须再次确认目标路径。
brown@myvis0612:~/linux-lab/work$ rm -r delete-test
# 切换到目录：~/linux-lab/work。
brown@myvis0612:~/linux-lab/work$ cd ~/linux-lab/work

# ==================== 13. 移动文件 ====================
# 创建空文件；已存在时更新其时间戳：move-source.txt。
brown@myvis0612:~/linux-lab/work$ touch move-source.txt
# 移动或重命名：从 move-source.txt 到 ../backup/。
brown@myvis0612:~/linux-lab/work$ mv move-source.txt ../backup/
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/work$ ls -l
total 20
drwxrwxr-x 2 brown brown 4096 Oct  6 07:39 archive-test
drwxrwxr-x 2 brown brown 4096 Oct  6 07:28 glob-backup
drwxrwxr-x 2 brown brown 4096 Oct  6 07:27 glob-source
-rw-rw-r-- 1 brown brown   26 Oct  6 07:30 original.txt
drwxrwxr-x 5 brown brown 4096 Oct  6 07:32 project
# 切换到目录：~/linux-lab/work。
brown@myvis0612:~/linux-lab/work$ cd ~/linux-lab/work
# 创建空文件；已存在时更新其时间戳：move-source.txt。
brown@myvis0612:~/linux-lab/work$ touch move-source.txt
# 切换到目录：~/linux-lab/work。
brown@myvis0612:~/linux-lab/work$ cd ~/linux-lab/work

# ==================== 14. 使用花括号批量创建文件 ====================
# 创建目录：batch。
brown@myvis0612:~/linux-lab/work$ mkdir batch
# 切换到目录：batch。
brown@myvis0612:~/linux-lab/work$ cd batch
# 创建空文件；已存在时更新其时间戳：file{1..10}.txt。
brown@myvis0612:~/linux-lab/work/batch$ touch file{1..10}.txt
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/work/batch$ ls -l
total 0
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file10.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file4.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file5.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file6.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file7.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file8.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file9.txt
# 创建空文件；已存在时更新其时间戳：number{01..10}.txt。
brown@myvis0612:~/linux-lab/work/batch$ touch number{01..10}.txt
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/work/batch$ ls -l
total 0
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file10.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file4.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file5.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file6.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file7.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file8.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file9.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number01.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number02.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number03.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number04.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number05.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number06.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number07.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number08.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number09.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number10.txt
# 创建空文件；已存在时更新其时间戳：date{A..E}.txt。
brown@myvis0612:~/linux-lab/work/batch$ touch date{A..E}.txt
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/work/batch$ ls -l
total 0
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateA.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateB.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateC.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateD.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateE.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file10.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file4.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file5.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file6.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file7.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file8.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file9.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number01.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number02.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number03.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number04.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number05.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number06.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number07.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number08.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number09.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number10.txt
# 创建空文件；已存在时更新其时间戳：test{1..5}_{a..c}.txt。
brown@myvis0612:~/linux-lab/work/batch$ touch test{1..5}_{a..c}.txt
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/work/batch$ ls -l
total 0
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateA.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateB.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateC.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateD.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:25 dateE.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file1.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file10.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file2.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file3.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file4.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file5.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file6.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file7.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file8.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:22 file9.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number01.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number02.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number03.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number04.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number05.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number06.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number07.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number08.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number09.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:24 number10.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test1_a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test1_b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test1_c.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test2_a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test2_b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test2_c.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test3_a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test3_b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test3_c.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test4_a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test4_b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test4_c.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test5_a.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test5_b.txt
-rw-rw-r-- 1 brown brown 0 Oct  6 08:34 test5_c.txt
# 统计 ls -l 输出的总行数。
brown@myvis0612:~/linux-lab/work/batch$ ls -l | wc -l
41
# 切换到目录：~/linux-lab。
brown@myvis0612:~/linux-lab/work/batch$ cd ~/linux-lab

# ==================== 15. 使用 Here Document 与 Vim ====================
# 递归创建目录，缺失的父目录一并创建：vim-lab。
brown@myvis0612:~/linux-lab$ mkdir -p vim-lab
# 切换到目录：vim-lab。
brown@myvis0612:~/linux-lab$ cd vim-lab
# 使用 Here Document 将后续多行内容写入 practice.txt。
brown@myvis0612:~/linux-lab/vim-lab$ cat > practice.txt <<'EOF'
> Line 1: Linux
> Line 2: AWS
> Line 3: Docker
> Line 4: Kubernetes
> Line 5: Terraform
> Line 6: Ansible
> Line 7: Git
> Line 8: GitHub
> Line 9: Python
> Line 10: Bash
> Line 11: Networking
> Line 12: Security
> Line 13: Monitoring
> Line 14: Prometheus
> Line 15: Grafana
> EOF
# 显示文件内容：practice.txt。
brown@myvis0612:~/linux-lab/vim-lab$ cat practice.txt
Line 1: Linux
Line 2: AWS
Line 3: Docker
Line 4: Kubernetes
Line 5: Terraform
Line 6: Ansible
Line 7: Git
Line 8: GitHub
Line 9: Python
Line 10: Bash
Line 11: Networking
Line 12: Security
Line 13: Monitoring
Line 14: Prometheus
Line 15: Grafana
# 使用 Vim 打开并编辑文件：practice.txt。
brown@myvis0612:~/linux-lab/vim-lab$ vim practice.txt
# 切换到目录：~/linux-lab。
brown@myvis0612:~/linux-lab/vim-lab$ cd ~/linux-lab

# ==================== 16. Unit 03 综合练习：初始化目录 ====================
# 强制递归删除目录树：unit03-final。
# 注意：这是递归删除操作，执行前必须再次确认目标路径。
brown@myvis0612:~/linux-lab$ rm -rf unit03-final
# 创建目录：unit03-final。
brown@myvis0612:~/linux-lab$ mkdir unit03-final
# 切换到目录：unit03-final。
brown@myvis0612:~/linux-lab$ cd unit03-final
# 创建目录：source。
brown@myvis0612:~/linux-lab/unit03-final$ mkdir source
# 创建目录：work。
brown@myvis0612:~/linux-lab/unit03-final$ mkdir work
# 创建目录：result。
brown@myvis0612:~/linux-lab/unit03-final$ mkdir result
# 创建目录：special。
brown@myvis0612:~/linux-lab/unit03-final$ mkdir special
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/unit03-final$ ls -l
total 16
drwxrwxr-x 2 brown brown 4096 Oct  7 02:05 result
drwxrwxr-x 2 brown brown 4096 Oct  7 02:05 source
drwxrwxr-x 2 brown brown 4096 Oct  7 02:05 special
drwxrwxr-x 2 brown brown 4096 Oct  7 02:05 work
# 显示当前所在目录的绝对路径。
brown@myvis0612:~/linux-lab/unit03-final$ pwd
/home/brown/linux-lab/unit03-final
# 切换到目录：~/linux-lab/unit03-final/source。
brown@myvis0612:~/linux-lab/unit03-final$ cd ~/linux-lab/unit03-final/source

# ==================== 17. 综合练习：文件、目录与符号链接 ====================
# 把内容覆盖写入文件 text.txt。
brown@myvis0612:~/linux-lab/unit03-final/source$ echo "hello linux" > text.txt
# 创建目录：directory。
brown@myvis0612:~/linux-lab/unit03-final/source$ mkdir directory
# 创建符号链接 symlink.txt，使其指向 text.txt。
brown@myvis0612:~/linux-lab/unit03-final/source$ ln -s text.txt symlink.txt
# 创建空文件；已存在时更新其时间戳：empty.txt。
brown@myvis0612:~/linux-lab/unit03-final/source$ touch empty.txt
# 列出与模式匹配的内容：-l。
brown@myvis0612:~/linux-lab/unit03-final/source$ ls -l
total 8
drwxrwxr-x 2 brown brown 4096 Oct  7 02:09 directory
-rw-rw-r-- 1 brown brown    0 Oct  7 02:09 empty.txt
lrwxrwxrwx 1 brown brown    8 Oct  7 02:09 symlink.txt -> text.txt
-rw-rw-r-- 1 brown brown   12 Oct  7 02:09 text.txt
# 切换到目录：~/linux-lab/unit03-final/work。
brown@myvis0612:~/linux-lab/unit03-final/source$ cd ~/linux-lab/unit03-final/work

# ==================== 18. 综合练习：创建文件并匹配文件名 ====================
# 创建空文件；已存在时更新其时间戳：app1.txt app2.txt app3.txt app4.txt app5.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ touch app1.txt app2.txt app3.txt app4.txt app5.txt
# 创建空文件；已存在时更新其时间戳：appA.txt appB.txt appC.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ touch appA.txt appB.txt appC.txt
# 创建空文件；已存在时更新其时间戳：log1.txt log2.txt log3.log。
brown@myvis0612:~/linux-lab/unit03-final/work$ touch log1.txt log2.txt log3.log
# 创建空文件；已存在时更新其时间戳：data01.txt data02.txt data03.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ touch data01.txt data02.txt data03.txt
# 列出与模式匹配的内容：app*。
brown@myvis0612:~/linux-lab/unit03-final/work$ ls app*
app1.txt  app2.txt  app3.txt  app4.txt  app5.txt  appA.txt  appB.txt  appC.txt
# 列出与模式匹配的内容：app?.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ ls app?.txt
app1.txt  app2.txt  app3.txt  app4.txt  app5.txt  appA.txt  appB.txt  appC.txt
# 列出与模式匹配的内容：app[123].txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ ls app[123].txt
app1.txt  app2.txt  app3.txt
# 列出与模式匹配的内容：app[1-5].???。
brown@myvis0612:~/linux-lab/unit03-final/work$ ls app[1-5].???
app1.txt  app2.txt  app3.txt  app4.txt  app5.txt
# 列出与模式匹配的内容：app[!1-3].txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ ls app[!1-3].txt
app4.txt  app5.txt  appA.txt  appB.txt  appC.txt
# 列出与模式匹配的内容：app[^1-3].txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ ls app[^1-3].txt
app4.txt  app5.txt  appA.txt  appB.txt  appC.txt
# 切换到目录：~/linux-lab/unit03-final/result。
brown@myvis0612:~/linux-lab/unit03-final/work$ cd ~/linux-lab/unit03-final/result

# ==================== 19. 综合练习：按类型分类复制文件 ====================
# 创建目录：logs。
brown@myvis0612:~/linux-lab/unit03-final/result$ mkdir logs
# 复制文件或匹配到的文件：从 ../work/*.log 到 logs/。
brown@myvis0612:~/linux-lab/unit03-final/result$ cp ../work/*.log logs/
# 以长格式查看匹配项或目录内容：logs。
brown@myvis0612:~/linux-lab/unit03-final/result$ ls -l logs
total 0
-rw-rw-r-- 1 brown brown 0 Oct  7 03:12 log3.log
# 创建目录：data。
brown@myvis0612:~/linux-lab/unit03-final/result$ mkdir data
# 复制文件或匹配到的文件：从 ../work/data*.txt 到 data/。
brown@myvis0612:~/linux-lab/unit03-final/result$ cp ../work/data*.txt data/
# 以长格式查看匹配项或目录内容：data。
brown@myvis0612:~/linux-lab/unit03-final/result$ ls -l data
total 0
-rw-rw-r-- 1 brown brown 0 Oct  7 03:14 data01.txt
-rw-rw-r-- 1 brown brown 0 Oct  7 03:14 data02.txt
-rw-rw-r-- 1 brown brown 0 Oct  7 03:14 data03.txt
# 切换到目录：~/linux-lab/unit03-final/work。
brown@myvis0612:~/linux-lab/unit03-final/result$ cd ~/linux-lab/unit03-final/work

# ==================== 20. 综合练习：创建并备份项目目录 ====================
# 创建目录：project。
brown@myvis0612:~/linux-lab/unit03-final/work$ mkdir project
# 创建目录：project/src。
brown@myvis0612:~/linux-lab/unit03-final/work$ mkdir project/src
# 创建目录：project/docs。
brown@myvis0612:~/linux-lab/unit03-final/work$ mkdir project/docs
# 创建目录：project/config。
brown@myvis0612:~/linux-lab/unit03-final/work$ mkdir project/config
# 把内容覆盖写入文件 project/src/main.c。
brown@myvis0612:~/linux-lab/unit03-final/work$ echo "main program" > project/src/main.c
# 把内容覆盖写入文件 project/docs/readme.md。
brown@myvis0612:~/linux-lab/unit03-final/work$ echo "documentation" > project/docs/readme.md
# 把内容覆盖写入文件 project/config/app.conf。
brown@myvis0612:~/linux-lab/unit03-final/work$ echo "port=8080" > project/config/app.conf
# 查找指定路径下的全部普通文件：project。
brown@myvis0612:~/linux-lab/unit03-final/work$ find project -type f
project/config/app.conf
project/src/main.c
project/docs/readme.md
# 切换到目录：~/linux-lab/unit03-final/result。
brown@myvis0612:~/linux-lab/unit03-final/work$ cd ~/linux-lab/unit03-final/result
# 递归复制并尽量保留属性：从 ../work/project 到 project-backup。
brown@myvis0612:~/linux-lab/unit03-final/result$ cp -a ../work/project project-backup
# 切换到目录：~/linux-lab/unit03-final/result。
brown@myvis0612:~/linux-lab/unit03-final/result$ cd ~/linux-lab/unit03-final/result
# 查找指定路径下的全部普通文件：project-backup。
brown@myvis0612:~/linux-lab/unit03-final/result$ find project-backup -type f
project-backup/config/app.conf
project-backup/src/main.c
project-backup/docs/readme.md
# 切换到目录：~/linux-lab/unit03-final/work。
brown@myvis0612:~/linux-lab/unit03-final/result$ cd ~/linux-lab/unit03-final/work

# ==================== 21. 综合练习：覆盖写入与追加写入 ====================
# 把内容覆盖写入文件 output.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ echo "line 1" > output.txt
# 显示文件内容：output.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ cat output.txt
line 1
# 把内容追加写入文件 output.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ echo "line 2" >> output.txt
# 把内容追加写入文件 output.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ echo "line 3" >> output.txt
# 显示文件内容：output.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ cat output.txt
line 1
line 2
line 3
# 把内容覆盖写入文件 output.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ echo "new line 1" > output.txt
# 显示文件内容：output.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ cat output.txt
new line 1

# ==================== 22. 综合练习：生成序列并截取文件内容 ====================
# 生成数字序列并覆盖写入文件 numbers.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ seq 1 20 > numbers.txt
# 显示文件内容：numbers.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ cat numbers.txt
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
# 显示 numbers.txt 的前 5 行。
brown@myvis0612:~/linux-lab/unit03-final/work$ head -n 5 numbers.txt
1
2
3
4
5
# 显示 numbers.txt 的后 10 行。
brown@myvis0612:~/linux-lab/unit03-final/work$ tail -n 10 numbers.txt
11
12
13
14
15
16
17
18
19
20
# 提取 numbers.txt 的前 5 行并覆盖写入 first5.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ head -n 5 numbers.txt > first5.txt
# 提取 numbers.txt 的后 5 行并追加到 first5.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ tail -n 5 numbers.txt >> first5.txt
# 显示文件内容：first5.txt。
brown@myvis0612:~/linux-lab/unit03-final/work$ cat first5.txt
1
2
3
4
5
16
17
18
19
20
# 切换到目录：~/linux-lab/unit03-final/work。
brown@myvis0612:~/linux-lab/unit03-final/work$ cd ~/linux-lab/unit03-final/work

# ==================== 23. 综合练习：统计文件数量 ====================
# 查找全部普通文件并统计数量。
brown@myvis0612:~/linux-lab/unit03-final/work$ find . -type f | wc -l
20
# 查找 .txt 普通文件并统计数量。
brown@myvis0612:~/linux-lab/unit03-final/work$ find . -type f | grep '\.txt$' | wc -l
16
```

