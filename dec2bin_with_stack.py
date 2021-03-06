from stack import Stack

def dec2bin_with_stack(decnum):

    s = Stack()
    while decnum > 0:
        dig = decnum % 2
        decnum = decnum // 2
        s.push(dig)
    str_binary = ''
    while not s.isEmpty():
        str_binary += str(s.pop())

    return str_binary

if __name__ == "__main__":
    decnum = 9
    print(dec2bin_with_stack(decnum))