import sys
sys.path.append('..')
# from ..src.file import file_encrypt, file_decrypt
from src.encrypi import encrypt, dump, dedump, decrypt


def encrypi_mod(test_str):
    assert isinstance(test_str, str), 'value err'
    src_text = test_str.encode()
    cipher_ls = encrypt(src_text)

    dump_bytes = dump(cipher_ls)
    src_ls = dedump(dump_bytes)
    assert src_ls == cipher_ls, f'cipher_ls => dedump \n {cipher_ls} => {src_ls}'

    decrypt_text = decrypt(src_ls)
    assert decrypt_text == src_text, f'encrypt => decrypt \n {src_text} => {decrypt_text}'


def main():
    encrypi_mod('hello world!!')
    # ascii
    encrypi_mod('中文测试')
    # unicode
    encrypi_mod('')
    # empty input

    # # encrypt test
    # file_encrypt('readme.md')
    # # deencrypt test
    # file_decrypt('readme.md.pi')

    print('tests done!')


if __name__ == '__main__':
    main()
