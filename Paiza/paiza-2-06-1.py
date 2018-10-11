﻿# coding: utf-8
'''
 演習課題「西暦年を昭和年に変換してみよう」
右側のコードエリアのプログラムをもとに、プログラムを完成させてください。

seireki変数には、西暦年として 1926~1988 の中から選ばれた数字が1つ代入されます。
選ばれた西暦年を昭和年に変換し「西暦19○○年は昭和○○年です」と
出力してください。

昭和元年(1年)は1926年です。1926年が与えられた場合、
「西暦1926年は昭和1年です。」と表示してください。
'''

# 西暦を昭和年に変換
import random
seireki = random.randint(1926, 1988) #西暦年
print("西暦" + str(seireki) + "年は", end = "")

# 昭和年を計算
showa = seireki-1925
# 昭和年を出力
print("昭和" + str(showa) + "年です。")