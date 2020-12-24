# import cv2
import numpy as np #导入库
# cap = cv2.VideoCapture(0) #设置摄像头 0是默认的摄像头 如果你有多个摄像头的话呢，可以设置1,2,3....
# while True:   #进入无限循环
# 	ret,frame = cap.read() #将摄像头拍到的图像作为frame值
# 	cv2.imshow('frame',frame) #将frame的值显示出来 有两个参数 前一个是窗口名字，后面是值
# 	c = cv2.waitKey(1) #判断退出的条件 当按下'Q'键的时候呢，就退出
# 	if c == ord('q'):
# 		break
# cap.release()  #常规操作
# cv2.DestroyAllWindows()

import json
with open("records.json",'r',encoding='utf-8') as load_f:
	load = json.load(load_f)

with open("records2.json",'r',encoding='utf-8') as load_f:
	load2 = json.load(load_f)

triangleCount = {}
for item in load2:
	triangleCount[item['name']] = [item['triangleCount'],item['img'],item['id'],item['sex']]


t = [set(),set(),set()]
m = 35000
n = 35000
a = np.zeros((m, n), dtype=np.int)
b = np.zeros((m, n), dtype=np.int)
for item in load:
	cnt = 0
	for item1 in item['intermediateCommunityIds']:
		t[cnt].add(item1)
		cnt = cnt + 1
	a[item['intermediateCommunityIds'][2]][item['intermediateCommunityIds'][1]] = 1
	b[item['intermediateCommunityIds'][1]][item['intermediateCommunityIds'][0]] = 1

print(a[26391][16342])
# tmp = {
# 	"id":None,
# 	"name":None,
# 	"children":[]
# }

data = []


def dfs(cnt, id):
	tmp = []
	if cnt == 0:
		children = []
		for item in load:
			if item['intermediateCommunityIds'][0] == id:
				children.append({"name": item['name'],
								 "triangleCount": triangleCount[item['name']][0],
								 "img": triangleCount[item['name']][1],
								 "id": triangleCount[item['name']][2],
								 "sex": triangleCount[item['name']][3],})
		return {
			"id": id,
			"children": children
		}
	if cnt == 1:
		count = 0
		for item in b[id]:
			if item == 1:
				print(count)
				tmp.append(dfs(cnt-1, count))
			count = count + 1
	if cnt == 2:
		count = 0
		for item in a[id]:
			if item == 1:
				print(count)
				tmp.append(dfs(cnt-1, count))
			count = count + 1
	return {
			"id": id,
			"children": tmp
		}



for item in t[2]:
	data.append(dfs(2,item))
res = {
	"id": 0,
	"children": data
}
# res = json.dumps(res)
print(type(res))
filename = 'res.json'
with open(filename,'w') as file_obj:
	json.dump(res,file_obj)