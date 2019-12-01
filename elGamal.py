import math
import random

def main():
    # the range of numbers is usually a lot bigger but for the sake of the problem
    # i just kept it small so computation does not take that long

    q = random.randint(15000000, 25000000)
    g = random.randint(2, q)
    # private key of sender 
    keyPr = generatePrimeNum(q) 
    # modular exponentiation using standard library
    h = pow(g, keyPr, q)
    # message to be sent and encrypted 
    messageToEncrypt = input("Please type a message to Encrypt:\n ")
    # returned message to be encrypted and
    # public key made by the receiver
    encryptedMsg, keyPub = encrypt(messageToEncrypt, q, h, g)
    # prints encrypted message
    print('Encrypted Message: {}'.format(encryptedMsg))
    decryptedMsg = decrypt(encryptedMsg, keyPub, keyPr, q)
    decryptedMsg = ''.join(decryptedMsg)
    # then print decrypted message
    print('Decrypted Message: {}'.format(decryptedMsg))



# this checks whether or not the randomly generated number is prime
# returns true if prime, false otherwise
def isPrime(num):
    for i in range(2, num // 2):
        if(num % i) == 0:
            return False 
    return True

# returns a prime number
def generatePrimeNum(q):
    # this should be a large prime number close to 200 to 300 digits
    # for the sake of runtime and demonstration will choose a small prime number
    number = 6
    while not isPrime(number):
        number = random.randint(15000000, q - 2)
    return number


# logic to encrypt the plain text
# returns tuple: encryptedMsg, and pubK
def encrypt(message, q, h, g):
    pubK = generatePrimeNum(q)
    c1 = pow(h, pubK, q) 
    c2 = pow(g, pubK, q) 
    msgVal = [c1*ord(x) for x in message]
    return msgVal, c2

# logic to decypt the cipher text
def decrypt(cipherT, pub, pri, q):
    h = pow(pub, pri, q)
    return [chr(int(i / h))for i in cipherT]
    
if __name__ == '__main__': main()