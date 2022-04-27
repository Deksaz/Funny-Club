
import random


x=["เข้าใจโจทย์แต่ไม่รู้ไปทางไหน ขออภัยที่เสียเวลาตรวจครับ"]
print(x)

name = ["felix","sancho","Richarison","torreira","odegaard","berwijn","matinez","jovic","militao",
        "havertz","chalov","torres","haaland","rodrygo","lee kang in","mpappe","hakimi","van der beek",
        "aouar","zaniolo","mount","hector","maret","golovin","neres","maximin","dembele","azmoun",
        "bailey","dumfries","valverde","firpo","kluiver","foden","davies","kubo","matondo","diaby",
        "deksaz","sanu","sarr","lodi","wanbissaka","torres","ikone","under","kean","onyekuru","elliott","ndidi"]

randomlist1 = random.sample(range(0,50),15)

print("Liverpoll=",randomlist1)
print(len(randomlist1))


randomlist2 = random.sample(range(0,50),15)

print("Bacelonas=",randomlist2)
print(len(randomlist2))

randomlist3 = random.sample(range(0,50),15)

print("Bayern Munic=",randomlist3)
print(len(randomlist3))

randomlist4 = random.sample(range(0,50),15)

print("Juventas=",randomlist4)
print(len(randomlist4))


#name = str(input("Name:"))
#if name


