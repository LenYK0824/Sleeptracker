import os
import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 文件存储路径
FILE_NAME = "sleep_records.csv"
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def load_records():
    """加载历史记录"""
    records = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # 跳过标题行
            for row in reader:
                records.append({
                    "date": datetime.strptime(row[0], "%Y-%m-%d"),
                    "weekday": row[1],
                    "bedtime": datetime.strptime(row[2], "%H:%M").time()
                })
    return records

def save_records(records):
    """保存记录到CSV文件"""
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["日期", "星期", "就寝时间"])
        for r in records:
            writer.writerow([
                r["date"].strftime("%Y-%m-%d"),
                r["weekday"],
                r["bedtime"].strftime("%H:%M")
            ])

def delete_record(records):
    """删除指定日期的记录"""
    while True:
        print("\n=== 删除记录 ===")
        date_str = input("请输入要删除的日期（YYYY-MM-DD 格式，输入 q 返回）：")
        
        if date_str.lower() == 'q':
            return
        
        try:
            target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            # 查找匹配记录
            to_delete = [r for r in records if r["date"].date() == target_date]
            
            if not to_delete:
                print(f"{date_str} 没有找到记录")
                input("按回车键继续...")
                continue
                
            print(f"找到 {len(to_delete)} 条记录：")
            print("{:<12} {:<10} {:<8}".format("日期", "星期", "就寝时间"))
            print("-" * 30)
            for r in to_delete:
                print("{:<12} {:<10} {:<8}".format(
                    r["date"].strftime("%Y-%m-%d"),
                    r["weekday"],
                    r["bedtime"].strftime("%H:%M")
                ))
            
            confirm = input("\n确认删除以上记录吗？(y/n)：")
            if confirm.lower() == 'y':
                # 保留其他日期的记录
                new_records = [r for r in records if r["date"].date() != target_date]
                save_records(new_records)
                print("记录已删除！")
                input("按回车键返回...")
                return True
            else:
                print("取消删除")
                return False
                
        except ValueError:
            print("日期格式错误，请重新输入")

def add_record(records):
    """添加新的记录（含返回选项）"""
    while True:
        time_str = input("\n请输入昨晚就寝时间（HH:MM 格式，输入 q 返回主菜单）：")
        if time_str.lower() == 'q':
            return
        
        try:
            bedtime = datetime.strptime(time_str, "%H:%M").time()
            today = datetime.now().date()
            
            # 覆盖当天旧记录
            new_records = [r for r in records if r["date"].date() != today]
            new_records.append({
                "date": datetime.combine(today, datetime.min.time()),
                "weekday": datetime.now().strftime("%A"),
                "bedtime": bedtime
            })
            
            save_records(new_records)
            print(f"{today} 记录已保存！")
            input("按回车键继续...")
            return
        except ValueError:
            print("格式错误，请重新输入！")

def view_records(records):
    """查看历史记录（含返回选项）"""
    while True:
        print("\n=== 历史记录 ===")
        if not records:
            print("暂无记录")
        else:
            print("{:<12} {:<10} {:<8}".format("日期", "星期", "就寝时间"))
            print("-" * 30)
            for r in sorted(records, key=lambda x: x["date"], reverse=True):
                print("{:<12} {:<10} {:<8}".format(
                    r["date"].strftime("%Y-%m-%d"),
                    r["weekday"],
                    r["bedtime"].strftime("%H:%M")
                ))
        
        choice = input("\n输入 q 返回主菜单：")
        if choice.lower() == 'q':
            return

def plot_records(records):
    """生成优化后的统计图表（已修复日期范围错误）"""
    if not records:
        print("暂无数据可生成图表")
        input("按回车键返回...")
        return
    
    # 准备数据
    sorted_records = sorted(records, key=lambda x: x["date"])
    dates = [r["date"] for r in sorted_records]
    
    # 使用有效基准日期（1970-01-01）
    base_date = datetime(1970, 1, 1)
    times = [datetime.combine(base_date, r["bedtime"]) for r in sorted_records]

    # 创建画布和坐标轴
    plt.figure(figsize=(12, 7))
    ax = plt.gca()
    
    # 绘制带数据标记的折线图
    ax.plot(dates, times, 
           marker='o', 
           markersize=8,
           linestyle='--',
           color='#2c7bb6',
           linewidth=2,
           markerfacecolor='#d7191c',
           markeredgewidth=1)
    
    # 设置日期格式
    date_format = mdates.DateFormatter('%m/%d')
    ax.xaxis.set_major_formatter(date_format)
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    
    # 设置时间格式（仅显示小时:分钟）
    time_format = mdates.DateFormatter('%H:%M')
    ax.yaxis.set_major_formatter(time_format)
    
    # 自动旋转日期标签
    plt.xticks(rotation=45, ha='right')
    
    # 添加数据标签
    for date, time in zip(dates, times):
        plt.text(date, time, 
                time.strftime("%H:%M"),
                ha='center',
                va='bottom',
                fontsize=9,
                color='#2c7bb6')
    
    # 设置坐标轴范围
    buffer = 0.5  # 半天的缓冲期
    ax.set_xlim([min(dates) - timedelta(days=buffer), 
                max(dates) + timedelta(days=buffer)])
    
    # 设置网格线和样式
    ax.grid(True, 
           linestyle='--', 
           alpha=0.7,
           color='#cccccc')
    
    # 添加标题和标签
    plt.title("就寝时间趋势分析", 
             fontsize=14, 
             pad=20,
             color='#2c7bb6')
    plt.xlabel("日期", 
              fontsize=12,
              labelpad=10)
    plt.ylabel("就寝时间", 
              fontsize=12,
              labelpad=10)
    
    # 优化布局
    plt.tight_layout()
    
    # 显示图表
    plt.show()
    input("图表已显示，按回车键返回主菜单...")

def main():
    records = load_records()
    
    while True:
        print("\n=== 睡眠时间记录系统 ===")
        print("1. 添加今日记录")
        print("2. 查看历史记录")
        print("3. 显示统计图表")
        print("4. 删除记录")
        print("5. 退出系统")
        
        choice = input("请输入选项（1-5）：")
        
        if choice == "1":
            add_record(records)
            records = load_records()
        elif choice == "2":
            view_records(records)
        elif choice == "3":
            plot_records(records)
        elif choice == "4":
            if delete_record(records):
                records = load_records()
        elif choice == "5":
            print("感谢使用，再见！")
            break
        else:
            print("无效输入，请重新选择")
            input("按回车键继续...")

if __name__ == "__main__":
    main()