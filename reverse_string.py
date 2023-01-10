word = input("Enter a word : ")
length_of_word = len(word)
num = length_of_word - 1

while (num != -1):
    print(word[num], end="")
    num -= 1
