import random,pyperclip

Upper="QWERTYUIOPASDFGHJKLZXCVBNM"
Lower="qwertyuiopasdfghjklmnbvcxz"
Number="1234567890"

Character="~`!@#$%\"^&*()_-+=[]:;\\'<>,./?"

all=Character+Upper+Lower+Number
lenght=10
password="".join(random.sample(all,lenght))
print("Your random generated password is\n"+password)
pyperclip.copy(password)