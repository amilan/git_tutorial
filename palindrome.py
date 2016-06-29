import copy

def is_palindrome(word):
    chars = list(word)
    rev = copy.copy(chars)
    rev.reverse()

    if rev == chars:
        return True
    else:
        return False

def test():
    print("Is word a palindrome?")
    print("radar?", is_palindrome("radar"))
    print("brexit?", is_palindrome("brexit"))

if __name__  == '__main__':  
    test()
