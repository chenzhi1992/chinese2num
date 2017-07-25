# coding:utf-8
# author: Tian

import time

class trans_money():
    def __init__(self):
        # 记录个、十、百、...亿每一位的数字，一共9位
        self.num_money = []
        # 钱中数量单位
        self.mon = ['十', '百', '千', '万', '亿']
        # 判断数字是否是正确标准的,1:标准的数字, 0:不标准的数字
        self.isRightNum = 1

    def char2digit(self, m_str):
        '''
        函数作用：判断m_str中有没有数字，并将数字存入num_money中。没有数字，存0
        :param m_str: 输入汉字钱的字符串，并存入列表中
        :return: 无
        '''
        if '一'  in m_str or '1' in m_str:
            money = 1
        elif '二' in m_str or '两' in m_str or '2' in m_str:
            money = 2
        elif '三' in m_str or '3' in m_str:
            money = 3
        elif '四' in m_str or '4' in m_str:
            money = 4
        elif '五' in m_str or '5' in m_str:
            money = 5
        elif '六' in m_str or '6' in m_str:
            money = 6
        elif '七' in m_str or '7' in m_str:
            money = 7
        elif '八' in m_str or '8' in m_str:
            money = 8
        elif '九' in m_str or '9' in m_str:
            money = 9
        else:
            money = 0
        self.num_money.append(money)

    def cut(self, num, m_str):
        '''
        函数作用：将m_str以'亿，万，千，百，十'为分割区间分成左右两个部分
        :param num: 类型int，用于提取mon［num］中的值，即提取钱的某一个数量单位
        :param m_str: 输入汉字钱的字符串，并存入列表中
        :return: 返回m_str被分成的俩个值

        例子：cut（2，［'五','千','五','百'］）
             返回：［'五'］，［'五'，'百'］
        '''
        a = self.mon[num]
        ind = m_str.index(a)
        m_left = m_str[:ind]
        m_right = m_str[ind + 1 :]
        return m_left, m_right

    def func3(self, m_str):
        '''
        计算m_str中数字的个数, 为了处理一千二,一万二这样特殊的情况
        当个数为1时,满足一千二这种特殊情况
        :param m_str: 存钱字符的列表
        :return num: 返回m_str中数字的个数
        '''
        num = 0
        _str = ['零', '0', '一', '1', '二', '两', '2', '三', '3', '四', '4', '五', '5', '六', '6', '七', '7', '八', '8', '九', '9']
        for ind, s in enumerate(m_str):
            if s in _str:
                num += 1
        return num

    def func4(self, num, m_str):
        '''
        判断m_str是否是纯数字
        :param m_str: 存钱字符的列表
        :return num: 返回m_str中数字的个数
        '''
        # 将字符串转换成数字
        _str = ''.join(m_str)
        try:
            _num = int(_str)
        except ValueError:
            self.isRightNum = 0
        else:
            self.isRightNum = 1
            for i in range(num):
                _n = pow(10, num - i)
                num1 = int(_num / _n)  # 千万位的数字
                self.num_money.append(num1)
                _num -= (num1 * _n)
            self.num_money.append(_num)
        # _num = int(_str)
        # for i in range(num):
        #     _n = pow(10, num - i)
        #     num1 = int(_num / _n)  # 千万位的数字
        #     self.num_money.append(num1)
        #     _num -= (num1 * _n)
        # self.num_money.append(_num)

    def fact(self, a, m_str):
        if a < 0:
            self.char2digit(m_str)
        else:
            if self.mon[a] in m_str:
                m_left, m_right = self.cut(a, m_str)
                # 针对十的特殊情况,例如十块,十万,一千零十
                if self.mon[a] == '十':
                    if m_left == ['零'] or m_left == []:
                        m_left = ['一']
                if self.mon[a] == '万':
                    # 判断左边字符串是不是纯数字
                    if '一' not in m_left and '二' not in m_left and '两' not in m_left and '三' not in m_left and '四' not in m_left and '五' not in m_left and '六' not in m_left and '七' not in m_left and '八' not in m_left and '九' not in m_left and '十' not in m_left \
                            and '百' not in m_left and '千' not in m_left:
                        self.func4(a, m_left)
                    else:
                        self.fact(2, m_left)
                else:
                    self.char2digit(m_left)

                # 针对一万二,一千二等特殊情况
                if self.func3(m_right) == 1:
                    self.char2digit(m_right)
                    if a == 4:
                        for i in range(1, 8):
                            self.num_money.append(0)
                    if a == 3:
                        for i in range(1, 4):
                            self.num_money.append(0)
                    if a == 2:
                        for i in range(1, 3):
                            self.num_money.append(0)
                    if a == 1:
                        self.num_money.append(0)
                else:
                    # 判断右边是否为纯数字且非空,if是纯数字的话,调用func4,不是则调用fact
                    if '一' not in m_right and '二' not in m_right and '两' not in m_right and '三' not in m_right and '四' not in m_right and '五' not in m_right and '六' not in m_right and '七' not in m_right and '八' not in m_right and '九' not in m_right \
                            and '十' not in m_right and '百' not in m_right and '千' not in m_right and len(m_right) > 0:
                        # 判断右边有没有'零'字,例如2万零200,右边字符串为'零200',去除'零'取出'200'进行计算
                        if '零' in m_right:
                            m_right = m_right[1:]
                        if '块' in m_right or '元' in m_right:
                            m_right = m_right[:-1]
                        if len(m_right) > 0:
                            self.func4(a, m_right)
                    else:
                        self.fact(a - 1, m_right)
            else:
                if a == 3:
                    self.num_money.append(0)
                    self.num_money.append(0)
                    self.num_money.append(0)
                    self.num_money.append(0)
                else:
                    m_left = '0'
                    self.char2digit(m_left)
                self.fact(a - 1, m_str)

    def func5(self, num, m_str):
        '''
        先判断有没有'毛'或者'角',先处理毛角的情况,再处理其他部分
        :param num:
        :param m_str:
        :return:
        '''
        # 既有分又有角的情况
        if ('分' in m_str and '角' in m_str) or ('分' in m_str and '毛' in m_str):
            new_str = m_str[:-4]
            self.fact(num, new_str)
            self.char2digit(m_str[-4])
            self.char2digit(m_str[-2])
        # 有分无角、毛的情况
        elif '分' in m_str and '角' not in m_str and '毛' not in m_str:
            new_str = m_str[:-2]
            self.fact(num, new_str)
            self.num_money.append(0)
            self.char2digit(m_str[-2])
        # 没有分有毛或者角
        elif '分' not in m_str and ('毛' in m_str or '角' in m_str):
            new_str = m_str[:-2]
            self.fact(num, new_str)
            self.char2digit(m_str[-2])
        else:
            # 没有毛或者角
            self.fact(num, m_str)

    def integrate(self, num, m_str):
        # 纯数字
        if '一' not in m_str and '二' not in m_str and '两' not in m_str and '三' not in m_str and '四' not in m_str and '五' not in m_str \
            and '六' not in m_str and '七' not in m_str and '八' not in m_str and '九' not in m_str and '十' not in m_str and '百' not in m_str \
                and '千' not in m_str and '万' not in m_str and '亿' not in m_str:
            if '块' in m_str:
                ind = m_str.index('块')
                m_left = m_str[:ind]
                m_right = m_str[ind + 1:]
                str1 = "".join(m_left)
                money1 = float(str1)
                if len(m_right) > 0:
                    self.func5(num, m_right)
                    money2 = self.num2money(self.num_money)
                    return money1 + money2
                else:
                    return money1
            elif '元' in m_str:
                ind = m_str.index('元')
                m_left = m_str[:ind]
                m_right = m_str[ind + 1:]
                str1 = "".join(m_left)
                money1 = float(str1)
                if len(m_right) > 0:
                    self.func5(num, m_right)
                    money2 = self.num2money(self.num_money)
                    return money1 + money2
                else:
                    return money1
            elif '角' not in m_str and '毛' not in m_str and '分' not in m_str:
                str1 = "".join(m_str)
                money1 = float(str1)
                return money1
            else:
                self.func5(num, m_str)
                money = self.num2money(self.num_money)
                return money
        else:
            self.func5(num, m_str)
            money = self.num2money(self.num_money)
            return money

    def num2money(self, liststr):
        _money = 0
        for ind, num in enumerate(liststr):
            m = num * pow(10, 8 - ind)
            _money += m
        return _money

    def mainfunc(self, m_str):
        trans.num_money = []
        start = time.time()
        num = 4
        liststr = list(m_str)
        # while True:
        #     try:
        #         liststr.remove('块')
        #     except ValueError:
        #         break
        #
        # while True:
        #     try:
        #         liststr.remove('元')
        #     except ValueError:
        #         break

        money = self.integrate(num, liststr)
        money = float(money)
        end = time.time()
        print('{} seconds\n'.format(end - start))
        return money

if __name__ == '__main__':
    trans = trans_money()
    count = 0
    for line in open('money'):
        # count += 1
        # if count % 2 == 0:
        money_str = line.strip().split(':')[1]
        # money_str = ''.join(moneylist)
        print(money_str)
        money = trans.mainfunc(money_str)
        print('isRightNum is %d' % trans.isRightNum)
        print(money)
        # else:
        #     pass
    # money_str = '1万'
    # money_str = list(money_str)
    # money = trans.mainfunc(money_str)
    # print(money)
    # print('isRightNum is %d' % trans.isRightNum)
