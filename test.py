
import re


# ============================================================
# EXPRESSÕES REGULARES
# ============================================================

expressoes = {

    # 1. Binários pares
    "Binários pares":
        r"\b[01]*0\b",

    # 2. Palavras binárias terminadas em 00
    "Binários terminados em 00":
        r"\b[01]*00\b",

    # 3. Strings entre aspas
    "Strings entre aspas":
        r'"[^"\n]*"',

    # 4. Telefones de Santa Catarina
    # DDDs: 47, 48 e 49
    "Telefones de SC":
        r"\(?4[789]\)?\s?9?\d{4}-?\d{4}",

    # 5. Placas brasileiras
    # Modelo antigo: ABC-1234
    # Modelo Mercosul: ABC1D23
    "Placas brasileiras":
        r"\b(?:[A-Z]{3}-?\d{4}|[A-Z]{3}\d[A-Z]\d{2})\b",

    # 6. E-mails .br ou .com.br
    "E-mails .br ou .com.br":
        r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(?:com\.br|br)\b",

    # 7. Comentários de linha
    "Comentários de linha":
        r"//[^\n]*",

    # 8. Comentários de múltiplas linhas
    "Comentários multilinha":
        r"/\*[\s\S]*?\*/"
}


# ============================================================
# LEITURA DO ARQUIVO
# ============================================================

def ler_arquivo():

    nome_arquivo = "texto.txt"

    try:

        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            return arquivo.read()

    except FileNotFoundError:

        print(f"\nERRO: O arquivo '{nome_arquivo}' não foi encontrado.")
        print("Coloque o arquivo texto.txt na mesma pasta do programa.")

        return None

    except Exception as erro:

        print(f"\nERRO ao abrir o arquivo: {erro}")

        return None


# ============================================================
# ANÁLISE DO TEXTO
# ============================================================

def analisar_texto(texto):

    print("\n")
    print("=" * 70)
    print("                 RESULTADO DA ANÁLISE")
    print("=" * 70)

    encontrou_alguma_coisa = False

    for nome, padrao in expressoes.items():

        resultados = re.findall(padrao, texto)

        # Remove duplicados mantendo a ordem
        resultados_unicos = list(dict.fromkeys(resultados))

        print(f"\n[{nome}]")
        print("-" * 70)

        if resultados_unicos:

            encontrou_alguma_coisa = True

            for resultado in resultados_unicos:
                print(f"  ✓ {resultado}")

            print(f"\n  Total encontrado: {len(resultados_unicos)}")

        else:

            print("  Nenhuma ocorrência encontrada.")

    print("\n")
    print("=" * 70)

    if encontrou_alguma_coisa:
        print("Análise concluída.")
    else:
        print("Nenhuma das expressões foi encontrada no texto.")

    print("=" * 70)


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print("=" * 70)
    print("          RECONHECEDOR DE EXPRESSÕES REGULARES")
    print("=" * 70)

    print("\nAnalisando automaticamente o arquivo: texto.txt")

    texto = ler_arquivo()

    if texto is not None:

        print("Arquivo carregado com sucesso!")

        analisar_texto(texto)


# ============================================================
# EXECUÇÃO
# ============================================================

if __name__ == "__main__":
    main()