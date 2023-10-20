#該如何讀取xml檔案
import xml.etree.ElementTree as ET #匯入函式庫
def compound_interest(x,s,y):
    total = 0 #計算複利的總和
    for i in range(y):#總共y年
        total = (total + x)#經過複利的金額+新投資的金額
        total = total*(1+s/100)#複利
    return total
# 解析XML文件

tree = ET.parse("setting.xml") #讀取setting.xml的檔案
root = tree.getroot() #建立樹結構
# 如何把樹結構轉化成pythond可使用之資料???
# 创建一个空字典: 在python裡類似樹結構的東西，都是以{}建立

data_dict = {} #data={key:value}
# 遍历XML元素并将其存储在字典中
for element in root:
    key = element.tag  # 讀取tag:x, s, y
    value = element.text  # 讀取裡面文字 10000, 10, 20(被tag包夾的文字)
    data_dict[key] = value #把資料存到python裡的字典處理
# 打印字典
print(data_dict)
x = int(data_dict['x']) #讀取裡面的值
s = int(data_dict['s'])
y = int(data_dict['y'])
# x = int(input("每年投資的金額"))
# s = int(input("年利率"))
# y = int(input("年份"))

print(compound_interest(x,s,y)) #算出成果
# 算出來 還要存至記事本
# 打開記事本檔案
file = open("result.txt","w",encoding="utdf-8")
# result.txt -> 檔案名
# "w" -> write寫入
# encoding -> 文字編碼 臺灣用"utf-8" 中國"big-5"
file.write("本金:"+str()+"\n")
file.write("年利率:"+str(s)+"\n")
file.write("投資年分:"+str(y)+"\n")
file.write("-------以下為可的金額-------\n")
# file.write(str(int(compound_interest(x,s,y)))+".00元")
num = compound_interest(x,s,y)
file.write(f"{num:.2f}元") #字串格式化
file.close()