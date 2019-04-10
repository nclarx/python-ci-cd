a = "Message"
b = "Message"

variable_a = id(a)
variable_b = id(b)


print('The id of variable a is:', variable_a)
print('the id of variable_b is:', variable_b)

print('')

print('HOWEVER')

print('')

listOne = [1, 2, 3, 4, 5]

listTwo = listOne

listOneId = id(listOne)
listTwoId = id(listTwo)

print('The id of listOne is:', listOneId)
print('the id of listTwo is:', listTwoId)
