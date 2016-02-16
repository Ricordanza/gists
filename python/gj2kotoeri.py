#!/usr/bin/python
# coding: UTF-8

#事前にタブ(¥t)区切りをカンマ(,)に変更しておいてから実地

f = open('./Google日本語入力辞書ファイル.txt')
lines2 = f.readlines()
f.close()

for line in lines2:
    args = line.split(',')
    with open("kotoeri.txt", 'a') as file:
        file.write("<dict>")
        file.write("<key>phrase</key>")
        file.write("<string>" + args[1] + "</string>")
        file.write("<key>shortcut</key>")
        file.write("<string>" + args[0] + "</string>")
        file.write("</dict>")
print
