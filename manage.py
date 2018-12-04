import click
from src.file import file_encrypt, file_decrypt


@click.command()
@click.option('--mode', '-m', default='en', type=click.Choice(['en', 'encrypt', 'de', 'decrypt']), help='Choose encryption or decrypt.')
@click.option('--output', '-o', default=None, help='Output file name.')
@click.argument('file_name', type=click.Path(exists=True))
def cli(file_name, mode, output):
    """
    -- Encryπ --\n
    Put your files in π! ? This tool can encrypt your files into PI! And quickly recover your encrypted information.
    """
    if mode in ['en', 'encrypt']:
        # encrypt
        file_encrypt(file_name, output)
        return
    # decrypt
    file_decrypt(file_name, output)


if __name__ == '__main__':
    cli()
