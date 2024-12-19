from binascii import hexlify, unhexlify

def score_calc(text):
    """Calculate score for a given English text, using letter frequencies."""

    text = text.lower()
    freq_dic = {
        'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
        'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
        'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
        'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }
    score = 0
    for char in text:
        score += freq_dic.get(char, 0)
    return score

def xor_decipher(hex):
    """Decipher the hex encoded string
    by identifying the character used when the highest score is obtained.
    """

    best_score = 0
    key = ''
    deciphered_msg = ''
    bytes1 = unhexlify(hex)

    for i in range(256):
        try:
            text = bytes([b1 ^ i for b1 in bytes1]).decode('ascii')
        except UnicodeDecodeError:
            continue

        curr_score = score_calc(text)
        if curr_score >= best_score:
            best_score = curr_score
            key = bytes([i]).decode('ascii')
            deciphered_msg = text
    
    return key, deciphered_msg, best_score

if __name__ == "__main__":
    key, decipherd_msg, best_score = xor_decipher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    print(f"The key is {key}.")
    print(f"The deciphered message is \"{decipherd_msg}\".")