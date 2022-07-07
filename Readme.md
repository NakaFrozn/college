# 抓取PDF中的表格
@Naka_Frozn  
2022-07-04

## 安装与准备
请在使用前安装库与代码
若你使用Windows 32bit or 64bit 操作系统，请按以下说明操作  
1. 安装camelot-py库，可使用pip install camelot-py  
2. 安装opencv-python库，可使用pip install opencv-python  
3. 请在网站下载Ghostscript，并配置环境变量，参照本网站 https://camelot-py.readthedocs.io/en/master/user/install-deps.html  
4. 安装Pycryptodome库。  

<b>若你使用Anaconda等环境，请一定在Anaconda中安装以上涉及的库</b>  

你需要在使用前做以下事情：
1. 确保你已经安装好所有库与配置完成
2. 在目录下新建/downloads/文件夹，并以将每个年份的报告pdf放在以年份命名的子目录下。    

## 使用注意事项
1. Camelot库无法识别图像表格，只能抓取文本表格。  
2. PDF抓取时间大约在30s-60s一份就业质量报告，若遇到识别错误，会弹出是否继续识别的请求。在一般情况下，不建议打断识别进程。识别一年的就业质量报告可能需要40分钟到一个小时的时间。
3. 由于各校会美化表格，在识别过程中会遇到识别结果错位，或无法识别的情况。请翻阅控制台记录，如遇到camelot无法识别时，会出现建议手动的提示。  

## 联系方式
使用中有遇到问题，请查阅  https://camelot-py.readthedocs.io/en/master/  
或联系 jonaszhxie@outlook.com 
