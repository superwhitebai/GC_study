# -*- coding: utf-8 -*-
# @Time    : 2025/3/16  22:46
# @Author  : Wenl
# @FileName: GC_study.py
# @Software: PyCharm
"""
    Description:特别注意命名，注意格式     
"""
from pywin.Demos.ocx.ocxtest import test1


def Zwl(name):
    print('嗨，%s' % name)
zwl = Zwl('张文亮')

#关键字参数
def eat(zwl1,zwl2):
    print(zwl1 + '把' + zwl2 + '吃掉了')
zwl3 = eat('张文亮','蛋糕')

#默认参数
def acquiesce(name = '张文亮',word='编程可以改变世界vvv'):
    print(name + '—>' + word)
zwl4 = acquiesce()


def watchMovie(name="张文亮",cigarette=True,beer=True,girlfriend=True):
    sentence = name + "带着"
    if cigarette:
        sentence = sentence + '香烟'
    if beer:
        sentence = sentence + "啤酒"
    if girlfriend:
        if cigarette or beer:
            sentence = sentence + "和女朋友1111"
        else:
            sentence = sentence + "女朋友"
    sentence = sentence + "去看电影了"
    return sentence
result = watchMovie(girlfriend=False)
print(result)

#收集参数
def tes1t(*params):
    print('有 %d 个参数' % len(params))
    print('第二个参数是：',params[1])

result1 = tes1t('F','i','S','h','c')

#局部变量
# def discount(price,rate):
#     final_paice = price * rate
#     return final_paice
# old_price = float(input('请输入原价：'))
# rate = float(input('请输入折扣率：'))
# New = discount(old_price,rate)
# print('打折后价格是：%.2f' % New)
# print('试图在函数外部访问局部变量final_paice的值：%.2f' % New)

#全局变量
# def discount1(price,rate):
#     final_paice1 = price * rate
#     print('试图在函数外部访问局部变量old_price1的值：%.2f' % old_price1)
#     return final_paice1
# old_price1 = float(input('请输入原价：'))
# rate1 = float(input('请输入折扣率：'))
# New1 = discount1(old_price1,rate1)
# print('打折后价格是：%.2f' % New1)

#尝试在discount1中修改一个全局变量
def discount1(price,rate):
    final_paice1 = price * rate
    #下面试图修改全局变量的值
    print('试图在函数外部访问局部变量old_price1的值：%.2f' % old_price1)
    return final_paice1
old_price1 = float(input('请输入原价：'))
rate1 = float(input('请输入折扣率：'))
New1 = discount1(old_price1,rate1)
print('全局变量old_price现在的值是：%.2f' % old_price1)
print('打折后价格是：%.2f' % New1)


























