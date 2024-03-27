# telegram_chatgpt_docker
## 部署说明
1. 登录阿里云，并连接到服务器
2. 通过【ps -ef | grep python】命令，可以查看目前正在运行的python进行，包含【python main.py】的是telegram进程
3. 可以通过【kill -9 进程编号】结束进程
4. 可以通过【tail -f ./telegram_bot_docker/nohup.out】命令查看进程运行日志