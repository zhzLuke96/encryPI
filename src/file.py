from .encrypi import encrypt, decrypt, dump, dedump

__all__ = ("file_encrypt", "file_decrypt")


def file_encrypt(file_name):
    with open(file_name, "rb") as rf, open(file_name + '.pi', 'wb+') as wf:
        ciphertext = encrypt(rf.read())
        wf.write(dump(ciphertext))
    print(f'ciphertext dump in [{file_name}.pi]')


def file_decrypt(file_name):
    with open(file_name, "rb") as rf, open(file_name + '.de', "wb+") as wf:
        ciphertext = rf.read()
        srctext = decrypt(dedump(ciphertext))
        wf.write(srctext)
    print(f'srctext dump in [{file_name}.de]')
