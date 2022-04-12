## geometry_scale

几何选型：

![image-20220409142243049](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409142243049.png)

[参考文献--微尺度流动研究中的几个问题](E:\论文\微尺度流动研究中的几个问题.pdf)

> 陶然,权晓波,徐建中. 微尺度流动研究中的几个问题[J]. 工程热物理学报,2001,22(5):575-577. DOI:10.3321/j.issn:0253-231X.2001.05.015.

## boundary_conditions

### 1 inlet_velocity

#### 1.1 选取微泵类型

[引用文献--微泵驱动方式比较研究.pdf](E:\论文\绪论引用文章\微泵驱动方式比较研究.pdf)

> 罗玉元,张国贤. 微泵驱动方式比较研究[J]. 液压与气动,2003(7):43-46. DOI:10.3969/j.issn.1000-4858.2003.07.021.



![image-20220409131550254](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409131550254.png)

故可以使用 **可靠性极好**的 **静电微泵**

#### 1.2 确定静电微泵的数据

[引用文献--Design and simulation of an electrostatic micropump for drug-delivery applications](E:\论文\绪论引用文章\微型静电泵的设计以及仿真.pdf)

> Bourouina T, Bossebuf A, Grandchamp J P. Design and simulation of an electrostatic micropump for drug-delivery applications[J]. Journal of Micromechanics and Microengineering, 1997, 7(3): 186.

![image-20220409142004896](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409142004896.png)

如上图确定数据为 $平均体积流量为：150 nL/ min$

故计算得到不同尺寸下的入口速度为：

| 管径 | 入口速度m/s |
| ---- | ----------- |
| 50   | 0.00127324  |
| 40   | 0.001989437 |
| 25   | 0.005092958 |
| 20   | 0.007957747 |

![image-20220409162447540](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409162447540.png)

### 2  outlet

> fluent教学论坛  http://www.lanmaowang.com/?s=%E8%BE%B9%E7%95%8C%E6%9D%A1%E4%BB%B6

由于雷诺数比较小，且流动工质为水

故该流动为**不可压缩层流**，且流动过程中没有明显的密度变化

有两种可选择的边界条件

| boundary conditions |
| ------------------- |
| outlet_pressure     |
| outflow             |

#### 2.1 outflow

![image-20220409143353100](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409143353100.png)

![image-20220409160941976](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409160941976.png)

计算结果(速度云图)可看到

> 条件为:
>
> L = $1000 \mu m$
>
> D = $50\mu m$
>
> $u_m = 0.00127324$

![image-20220409154734692](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409154734692.png)

#### 2.2 outlet_pressure

![image-20220409161246748](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409161246748.png)

![image-20220409161229516](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409161229516.png)

> 条件为:
>
> L = $1000 \mu m$
>
> D = $50\mu m$
>
> $u_m = 0.00127324$

计算结果(速度云图)为

![image-20220409155945539](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409155945539.png)

#### 2.3 comparison of two results

unit : Pa

![image-20220409162037369](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409162037369.png)

两种出口边界条件压降$\Delta p$计算结果相差 0.6824373 Pa



#### 2.4 遗留下来的问题

<font color = 'red'>关于两种出口边界条件的选择不是很明确，</font>

* 仿真论坛中提出

![image-20220409163017265](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409163017265.png)

​	不可压缩流动推荐使用**自由流出(outflow)**出口条件

* 对于压力出口条件

![image-20220409163323810](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409163323810.png)

![image-20220409163401775](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20220409163401775.png)

而在两次计算中，流动都未出现回流问题

<font color = "red">问：1. 对于两种边界条件的优劣性如何判断；2. 该选用何种比较合适 </font>



