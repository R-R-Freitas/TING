from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file = txt_importer(path_file)
    repeated = False
    for file in range(len(instance)):
        if path_file == instance.search(file)["nome_do_arquivo"]:
            repeated = True
            break
    if not repeated:
        file_data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        instance.enqueue(file_data)
        print(file_data)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        removed = instance.dequeue()
        if removed:
            print(
                "Arquivo %s removido com sucesso"
                % (removed["nome_do_arquivo"])
            )


def file_metadata(instance, position):
    if position not in range(len(instance)):
        print("Posição inválida", file=sys.stderr)
    else:
        print(instance.search(position))
