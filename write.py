def write(a=""):
    with open("test.txt",'a',encoding='utf-8') as f:
        f.write("\n"+a)