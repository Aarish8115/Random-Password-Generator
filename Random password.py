import random # importing rrandom module
import pyperclip # importing pyperclip module

# the password will be made of them choosen randomly
Upper="QWERTYUIOPASDFGHJKLZXCVBNM"
Lower="qwertyuiopasdfghjklmnbvcxz"
Number="1234567890"
Character="~`!@#$%\"^&*()_-+=[]:;\\'<>,./?"

# so that the password contains everything - Uppercase,Lowercase,Numbers and characters
all=Character+Upper+Lower+Number

# length of the password
length=10

# creating the password using random module
password="".join(random.sample(all,length))

# printing the password
print("Your random generated password is\n"+password)

# this line so that the password is automatically copied to your clipboard
pyperclip.copy(password)