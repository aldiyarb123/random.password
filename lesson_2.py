import random

password =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght_pass = int(input("Введите длину пароля: "))
final_pass = ""

for i in range(lenght_pass):
    final_pass += random.choice (password)
    # 1-й символ - B 2-й символ - j

print("Ваш пароль", final_pass)