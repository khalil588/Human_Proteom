import future
from future.moves import tkinter
from tkinter import messagebox
from tkinter import *

def read_words(f) :
    ls =[]
    for x in f :
        x=x.strip("\n")
        if len(x) >= 3 :
            ls.append(x.upper())
    return ls
def read_sequences(f):

    a=f.readlines()
    seq=[]
    for e in a:
        e=e.strip("\n")
        if e[0] == ">":
            e = e.split("|")
            seq.append(e[1])
    ls = []
    val = ""
    for x in a:
        a = x.find("|")
        if a < 0:
            val = val + x.strip("\n")
        else:
            ls.append(val)
            val = ""
    d={}
    for i in range(len(seq)):
        d[seq[i]]=ls[i]
    return (d)


"""
def search_words_in_proteome_Res(liste1, dict):
    occ = 0
    d = {}
    for i in liste1:
        occ = 0
        for e in dict.values():
            if i in e:
                occ += 1
                d[i] = occ
    for v in d:
        print(v, ' found in', d[v], 'sequences', '\n')
"""
def search_words_in_proteome(liste1,dict) :
    d = {}
    for x in liste1 :
        c = 0
        for j in dict.values():
            c += j.count(x)
        if c > 0 :
            d[x] = c

    return d




def find_most_frequent_word(dict2,dict) :
    x = ""
    y = 0
    for i, j in dict2.items():
        if y < j :
            x = i
            y = j

    print(" the most frequent word is "+x+" found in "+str(y)+" sequences ")
    z =(y/len(dict))*100
    print(" with a pourcentage "+str(z)+"% of the whole human proteomes")



def graph_func(name,dict):
    c = 0
    for  j in dict.values():
        if (j.find(name.upper())>-1):
            c+=1
    m = "the name :"+name+" was found in "+str(c)+" sequences"
    msg = messagebox.showinfo("hello user",m)
def graph(dict) :
    main = Tk()
    main.title("Hire now!")
    L1 = Label(main,text="enter a word :")
    L1.pack(side = LEFT)
    E1 = Entry(main,bd = 20)
    E1.pack(side = RIGHT)
    b = Button(main,text ="   ok   ", command =lambda :graph_func(E1.get(),dict))
    b.pack(side = LEFT)
    b = Button(main,text ="cancel   ",command = main.destroy)
    b.pack(side = RIGHT)
    main.mainloop()












