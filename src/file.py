from .encrypi import encrypt, decrypt, dump, dedump

__all__ = ("file_encrypt", "file_decrypt")


def file_encrypt(file_name, output=None):
    if output is None:
        output = file_name + '.pi'
    with open(file_name, "rb") as rf, open(output, 'wb+') as wf:
        ciphertext = encrypt(rf.read())
        wf.write(dump(ciphertext))
    print(f'Cipher-file save as [ {output} ].')


def file_decrypt(file_name, output=None):
    if output is None:
        output = file_name + '.de'
    with open(file_name, "rb") as rf, open(output, "wb+") as wf:
        ciphertext = rf.read()
        srctext = decrypt(dedump(ciphertext))
        wf.write(srctext)
    print(f'Decrypt-file save as [ {output} ].')
