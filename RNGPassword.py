import random  
Let = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V', 'W','X','Y','Z']
q =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=['1','2','3','4','5','6','7','8','9','0']
v = ['!','@','$','%','^','&','*']
print(len(Let),len(q),len(n),len(v))
len_l = int(input("Please enter the minimum amount of uppercase letters you want in your password: "))
len_q = int(input("Please enter the minimum amount of lowercase letters you want in your password: "))
len_v = int(input("Please enter the minimum amount of special characters you want in your password: "))
len_n = int(input("Please enter the minimum amount of numbers you want in your password: "))
Q = ""
L = ""
V = ""
N = ""
for i in range(len_l):
    L+=random.choice(Let)
for j in range(len_q):
      Q += random.choice(q)
for k in range(len_n):
    N += random.choice(n)
for m in range(len_v):
    V += random.choice(v)
e = len_l+len_q+len_v+len_n 
finpass = ""
finpass_list = list(Q+L+V+N)
for u in range(e):
    finpass += random.choice(finpass_list)
    finpass_list.remove(finpass[-1])
print (finpass)