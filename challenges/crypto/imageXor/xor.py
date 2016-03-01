def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))


data = bytearray(open('image.bmp', 'rb').read())

key = bytearray(b"yoloSwagg")

print(str(xor(data, key).decode('latin-1')))
