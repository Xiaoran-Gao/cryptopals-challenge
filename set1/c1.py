from binascii import hexlify, unhexlify
from base64 import b64decode, b64encode

def hex_to_base64(hex):
    """Convert hex to base64."""

    raw = unhexlify(hex)
    return b64encode(raw).decode('ascii')

if __name__ == "__main__":
    assert hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") \
        == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"