# 增加count功能,掌握文件讀取狀態
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 :
			print(len(data))

print(len(data))
print('檔案內容總共有', len(data), '筆留言')
print('第一筆留言內容如下: ')
print(data[0])
print('--------------------------------------------------------------------')
print('第二筆留言內容如下: ')
print(data[1])