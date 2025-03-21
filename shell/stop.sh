#!/usr/bin/env bash

# 定义配置文件名
CONFIG_FILE="uwsgi_day06.ini"

# 定义颜色代码
RED='\033[31m'
GREEN='\033[32m'
BLUE='\033[34m'
NC='\033[0m' # 重置颜色

# 打印标题
echo -e "${BLUE}-------------------- WSGI 进程 --------------------${NC}"

# 查找与配置文件相关的进程
PROCESSES=$(ps -ef | grep "$CONFIG_FILE" | grep -v grep)

# 检查是否有相关进程
if [[ -z "$PROCESSES" ]]; then
    echo -e "${GREEN}没有找到与 ${CONFIG_FILE} 相关的进程。${NC}"
    exit 0
fi

# 显示相关进程
echo "$PROCESSES"

# 提示即将关闭进程
echo -e "\n${RED}-------------------- 即将关闭进程 --------------------${NC}"
sleep 0.5

# 提取进程 ID 并终止进程
PIDS=$(echo "$PROCESSES" | awk '{print $2}')
echo -e "${RED}正在终止以下进程 ID: ${PIDS}${NC}"
echo "$PIDS" | xargs kill -9

# 检查是否成功终止
sleep 0.5
if ps -p $PIDS > /dev/null 2>&1; then
    echo -e "${RED}未能成功终止所有进程。${NC}"
else
    echo -e "${GREEN}所有进程已成功终止。${NC}"
fi