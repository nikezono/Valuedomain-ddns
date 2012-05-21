ddns
====

ダイナミックDNSのためのやつ

修正すべき点
*毎回チェック時にメールを飛ばす（cronがやってくれるからいらない疑惑）
*wgetを使うようにしたがmacだとcurlにすべきか

以下修正した点
*pythonのsocket.gethostbynameではローカルIPアドレスを取得してしまうことがあるようなので

commandsでipcheck.netに接続する手法もとりいれるか