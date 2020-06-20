info={'mooman74':'alskes145',
      'meramo1986':'kehns010101',
      'nickyD':'world1star',
      'george2':'booo3oha',
      'admin00':'admin1234',}
print("Welcome to the Database Admin Program\n")
username=str(input("Enter your username: "))
password=str(input("Enter your password: "))
if username in info.keys():
  if info[username]==password:
    print("Hello",username,"!","You are logged in!")
    if username=="admin00":
      print("\nHere is the current user database:")
      for k,v in info.items():
       print("Username:",k,"\t","Password:",v)
    else:
      choice=str(input("Would you like to change your password?(y/n):"))
      if choice=="y":
        newpassword=str(input("What would you like your new password to be?:"))
        if len(newpassword)>=8:
            password=newpassword
        else:
            print("Minimum 8 characters required!")
        print("Your password is",password)
      else:
           print("No problem!")
  else:
    print("Make sure you've entered the correct password.")
else:
 print("Sorry,username not in database")
