dogru_skor = 0
yanlis_skor = 0
import random
for i in range (1):
    a = random.randrange(10,99)
    vec = str(a)
    if vec[0] == vec[1]:
        a = random.randrange(10,99)

b = input('please enter a number between 10 and 99: ')
while int(b) > 98 or int(b) < 10 :
        print("you didn't enter a number between 10 and 99! ")
        b = input("please enter a number between 10 and 99: ")
if a == b :
    dogru_skor+=1
else:
    yanlis_skor-=1

print("the number was:", a)

print(dogru_skor + yanlis_skor)
              
        
        
