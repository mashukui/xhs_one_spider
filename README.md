# xhs_one_spider
> 马哥原创：爬小红书聚合软件。支持3个功能，含：根据搜索关键词爬笔记与评论、根据主页链接爬笔记、uid与链接转换。
> 本工具仅限学术交流使用，严格遵循相关法律法规，符合平台内容的合法及合规性，禁止用于任何商业用途！

# 一、背景分析与结果展示
## 1.1 开发背景

我是[@马哥python说](https://github.com/mashukui)，一枚10年+程序猿，现全职独立开发。
<img width="2046" height="328" alt="xhs_slogon" src="https://github.com/user-attachments/assets/1396379d-fc59-4848-a831-60eb2bd24ebc" />
小红书作为国内极具影响力的社区种草平台，汇聚了大量用户且拥有极高的日活跃度，其笔记数据蕴含丰富的信息价值。之前，为了满足大家不同的数据采集需求，我分别独立开发了三款软件：针对评论采集的“[爬小红书搜索评论软件](https://github.com/mashukui/xhs_search_comment_tool)”、专门采集特定博主内容的“[爬小红书博主软件](https://github.com/mashukui/xhs_user_post_tool)”，还有专门转换链接uid的“[小红书转换工具](https://github.com/mashukui/xhs_trans_tool)”。

这三款软件采集起来挺稳定、数据也全，但部分用户反馈，要是又想采评论又想采主页笔记，来回切换软件，用着有点麻烦。为了解决这个痛点，我把这三款软件整合到一起了，推出了全新的“**爬小红书聚合软件v1.0**”。这款软件把评论采集、达人笔记采集、uid转换这三个核心功能都包含了，提供一站式搞定的小红书数据采集方案。

## 1.2 适用人群与场景
软件适用于：
- **获客截流**：从相关行业、品牌热门作品下的评论区精准采集目标用户；
- **数据分析**：采集小红书平台数据，用于社会舆情挖掘、网络传播研究等；
- **内容创作**：分析优质博主的内容风格、热门话题，为自身创作提供参考；
- **红薯运营**：主页链接uid与小红书号的转换，需要跨工具协作的从业者。

## 1.3 结果展示
**【功能1】采集搜索笔记和评论**

采集评论界面：
![采集评论界面](https://files.mdnice.com/user/32110/ee04956a-fc9f-43f5-b115-19c8cd0a0e86.jpg)

采集到的笔记数据：（共19个字段，含：关键词,序号,笔记id,笔记链接,笔记链接_长,头图链接,笔记类型,用户id,用户主页链接,用户昵称,点赞数,笔记标题,笔记正文,收藏数,评论数,转发数,发布时间,修改时间,IP属地）
![搜索笔记.csv](https://files.mdnice.com/user/32110/5a5e5f6c-786f-4549-94a4-70964b49be79.png)

采集到的评论数据：（共11个字段，含： 笔记链接,笔记链接_长,页码,评论者昵称,评论者id,评论者主页链接,评论时间,评论IP属地,评论点赞数,评论级别,评论内容）
![评论.csv](https://files.mdnice.com/user/32110/5ce3064c-832a-4ee0-ac85-0ce7abba145f.png)


自动下载搜索到的笔记图片：
![搜索笔记图片](https://files.mdnice.com/user/32110/f8a10524-685b-460f-8c74-5f1431bfe4d8.png)

**【功能2】根据主页链接采集笔记**

采集主页笔记界面：
![采集主页笔记页面](https://files.mdnice.com/user/32110/0b970c66-ae38-4185-821e-f1640e9ff6a2.jpg)

采集主页笔记结果：（含18个字段，含： 作者昵称,作者id,作者链接,页码,笔记标题,笔记id,笔记链接,笔记链接_长,头图链接,笔记类型,点赞数,收藏数,评论数,转发数,笔记正文,发布时间,修改时间,IP属地）
![主页笔记.csv](https://files.mdnice.com/user/32110/4fea9e53-79e9-4490-9496-32c7f408afa5.png)

采集到的主页笔记图片文件：
![主页笔记图片](https://files.mdnice.com/user/32110/4dcf4e6a-f770-4a33-95ee-db170078aa57.png)

**【功能3】链接与uid转换**

转换功能1：主页链接转xhs号
![转换功能1：主页链接转xhs号](https://files.mdnice.com/user/32110/868991d4-9b63-4479-a9e1-dffc562f87ac.jpg)

转换功能2：xhs号转主页链接（含uid）
![转换功能2：xhs号转主页链接（含uid）](https://files.mdnice.com/user/32110/aed92d65-f305-4ac2-9a20-ccd06e5e49d6.jpg)

转换功能3：app端作品链接转pc端作品链接
![转换功能3：app端作品链接转pc端作品链接](https://files.mdnice.com/user/32110/7faa66a9-5c2e-420b-85b4-f7a92796dd6d.jpg)

## 1.4 软件说明
几点说明，请详读：
1. Windows系统、Mac系统均可直接运行，无需配置编程环境
2. 软件含三个核心功能：①根据关键词/笔记链接采集评论；②根据主页链接采集笔记；③uid转换
3. 软件通过接口协议采集，并非通过模拟浏览器等RPA类，稳定性较高
4. 软件运行完成后，会在当前文件夹（即，软件所在文件夹）生成csv结果文件
5. 采集过程中，每采集一页，存一次csv。并非采完最后一次性保存！防止因异常中断导致丢失前面的数据（每页请求间隔1~2s，可自定义设置）
6. 采集过程中，有log文件详细记录运行过程，方便回溯

# 二、主要技术
## 2.1 模块分工
软件全部模块采用python语言开发，主要分工如下：
```python
tkinter：GUI软件界面
requests：发送请求
json：解析返回的响应数据
pandas：保存csv数据结果
logging：运行过程中日志记录
```
出于版权考虑，暂不公开源码，仅向用户提供软件使用。 

## 2.2 部分代码

部分代码实现： 

发送请求并解析数据：
```python
# 发送请求
r = requests.get(url, headers=h1, params=params)
# 解析数据
json_data = r.json()
```
解析响应数据，以“评论内容”字段为例：
```python
for c in json_data['data']['comments']:
	# 评论内容
	content = c['content']
	self.tk_show('评论内容:' + str(content))
	content_list.append(content)
```
保存结果数据到csv文件：
```python
# 保存数据到DF
df = pd.DataFrame(
	{
		'笔记链接': 'https://www.xiaohongshu.com/explore/' + note_id,
		'笔记链接_长': note_url2,
		'页码': page,
		'评论者昵称': nickname_list,
		'评论者id': user_id_list,
		'评论者主页链接': user_link_list,
		'评论时间': create_time_list,
		'评论IP属地': ip_list,
		'评论点赞数': like_count_list,
		'评论级别': comment_level_list,
		'评论内容': content_list,
	}
)
# 设置csv文件表头
if os.path.exists(self.result_file3):
	header = False
else:
	header = True
# 保存到csv
df.to_csv(self.result_file3, mode='a+', header=header, index=False, encoding='utf_8_sig')
self.tk_show('文件保存成功：' + self.result_file3)
```
底部版权声明：
```python
# 版权信息
copyright = tk.Label(root, text='@马哥python说 All rights reserved.', font=('仿宋', 10), fg='grey')
copyright.place(x=290, y=625)
```
日志记录模块：
```python
def get_logger(self):
    self.logger = logging.getLogger(__name__)
    # 日志格式
    formatter = '[%(asctime)s-%(filename)s][%(funcName)s-%(lineno)d]--%(message)s'
    # 日志级别
    self.logger.setLevel(logging.DEBUG)
    # 控制台日志
    sh = logging.StreamHandler()
    log_formatter = logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M:%S')
    # info日志文件名
    info_file_name = time.strftime("%Y-%m-%d") + '.log'
    # 保存到特定目录下
    case_dir = r'./logs/'
    info_handler = TimedRotatingFileHandler(filename=case_dir + info_file_name,
                                        when='MIDNIGHT',
                                        interval=1,
                                        backupCount=7,
                                        encoding='utf-8')
```

# 三、功能与使用
## 3.1 一键配置cookie
开始采集前，先用内置的《cookie小工具》自动配置好cookie。
![7c14954d150d91af132bc7d82bb64cc3](https://github.com/user-attachments/assets/d7ade547-18d9-4d49-9a46-c7103e2b8ed3)

这样，获取到的cookie值就自动写入cookie.txt文件中了，告别繁琐的手动获取。
## 3.2 软件登录
用户登录界面：需要登录。
## 3.3 启动采集
1）登录成功之后，选择需要的功能模块（搜索笔记/博主笔记/评论）；

2）设置相关参数（如关键词、时间范围、博主链接等）；

3）点击「开始执行」，等待采集完成（可实时查看采集进度）；

4）采集完成后，在默认的当前文件夹中查看csv数据文件或图片下载等。

## 3.4 演示视频
软件使用的完整过程演示视频：[【工具演示】小红书聚合采集软件](https://mp.weixin.qq.com/s/t9cKGsgJoI9rca3I1w5RdA)

# 四、付费说明
## 4.1 卡密说明
费用如下：
```python
日卡：使用期限1天，39元。日卡仅能购买一次。适合试用等临时需求
月卡：使用期限1个月，149元。月卡可多次购买。适合短期采集需求
季卡：使用期限3个月，399元。季卡可多次购买。适合中期采集需求
年卡：使用期限1年，799元。年卡可多次购买。适合长期采集需求
```
**方式一：自助开通（推荐）**

开通入口：https://mgnb.pro/product/xhs

**方式二：自助开通**

开通入口：https://kjyjf.xetlk.com/s/1dk7Wy

**方式三：手动开通，付费后加v（493882434）对接**
<img width="2324" height="604" alt="收款码v5" src="https://github.com/user-attachments/assets/a44fa968-e5bb-4668-922a-1d9ca94d358e" />

## 4.2 一机一码
为防止软件被恶意转卖，采用一机一码机制，一个卡密只能在一台电脑运行、不可多电脑运行。

## 4.3 软件多开
一台电脑仅允许运行一个软件，不支持软件多开。

## 4.4 软件维护
软件由本人独立原创开发，长期维护更新，提供稳定运行。

# 五、软件获取
公众号"**老男孩的平凡之路**"，后台回复"**爬小红书聚合软件**"获取最新版软件安装包。
<img width="1938" height="364" alt="二维码-公众号放底部v2" src="https://github.com/user-attachments/assets/c5d7b4b4-b507-4734-b004-63b99abe370a" />
