from binascii import hexlify, unhexlify

def fixed_xor(hex1, hex2):
    """Take two equal-length buffers and produce their XOR combination."""

    bytes1 = unhexlify(hex1)
    bytes2 = unhexlify(hex2)

    if len(bytes1) != len(bytes2):
        raise ValueError("Lengths not equal")

    return hexlify(bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])).decode('ascii')

if __name__ == "__main__":
    assert fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") \
        == "746865206b696420646f6e277420706c6179"