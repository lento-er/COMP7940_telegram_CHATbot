# telegram_chatgpt_docker
## 部署说明
1. 登录阿里云，并连接到服务器
2. 通过【ps -ef | grep python】命令，可以查看目前正在运行的python进行，包含【python main.py】的是telegram进程
3. 可以通过【kill -9 进程编号】结束进程
4. 可以通过【tail -f ./telegram_bot_docker/nohup.out】命令查看进程运行日志
5. 若需手动更新阿里云上的代码，可先进入【cd /root/telegram_bot_dcker】目录，然后执行【git pull origin main】
6. 更新完以后，通过【nohup python main.py】运行服务