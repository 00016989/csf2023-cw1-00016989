str1 = input("Your mixed word: ")
Char = 0
Digit = 0
Symbol = 0
for i in str1:
    if i.isalpha():
        # print(i)
        Char += 1
    elif i.isdigit():
        # print(i)
        Digit += 1
    else:
        # print(i)
        Symbol += 1
print(f"Total numbers of chars, digits, letters:\n"
      f"Symbol: {Char}\nDigit: {Digit}\nChar: {Symbol}")
