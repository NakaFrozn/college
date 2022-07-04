# %%
import camelot
import os
import re

# %%
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


def get_tables(year,file):
    file_path="./downloads/"+year+"/"+file
    if os.path.exists("./output/"+year)==False:    # Check if folder has been created
        os.mkdir("./output/"+year)
    output_path="./output/"+year+"/"+file+".xlsx"
    school = file.split(".")[0]
    try:
        tables = camelot.read_pdf(file_path,flavor='stream',pages='1-end')
        tables.export(path=output_path,f='excel')
    except IndexError:
        print("Camelot可能无法处理当前文件，尝试手动")
        return
    except(Exception) as e:
        print("处理",year,"/",file,"时遇到问题。")
        print(e)
        return -1
    print("处理",year,"/",file,"已完成。")
    return 0

# 控制台测试，日常请勿执行。
#get_tables("2017","中南财经政法大学2017届毕业生就业质量报告.pdf")


# %%
# Read the pdf files
print("Reading files in /downloads folder")
folder_list = os.listdir("./downloads")
folder_list_select = [x for x in folder_list if re.findall(r'\.',x)==[]]
print("当前download库中有以下年份的文件，请选择年份处理，或选择all\n")
for i in folder_list_select:
    print(i)
year = input(i)
if year == "all":
    year_list = folder_list_select
    for year in year_list:
        read_files(year)
else:
    read_files(year)



