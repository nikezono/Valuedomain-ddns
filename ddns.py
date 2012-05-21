#-*-coding: utf-8 -*-
#valuedomainへのddnsをやってくれる適当スクリプト
#例外やエラー時にメールでも送るぐらい気を利かせたいがやらない
#コマンドライン引数は
#domain(ex:nikezono.net),password,header(nameで遊ばないなら*でいい)

import socket
import urllib
import sys

ip = socket.gethostbyname(socket.gethostname())

def post(domain,password,header):

  #hashデータを作る

  param = {}
  param['d'] = domain
  param['p'] = password
  param['h'] = header
  param['i'] = ip

  #おもむろにgetする。urllibの仕様上これでgetになり、+を,に変えるとgetらしい
  param = urllib.urlencode(param)
  return urllib.urlopen('http://dyn.value-domain.com/cgi-bin/dyn.fcg?'+ param)

#コマンドライン引数の取得
#第一引数はファイル名

argvs = sys.argv
argc= len(argvs)

#debug
print argvs
print argc
print 

if (argc != 4) :
  print 'arguments error'
  quit()

d = argvs[1]
p = argvs[2]
h = argvs[3]

res = post(d,p,h)
print res.read()
