ddns
====

ValuedomainでDynamicDNSシステムを利用するためのスクリプト  
cronでまわす仕様  

ファイル
* ddns.py プログラム本体 だいたいこれで動く
* ddns_curl.py wgetを使っている部分でエラーが出る場合にcurlを使うようにしたversion

修正すべき点  
* 毎回チェック時にメールを飛ばす（cronがやってくれるからいらない疑惑）  
* wgetを使うようにしたがmacだとcurlにすべきか

以下修正した点  
* pythonのsocket.gethostbynameではローカルIPアドレスを取得してしまうことがあるようなので  
commandsでipcheck.netに接続する手法もとりいれるか