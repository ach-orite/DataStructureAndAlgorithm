算法复习——排序
时间限制为1s时，大O为10000000时勉强可行，100,000,000时很悬。

算法分析
时间复杂度-执行时间(比较和交换次数)
空间复杂度-所消耗的额外内存空间
使用小堆栈或表
使用链表或指针、数组索引来代表数据
排序数据的副本
对具有重键的数据(同一组数按不同键多次排序)进行排序时，需要考虑排序方法的稳定性，在非稳定性排序算法中需要稳定性时可考虑加入小索引。

稳定性：如果排序后文件中拥有相同键的项的相对位置不变，这种排序方式是稳定的。

常见的排序算法根据是否需要比较可以分为如下几类：

Comparison Sorting
Bubble Sort
Selection Sort
Insertion Sort
Shell Sort
Merge Sort
Quck Sort
Heap Sort
Bucket Sort
Counting Sort
Radix Sort

从稳定性角度考虑可分为如下两类：

稳定
非稳定