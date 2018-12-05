import sys
sys.path.append('..')
# from ..src.file import file_encrypt, file_decrypt
from src.mode.pi.pi import encrypt, dump, dedump, decrypt


def encrypi_mod(test_bytes):
    assert isinstance(test_bytes, bytes), 'value err'
    cipher_ls = encrypt(test_bytes)

    dump_bytes = dump(cipher_ls)
    src_ls = dedump(dump_bytes)
    assert src_ls == cipher_ls, f'cipher_ls => dedump \n {cipher_ls} => {src_ls}'

    decrypt_text = decrypt(src_ls)
    assert decrypt_text == test_bytes, f'encrypt => decrypt \n {test_bytes} => {decrypt_text}'


def main():
    encrypi_mod(b'hello world!!')
    # ascii
    encrypi_mod('中文测试'.encode())
    # unicode
    encrypi_mod(b'')
    # empty input
    encrypi_mod(b'\0')
    # \o input
    encrypi_mod(b'\0' * 16)
    # mulit \0

    # # encrypt test
    # file_encrypt('readme.md')
    # # deencrypt test
    # file_decrypt('readme.md.pi')

    print('tests done!')


if __name__ == '__main__':
    main()
