#!/usr/bin/python3
#
#
#

__author__ = "A.Q. Zimdars"
__copyright__  = "Copyright 2019 Zimdars"
__license__ = "CC BY-SA 4.0"
__version__ = "1.0"

from time import sleep
from string import ascii_lowercase, ascii_uppercase, digits
from random import randrange

def convBinStr (inputString):
    """
    convBinStr (inputString)
    Translate the inputString by letter/digit into ASCII binary code as string.
    
    Every character in the constants ascii_lowercase, ascii_uppercase or digits from the string library is translated into a seven digit binary string. Any other character is omitted.
    
    The return is a string, letters are seperated by a whitespace, whitespace in inputString are retained.
    """
    
    lettersFirst = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"}
    
    letters = dict({
        ("a", "0001"),
        ("b", "0010"),
        ("c", "0011"),
        ("d", "0100"),
        ("e", "0101"),
        ("f", "0110"),
        ("g", "0111"),
        ("h", "1000"),
        ("i", "1001"),
        ("j", "1010"),
        ("k", "1011"),
        ("l", "1100"),
        ("m", "1101"),
        ("n", "1110"),
        ("o", "1111"),
        ("p", "0000"),
        ("q", "0001"),
        ("r", "0010"),
        ("s", "0011"),
        ("t", "0100"),
        ("u", "0101"),
        ("v", "0110"),
        ("w", "0111"),
        ("x", "1000"),
        ("y", "1001"),
        ("z", "1010")})
    
    numbers = dict({
        ("0", "0000"),
        ("1", "0001"),
        ("2", "0010"),
        ("3", "0011"),
        ("4", "0100"),
        ("5", "0101"),
        ("6", "0110"),
        ("7", "0111"),
        ("8", "1000"),
        ("9", "1001")})
    
    binaryResult = ""
    for i in range(len(inputString)):
        if (not(binaryResult == "") and inputString [i] in (ascii_lowercase + ascii_uppercase + digits + " ")):
            binaryResult += " "
        if (inputString [i] in ascii_lowercase):
            if (inputString [i] in lettersFirst):
                binaryResult += "110"
            else:
                binaryResult += "111"
            
        elif (inputString [i] in ascii_uppercase):
            if (inputString [i].lower() in lettersFirst):
                binaryResult += "100"
            else:
                binaryResult += "101"
            
        elif (inputString [i] in digits):
            binaryResult += "011"
            binaryResult += numbers [inputString [i]]
            continue
        
        else:
            continue
            
        binaryResult += letters [inputString [i].lower()]
    
    return (binaryResult)

def prayer (n, choice=None):
    """
    prayer (n, choice=None)
    Return array of n lines of prayer (in Latin tongue) in binary numbers as strings.
    
    n is the number of lines of prayer. Choice determines the type of prayer (cf. below), no argument given displays a prompt.
    The litany is returned as an array of strings.
    
    The coice takes the following arguments:
    1: Calm the machine spirit
    2: Awaken the machine
    3: Repair this machine
    4: Communicate with the others
    5: Prepare for action
    """
    
    assert type(n)==int, "lines must be an interger value"    
    
    # Latin strings of litany in plain text.
    CALM = convBinStr("seda ea machina")
    CALM_HOLY = convBinStr("seda ea sancta machina")
    CALM_SELF = convBinStr("spiritus machinus seda te")

    GLORIA = convBinStr("Gloria Omnissiah")
    AVE = convBinStr("Ave Deus Mechanicus")
    THANK = convBinStr("gratia Deo Mechanico")
    THANK_AND_PRAISE = convBinStr("gratia et gloria Omnissiah")

    REPAIR = convBinStr("repara ea machina")
    REPAIR_OMNISSIAH = convBinStr("Deus Mechanicus repara")

    PREPARE_BATTLE = convBinStr("para te pro pugna")
    PREPARE_WAR = convBinStr("para te pro bello")
    PREPARE_WAR_BATTLE = convBinStr("para te pro bello et pugna")

    COMMUNICATE = convBinStr("communica cum ceteris machinis")

    AWAKEN = convBinStr("excita")
    AWAKEN_SPIRIT = convBinStr("spiritus machinus excita")
    
    
    # Prompt for choice, if and as long as there is no (valid) choice given. Please note that an invalid argument at function call will result in the function returning None.
    while (choice == None):
        print ("What is it, you require?")
        print ("1) Calm the machine spirit")
        print ("2) Awaken the machine")
        print ("3) Repair this machine")
        print ("4) Communicate with the others")
        print ("5) Prepare for action")
        choice = input().strip()

        if not(choice in ["1", "2", "3", "4", "5"]):
            choice = None
    
    # The contents of the litany is composed as given by the choice variable.
    litany = []
    if (choice == "1"):
        litany.append(CALM)
        litany.append(CALM_SELF)
        litany.append(GLORIA)
        litany.append(THANK)
        litany.append(THANK_AND_PRAISE)
            
    elif (choice == "2"):
        litany.append(AWAKEN)
        litany.append(AWAKEN_SPIRIT)
        litany.append(GLORIA)
        litany.append(THANK)
        litany.append(THANK_AND_PRAISE)

    elif (choice == "3"):
        litany.append(REPAIR)
        litany.append(REPAIR_OMNISSIAH)
        litany.append(GLORIA)
        litany.append(THANK)
        litany.append(THANK_AND_PRAISE)
        
    elif (choice == "4"):
        litany.append(COMMUNICATE)
        litany.append(GLORIA)
        litany.append(THANK)
        litany.append(THANK_AND_PRAISE)
        
    elif (choice == "5"):
        litany.append(PREPARE_BATTLE)
        litany.append(PREPARE_WAR)
        litany.append(PREPARE_WAR_BATTLE)
        litany.append(GLORIA)
        litany.append(THANK)
        litany.append(THANK_AND_PRAISE)
    else:
        return None
    
    # An array of n elements, randomly chosen lines of content, is generated and returned.
    binaryLitany = []
    for i in range (n):
        l = randrange(len(litany))
        binaryLitany.append(litany[l])
    
    return binaryLitany


# Display a prayer, the type of which will be prompted for.
# The prayer is 1000 lines long, displayed line by line with a 0.03s delay.
if (__name__ == "__main__"):

    lines = 10**3
    delay = 0.03

    prayerArray = prayer(lines)
    for i in range(lines):
        print(prayerArray[i])
        sleep(delay)