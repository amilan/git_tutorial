import copy
import string

def is_palindrome(word):
    # Make check for palindrome independent of whitespace, punctuation
    # and capitalisation. It has not been specified if digits should
    # be ignored or not, so they are left in.
    chars = list(word.translate(None, string.punctuation + string.whitespace).lower())
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
    print("Able was I ere I saw Elba?", 
           is_palindrome("Able was I ere I saw Elba"))

if __name__  == '__main__':  
    test()
