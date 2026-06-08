# date 查看当前时间
```bash
brown@brown-vm:~$ date
Thu Jun  4 02:38:01 AM UTC 2026
brown@brown-vm:~$ date +%Y/%m/%d
2026/06/04
```
> date +格式

格式	含义	示例
%Y	四位年份	2026
%y	两位年份	26
%m	月份	    06
%d	日期	    04
%H	小时(24小时制)	15
%M	分钟	    20
%S	秒	30
%a	简写星期	Mon
%A	完整星期	Monday
%b	简写月份	Jun
%B	完整月份	June
%s	Unix时间戳	1780540000

# date -d 查看指定日期(可以加偏移量去运算)

```bash
brown@brown-vm:~$ date -d "2 days ago" +%Y/%m/%d
2026/06/02
brown@brown-vm:~$ date -d yesterday
Wed Jun  3 02:47:28 AM UTC 2026
```

> ""里面可以加偏移量去运算   后面可以+格式去规范
```bash
brown@brown-vm:~$ date -d "2026-05-01 +3 days" +%Y-%m-%d
2026-05-04
```
```bash
brown@brown-vm:~$ date -d "2025-12-25 1 day ago" +%Y-%m-%d
2025-12-24
```

> Linux 系统的 date -d 命令底层挂载了一个自然语言语法解析器（GNU String Parser）

1. 矢量位移词（方向与步长控制）
用来控制时间轴是往前滚（过去）还是往后滚（未来），以及滚动的单位。


`ago`向前追溯（减法算术）。只能放在时间单位的后面，代表从当前基准点往过去推。
 `date -d "5 days ago"` （物理计算 5 天前的绝对日期） 

`+` 或 `-`正负号算术指针。`+` 代表向未来加，`-` 代表向过去减。必须写在数字前面。
  `date -d "2026-05-01 -10 days"` （以 5 月 1 日为基准，强行向过去回滚 10 天） 

 `day` / `days` （天）
 `month` / `months` （月）
 `year` / `years` （年）
 `hour` / `hours` （小时）
 `minute` / `minutes` （分钟）
 `second` / `seconds` （秒） 

  `date -d "2 years +3 months"` （计算 2 年零 3 个月后的时间） 

2. 相对基准动态词（指代当前物理时钟）
用来直接指代执行命令的那一瞬间，宿主机硬件时钟所处的时空坐标。

`now` / `today`*当前时钟起点。代表执行命令的这一秒。如果不写基准点，默认就是 `now`。 |`date -d "now +2 hours"` （计算从现在这一秒往后推 2 个小时的精准时钟） 

`yesterday`昨天相当于底层自动执行了 `now - 1 day` 算术。 
 `date -d "yesterday"` 

`tomorrow`明天。相当于底层自动执行了 `now + 1 day` 算术。 
 `date -d "tomorrow"` 

3. 序数与周期限定词（高维时间跨越）
用来精准锁死某一个特定周期的起点或终点。


`next`下一个周期。往后强行推进一个指定的单位或星期。 
 `date -d "next monday"`（物理计算下周一是几号）
 `date -d "next month"` （物理计算下个月的今天） 

`last` 上一个周期。往前强行倒退一个指定的单位或星期。
 `date -d "last sunday"`（物理计算上周日是几号）
 `date -d "last year"` （物理计算去年的今天） 

 `this`当前周期。通常用来锁定当前星期的某一天。  
`date -d "this friday"` （物理计算本周五是几号） 


4. 文本时间硬编码词（月份与星期的全称/缩写）

星期集合：`Sunday`(`sun`), `Monday`(`mon`), `Tuesday`(`tue`), `Wednesday`(`wed`), `Thursday`(`thu`), `Friday`(`fri`), `Saturday`(`sat`)

月份集合：`January`(`jan`), `February`(`feb`), `March`(`mar`), `April`(`apr`), `May`, `June`(`jun`), `July`(`jul`), `August`(`aug`), `September`(`sep`), `October`(`oct`), `November`(`nov`), `December`(`dec`)


# date -u 把你的操作系统时钟，强行切换到“英国格林威治零时区（UTC）+0 来显示时间。
```bash
brown@brown-vm:~$ date -u
Thu Jun  4 03:21:05 AM UTC 2026
```