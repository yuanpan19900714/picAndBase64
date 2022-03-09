import base64
f=open('D:\\03-life\\01-Documents\\1寸.jpg','rb') #二进制方式打开图文件
ls_f=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
f.close()
print(str(ls_f,'utf-8'))