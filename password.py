password = 'a123456'
i = 3
while True:
	pwd = input('Enter password: ')
	if pwd == password:
		print('Success')
		break
	else:
		i = i - 1
		print('wrong still have', i, 'chance')
		if i == 0:
			print('failed')
			break