import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*?"
no_of_chars_wanted=int(input("Enter the number of characters for random password : "))
no_of_passwords_wanted=int(input("Enter the number of random passwords needed : "))
for k in range(0,no_of_passwords_wanted):
  x=[]
  for i in range(0,no_of_chars_wanted):
    random_int=random.randint(0,len(chars)-1)
    x.append(chars[random_int])
  y="".join(x)
  print("Here is your random password ",y)
