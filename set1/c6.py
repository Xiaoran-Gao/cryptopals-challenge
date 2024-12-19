from base64 import b64decode, b64encode

def hamming_dist(str1, str2):
    """Compute the Hamming distance, which is the number of differing bits.

    >>> test = hamming_dist("this is a test", "wokka wokka!!!")
    >>> test
    37
    """

    dist = 0
    for i, j in zip(bytes(str1, encoding='utf-8'), bytes(str2, encoding='utf-8')):
        dist += (i ^ j)
    return dist

if __name__ == "__main__":
    print(hamming_dist("this is a test", "wokka wokka!!!"))