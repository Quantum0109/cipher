alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet = alphabet + alphabet.upper()

message = "слово"

def encrypt(message: str, shift: int) -> str:
	result = ""
	for i in message:
		if i in alphabet:
			index = alphabet.index(i)
			index_shifted = (index + shift) % len(alphabet)
			result += alphabet[index_shifted]
		else: 
			result += i
	return result
message_encrypted = encrypt(message, 1)
def deciphement(message_encrypted: str, func) -> str:
	for i in range(len(alphabet)):
		print(i, encrypt(message_encrypted, i * -1))

print(encrypt(message, 1))
deciphement(message_encrypted, encrypt)