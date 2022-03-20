import random,os
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import sys 

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'D':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
    # Loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Symbol is not in LETTERS; just add it:
            translated += symbol
    return translated

def process(sourceDir,DestDir,action,key):
    print(f'inside process sourceDir - {sourceDir} DestDir - {DestDir} action = {action} - key - {key}')
    for filename in os.listdir(os.path.join(sourceDir)):
        newfile = translateMessage(key,filename,action)  
        print(f'processing file - {filename}')
        with open(os.path.join(DestDir,newfile),'w') as fp1:
            with open(os.path.join(sourceDir,filename),'r') as fp:
                for lines in fp:
                    fp1.write(translateMessage(key,lines,action))
            print(f"{filename} ====> {newfile} created successfully...")
    print('done...')   

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == "__main__":
    #l_key = getRandomKey()
    #print(l_key)
    if len(sys.argv) != 5:
        print('Incorrect Format: Use Pgmname [E|D] sourceDir DestDir Key')
        sys.exit(0)
    action      = sys.argv[1]
    sourceDir   = sys.argv[2]
    destDir     = sys.argv[3]
    key         = sys.argv[4]
    if not os.path.exists(sourceDir):
        print('Incorrect sourceDir')
        sys.exit(0)
    if not os.path.exists(destDir):
        print('Incorrect destDir')
        sys.exit(0)
    if action not in ('E','D'):
        print('Incorrect Action')
        sys.exit(0)

    process(sourceDir,destDir,action,key)
    
  