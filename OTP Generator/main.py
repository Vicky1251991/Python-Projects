import string
import random

try:
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("Enter the password length: "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    print("Your password is: ")
    print("".join(random.sample(s, plen)))

    if plen == 0:
        print("Please enter a greter number..")

except(ValueError, NameError):
    print("Please enter a valid number..")
