# xhs_one_spider

> 🔥 Xiaohongshu data collection tool / Xiaohongshu crawler GUI, supporting note collection, comment collection, creator profile note collection, image download, CSV export, and link conversion.
>
> 💡 Supports Windows/macOS with no Python environment required. This repository is used for software introduction, release distribution, usage documentation, and issue feedback. The complete source code is not publicly available.
>
> [⬇️Download Latest Release](https://github.com/mashukui/xhs_one_spider/releases/) | [🎬Video Demo](https://www.bilibili.com/video/BV1Z6rHBfExT/) | [💳Purchase Access](https://mgnb.pro/product/xhs)

<p align="center">
  <a href="README.md">简体中文 README</a> | <a href="README.en.md">English README</a>
</p>

## 👋 Overview

`xhs_one_spider` is a desktop GUI tool designed for Xiaohongshu data collection scenarios. It combines search note collection, comment collection, creator profile note collection, and link conversion into one client. Users do not need to install or configure a Python environment. Download the client, log in, and start using it.

It is suitable for the following scenarios:

| Scenario | Description |
| --- | --- |
| ✅ Lead generation | Collect potential leads from comments under industry, brand, or competitor-related notes |
| ✅ Seeding analysis | Collect keyword-related notes, comments, and interaction data to analyze user interests |
| ✅ Content research | Analyze high-quality creator notes, topic directions, and engagement performance |
| ✅ Xiaohongshu operations | Convert profile links, Xiaohongshu IDs, uids, and note links between different formats |

## ⚙️ Features

| Feature | Description | Output |
| --- | --- | --- |
| ✅ Search note collection | Search Xiaohongshu notes by keyword and collect basic note data | CSV, image files |
| ✅ Comment collection | Collect comments from search results or specified note links | CSV |
| ✅ Creator profile note collection | Collect note lists from creator profile links | CSV, image files |
| ✅ Link and uid conversion | Convert between profile links, Xiaohongshu IDs, uids, and note links | CSV |
| ✅ Incremental saving | Save data to CSV after each page to reduce data loss caused by interruptions | CSV |
| ✅ Runtime logs | Record runtime logs for troubleshooting | logs files |

## 🚀 Quick Start

1. Open [Releases](https://github.com/mashukui/xhs_one_spider/releases/) and download the latest version.
2. Extract the package and run the client for your operating system.
3. Use the built-in cookie helper to configure your cookie.
4. Log in to the software account.
5. Select a collection module and enter a keyword, note link, or creator profile link.
6. Click "Start" and wait for the collection task to finish.
7. Check the CSV files, image files, and log files in the software directory.

## 💻 Supported Platforms

| Platform | Support |
| --- | --- |
| Windows | Supported. Download and run the Windows client |
| macOS | Supported. Download and run the macOS client |

## 🖼️ Screenshots

### Search Note and Comment Collection

Comment collection interface:

![Comment collection interface](https://files.mdnice.com/user/32110/ee04956a-fc9f-43f5-b115-19c8cd0a0e86.jpg)

Search note result:

![Search notes CSV](https://files.mdnice.com/user/32110/5a5e5f6c-786f-4549-94a4-70964b49be79.png)

Comment collection result:

![Comments CSV](https://files.mdnice.com/user/32110/5ce3064c-832a-4ee0-ac85-0ce7abba145f.png)

Automatically downloaded search note images:

![Search note images](https://files.mdnice.com/user/32110/f8a10524-685b-460f-8c74-5f1431bfe4d8.png)

### Creator Profile Note Collection

Creator profile note collection interface:

![Creator profile note collection interface](https://files.mdnice.com/user/32110/0b970c66-ae38-4185-821e-f1640e9ff6a2.jpg)

Creator profile note result:

![Creator profile notes CSV](https://files.mdnice.com/user/32110/4fea9e53-79e9-4490-9496-32c7f408afa5.png)

Automatically downloaded creator profile note images:

![Creator profile note images](https://files.mdnice.com/user/32110/4dcf4e6a-f770-4a33-95ee-db170078aa57.png)

### Link and uid Conversion

Convert a profile link to a Xiaohongshu ID:

![Convert profile link to Xiaohongshu ID](https://files.mdnice.com/user/32110/868991d4-9b63-4479-a9e1-dffc562f87ac.jpg)

Convert a Xiaohongshu ID to a profile link:

![Convert Xiaohongshu ID to profile link](https://files.mdnice.com/user/32110/aed92d65-f305-4ac2-9a20-ccd06e5e49d6.jpg)

Convert a mobile app note link to a PC note link:

![Convert app note link to PC note link](https://files.mdnice.com/user/32110/7faa66a9-5c2e-420b-85b4-f7a92796dd6d.jpg)

## 📊 Output Fields

The software generates different CSV files based on the selected collection module. Since there are many fields, the main field groups are shown first. You can expand the sections below to view the full field lists.

### Search Note Data

- Collection info: keyword, index
- Note info: note id, note link, long note link, cover image link, note type, note title, note content
- Author info: user id, user profile link, user nickname
- Interaction data: likes, favorites, comments, shares
- Time and location: published time, modified time, IP location

<details>
<summary>View full search note fields</summary>

Keyword, index, note id, note link, long note link, cover image link, note type, user id, user profile link, user nickname, likes, note title, note content, favorites, comments, shares, published time, modified time, IP location

</details>

### Comment Data

- Collection info: note link, long note link, page
- Commenter info: commenter nickname, commenter id, commenter profile link
- Comment info: comment time, comment IP location, comment likes, comment level, comment content

<details>
<summary>View full comment fields</summary>

Note link, long note link, page, commenter nickname, commenter id, commenter profile link, comment time, comment IP location, comment likes, comment level, comment content

</details>

### Creator Profile Note Data

- Collection info: page
- Author info: author nickname, author id, author profile link
- Note info: note title, note id, note link, long note link, cover image link, note type, note content
- Interaction data: likes, favorites, comments, shares
- Time and location: published time, modified time, IP location

<details>
<summary>View full creator profile note fields</summary>

Author nickname, author id, author link, page, note title, note id, note link, long note link, cover image link, note type, likes, favorites, comments, shares, note content, published time, modified time, IP location

</details>

## 🛠️ Technical Notes

The software is developed in Python. Core modules include:

| Module | Purpose |
| --- | --- |
| tkinter | GUI interface |
| requests | API requests |
| json | Response parsing |
| pandas | CSV export |
| logging | Runtime logging |

The software collects data through interface requests and does not rely on browser automation or RPA-style operations. During collection, results are saved by page by default. The request interval is usually about 1-2 seconds, which helps control the collection pace and reduce data loss caused by unexpected interruptions.

## 💰 Pricing

| Plan | Duration | Price | Recommended Usage |
| --- | --- | --- | --- |
| Day pass | 1 day | 39 CNY | Trial use or small one-time tasks |
| Monthly pass | 1 month | 149 CNY | Short-term collection needs |
| Quarterly pass | 3 months | 399 CNY | Medium-term collection needs |
| Yearly pass | 1 year | 799 CNY | Long-term stable use |

Purchase page: [https://mgnb.pro/product/xhs](https://mgnb.pro/product/xhs)

## 🔐 License and Activation Rules

- The software uses a one-device-one-license mechanism. One license key can only be used on one computer.
- Only one software instance is allowed on a single computer. Multiple concurrent instances are not supported.
- The software is maintained by the author, and future versions will be published through GitHub Releases.

## ❓ FAQ

### Do I need to install Python?

No. The software is packaged as a desktop client. Download the version for your operating system and run it directly.

### What is the cookie used for?

The cookie allows the software to access platform data under your current account session. Please use your own account cookie and keep related files secure.

### Will collected data be lost if the task is interrupted?

The software saves CSV files by page instead of waiting until the whole task is complete. If the task is interrupted, data from completed pages is usually still preserved in the result files.

### Where are result files saved?

By default, result files are saved in the software directory. CSV files, image files, and log files are generated by feature module.

### How much data can it collect?

The actual amount of data depends on the keyword, account status, platform API response, network environment, and collection frequency. It is recommended to set a reasonable collection range and request interval.

### What should I do if an error occurs?

Check the log files under the `logs` directory first. When reporting an issue, please provide:

- Software version
- Operating system
- Feature module used
- Keyword, creator profile link, or note link entered
- Error screenshot
- Log content around the time when the error occurred

## ⚠️ Compliance Statement

This software is intended only for lawful data analysis, learning, research, and authorized business scenarios. Users are responsible for complying with the target platform's terms of service, privacy policy, and applicable laws and regulations.

Do not use this software for:

- High-frequency, malicious, or destructive requests
- Unauthorized collection, distribution, or sale of sensitive personal information
- Activities that infringe the lawful rights of platforms, creators, or users
- Any other behavior that violates laws, regulations, or platform rules

Users are solely responsible for risks and liabilities caused by improper use.

## 📦 Get the Software

- GitHub Releases: [https://github.com/mashukui/xhs_one_spider/releases/](https://github.com/mashukui/xhs_one_spider/releases/)
- WeChat official account: `老男孩的平凡之路`
- Reply in the WeChat official account: `爬小红书聚合软件`

<img width="573" height="196" alt="二维码-公众号放底部v4" src="https://github.com/user-attachments/assets/9ad83e33-0029-433c-b2b2-6ca47e2f61eb" />
