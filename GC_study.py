# -*- coding: utf-8 -*-
# @Time    : 2025/3/16  22:46
# @Author  : Wenl
# @FileName: GC_study.py
# @Software: PyCharm
"""
    Description:特别注意命名，注意格式     
"""
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