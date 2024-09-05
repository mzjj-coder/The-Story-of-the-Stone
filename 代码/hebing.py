import csv
import glob

files = glob.glob('*.csv') #遍历当前目录下的csv文件
readList = []  # 用来装合并文件的内容
titleList = ["弹幕ID","用户名","弹幕内容","发布时间","点赞数","期数"]  # 文件标题

for i in files:
    # i 是文件名
    #############读取多个csv文件内容###################
    with open(i.format(i), 'r', newline="", encoding="utf-8") as read_csvfile:
        readcsv_all = csv.reader(read_csvfile)
        next(read_csvfile)  # 跳过第一行“标题”
        for line in readcsv_all:

            output = i.rsplit('.', 1)[0]#文件名分隔取.前面的字符

            line.append(output)  # 添加“文件名”作为新的列
            readList.append(line)

        ############写入文件##############################
with open('CLEAN_data.csv', 'a+', newline="", encoding="utf-8") as f:
    csv_write = csv.writer(f)
    csv_write.writerow(titleList)  # 写入文件标题
    for line in readList:


        csv_write.writerow(line)
