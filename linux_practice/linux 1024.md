```bash
# ==================== 50. 查看当前 Shell 与 Bash 环境 ====================
# 查看主目录内容和当前用户的默认 Shell。
brown@myvis0612:/$ ls -l "$HOME"
total 16
drwxrwxr-x 12 brown brown  4096 Oct 15 01:55 linux-lab
-rw-r--r--  1 brown brown 11295 Jun 17 06:49 s
brown@myvis0612:/$ echo "$SHELL"
/bin/bash

# $$ 表示当前 Shell 的进程号；用 ps 查看当前 Shell 进程及其父进程。
brown@myvis0612:/$ ps -p "$$" -o pid,ppid,comm,args
    PID    PPID COMMAND         COMMAND
   1576    1575 bash            -bash

# 单引号不展开变量，因此这里原样输出 $BASH_VERSION。
brown@myvis0612:/$ echo '$BASH_VERSION'
$BASH_VERSION

# $0 表示当前 Shell 或脚本的调用名称；-bash 中的前导连字符表示登录 Shell。
brown@myvis0612:/$ echo "$0"
-bash

# shopt -q 不直接输出内容，而通过退出状态表示结果；状态 0 表示当前是登录 Shell。
brown@myvis0612:/$ shopt -q login_shell
brown@myvis0612:/$ echo "login_shell status: $?"
login_shell status: 0

# 查询当前用户的账户记录，最后一个字段 /bin/bash 是登录 Shell。
brown@myvis0612:~/linux-lab/unit07-bash$ getent passwd "$(id -un)"
brown:x:1000:1000:brown:/home/brown:/bin/bash

# ==================== 51. 定义变量并练习引用和命令替换 ====================
# Shell 变量赋值时，等号两侧不能有空格。
brown@myvis0612:/$ name="brown"
brown@myvis0612:/$ course="Linux Bash"
brown@myvis0612:/$ echo "$name"
brown

# 双引号会展开变量；变量名必须完整写在 $ 后面。
brown@myvis0612:/$ echo "i am learning $"
i am learning $
brown@myvis0612:/$ echo "i am learning $course"
i am learning Linux Bash

# 单引号会阻止变量展开，因此输出的是变量名称本身。
brown@myvis0612:/$ echo 'I am learning $course'
I am learning $course

# $(命令) 执行命令替换；$((表达式)) 执行整数算术运算。
brown@myvis0612:/$ echo "Home directory: $HOME"
Home directory: /home/brown
brown@myvis0612:/$ echo "Current directory: $(pwd)"
Current directory: /
brown@myvis0612:/$ echo "Arithmetic result: $((3 + 4 * 2))"
Arithmetic result: 11

# ==================== 52. 区分普通变量与环境变量 ====================
# 未导出的普通 Shell 变量不会被子 Shell 继承。
brown@myvis0612:/$ lab_note="ordinary variable"
brown@myvis0612:/$ bash -c 'printf "Child sees lab_note: <%s>\n" "${lab_note-unset}"'
Child sees lab_note: <unset>

# export 后，变量会进入环境并传递给新启动的子进程。
brown@myvis0612:/$ export lab_note="exported variable"
brown@myvis0612:/$ bash -c 'printf "Child sees lab_note: <%s>\n" "${lab_note-unset}"'
Child sees lab_note: <exported variable>
brown@myvis0612:/$ export LAB_CLASS="bash-practice"
brown@myvis0612:/$ bash -c 'echo "Inside child: $LAB_CLASS"'
Inside child: bash-practice
brown@myvis0612:/$ echo "Inside parent: $LAB_CLASS"
Inside parent: bash-practice

# 子 Shell 可以修改自己的变量副本，但不会反向改变父 Shell 的值。
brown@myvis0612:/$ export LAB_COUNT=10
brown@myvis0612:/$ bash -c 'export LAB_COUNT=99; echo "Child value: $LAB_COUNT"'
Child value: 99
brown@myvis0612:/$ echo "Parent value: $LAB_COUNT"
Parent value: 10

# ==================== 53. 查看 PATH 并验证命令查找机制 ====================
# PATH 使用冒号分隔多个命令搜索目录。
brown@myvis0612:/$ printf '%s\n' "$PATH"
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

# 将冒号替换为换行，便于逐项查看搜索路径。
brown@myvis0612:/$ printf '%s\n' "$PATH" | tr ':' '\n'
/usr/local/sbin
/usr/local/bin
/usr/sbin
/usr/bin
/sbin
/bin
/usr/games
/usr/local/games
/snap/bin

# command -v 可显示命令最终解析为别名、内建命令还是可执行文件路径。
brown@myvis0612:/$ command -v ls
alias ls='ls --color=auto'
brown@myvis0612:/$ command -v bash
/usr/bin/bash
brown@myvis0612:/$ command -v python3
/usr/bin/python3

# 在子 Shell 中临时把 PATH 改为不存在的目录，ls 因无法定位而执行失败。
# 使用圆括号可把 PATH 的修改限制在子 Shell 内，不影响当前父 Shell。
brown@myvis0612:/$ (
>     PATH="/definitely-not-a-real-directory"
>     ls
> )
Command 'ls' is available in the following places
 * /bin/ls
 * /usr/bin/ls
The command could not be located because '/bin:/usr/bin' is not included in the PATH environment variable.
ls: command not found

# 在无效目录后保留原 PATH，Shell 仍能继续找到并执行 ls。
brown@myvis0612:/$ (
>     PATH="/definitely-not-a-real-directory:$PATH"
>     ls
> )
bin   cdrom  etc   lib    lost+found  mnt  proc  run   snap  sys  usr
boot  dev    home  lib64  media       opt  root  sbin  srv   tmp  var

# ==================== 54. 查看命令退出状态并用于条件判断 ====================
# $? 保存最近一条命令的退出状态；0 通常表示成功，非 0 表示失败。
brown@myvis0612:/$ true
brown@myvis0612:/$ echo "$?"
0
brown@myvis0612:/$ false
brown@myvis0612:/$ echo "$?"
1

# grep -q 只通过退出状态报告是否找到内容，不输出匹配行。
# /etc/os-release 中没有区分大小写完全一致的“Linux”，所以执行 else 分支。
brown@myvis0612:/$ if grep -q "Linux" /etc/os-release; then
>     echo "Linux was found"
> else
>     echo "Linux was not found"
> fi
Linux was not found

# ==================== 55. 查看 Bash 启动文件 ====================
# 列出主目录中的隐藏文件，并确认 .bashrc 与 .profile 的权限和大小。
brown@myvis0612:/$ ls -la ~
total 64
drwxr-x---  6 brown brown 4096 Oct 14 08:16 .
drwxr-xr-x  6 root  root  4096 Oct 10 03:35 ..
-rw-------  1 brown brown   78 Oct 14 08:07 .bash_history
-rw-r--r--  1 brown brown  220 Feb 13  2026 .bash_logout
-rw-r--r--  1 brown brown 3771 Feb 13  2026 .bashrc
drwx------  2 brown brown 4096 Jun 13 01:25 .cache
drwx------  3 brown brown 4096 Oct 14 08:16 .config
-rw-------  1 brown brown   44 Jun 17 06:51 .lesshst
-rw-r--r--  1 brown brown  807 Feb 13  2026 .profile
drwx------  2 brown brown 4096 Jun 12 09:52 .ssh
-rw-------  1 brown brown 4199 Oct  6 09:55 .viminfo
drwxrwxr-x 12 brown brown 4096 Oct 15 01:55 linux-lab
-rw-r--r--  1 brown brown 11295 Jun 17 06:49 s
brown@myvis0612:/$ ls -l ~/.bashrc ~/.profile 2>/dev/null
-rw-r--r-- 1 brown brown 3771 Feb 13  2026 /home/brown/.bashrc
-rw-r--r-- 1 brown brown  807 Feb 13  2026 /home/brown/.profile

# 显示 .bashrc 的前 160 行，观察非交互 Shell 判断、历史记录、提示符和别名等设置。
brown@myvis0612:/$ sed -n '1,160p' ~/.bashrc
# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

HISTSIZE=1000
HISTFILESIZE=2000
shopt -s checkwinsize

# 部分系统默认的提示符配置和常用别名。
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# ==================== 56. 创建并执行 Bash 环境检查脚本 ====================
# 目标目录最初不存在，因此 cd 失败；随后创建目录再继续实验。
brown@myvis0612:/$ cd ~/linux-lab/unit07-bash
-bash: cd: /home/brown/linux-lab/unit07-bash: No such file or directory
brown@myvis0612:/$ cd ~/linux-lab
brown@myvis0612:~/linux-lab$ mkdir unit07-bash
brown@myvis0612:~/linux-lab$ cd unit07-bash

# 使用带单引号的 Here Document 写入脚本，防止创建文件时提前展开变量。
brown@myvis0612:~/linux-lab/unit07-bash$ cat > bash-check.sh <<'EOF'
> #!/usr/bin/env bash
>
> printf '%s\n' "=== Bash environment check ==="
> printf 'Bash version: %s\n' "${BASH_VERSION:-not running under Bash}"
> printf 'Current user: %s\n' "$(id -un)"
> printf 'Home directory: %s\n' "$HOME"
> printf 'Working directory: %s\n' "$PWD"
>
> LAB_MESSAGE="This is a local shell variable"
> printf 'Message: %s\n' "$LAB_MESSAGE"
>
> if grep -q "Linux" /etc/os-release; then
>     printf '%s\n' "OS check: Linux found"
> else
>     printf '%s\n' "OS check: Linux not found"
> fi
>
> printf '%s\n' "=== Check complete ==="
> EOF

# bash -n 仅检查语法，不执行脚本；状态 0 表示未发现语法错误。
brown@myvis0612:~/linux-lab/unit07-bash$ bash -n bash-check.sh
brown@myvis0612:~/linux-lab/unit07-bash$ echo "Syntax check status: $?"
Syntax check status: 0

# 直接交给 bash 解释执行，此时脚本不需要具有执行权限。
brown@myvis0612:~/linux-lab/unit07-bash$ bash bash-check.sh
=== Bash environment check ===
Bash version: 5.3.9(1)-release
Current user: brown
Home directory: /home/brown
Working directory: /home/brown/linux-lab/unit07-bash
Message: This is a local shell variable
OS check: Linux not found
=== Check complete ===
brown@myvis0612:~/linux-lab/unit07-bash$ echo "Script status: $?"
Script status: 0

# 添加所有者执行权限后，可通过脚本路径直接运行；Shebang 指定使用 Bash。
brown@myvis0612:~/linux-lab/unit07-bash$ chmod u+x bash-check.sh
brown@myvis0612:~/linux-lab/unit07-bash$ ./bash-check.sh
=== Bash environment check ===
Bash version: 5.3.9(1)-release
Current user: brown
Home directory: /home/brown
Working directory: /home/brown/linux-lab/unit07-bash
Message: This is a local shell variable
OS check: Linux not found
=== Check complete ===

# ==================== 57. 使用后台进程与特殊变量 $! ====================
# 在后台启动 sleep；Shell 输出作业号 [1] 和进程号 96295。
brown@myvis0612:~/linux-lab/unit07-bash$ sleep 300 &
[1] 96295

# $! 保存最近启动的后台进程 PID，将其记录到普通变量 PID。
brown@myvis0612:~/linux-lab/unit07-bash$ PID=$!
brown@myvis0612:~/linux-lab/unit07-bash$ printf 'Started test process: PID=%s\n' "$PID"
Started test process: PID=96295
brown@myvis0612:~/linux-lab/unit07-bash$ ps -p "$PID" -o pid,ppid,stat,comm,args
    PID    PPID STAT COMMAND         COMMAND
  96295    1576 S    sleep           sleep 300

# 执行 kill 时进程已经结束，因此报告 No such process；作业完成通知也随之出现。
brown@myvis0612:~/linux-lab/unit07-bash$ kill -TERM "$PID"
-bash: kill: (96295) - No such process
[1]+  Done                       sleep 300

# 再次查询时只显示表头，确认该 PID 已不存在。
brown@myvis0612:~/linux-lab/unit07-bash$ sleep 1
brown@myvis0612:~/linux-lab/unit07-bash$ ps -p "$PID" -o pid,stat,comm
    PID STAT COMMAND
```
