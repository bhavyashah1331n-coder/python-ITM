num=int(input("Enter the Number: "))
sum_of_divisiors=0
for i in range(1,num):
    if num%i==0:
        sum_of_divisiors += i

if sum_of_divisiors==num:
    print(num,"is a perfect Number!")
else:
    print(num,"is not a perfect Number!")
