
def count_char(words):
    keys=words.lower()
    count_dict  = {}
    for char in keys:
        if (char!= " "):
            if char in count_dict.keys():   
                 count_dict[char] = count_dict[char] + 1
            else:
                count_dict[char] = 1
    return count_dict
            
def switching(words):
    reversed_words = ""
    for char in words:
        if (char.islower()):
            big=char.upper()
            reversed_words = reversed_words + big
        else :
            small = char.lower()
            reversed_words = reversed_words + small
    return reversed_words
    
    
while(True):
    words = input("Input:")
    if (words == "STOP") :
        print("Bye")
        break
    else :
        count_dict = count_char(words)
        print(count_dict)
        print(switching(words))
