# telegram_chatgpt_docker
## 部署说明
1. 登录阿里云，并连接到服务器
2. 通过【ps -ef | grep python】命令，可以查看目前正在运行的python进程，包含【python main.py】的是telegram_chat_bot进程
3. 可以通过【kill -9 进程编号】结束进程
4. 可以通过【tail -f /root/chatbot_log/output.log】命令查看进程运行日志
5. 若更新了GitHub上的代码，进入【cd /root/COMP7940_telegram_CHATbot/】目录，然后执行【git pull origin main】
6. 更新完以后，通过【nohup python /root/COMP7940_telegram_CHATbot/main.py > /root/chatbot_log/output.log 2>&1 &】运行服务