#1 Replace all the occurrences of a specified word with another word
def replace_text():
    old_word = input("Enter word to be replaced: ").lower()
    new_word = input("Enter replacement word: ")
    
    with open("sample.txt") as file:
        content = file.readlines()

    new_lines = []
    for line in content:
        old_line = line.lower()
        if old_word in old_line:
            new_line = ""
            count = 0
            while count < len(line):
                if old_line[count:count+len(old_word)] == old_word:
                    new_line += new_word
                    count += len(old_word)
                else:
                    new_line += line[count]
                    count += 1
            new_lines += new_line
        else:
            new_lines += line
           

    with open("sample.txt", "w" ) as file:
        for line in new_lines:
            for char in line:
                file.write(char)

    print("sample.txt")

replace_text()


#2 Count the frequency of a single word that is given by the user
def frequency_counter():
    input_word = input("Enter word to be counted: ")
    
    with open("sample.txt") as file:
        content = file.readlines()

    count = 0
    for line in content:
        lowercase_line=line.lower()
        index = 0
        while index < len(lowercase_line):
                if lowercase_line[index:index+len(input_word)] == input_word:
                    count += 1
                    index += len(input_word)
                else:
                    index += 1

    print("The word", input_word, "appears", count, " times in the file.")

frequency_counter()


#3 Count the number of sentences, words and characters, that end with a period
def counter():
    count_sentence = 0
    count_words = 0
    count_char = 0

    with open("sample.txt") as file:
        content = file.readlines()

    for line in content:
        in_word = False  

        for char in line:
            count_char += 1  

            if char == '.':
                count_sentence += 1
            
            if char.isalnum():  
                if not in_word:  
                    count_words += 1
                    in_word = True
            else:
                in_word = False  


    print("There are", count_sentence, "sentences ending with a period.")
    print("There are", count_words, "words.")
    print("There are", count_char, "characters.")

counter()


#4 Find the longest word and display it's count
def longest_word():
    
    with open("sample.txt") as file:
        content = file.readlines()
   
    longest_word = ""
    current_word = ""
    
    for line in content:
        for word in line:
            if word.isalpha():
                current_word += word
            else:
                if len(current_word)>len(longest_word):
                    longest_word=current_word
                current_word = ""
    
    print("The longest word is ", longest_word, " with ", len(longest_word), " letters.")

longest_word()
            

#5 Find all the palindromic words in the text
def palindrome():
    
    with open("sample.txt") as file:
        content = file.readlines()

    count = 0
    current_word = ""
    palindromes = []

    for line in content:
        for char in line:
            if char.isalpha():
                current_word = char + current_word
            else:
                if len(current_word)>1:
                    reversed_word = ""
                    for char in current_word:
                        reversed_word = char + reversed_word
                    if current_word.lower() == reversed_word.lower():
                        count += 1
                        palindromes += [current_word]
                current_word = ""
        if len(current_word)>1:
            reversed_word = ""
            for char in current_word:
                reversed_word = char + reversed_word
            if current_word.lower() == reversed_word.lower():
                count += 1
                palindromes += [current_word]
        current_word = ""

    print("The palindromes are ", palindromes)

palindrome()