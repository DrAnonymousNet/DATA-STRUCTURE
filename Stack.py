class Stack():
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        raise IndexError("Peek from empty stack")

    def isempty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

def reverse(text):
    stack = Stack()
    for c in text:
        stack.push(c)
    r_text = ""

    for i in range(len(stack)):
        r_text += stack.pop()
    return r_text

def balance_parenthesis(text):
    stk = Stack()
    opening = "({["
    closing = ")}]"
    for c in text:
        if c in opening:
            stk.push(c)
        elif c in closing:
            flag = match(stk.pop(), c)
            if not flag:
                return False
    if not stk.isempty():
        return False
    return True

def match(open, close):
    opening = "([{"
    closing = ")]}"
    return opening.index(open) == closing.index(close)


def decimal_binary(num, base):
    nums = "0123456789ABCDEF"
    stk = Stack()

    while num != 0:
        rem = num%base
        stk.push(nums[rem])
        num = num//base
    bin = ""
    for i in range(len(stk)):
        bin += str(stk.pop())
    return bin


def pre(op , ops):
    opertors = {"+":2 , "-":2, "*" : 3, "/":3, "(":1}
    return opertors[op] == opertors[ops]

def infixToPostfix(text):
    operator_stacks = Stack()
    operand_stacks = Stack()

    opertors = {"+": 2, "-": 2, "*": 3, "/": 3, "(":1}

    for c in text:

        if c == "(":
            print(0)
            operator_stacks.push(c)
        elif ")" in c:
            print(operator_stacks.stack)
            while operator_stacks.peek() != "(":
                operand_stacks.push(operator_stacks.pop())
            operator_stacks.pop()
        elif c not in opertors.keys():
            operand_stacks.push(c)
            print(1)

        elif c in opertors.keys():
            if operator_stacks.isempty():
                operator_stacks.push(c)
                print(2)
            elif not operator_stacks.isempty():
                print(3)
                if operator_stacks.peek() == "(":
                    operator_stacks.push(c)
                    continue
                flag = pre(c , operator_stacks.peek())
                if flag:
                    operand_stacks.push(operator_stacks.pop())
                    operator_stacks.push(c)
                    print(4)
                elif not flag:
                    print(5)
                    if opertors[operator_stacks.peek()] > opertors[c]:
                        print(6)
                        operand_stacks.push(operator_stacks.pop())


                        if len(operator_stacks) >= 1:

                            while len(operator_stacks) >= 1:
                                print(8)
                                operand_stacks.push(operator_stacks.pop())
                        operator_stacks.push(c)


                    elif opertors[operator_stacks.peek()] < opertors[c]:
                        print(7)
                        operator_stacks.push(c)

        #print(operator_stacks.stack, operand_stacks.stack)

    while not operator_stacks.isempty():
        operand_stacks.push(operator_stacks.pop())
    print(operand_stacks.stack)

print(infixToPostfix("a+b*c/(d-e)"))




