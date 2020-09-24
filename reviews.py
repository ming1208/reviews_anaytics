data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
print(len(data))
print('檔案內容總共有', len(data), '筆留言', '其中的第一筆留言內容如下: ')
print('-----------------------------------------------------------')
print(data[0])