import bcrypt

print("Enter the number of passwords to hash")
n = int(input())
file = open(r"D:\\MD5.txt", "w")

while(n):
    print("Enter the password which needs to be hashed")
    password = input()
    encoded_password = password.encode()
    hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    decoded_hash = hashed.decode("utf-8")
    print("The hashed password is: ", hashed)
    print("Decode hashed password: ", decoded_hash)
    file.write(decoded_hash)
    file.write("\n")
    n = n-1

file.close()
