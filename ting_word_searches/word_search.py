def exists_word(word, instance):
    results = []
    index = 0
    while index < len(instance):
        current_file = instance.search(index)
        line_number = 1
        for line in current_file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                if (
                    len(results) > 0
                    and results[-1]["arquivo"]
                    == current_file["nome_do_arquivo"]
                ):
                    results[-1]["ocorrencias"].append(
                        {"linha": line_number}
                    )
                else:
                    results.append(
                        {
                            "palavra": word,
                            "arquivo": current_file["nome_do_arquivo"],
                            "ocorrencias": [
                                {"linha": line_number}
                            ],
                        }
                    )
            line_number += 1
        index += 1
    return results


def search_by_word(word, instance):
    results = []
    index = 0
    while index < len(instance):
        current_file = instance.search(index)
        line_number = 1
        for line in current_file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                if (
                    len(results) > 0
                    and results[-1]["arquivo"]
                    == current_file["nome_do_arquivo"]
                ):
                    results[-1]["ocorrencias"].append(
                        {"linha": line_number, "conteudo": line}
                    )
                else:
                    results.append(
                        {
                            "palavra": word,
                            "arquivo": current_file["nome_do_arquivo"],
                            "ocorrencias": [
                                {"linha": line_number, "conteudo": line}
                            ],
                        }
                    )
            line_number += 1
        index += 1
    return results
