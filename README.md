# ansible-role-firewalld [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-firewalld.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-firewalld)

CentOS 7 の firewalld の設定をおこなう ansible role です。

* ssh(22/tcp) のみを公開
* データを持たないパケットの接続を破棄
* SYN flood 攻撃と思われる接続を破棄
* ステルススキャンと思われる接続を破棄

## 設定項目

以下の設定項目は上書き可能。

| 項目名                 | デフォルト値 | 説明                         |
| ---------------------- | ------------ | ---------------------------- |
| firewall_enabled_ports | 22/tcp       | 公開するポート番号（複数可） |
