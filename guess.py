import random

r = random.randint(1, 100)
while True:
	num = input('請輸入數字：')#字串
	num = int(num) #轉換成數字
	if r == num:
		print('終於猜對了')
		break
	elif r < num:
		print('比答案大')
	elif r > num:
		print('比答案小')		
		
