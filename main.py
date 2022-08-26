import os
import json
from shutil import copyfile
from sys import exit
import colorama
from colorama import  init,Fore,Back,Style
import re
import shutil
import stat
init(autoreset=True)
times = 0
for root, dirs, files in os.walk("E://bilibilidownload//ss1733//"):
	#print("当前目录路径:", root)
	#print("当前目录下所有子目录:", dirs)
	#print("当前路径下所有非目录子文件:", files)
	if times == 0:
		all = dirs
		for folder in all:
			path = root + folder +"//1//" + folder + ".info"
			with open(path,encoding='utf-8') as f_obj:
				cont = json.load(f_obj)
				dis = cont["Description"]
				dis = dis.replace(" / "," ")
				a = root + folder +"//1//" + folder + "_1_0.mp4"  #源文件的名称
				b = "E://done//" + folder + "_1_0.mp4"  #复制后文件名称
				c = "E://done//" + dis + ".mp4"  #重命名后文件名称
				#b = root + folder +"//1//" + dis + ".mp4"
				#c = "E://done//" + dis + ".mp4"
				copyfile(a,b)
				try:
					os.rename(b,c)
				except FileExistsError:
					print(Back.RED + "警告：文件重名" )
					print("文件：" + c )
					choice = input("A=替换 B=跳过 请选择：")
					if choice.lower() == "a":
						os.remove(c)
						os.rename(b,c)
						print(Back.GREEN + "处理完成！")
						print( "标题："+ dis +"\n" + "路径：" + c + "\n" )
						continue
					elif choice.lower() == "b":
						print("\n")
						pass
					else:
						print("输入无效，已跳过！\n")
						pass
				print( "标题："+ dis +"\n" + "路径：" + c + "\n" )
				f_bin = open(c,"rb")
				f_bin.seek(3)
				done_fbin = f_bin.read()
				#print(f_bin)
				with open(c,"wb") as file_object:
					file_object.write(done_fbin)
				file_object.close()
				f_bin.close()
				print(Back.GREEN + "处理完成！")
	else:
		times = 1
	
	
	

"E://bilibilidownload//ss21717//18231463//1//18231463.info"
