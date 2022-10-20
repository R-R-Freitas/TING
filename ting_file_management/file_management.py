import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
        with open(path_file, mode="r") as file:
            file_lines = file.read().splitlines()
            file.close()
            return file_lines
    except FileNotFoundError:
        print("Arquivo %s não encontrado" % (path_file), file=sys.stderr)
