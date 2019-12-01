## George Jr. Escobar
## CSC 698

## To Run
```
python3 elGamal.py
```

# Project Input:
'Please type a message to Encrypt: '
    'this should be a string message'

# Project Output:
    Please type a message to Encrypt:
    this should be a string message
    Encrypted Message: [582230564, 521999816, 527019045, 577211335, 160615328, 577211335, 521999816, 557134419, 587249793, 542076732, 501922900, 160615328, 491884442, 506942129, 160615328, 486865213, 160615328, 577211335, 582230564, 572192106, 527019045, 552115190, 516980587, 160615328, 547095961, 506942129, 577211335, 577211335, 486865213, 516980587, 506942129]
    Decrypted Message: this should be a string message

# How the Code Works
    I chose to implemenet the Elgamal encryption. The Elgamal encryption
    uses an asymmetric encryption algorithm, based on the Diffie-Hellman key
    exchange. The reciever of data generates a public and private key. This reciever
    first chooses a very large number q, for my program I chose q to be in the range of
    15000000 - 25000000. This should be even bigger, but for the sake of the program,
    I chose something that would not take too long to compute, even with a long message.
    Then an element g from group q is chosen whose element a such that gcd(a, q) = 1(prime number).
    Then the receiver computes g^a. The receiver then publishes everything except a which
    will be its private key. The sender then encrypts their message with the recievers public key.
    The sender then selects an element from the same group such that the gcd(k, q) = 1
    Then computes the g^k, g^ak and multiplies the message with g^ak and sends
    a public Key and the encrypted message. Then the reciever decrypts the message
    using public key of sender^receiver own private key mod q and divides the 
    ecnrypted message by this product to obtain the message. 
