# # Exercise 1
# Stack = []
# TopOfStack = -1
#
# for i in range(10):
#     Stack.append(-1)
#
# def IsEmpty():
#     if TopOfStack == -1:
#         return True
#     else:
#         return False
#
#
# def IsFull():
#     if TopOfStack == 9:
#         return True
#     else:
#         return False
#
# print(Stack)
# print(TopOfStack)
# print(IsEmpty())
# print(IsFull())
from xml.etree.ElementTree import tostring

# # Exercise 2
# Stack = []
# for i in range(10):
#     Stack.append(-1)
# TopOfStack = -1
# def Push(Item):
#     global TopOfStack
#     if TopOfStack == 9:
#         return False
#     else:
#         TopOfStack += 1
#         Stack[TopOfStack] = Item
#         return True
# print(Push(15))
# print(Push(27))
# print(Stack[TopOfStack - 1], Stack[TopOfStack])
# print(TopOfStack)

# # Exercise 3
# Stack = [10, 20, 30]
# for i in range(7):
#     Stack.append(-1)
# TopOfStack = 2
# def Pop():
#     global Stack_1
#     global TopOfStack
#     varia = 0
#     if TopOfStack == -1:
#         return -1
#     else:
#         varia = Stack[TopOfStack]
#         Stack[TopOfStack] = -1
#         TopOfStack -= 1
#         return varia
# print(Pop())
# print(TopOfStack)
# print(Stack[TopOfStack - 1])
# print(Stack[TopOfStack])
# print(Stack[TopOfStack + 1])

# # Exercise 4
# Stack = [8, 3]
# for i in range(8):
#     Stack.append(-1)
# TopOfStack = 1
# def Peek():
#     global Stack
#     global TopOfStack
#     if TopOfStack == -1:
#         return -1
#     else:
#         return Stack[TopOfStack]
#
#
# def Size():
#     global TopOfStack
#     return TopOfStack + 1
# print(Peek())
# print(Stack[TopOfStack])
# print(Size())

# Exercise 5
Stack = []
for i in range(10):
    Stack.append("a")
TopOfStack = 9
def ReverseWord(Word):
    global Stack
    global TopOfStack
    if TopOfStack == 9:
        for i in range(10):
            Stack.pop()
            TopOfStack -= 1
    Rev = ""
    for i in Word:
        Stack.append(i)
        TopOfStack += 1
    for i in range(TopOfStack, -1, -1):
        Rev = Rev + Stack[i]
    return Rev
print(ReverseWord("HELLO"))
