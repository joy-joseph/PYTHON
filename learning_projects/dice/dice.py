import random
min=1;max=6;c=0
print("Roll the die? 0=NO,1=YES:",end=" ")
i=int(input())
while i==1:
    print(random.randint(min,max))
    print("Roll again? 0=NO,1=YES:",end=" ")
    c+=1
    i=int(input())
print("Thank you!!! You've rolled the dice",c,"times.")