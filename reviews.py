# 增加count功能,掌握文件讀取狀態
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0 :
			print(len(data))
print('檔案內容總共有', len(data), '筆留言')
print('第一筆留言內容如下: ')
print(data[0])

#計算留言平均長度
sum_len = 0
for d in data:
    sum_len += len(d)
    print(sum_len)

print('留言的平均長度: ',sum_len/len(data))

#增加留言長度<100的篩選功能
new =[]
for d in data:
    if len(d) < 100:
        new.append(d)
print('總共有', len(new), '筆留言長度小於100')
print('第一筆留言內容如下: ')
print(new[0])
print('--------------------------------------------------------------------')
print('第二筆留言內容如下: ')
print(new[1])

#統計留言內容提到good的筆數
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('總共有', len(good), '筆留言提到good')

#計數文字數與查詢文字出現次數
wc = {}
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1 #若字典裡已有，則在既有value值上再加1
        else:
            wc[word] = 1 #若字典裡沒有，則增加新的key進入wc內
for word in wc:
    if wc[word] > 100:
        print(word, wc[word])
print(len(wc))
print(wc['Allen'])
while True:
    word = input('請問您想查詢什麼字? ')  
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過的次數為: ', wc[word])
    else:
        print('這個字未曾出現過喔!')
print('感謝您的查詢!')


