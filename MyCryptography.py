# I used this page for assistance
# https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/

import rsa

publicKey, privateKey = rsa.newkeys(128)

# Gets the two inputs and adds them together
input1 = int(input(" Please Enter the First Number to Sum: "))
input2 = int(input(" Please Enter the Second Number to Sum: "))
total_pre_rsa = input1 + input2
total_post_rsa = rsa.encrypt(str(total_pre_rsa).encode(), publicKey)
decrypted = rsa.decrypt(total_post_rsa, privateKey).decode()

# Prints the sum of the two inputs
print("Sum pre-RSA", total_pre_rsa)


def my_function():
    # Encrypts total_pre_rsa
    print("pre-rsa result", total_pre_rsa)
    print("Post rsa result", total_post_rsa)
    print("")


def my_function1():
    # Decrypts total_pre_rsa
    print("Decrypted total_post_rsa: ", decrypted)


my_function()
my_function1()
