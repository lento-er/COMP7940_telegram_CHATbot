# telegram_chatgpt_docker
## 部署说明
1. 登录阿里云，并连接到服务器
2. 通过【systemctl status chat_bot】命令，查看服务运行状态
3. 可以通过【systemctl stop chat_bot】结束服务、【systemctl restart chat_bot】重启服务
4. 可以通过【journalctl -u chat_bot -f】命令查看服务运行日志
5. 若通过push更新了GitHub上的代码，会自动pull最新的代码到阿里云服务器上，并重启服务