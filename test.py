import re

expressoes = {

    "Binários pares":
        r"\b[01]+0\b",

    "Binários terminados em 00":
        r"\b[01]+00\b",

    "Strings entre aspas":
        r'"[^"\n]*"',

    "Telefones de SC":
        r"(?<!\d)\(?4[789]\)?\s?(?:9\d{4}|\d{4})-?\d{4}(?!\d)",

    "Placas modelo antigo":
        r"\b[A-Z]{3}-?\d{4}\b",

    "Placas Mercosul":
        r"\b[A-Z]{3}\d[A-Z]\d{2}\b",

    "E-mails .br ou .com.br":
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com\.br|br)\b",

    "Comentários de linha":
        r"//[^\n]*",

    "Comentários multilinha":
        r"/\*[\s\S]*?\*/",

    "CEP":
        r"\b\d{5}-?\d{3}\b",

    "CPF":
        r"\b(?:\d{3}\.\d{3}\.\d{3}-\d{2}|\d{11})\b",

    "CNPJ":
        r"\b(?:\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}|\d{14})\b",

    "Datas":
        r"\b(?:0?[1-9]|[12]\d|3[01])[\/.-](?:0?[1-9]|1[0-2])[\/.-]\d{4}\b",

    "Horários":
        r"\b(?:[01]\d|2[0-3]):[0-5]\d\b",

    "Valores em reais":
        r"R\$\s?\d{1,3}(?:\.\d{3})*(?:,\d{2})?",

    "Celulares":
        r"(?<!\d)\(?\d{2}\)?\s?9\d{4}-?\d{4}(?!\d)",

    "URLs":
        r"\b(?:https?://|www\.)[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?:/[^\s]*)?",

    "E-mails":
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",

    "Hashtags":
        r"(?<!\w)#[A-Za-zÀ-ÿ0-9_]+",

    "Menções":
        r"(?<!\w)@[A-Za-z0-9_]+",

    "Endereços IPv4":
        r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b",

    "Números decimais":
        r"\b\d+[,.]\d+\b",

    "Números inteiros":
        r"\b\d+\b",

    "Números hexadecimais":
        r"\b0[xX][0-9A-Fa-f]+\b"
}

def ler_arquivo():

    nome_arquivo = "texto.txt"

    try:

        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.readlines()

    except FileNotFoundError:

        print("\nERRO: O arquivo 'texto.txt' não foi encontrado.")
        print("Coloque o arquivo texto.txt na mesma pasta do programa.")

        return None

    except Exception as erro:

        print(f"\nERRO ao abrir o arquivo: {erro}")

        return None

def analisar_texto(linhas):

    print("\n")
    print("=" * 80)
    print("                    RESULTADO DA ANÁLISE")
    print("=" * 80)

    encontrou_alguma_coisa = False

    texto_completo = "".join(linhas)

    for nome, padrao in expressoes.items():

        ocorrencias = []

        if nome == "Comentários multilinha":

            for match in re.finditer(padrao, texto_completo):

                resultado = match.group()

                inicio = match.start()

                linha = texto_completo[:inicio].count("\n") + 1

                ocorrencias.append(
                    (resultado, linha)
                )

        else:

            for numero_linha, linha_texto in enumerate(
                linhas, start=1
            ):

                for match in re.finditer(
                    padrao,
                    linha_texto
                ):

                    resultado = match.group()

                    ocorrencias.append(
                        (resultado, numero_linha)
                    )

        print(f"\n[{nome}]")
        print("-" * 80)

        if ocorrencias:

            encontrou_alguma_coisa = True

            for resultado, linha in ocorrencias:
                resultado = resultado.replace(
                    "\n",
                    "\\n"
                )

                print(
                    f"  ✓ {resultado} "
                    f"→ linha {linha}"
                )

            print(
                f"\n  Total encontrado: "
                f"{len(ocorrencias)}"
            )

        else:

            print("  Nenhuma ocorrência encontrada.")

    print("\n")
    print("=" * 80)

    if encontrou_alguma_coisa:

        print("Análise concluída com sucesso!")

    else:

        print(
            "Nenhuma expressão foi encontrada "
            "no texto."
        )

    print("=" * 80)


def main():

    print("=" * 80)
    print("              RECONHECEDOR DE EXPRESSÕES REGULARES")
    print("=" * 80)

    print(
        "\nAnalisando automaticamente "
        "o arquivo: texto.txt"
    )

    linhas = ler_arquivo()

    if linhas is not None:

        print("Arquivo carregado com sucesso!")

        analisar_texto(linhas)

if __name__ == "__main__":
    main()