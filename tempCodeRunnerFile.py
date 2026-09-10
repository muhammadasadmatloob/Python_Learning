
def check_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    else:
        return False
            
    
words = input("enter any word:")
print(check_palindrome(words))
