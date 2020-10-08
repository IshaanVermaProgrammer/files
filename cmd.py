import webbrowser as wb
import os
def cd(fold):
    return os.chdir(fold)
def create(filwe):
    a=open(filwe,"w")
    return a.write("")
def mkdir(dirr):
    if not os.path.exists(dirr):
        return os.makedirs(dirr)
    else:
        return print("This directory already exists")
def delete(fil):
    return os.remove(fil)
def rmdir(path):
    return os.removedirs(path)
def ls(directory):
    i=0
    if directory==".":
        a=os.listdir()
    else:
        a=os.listdir(path=directory)
    while i<len(a):
        print(a[i]+"\n")
        i+=1
    return None
def url(link):
    return wb.open(link)
def read(file):
    a=open(file,"r")
    return print(a.read())
def interpret(cmd):
    n=0
    i=0
    x=0
    command=""
    while i<len(cmd):
        if cmd[i]==" ":
                command+="('"
        else:
            command+=cmd[i]
        i+=1
    command+="')"
    return eval(command)
def text():
    print("The text editor has been activated\n")
    opt=input("Write a new file or append to existing file?(w/a) ")
    if opt=="a":
        np=input("Enter file name(with extension) ")
        fil=open(np,"a")
        dat=open(np,"r")
        while True:
            texter=input(">>>")
            if texter=="/0":
                break
            else:
                fil.write(f"\n{texter}")
    else:
        name=input("Enter file name ")
        ext=input("Enter file extension ")
        name+="."
        fil=open(name+ext,"w")
        fil.write("")
        r=open(name+ext,"r")
        a=open(name+ext,"a")
        while True:
            texter=input(">>>")
            if texter=="/0":
                break
            else:
                if r.read()=="":
                    a.write(f"{texter}\n")
                else:
                    a.write(f"\n{texter}")
    return print("The text has been edited succesfully")
while True:
    command=input()
    if command=="close":
        break
    elif command=='search':
        i=input("Search ")
        a=f"https://www.google.com/search?q={i}&oq=hello&aqs=chrome..69i57j46i433j0i433j46i433j0i10i433j46i433j0j0i10i433.3070j0j7&sourceid=chrome&ie=UTF-8"
        wb.open(a)
    elif command=='text':
        text()
    else:
        interpret(command)
        
