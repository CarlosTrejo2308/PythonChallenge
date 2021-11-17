def rot(hidden: str, key: int) -> str:
    """
    Rotates the string by the key
    """
    for i in range(len(hidden)):
        if hidden[i].isalpha():
            if hidden[i].isupper():
                hidden = hidden[:i] + chr((ord(hidden[i]) - 65 + key) % 26 + 65) + hidden[i + 1:]
            else:
                hidden = hidden[:i] + chr((ord(hidden[i]) - 97 + key) % 26 + 97) + hidden[i + 1:]
    return hidden



if __name__ == '__main__':
    print(ord('a'))
    hidden = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    
    mytable = hidden.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "cdefghijklmnopqrstuvwxyzab"
    )
    print(hidden.translate(mytable))
    
    result = rot("Have you ever heard of jvon files !?", 2)
    print(result)