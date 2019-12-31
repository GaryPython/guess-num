import random

r = random.randint(1, 100)
count = 0
while True:
	count +=1 #count = count + 1
	num = input('請輸入數字：')#字串
	num = int(num) #轉換成數字
	if r == num:
		print('終於猜對了')
		break
	elif r < num:
		print('比答案大')
	elif r > num:
		print('比答案小')		
	print('這是你猜的第', count, '	次')
		
