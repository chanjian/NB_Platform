#!/usr/bin/env bash

# 配置参数
CONFIG_FILE="uwsgi.ini"  # uWSGI 配置文件
LOG_FILE="uwsgi.log"           # 日志文件
UWSGI_PATH="/envs/day06/bin/uwsgi"  # uWSGI 路径

# 打印当前 uWSGI 进程信息
echo -e "\033[34m--------------------wsgi process--------------------\033[0m"
ps -ef | grep "$CONFIG_FILE" | grep -v grep

# 暂停 0.5 秒
sleep 0.5

# 关闭 uWSGI 进程
echo -e '\n--------------------going to close--------------------'
PIDS=$(ps -ef | grep "$CONFIG_FILE" | grep -v grep | awk '{print $2}')

if [ -z "$PIDS" ]; then
    echo -e "\033[33mNo uWSGI process found.\033[0m"
else
    echo -e "Killing uWSGI processes: $PIDS"
    echo "$PIDS" | xargs kill -9
    if [ $? -eq 0 ]; then
        echo -e "\033[32mSuccessfully killed uWSGI processes.\033[0m"
    else
        echo -e "\033[31mFailed to kill uWSGI processes.\033[0m"
        exit 1
    fi
fi

# 暂停 0.5 秒
sleep 0.5

# 启动 uWSGI 服务
echo -e '\n----------starting uWSGI service----------'
"$UWSGI_PATH" --ini "$CONFIG_FILE" >> "$LOG_FILE" 2>&1 &

# 检查启动是否成功
if [ $? -eq 0 ]; then
    echo -e "\033[32muWSGI service started successfully.\033[0m"
else
    echo -e "\033[31mFailed to start uWSGI service.\033[0m"
    exit 1
fi

# 打印启动后的 uWSGI 进程信息
echo -e '\n----------checking uWSGI processes----------'
ps -ef | grep "$CONFIG_FILE" | grep -v grep