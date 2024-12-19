from binascii import hexlify, unhexlify

def rep_key_xor(text, key):
    """Encrypt the text, under the key given, using repeating-key XOR."""

    encrypted_text = bytes()
    i = 0
    for char in text.encode('ascii'):
        encrypted_text += bytes([char ^ key.encode('ascii')[i]])
        i = (i+1) % len(key)

    return hexlify(encrypted_text).decode('ascii')

if __name__ == "__main__":
    assert rep_key_xor("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE") \
        == "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"