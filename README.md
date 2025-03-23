# 🌙 睡眠时间追踪器

[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/yourusername/sleep-tracker/)

一个基于命令行的睡眠时间记录分析工具，自动生成可视化趋势图表，助您改善作息习惯。

![示例界面](https://via.placeholder.com/800x400.png/2c7bb6/ffffff?text=Sleep+Tracker+Demo)

## 目录
- [功能特性](#✨-功能特性)
- [快速开始](#🚀-快速开始)
  - [安装依赖](#安装依赖)
  - [运行程序](#运行程序)
- [使用指南](#📖-使用指南)
  - [主菜单](#主菜单导航)
  - [功能详解](#功能详解)
- [数据管理](#🔧-数据管理)
- [技术细节](#⚙️-技术细节)
- [常见问题](#❓-常见问题)
- [贡献指南](#👥-贡献指南)
- [许可证](#📄-许可证)

## ✨ 功能特性

### 核心功能
- **智能记录**
  - 🕒 自动捕获当前日期和时间
  - 📅 每天覆盖旧记录防止重复
  - 🌐 中英双语星期显示（自动识别系统语言）

### 数据分析
- 📈 **交互式图表**
  - 时间趋势折线图
  - 数据点标签显示具体时间
  - 自适应日期范围
- 📁 **数据导出**
  - 一键导出CSV
  - 支持Excel直接打开

### 用户体验
- 🛡 **输入验证**
  - 时间格式自动检查
  - 删除操作二次确认
- 🔄 **导航系统**
  - 任意界面返回主菜单
  - 操作结果即时反馈

## 🚀 快速开始

### 安装依赖
```bash
# 安装Matplotlib可视化库
pip install matplotlib
# 克隆仓库
git clone https://github.com/yourusername/sleep-tracker.git

# 进入目录
cd sleep-tracker

# 启动程序
python sleep_tracker.py

=== 睡眠时间记录系统 ===
1. 添加今日记录
2. 查看历史记录
3. 显示统计图表
4. 删除记录
5. 退出系统

请输入昨晚就寝时间（HH:MM 格式，输入 q 返回主菜单）：23:45
2024-03-15 记录已保存！

日期         星期        就寝时间
------------------------------
2024-03-15  Friday      23:45
2024-03-14  Thursday    00:30

确认删除以上记录吗？(y/n)：n
取消删除

日期,星期,就寝时间
2024-03-15,Friday,23:45
2024-03-16,Saturday,00:15

graph TD
    A[主菜单] --> B[添加记录]
    A --> C[查看记录]
    A --> D[统计图表]
    A --> E[删除记录]
    B --> F[CSV存储]
    C --> F
    D --> G[Matplotlib]
    E --> F

# 解决方案：在代码开头添加
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows
# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # MacOS

# Linux/Mac系统需要写权限
chmod 755 sleep_records.csv

---

### 配套资源建议
1. 在`screenshots/`目录添加实际运行截图：
   - `main-menu.png` 主菜单界面
   - `chart-demo.png` 统计图表示例
2. 添加`CONTRIBUTING.md`贡献指南
3. 创建`.github/ISSUE_TEMPLATE`用于问题反馈

此README提供完整的项目说明，用户可根据实际需求调整占位符内容（如GitHub仓库链接、示例图片等）。
