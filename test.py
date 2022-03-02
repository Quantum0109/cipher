import string

alphebet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alphebet_digits = len(str(len(alphebet)))

def encode(text: str) -> str:
    result = ""
    for i in text:
        if i not in alphebet:
            return ""
        a = alphebet.index(i)
        alphebet_digits = len(str(len(alphebet)))
        if len(str(a)) == alphebet_digits:
            result += str(a)
        else:
            zeroes = alphebet_digits - len(str(a))
            for j in range(zeroes):
                    result += "0"
            result += str(a)
    return result


def decode(text: str) -> str:
    result_decode = ""
    slices = len(text) // alphebet_digits
    step = 0
    for i in range(slices):
        b = text[step:step + alphebet_digits] 
        if b == "000":
            result_decode += alphebet[0]
        else:
            idx = b.lstrip("0")
            result_decode += alphebet[int(idx)]
        step += alphebet_digits
    return result_decode

print(decode(encode("Vasya")))








