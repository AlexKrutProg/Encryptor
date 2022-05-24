import sys
import argparse
from encryptor import Encryptor, InfoManager


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('--cipher', default="caesar")
    parser.add_argument('--key', default="1")
    parser.add_argument('--input_file', default=None)
    parser.add_argument('--output_file', default=None)
    return parser


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    manager = InfoManager(namespace.input_file, namespace.output_file)
    manager.read_text()

    if namespace.command == "encode":
        if namespace.cipher == "caesar":
            manager.text = [Encryptor.encode_word_caesar(line, namespace.key) for line in manager.text]
        elif namespace.cipher == "vigenere":
            manager.text = [Encryptor.encode_word_vigenere(line, namespace.key) for line in manager.text]
        elif namespace.cipher == "vernam":
            manager.text = [Encryptor.encode_word_vernam(line, namespace.key) for line in manager.text]
    elif namespace.command == "decode":
        if namespace.cipher == "caesar":
            manager.text = [Encryptor.decode_word_caesar(line, namespace.key) for line in manager.text]
        elif namespace.cipher == "vigenere":
            manager.text = [Encryptor.decode_word_vigenere(line, namespace.key) for line in manager.text]
        elif namespace.cipher == "vernam":
            manager.text = [Encryptor.decode_word_vernam(line, namespace.key) for line in manager.text]

    manager.write_text()
