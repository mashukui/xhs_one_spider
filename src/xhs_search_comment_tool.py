import random
import time
import json
import pandas as pd
import csv
import os
import datetime
import re
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import urllib.parse
import threading


class XhsSearchSpider:
    """小红书搜索与评论采集模块

    负责：
    1. 关键词搜索笔记列表
    2. 采集笔记详情
    3. 采集笔记评论（一级+二级评论）
    4. CSV输出与数据过滤
    """

    def __init__(self, search_keyword_list, note_type, sort, detail_tag, pic_tag, max_num_note, note_time,
                 note_id_list, note_link_list, kw_cmt_list,
                 start_date, end_date, ip_list, max_page_cmt, max_count, level2_val, cmt_tag_val, txt_msglist, logger):
        self.txt_msglist = txt_msglist
        self.logger = logger
        self.describe = []
        self.cookie = self.get_cookie()
        self.wait_sec = self.get_config_pub()
        self.search_keyword_list = search_keyword_list
        self.note_type = note_type
        self.sort_type = sort
        self.detail_tag = detail_tag
        self.pic_tag = pic_tag
        self.max_num_note = max_num_note
        self.note_time = note_time
        self.kw_cmt_list = kw_cmt_list
        self.start_date = start_date
        self.end_date = end_date
        self.ip_list = ip_list
        self.max_page_cmt = max_page_cmt
        self.max_count = max_count
        self.note_id_list = note_id_list
        self.note_link_list = note_link_list
        self.level2 = level2_val
        self.cmt_tag = cmt_tag_val
        now = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        self.result_file1 = '小红书搜索_{}.csv'.format(now)
        self.result_file2 = '小红书评论_{}.csv'.format(now)
        self.result_file3 = '小红书笔记_{}.csv'.format(now)

    def tk_show(self, context):
        self.logger.info(context)
        self.txt_msglist.delete('1.0', 'end')
        self.describe.append(context)
        self.txt_msglist.insert('insert', '\n'.join(self.describe))
        self.txt_msglist.see("end")

    def _safe_showinfo(self, title, message):
        try:
            if threading.current_thread() is threading.main_thread():
                self.txt_msglist.bell()
                messagebox.showinfo(title, message)
            else:
                self.txt_msglist.after(0, lambda: (self.txt_msglist.bell(), messagebox.showinfo(title, message)))
        except Exception as e:
            self.logger.error(f'[safe_showinfo] {e}')

    def _safe_showerror(self, title, message):
        try:
            if threading.current_thread() is threading.main_thread():
                self.txt_msglist.bell()
                messagebox.showerror(title, message)
            else:
                self.txt_msglist.after(0, lambda: (self.txt_msglist.bell(), messagebox.showerror(title, message)))
        except Exception as e:
            self.logger.error(f'[safe_showerror] {e}')

    def init_csv(self, v_result_file, csv_header):
        with open(v_result_file, 'a+', encoding='utf_8_sig', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_header)

    def trans_date(self, v_timestamp):
        timeArray = time.localtime(v_timestamp)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    def trans_note_type(self, v_str):
        if v_str == '不限':
            return 'all'
        elif v_str == '视频':
            return 'video'
        elif v_str == '图文':
            return 'normal'
        else:
            return 'all'

    def down_pic(self, v_url, pic_name):
        """[专有代码已移除] 下载图片文件"""
        pass

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

    def filter_data(self):
        """[专有代码已移除] 筛选评论数据"""
        pass

    def get_xhs_comment(self, v_note_id_list, v_note_link_list=None):
        """[专有代码已移除] 采集小红书笔记评论

        原实现核心流程：
        1. 遍历笔记ID列表
        2. 构造评论API请求参数和签名
        3. 请求评论接口，解析JSON
        4. 提取评论内容、评论者信息、IP属地、点赞数等
        5. 支持一级评论、二级评论、展开评论
        6. 多cookie轮换机制
        7. 分页循环，控制最大页数和最大采集量
        """
        self.tk_show('\n[专有代码已移除] 评论采集功能需要专有实现')
        self._safe_showinfo('提示', '评论采集功能需要专有实现，未包含在本开源版本中')

    def get_xhs_detail(self, v_keyword, v_note_idx, v_note_id, v_note_url, v_detail_tag, v_pic_tag):
        """[专有代码已移除] 采集小红书笔记详情

        原实现核心流程：
        1. 构造详情API请求参数和签名
        2. POST请求笔记详情接口
        3. 解析JSON提取笔记信息（标题、正文、作者、互动数据、图片列表等）
        4. 可选下载图片文件
        """
        return {}

    def get_xhs_search(self):
        """[专有代码已移除] 关键词搜索笔记列表

        原实现核心流程：
        1. 遍历搜索关键词列表
        2. 构造搜索API请求参数（关键词、排序、类型、时间等）
        3. 生成请求签名
        4. 请求搜索接口，解析JSON
        5. 提取笔记标题、链接、作者信息、互动数据
        6. 分页循环，控制最大笔记数
        7. 去重后可选触发详情采集和评论采集
        """
        self.tk_show('\n[专有代码已移除] 搜索采集功能需要专有实现')
        self._safe_showinfo('提示', '搜索采集功能需要专有实现，未包含在本开源版本中')

    def get_xsh_urls(self):
        """[专有代码已移除] 根据笔记链接采集评论/详情

        原实现：根据用户选择，依次调用详情采集和评论采集
        """
        self.tk_show('\n[专有代码已移除] 笔记链接采集功能需要专有实现')
        self._safe_showinfo('提示', '笔记链接采集功能需要专有实现，未包含在本开源版本中')
