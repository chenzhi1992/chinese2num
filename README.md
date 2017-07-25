# chinese2num
汉字钱数目转成阿拉伯数字

例子1:
输入: 1万块零1毛
返回: 10000.1
例子2:
输入: 十万五千零二元
返回: 105002.0

根据规则的形式将汉字钱数目转换为数字,因为用户的输入五花八门,所以有些情况我可能没有想到,后期可以继续修改.
我的代码可以满足以下情况:
1. 纯数字
2. 纯汉字
3. 汉字数字混合形式
4. 最大钱数目达到9亿九千九百九十九万...九块九毛九分
5. 适用于毛,角,分
...
