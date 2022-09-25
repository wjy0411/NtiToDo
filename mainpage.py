from asyncore import read
import os
from read import rreadls
from read import rread
from write import write
os.system("cls")
# print(rreadls("test.txt"))
test = rreadls("test.txt")
with open("test.txt",'r',encoding='utf-8') as f:
    temp = f.readlines()
temp = [x for x in temp if x.split()]
with open("test.txt",'w',encoding='utf-8') as f:
    f.write("".join(temp))
def reload():
    temp = []
    with open("test.txt",'r',encoding='utf-8') as f:
        temp = f.readlines()
    temp = [x for x in temp if x.split()]
    with open("test.txt",'w',encoding='utf-8') as f:
        f.write("".join(temp))
    os.system("cls")
def mainPage():
    test = rreadls("test.txt")
    print("task:")
    for i in test:
        if i!=None:
            print("\t"+i)
        else:
            break
    print()

mainPage()
while(1):
    comm = input("Command:")
    if comm == "new":
        os.system("cls")
        co = input("new task:\t")
        write(co)
        os.system("cls")
        mainPage()
    if comm == "reload":
        reload()
        mainPage()
    if comm == "remove":
        os.system("cls")
        co = input("remove task:\t")
        n = rread("test.txt")
        n = n.replace(co,'')
        with open("test.txt",'w',encoding='utf-8') as f:
            f.write(n)   
        reload()
        temp = []
        with open("test.txt",'r',encoding='utf-8') as f:
            temp = f.readlines()
        temp = [x for x in temp if x.split()]
        with open("test.txt",'w',encoding='utf-8') as f:
            f.write("".join(temp))
        reload()
        os.system("cls")
        reload()
        mainPage()
    if comm == "exit":
        exit()