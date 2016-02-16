# -*- coding: utf-8 -*-

import sys # モジュール属性 argv を取得するため
import os # osモジュールのインポート
import os.path
 
 # コマンドライン引数を格納したリストの取得
argvs = sys.argv

# 引数の個数
argc = len(argvs)

if (argc <= 1):
    print 'usage : python %s script' % sys.argv[0]
    quit()

# 処理対象ディレクトリ
targetdir = './'

# ディレクトリ指定がある場合
if (argc > 1):
    targetdir = argvs[1]

# os.listdir('パス')
# 指定したパス内の全てのファイルとディレクトリを要素とするリストを返す
files = os.listdir(targetdir)
 
for file in files:
#    print os.path.isdir(file)
    if (os.path.isdir(file)):
        continue
    lines = open(file, 'r').readlines()
    rlines = [l for l in lines if argvs[2] in l]
    for line in rlines:
        print line.rstrip()