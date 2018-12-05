from .main import encrypt, decrypt, dump, dedump
from .mode import pi as default_mode
__all__ = ("file_encrypt", "file_decrypt")
from .fsize import file_size


def file_encrypt(file_name, output=None, mode=None):
    # default_mode
    if mode is None:
        get_byte = default_mode.get_byte
    else:
        m = __import__('mode.' + mode, globals(), level=1)
        g = getattr(m, mode)
        get_byte = g.get_byte
    # default output name
    if output is None:
        output = file_name + '.pi'
    # encrypt
    with open(file_name, "rb") as rf, open(output, 'wb+') as wf:
        ciphertext = encrypt(rf.read(), get_byte)
        wf.write(ciphertext)
    print(f'Cipher-file save as [ {output} ] {file_size(output)}.')


def file_decrypt(file_name, output=None, mode=None):
    # default_mode
    if mode is None:
        get_byte = default_mode.byte.get_byte
    else:
        get_byte = mode.byte.get_byte
    # default output name
    if output is None:
        output = file_name + '.de'
    # decrypt
    with open(file_name, "rb") as rf, open(output, "wb+") as wf:
        cipher_text = rf.read()
        decrypt_text = decrypt(cipher_text, get_byte)
        wf.write(decrypt_text)
    print(f'Decrypt-file save as [ {output} ] {file_size(output)}.')
