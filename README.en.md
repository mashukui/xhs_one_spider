# xhs_one_spider - Xiaohongshu Aggregator Spider

**Author:** @马哥python说

---

## Overview

Xiaohongshu (Little Red Book) is one of China's most influential community-driven product discovery platforms, with millions of users and extremely high daily active rates. The notes on this platform contain rich information value.

To meet different data collection needs, I independently developed three separate tools in the past:
- **Search Comment Spider**: For collecting comments based on search keywords
- **Creator Spider**: For collecting content from specific creators
- **Link Converter**: For converting links and user IDs

While these tools were stable and comprehensive, some users reported that having to switch between them when they wanted to collect both comments and creator notes was inconvenient. To solve this pain point, I integrated all three functions into one tool and launched the new **"Xiaohongshu Aggregator Spider v1.0"**. This software provides a one-stop solution for Xiaohongshu data collection, including comment collection, creator note collection, and link/ID conversion.

---

## Usage Scenarios

- **Lead Generation**: Precisely collect target users from comment sections of popular posts in related industries or brands
- **Data Analysis**: Collect Xiaohongshu platform data for social sentiment mining, online propagation research, etc.
- **Content Creation**: Analyze content styles and trending topics from top creators to provide references for your own content
- **Operation Management**: Convert home page links and user IDs, useful for professionals who need cross-tool collaboration

---

## Features

### Feature 1: Search Notes and Comments Collection

**Collection Interface:**

**Collected Note Data** (19 fields):
- Keyword, Serial Number, Note ID, Note Link, Long Note Link, Cover Image Link, Note Type, User ID, User Profile Link, User Nickname, Like Count, Note Title, Note Content, Favorite Count, Comment Count, Share Count, Publish Time, Modify Time, IP Location

**Collected Comment Data** (11 fields):
- Note Link, Long Note Link, Page Number, Commenter Nickname, Commenter ID, Commenter Profile Link, Comment Time, Comment IP Location, Comment Like Count, Comment Level, Comment Content

**Automatic Download of Search Result Images:**

---

### Feature 2: Collect Notes by Creator Profile Link

**Collection Interface:**

**Collected Creator Notes** (18 fields):
- Author Nickname, Author ID, Author Link, Page Number, Note Title, Note ID, Note Link, Long Note Link, Cover Image Link, Note Type, Like Count, Favorite Count, Comment Count, Share Count, Note Content, Publish Time, Modify Time, IP Location

**Collected Creator Note Images:**

---

### Feature 3: Link and ID Conversion

**Conversion 1: Home Page Link → Xiaohongshu ID**

**Conversion 2: Xiaohongshu ID → Home Page Link (with UID)**

**Conversion 3: App Link → PC Link**

---

## Important Notes

- Works on both Windows and Mac systems without requiring any programming environment setup
- Contains three core functions:
  1. Collect comments by keyword/note link
  2. Collect notes by creator profile link
  3. UID conversion
- Uses API protocols for data collection (not RPA simulation), ensuring high stability
- After the software completes, CSV result files are generated in the current folder (the folder where the software is located)
- Data is saved after each page is collected, not all at once at the end. This prevents data loss from unexpected interruptions (1-2 second request interval between pages, customizable)
- Detailed log files are recorded during collection for easy troubleshooting

---

## Technology Stack

All modules are developed in Python:

- **tkinter**: GUI interface
- **requests**: HTTP requests
- **json**: Response data parsing
- **pandas**: CSV data output
- **logging**: Runtime log recording

**Note:** Due to copyright concerns, source code is not publicly available. Only the software itself is provided to users.

---

## Code Examples

### Sending Requests and Parsing Data

```python
# Send request
r = requests.get(url, headers=h1, params=params)
# Parse data
json_data = r.json()
```

### Parsing Response Data (Example: Comment Content)

```python
for c in json_data['data']['comments']:
    # Comment content
    content = c['content']
    self.tk_show('Comment Content: ' + str(content))
    content_list.append(content)
```

### Saving Data to CSV File

```python
# Save data to DataFrame
df = pd.DataFrame({
    'Note Link': 'https://www.xiaohongshu.com/explore/' + note_id,
    'Long Note Link': note_url2,
    'Page Number': page,
    'Commenter Nickname': nickname_list,
    'Commenter ID': user_id_list,
    'Commenter Profile Link': user_link_list,
    'Comment Time': create_time_list,
    'Comment IP Location': ip_list,
    'Comment Like Count': like_count_list,
    'Comment Level': comment_level_list,
    'Comment Content': content_list,
})

# Set CSV headers
if os.path.exists(self.result_file3):
    header = False
else:
    header = True

# Save to CSV
df.to_csv(self.result_file3, mode='a+', header=header, index=False, encoding='utf_8_sig')
self.tk_show('File saved successfully: ' + self.result_file3)
```

### Copyright Footer

```python
# Copyright information
copyright = tk.Label(root, text='@马哥python说 All rights reserved.', font=('SimSun', 10), fg='grey')
copyright.place(x=290, y=625)
```

### Logging Module

```python
def get_logger(self):
    self.logger = logging.getLogger(__name__)
    # Log format
    formatter = '[%(asctime)s-%(filename)s][%(funcName)s-%(lineno)d]--%(message)s'
    # Log level
    self.logger.setLevel(logging.DEBUG)
    # Console log
    sh = logging.StreamHandler()
    log_formatter = logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M:%S')
    # Info log filename
    info_file_name = time.strftime("%Y-%m-%d") + '.log'
    # Save to specific directory
    case_dir = r'./logs/'
    info_handler = TimedRotatingFileHandler(
        filename=case_dir + info_file_name,
        when='MIDNIGHT',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
```

---

## Setup Instructions

1. Before starting, use the built-in **"Cookie Tool"** to automatically configure your cookie
2. After login, select the function module you need (Search Notes / Creator Notes / Comments)
3. Set relevant parameters (keywords, time range, creator link, etc.)
4. Click **"Start Execution"** and wait for collection to complete (you can view progress in real-time)
5. After completion, check the CSV data files or downloaded images in the default current folder

**Demo Video:** [Tool Demo] Xiaohongshu Aggregator Spider Collection Tool

---

## Pricing

| Plan | Duration | Price | Purchase Limit | Suitable For |
|------|----------|-------|----------------|--------------|
| Daily Pass | 1 day | ¥39 | One-time | Trial or temporary needs |
| Monthly Pass | 1 month | ¥149 | Multiple | Short-term collection needs |
| Quarterly Pass | 3 months | ¥399 | Multiple | Medium-term collection needs |
| Annual Pass | 1 year | ¥799 | Multiple | Long-term collection needs |

### Purchase Options

**Option 1: Self-Service (Recommended)**
- Link: https://mgnb.pro/product/xhs

**Option 2: Self-Service**
- Link: https://kjyjf.xetlk.com/s/1dk7Wy

**Option 3: Manual Setup**
- After payment, add WeChat (493882434) to connect

---

## Security & Usage Limits

- To prevent software resale, a **one-device-one-code** mechanism is used. Each code can only run on one computer
- Only one software instance is allowed per computer (multi-instance is not supported)

---

## Author Info

This software is independently developed and maintained by me, with long-term updates and stable operation guaranteed.

**Official Account:** "老男孩的平凡之路"
**Reply "爬小红书聚合软件" (Xiaohongshu Aggregator Spider) in the account's backend to get the latest installation package.**

---

## Disclaimer

This tool is for **academic exchange purposes only**. Please strictly comply with relevant laws and regulations, ensure the legality and compliance of platform content, and **prohibit any commercial use**!
