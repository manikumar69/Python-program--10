fh=open('prac10.txt','w')
#To convert from base 2 to base 10
number= input("Enter the number in base 2: ") 
answer = int(number,2)
print(answer)
fh.write('Answer in base 10:'+str(answer))
fh.write('\n')

#To convert from base 10 to base 2
num=int(input("Enter the number in base 10: "))
answer = bin(num)
print(answer[2:])
fh.write('Answer in base 2: '+str(answer[2:]))
fh.close()