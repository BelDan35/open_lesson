from itertools import cycle

# Функции методов шифрования

# Метод Виженера ------
# Шифратор
def encode_vijn(message, key, alp, b):
    f = lambda arg: alp[(alp.index(arg[0])+alp.index(arg[1])%b)%b]
    return ''.join(map(f, zip(message, cycle(key))))

# Дешифратор
def decode_vijn(message, key, alp, b):
    f = lambda arg: alp[alp.index(arg[0])-alp.index(arg[1])%b]
    return ''.join(map(f, zip(message, cycle(key))))

# Рельсовый метод ------
# Шифратор
def encode_rail_fence(message, key):
	rail = [['\n' for i in range(len(message))]
				for j in range(key)]
	dir_down = False
	row, col = 0, 0
	for i in range(len(message)):
		if (row == 0) or (row == key - 1):
			dir_down = not dir_down
		rail[row][col] = message[i]
		col += 1
		if dir_down:
			row += 1
		else:
			row -= 1
	result = []
	for i in range(key):
		for j in range(len(message)):
			if rail[i][j] != '\n':
				result.append(rail[i][j])
	return("" . join(result))

# Дешифратор
def decode_rail_fence(message, key):
	rail = [['\n' for i in range(len(message))]
				for j in range(key)]
	dir_down = None
	row, col = 0, 0
	for i in range(len(message)):
		if row == 0:
			dir_down = True
		if row == key - 1:
			dir_down = False
		rail[row][col] = '*'
		col += 1
		if dir_down:
			row += 1
		else:
			row -= 1		
	index = 0
	for i in range(key):
		for j in range(len(message)):
			if ((rail[i][j] == '*') and
			(index < len(message))):
				rail[i][j] = message[index]
				index += 1	
	result = []
	row, col = 0, 0
	for i in range(len(message)):	
		if row == 0:
			dir_down = True
		if row == key-1:
			dir_down = False		
		if (rail[row][col] != '*'):
			result.append(rail[row][col])
			col += 1	
		if dir_down:
			row += 1
		else:
			row -= 1
	return("".join(result))

# Метод Цезаря ------
# Шифратор
def encode_caesar(message, key, alp):

    message_lov = message.lower()
    result = ''

    for i in message_lov:
        position = alp.find(i)
        mew_position = position + key
        if i in alp:
            result += alp[mew_position]
        else:
            result += i
    return result

# Дешифратор
def decode_caesar(message, key, alp):

    message_lov = message.lower()
    result = ''

    for i in message_lov:
        position = alp.find(i)
        mew_position = position - key
        if i in alp:
            result += alp[mew_position]
        else:
            result += i
    return result