import camelot
import os
import re
import tkinter as tk
from tkinter.filedialog import askopenfilename

def read_files(year):
    folder_path = "./downloads/"+year+"/"
    try:
        file_list = os.listdir(folder_path)
    except(Exception) as e:
        print("读取文件出现问题")
        print(e)
        return -1
    n = len(file_list)
    if n==0:
        print(folder_path,"文件夹下无文件，请核实。")
        return 0
    for file_index in len(file_list):
        if re.findall(r'.pdf$', file_list[file_index])==[]:
            file_list.pop(file_index)
    del(file_index)
    count = 0
    for file in file_list:
        count = count + 1
        print("现在正在处理",file,"(",count,"/",n,")")
        i = get_tables(year,file)
        if i==-1:
            process_info = input("处理时遇到错误，是否继续？ Y/N")
            if process_info == 'Y' or process_info == 'y':
                continue
            else:
                print("已终止处理，请核查以下文件")
                print(folder_path,file)
                return -1
    print(year,"所有文件已处理完毕。")
    print("---------------------------------")
    return 0

def get_tables(year="",file="",method="multi",file_path="",output_path="./output/output.xlsx"):
    if os.path.exists("./output")==False:
        os.mkdir("./output")
    if method == "multi":
        file_path="./downloads/"+year+"/"+file
        output_path="./output/"+year+"/"+file+".xlsx"
        if os.path.exists("./output/"+year)==False:    # Check if folder has been created
            os.mkdir("./output/"+year)
        school = file.split(".")[0]
    try:
        print("Processing")
        tables = camelot.read_pdf(file_path,flavor='stream',pages='1-end')
        tables.export(path=output_path,f='excel')
    except IndexError:
        print("Camelot可能无法处理当前文件，尝试手动")
        return
    except(Exception) as e:
        print("处理",year,"/",file,"时遇到问题。")
        print(e)
        return -1
    if method=="multi":
        print("处理",year,"/",file,"已完成。")
    else:
        print("文件处理已完成，输出为output.xlsx。")
    return 0

# Read the pdf files
def main():
    print("Reading files in /downloads folder")
    folder_list = os.listdir("./downloads")
    folder_list_select = [x for x in folder_list if re.findall(r'\.',x)==[]]
    print("当前download库中有以下年份的文件，请选择年份处理，或选择all")
    print("自行选择文件请输入dialog(d)")
    print("退出请输入quit(q)\n")
    for i in folder_list_select:
        print(i)
    year = input("请输入命令：")
    if year == "dialog" or year =="d":
        root=tk.Tk()
        FilePath=""
        FilePath=askopenfilename()
        while FilePath=="" or re.findall(r'.pdf$', FilePath)==[]:
            print("未选择文件或选择的文件非pdf文件。继续？ y/n")
            a = input()
            if(a=="y" or a=="Y"):
                FilePath=askopenfilename()
                continue
            if(a=="n" or a=="N"):
                return 0
        get_tables(method="single",file_path=FilePath)
    elif year =="quit" or year=="q":
        print("程序已终止。")
        return 0
    elif year == "all":
        year_list = folder_list_select
        for year in year_list:
            read_files(year)
    else:
        read_files(year)
    return 0

if __name__=="__main__":
    main()


#%%
# 控制台测试，日常请勿执行。
#get_tables("2017","中南财经政法大学2017届毕业生就业质量报告.pdf")

