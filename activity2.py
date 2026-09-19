amount=int(input("enter the total withdrawal amount:"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("The number of 100 notes is:", note1)
print("The number of 50 notes is:", note2)
print("The number of 10 notes is:", note3)