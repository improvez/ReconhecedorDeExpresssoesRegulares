# 🔎 Reconhecedor de Expressões Regulares

> 🧠 Um sistema desenvolvido em **Python** para reconhecimento automático de padrões utilizando **Expressões Regulares (Regex)**.

---

## 🚀 Sobre o projeto

Este projeto tem como objetivo desenvolver um **reconhecedor de padrões em textos**, capaz de analisar automaticamente um arquivo `.txt` e identificar diferentes tipos de informações utilizando **Expressões Regulares**.

📄 O sistema lê o arquivo `texto.txt`, procura todas as expressões cadastradas e informa:

* 🔍 Qual padrão foi encontrado
* 📝 Qual foi o conteúdo reconhecido
* 📍 Em qual linha ele apareceu
* 🔢 Quantas ocorrências foram encontradas

Tudo isso de forma automática, sem a necessidade de selecionar manualmente qual expressão deve ser pesquisada.

---

## ✨ Funcionalidades

Atualmente o sistema reconhece diversos padrões:

| 🔎 Padrão                    | 📝 Exemplo                   |
| ---------------------------- | ---------------------------- |
| 🔢 Binário par               | `1010`                       |
| 🔢 Binário terminado em `00` | `1100`                       |
| 💬 String entre aspas        | `"Olá mundo"`                |
| 📞 Telefone de SC            | `(49) 99999-9999`            |
| 🚗 Placa antiga              | `ABC-1234`                   |
| 🚙 Placa Mercosul            | `BRA1E23`                    |
| 📧 E-mail `.br` / `.com.br`  | `usuario@email.com.br`       |
| 📧 E-mail                    | `usuario@gmail.com`          |
| 💬 Comentário de linha       | `// comentário`              |
| 📝 Comentário multilinha     | `/* comentário */`           |
| 📍 CEP                       | `89500-000`                  |
| 🪪 CPF                       | `123.456.789-00`             |
| 🏢 CNPJ                      | `12.345.678/0001-90`         |
| 📅 Data                      | `12/08/2026`                 |
| ⏰ Horário                    | `19:30`                      |
| 💰 Valor em reais            | `R$ 1.500,00`                |
| 📱 Celular                   | `(49) 99999-9999`            |
| 🌐 URL                       | `https://www.exemplo.com.br` |
| #️⃣ Hashtag                  | `#Python`                    |
| 👤 Menção                    | `@usuario`                   |
| 🌎 IPv4                      | `192.168.1.1`                |
| 🔢 Número decimal            | `23,5`                       |
| 🔢 Número inteiro            | `1500`                       |
| 🔐 Hexadecimal               | `0xFF`                       |

---

## 🧩 Como funciona?

O funcionamento do sistema é simples:

```text
              📄 texto.txt
                   │
                   ▼
            📖 Leitura do arquivo
                   │
                   ▼
          🔎 Análise com Regex
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
   🔍 Padrão encontrado    ❌ Não encontrado
        │
        ▼
   📍 Linha identificada
        │
        ▼
   📊 Resultado exibido
```

O programa percorre o conteúdo do arquivo e aplica cada expressão regular ao texto.

Quando encontra uma ocorrência, o sistema informa a **expressão encontrada e a linha onde ela está localizada**.

---

## 📁 Estrutura do projeto

```text
📦 reconhecedor-regex
│
├── 🐍 reconhecedor.py
│
├── 📄 texto.txt
│
└── 📖 README.md
```

### 🐍 `reconhecedor.py`

Arquivo principal do projeto.

Contém:

* Expressões regulares
* Leitura do arquivo
* Análise do texto
* Identificação das ocorrências
* Identificação das linhas
* Exibição dos resultados

### 📄 `texto.txt`

Arquivo utilizado como entrada.

É nele que devem ser inseridos os textos que serão analisados pelo programa.

### 📖 `README.md`

Documentação do projeto.

---

## ⚙️ Requisitos

Para executar o projeto, você precisa ter:

🐍 **Python 3.x**

Não é necessário instalar bibliotecas externas.

O projeto utiliza apenas módulos nativos do Python:

```python
import re
```

---

## ▶️ Como executar

### 1️⃣ Clone o projeto

```bash
git clone https://github.com/seu-usuario/reconhecedor-regex.git
```

### 2️⃣ Entre na pasta

```bash
cd reconhecedor-regex
```

### 3️⃣ Coloque o texto para análise

Edite o arquivo:

```text
📄 texto.txt
```

Por exemplo:

```text
Olá!

Meu CPF é 123.456.789-00.
Meu CEP é 89500-000.

Meu telefone é (49) 99999-9999.

Minha placa é BRA1E23.

Meu e-mail é aluno@universidade.com.br.

Acesse https://www.exemplo.com.br.

// comentário

/*
   comentário
   de múltiplas linhas
*/
```

### 4️⃣ Execute o programa

```bash
python reconhecedor.py
```

---

## 📊 Exemplo de resultado

O programa apresentará algo semelhante a:

```text
================================================================================
                    RESULTADO DA ANÁLISE
================================================================================

[CEP]
--------------------------------------------------------------------------------
  ✓ 89500-000 → linha 4

  Total encontrado: 1


[CPF]
--------------------------------------------------------------------------------
  ✓ 123.456.789-00 → linha 3

  Total encontrado: 1


[Telefones de SC]
--------------------------------------------------------------------------------
  ✓ (49) 99999-9999 → linha 6

  Total encontrado: 1


[Placas Mercosul]
--------------------------------------------------------------------------------
  ✓ BRA1E23 → linha 8

  Total encontrado: 1


[E-mails .br ou .com.br]
--------------------------------------------------------------------------------
  ✓ aluno@universidade.com.br → linha 10

  Total encontrado: 1
```

---

## 🧠 Tecnologias utilizadas

<div align="center">

🐍 **Python**

🔎 **Regular Expressions (Regex)**

📄 **Manipulação de arquivos `.txt`**

🧩 **Processamento de texto**

</div>

---

## 🎯 Objetivo acadêmico

O projeto foi desenvolvido com o objetivo de aplicar conceitos relacionados a:

* 📚 Linguagens Formais
* 🔤 Expressões Regulares
* 🧠 Reconhecimento de padrões
* 🔎 Análise léxica
* 💻 Programação em Python
* 📄 Processamento de arquivos

A proposta demonstra como expressões regulares podem ser utilizadas para identificar diferentes estruturas dentro de um texto de maneira automatizada.

---

## 🔮 Possíveis melhorias

Algumas funcionalidades que podem ser adicionadas futuramente:

* 📍 Identificar **linha e coluna** da ocorrência
* 🎨 Interface gráfica
* 📊 Gerar relatório automático
* 💾 Exportar resultados para `.csv`
* 🌐 Interface web
* 🔎 Permitir múltiplos arquivos
* ⚡ Destacar os padrões encontrados
* 📈 Exibir estatísticas da análise
* 🧩 Permitir adicionar novas Regex através de um arquivo de configuração

---

## 👨‍💻 Desenvolvido com ☕ e Python

> 🔎 **"Se existe um padrão, provavelmente existe uma Regex para encontrá-lo."**

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!

**🐍 Python + 🔎 Regex = 🧠 Reconhecimento de padrões**
