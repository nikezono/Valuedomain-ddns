ddns
====

ダイナミックDNSのためのやつ

修正すべき点
*毎回チェック時にメールを飛ばす（cronがやってくれるからいらない疑惑）
*pythonのsocket.gethostbynameではローカルIPアドレスを取得してしまうことがあるようなので
*commandsでipcheck.netに接続する手法もとりいれるか