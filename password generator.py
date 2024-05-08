import random
import string
length = int(input("Enter the length of the password: "))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special_character = string.punctuation
total = lower+ upper + numbers +special_character
T = random.sample(total,length)
password="".join(T)
print(password)
             
