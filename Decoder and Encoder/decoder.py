
######################################
########                      ########
# https://github.com/halilumutyalcin #
########                      ########
######################################

def encrypt(text):
    pswd = ""
    for k in text:
        print(k, "=>", chr(ord(k) + 5))
        pswd = pswd + chr(ord(k) + 5)
    print(text, " = >", pswd)

def decrypt(pswd):
    text = ""
    for k in pswd:
        print(k, "=>", chr(ord(k) - 5))
        text = text + chr(ord(k) - 5)
    print(pswd, " = >", text)

text = input("Enter the text to be encrypted:")
encrypt(text)

pswd = input("Enter the text to be decrypted:")
decrypt(pswd)
