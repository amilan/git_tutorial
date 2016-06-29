import sys
import warnings


def test_deprecation_warning():
    warnings.warn("This is a deprecated function, will disappear", DeprecationWarning)
    print 'still, the function continues'


def decypher(s):
    """Knowing that k -> m, o -> q, e -> g this function
    decyphers the string s and returns readable text."""
    return "".join(map(chr, [97+(ord(c)-95)%25 if c.isalpha() else ord(c) for c in s]))


def test_decypher():
    test_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddga"\
                  "gclr ylb rfyr'q ufw rfgq rcvr gq qm jmle."
  
    assert decypher(test_string) == "i hope you didnt translate it by hand. thats what computers are for. doing it in"\
                                    " by hand is inefficient and that's why this text is so long."

def is_vowel(c):
    """
   
    This was a difficult
    :param c: a letter
    :type: string
    """
    return c in 'aeoiuy'


if __name__ == '__main__':
    pass

