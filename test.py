import string

alphebet = string.ascii_lowercase + string.ascii_uppercase
alphebet += "0123456789_-"



def encode(text: str) -> str:
    result = ""
    for i in text:
        if len(str(alphebet.index(i))) == 1:
            result += "0" + str(alphebet.index(i))
        else:
            result += str(alphebet.index(i))
    return result

def decode(text: str) -> str:
    """
        пробежать по 2
        если 1 0 то откидываем 
        тщем индекс в алвовите и ретёрн по индексу из алфовита
    """