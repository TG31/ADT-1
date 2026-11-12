# Exercise 1
Stack = []
TopOfStack = -1

for i in range(10):
    Stack.append(-1)

def IsEmpty():
    return TopOfStack == -1


def IsFull():
    return TopOfStack == 9


# Exercise 2
Stack = []
for i in range(10):
    Stack.append(-1)
TopOfStack = -1

def Push(Item):
    global Stack, TopOfStack

    if TopOfStack == 9:
        return False

    TopOfStack += 1
    Stack[TopOfStack] = Item
    return True


# Exercise 3
Stack = []
for i in range(10):
    Stack.append(-1)
TopOfStack = -1

def Pop():
    global Stack, TopOfStack

    if TopOfStack == -1:
        return -1

    Item = Stack[TopOfStack]
    Stack[TopOfStack] = -1
    TopOfStack -= 1

    return Item

# Exercise 4
Stack = [8, 3]
for i in range(8):
    Stack.append(-1)
TopOfStack = 1

def Peek():
    if TopOfStack == -1:
        return -1

    return Stack[TopOfStack]


def Size():
    return TopOfStack + 1


# Exercise 5
Stack = []
for i in range(10):
    Stack.append(-1)
TopOfStack = -1

def ReverseWord(Word):
    global Stack, TopOfStack

    while TopOfStack != -1:
        Pop()

    for Letter in Word:
        Push(Letter)

    Rev = ""

    while TopOfStack != -1:
        Rev = Rev + Pop()

    return Rev
