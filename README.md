# ansible-role-firewalld [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-firewalld.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-firewalld)

CentOS 7 の firewalld の設定をおこなう ansible role です。

* データを持たないパケットの接続を破棄
* SYN flood 攻撃と思われる接続を破棄
* ステルススキャンと思われる接続を破棄
* fail2ban のサポート

fail2ban にて 3日間で 3回 banした IPアドレスは永久的に接続拒否する

## 設定項目

以下の設定項目は上書き可能。

| 項目名                 | デフォルト値 | 説明                         |
| ---------------------- | ------------ | ---------------------------- |
| firewall_enabled_ports | 22/tcp       | 公開するポート番号（複数可） |
| fail2ban_enabled_sshd  | no           | sshd の fail2ban を有効化    |
