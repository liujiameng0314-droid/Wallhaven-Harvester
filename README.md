# 🖼️ Wallhaven-Harvester

> 基于 DrissionPage 和 BeautifulSoup 的全自动 4K/高清壁纸批量下载工具。

## 💡 项目简介

**Wallhaven-Harvester** 是一个专门为壁纸爱好者设计的自动化脚本。它通过模拟浏览器操作，在著名的 [Wallhaven.cc](https://wallhaven.cc) 上执行关键词搜索，并自动解析、获取原图链接，最后批量下载到你指定的本地文件夹中。

相比于手动一张张右键保存，本工具可以让你一次性收割成百上千张高画质壁纸。

## ✨ 核心特性

* **🔍 动态搜索**: 支持用户自定义关键词，实时检索站内壁纸资源。
* **📑 多页抓取**: 模拟鼠标滚动加载，支持多页面壁纸链接同时获取。
* **🚀 原图解析**: 自动识别预览图背后的真实原图地址（Raw Image），确保下载的是最高画质。
* **📂 自动化归档**: 根据关键词自动创建本地文件夹，并按序号对壁纸进行重命名。

## 🛠️ 环境依赖

运行本项目前，请确保已安装以下 Python 扩展库：

```bash
pip install DrissionPage requests beautifulsoup4
