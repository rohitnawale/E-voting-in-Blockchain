def per(head, tail=''):
    if len(head)==0:
        print(tail)
    else:
        for i in range(len(head)):
            per(head[0:i]+head[i+1:],tail+head[i])

per('abc')