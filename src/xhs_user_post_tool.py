import random
import time
import csv
import datetime
import os
from functools import partial
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import re
import sys
import json
import logging
from logging.handlers import TimedRotatingFileHandler
import urllib.parse


class XhsUserPosted:
    """小红书用户主页笔记采集模块

    负责：
    1. 遍历用户链接列表
    2. 分页获取用户发布的笔记列表
    3. 可选采集笔记详情
    4. CSV输出和可选图片下载
    """

    def __init__(self, user_link_list, top_num, pic_tag, detail_tag, txt_msglist, logger):
        self.txt_msglist = txt_msglist
        self.logger = logger
        self.describe = []
        self.cookie_val = self.get_cookie()
        self.user_link_list = user_link_list
        self.top_num = int(top_num)
        self.pic_tag = pic_tag
        self.detail_tag = detail_tag
        self.wait_sec = self.get_config_pub()
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.result_file = '小红书博主笔记_{}.csv'.format(now)

    def tk_show(self, context):
        self.logger.info(context)
        self.txt_msglist.delete('1.0', 'end')
        self.describe.append(context)
        self.txt_msglist.insert('insert', '\n'.join(self.describe))
        self.txt_msglist.see("end")

    def trans_date(self, v_timestamp):
        timeArray = time.localtime(v_timestamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    def trans_note_type(self, v_str):
        if v_str == 'all':
            return '不限'
        elif v_str == 'video':
            return '视频'
        elif v_str == 'normal':
            return '图文'
        else:
            return '未知'

    def get_cookie(self, num_tag=0):
        """[专有代码已移除] 从 cookie.txt 读取cookie"""
        return ""

    def get_config_pub(self):
        try:
            with open('config_pub.json', 'r') as file:
                text = json.load(file)
            wait_sec = text['wait_sec']
            if wait_sec < 1:
                self.tk_show('\n等待时长需至少1秒，请重新配置！')
                exit(1)
            self.tk_show(f'\n读取config_pub成功, 等待间隔是:{wait_sec}s')
        except Exception as e:
            wait_sec = ''
            self.tk_show('\n读取config_pub失败！请检查config_pub.json')
            self.tk_show(str(e))
            exit(1)
        return wait_sec

    def down_pic(self, v_url, pic_name):
        """[专有代码已移除] 下载图片文件"""
        pass

    def init_csv(self, csv_header):
        with open(self.result_file, 'a+', encoding='utf_8_sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_header)
        self.tk_show('csv初始化完成')

    def get_xhs_detail(self, v_page, v_note_id, v_is_top, v_detail_tag, v_pic_tag):
        """[专有代码已移除] 采集笔记详情"""
        return {}

    def get_user_posted(self):
        """[专有代码已移除] 采集用户主页笔记列表

        原实现核心流程：
        1. 从用户链接提取 user_id
        2. 构造用户笔记API请求参数
        3. 生成请求签名
        4. 分页请求笔记列表接口
        5. 解析笔记信息（标题、类型、互动数据等）
        6. 可选采集笔记详情和下载图片
        7. 实时写入CSV
        """
        self.init_csv(csv_header=['页码', '笔记标题', '笔记类型', '笔记链接', '发布时间', '点赞数', '评论数', '收藏数', '转发数'])
        self.tk_show('\n[专有代码已移除] 用户笔记采集功能需要专有实现')
        self._safe_showinfo = lambda t, m: None
