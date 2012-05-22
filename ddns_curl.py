#-*-coding: utf-8 -*-
#valuedomainへのddnsをやってくれる適当スクリプト
#例外やエラー時にメールでも送るぐらい気を利かせたいがやらない
#コマンドライン引数は
#domain(ex:nikezono.net),password,header(nameで遊ばないなら*でいい)

import socket
import urllib
import sys
import commands
import string

#まずsocket.gethostbynameで現在のip取得するが
#なぜかローカルipを取得する場合があるのでその場合ネットワークから取得する
ip = socket.gethostbyname(socket.gethostname())
print ip

if(ip.find('192') != -1):
  ip = commands.getoutput('curl ipcheck.ieserver.net')
  print 'get global ip address from ipcheck.ieserver.net'
  print ip
  res = ip.splitlines()
  print res[5]
  print

##postメソッドを作成
def post(domain,password,header):

  #hashデータを作る

  param = {}
  param['d'] = domain
  param['p'] = password
  param['h'] = header
  param['i'] = res[5]

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

pos = post(d,p,h)
print pos.read()
