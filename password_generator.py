import random
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
           'x','y','z']
symbols=['!','@','!','#','$','%','^','&','*',"(",")",'-','_','+','=','{','}','[',
         ',','/',':',]
characters=['1','2','3','4','5','6','7','8','9','0']


length=int(input("Enter the length of the password"))
password=alphabets+symbols+characters
final_pass=random.choices(password,k=length)
random.shuffle(final_pass)



for i in final_pass:
         print(i,end="")






 



    




