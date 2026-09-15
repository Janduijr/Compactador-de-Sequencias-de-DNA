# Compactador de Sequências de DNA

Script em Python que compacta uma sequência de DNA (letras A, C, G, T) em um arquivo binário, usando apenas 2 bits por nucleotídeo em vez de 8 bits (1 byte) por caractere — uma economia de 75% de espaço.

## Como funciona

Cada nucleotídeo é representado por um código binário de 2 bits:

| Nucleotídeo | Código |
|---|---|
| A | 00 |
| C | 01 |
| G | 10 |
| T | 11 |

Em vez de guardar cada letra como um caractere de texto normal (que ocupa 1 byte = 8 bits), o programa guarda cada nucleotídeo usando só 2 bits, através da biblioteca `bitarray`.

## Arquivos utilizados

- **`arquivo.txt`** (entrada): arquivo de texto com a sequência de DNA, uma letra por linha (A, C, G ou T).
- **`compactado.bin`** (saída da compactação / entrada da descompactação): arquivo binário com a sequência compactada.
- **`descompactado.txt`** (saída final): texto reconstruído a partir do arquivo binário, formatado em linhas de até 70 caracteres.

## Funções

### `ler_documento()`
Lê o `arquivo.txt`, ignora linhas vazias e converte cada letra válida (A, C, G, T) no seu código de 2 bits correspondente, guardando tudo em um `bitarray`.

### `compactar()`
1. Chama `ler_documento()` para gerar os bits.
2. Escreve, no início do `compactado.bin`, a **quantidade de nucleotídeos** como texto (ex: `"150\n"`). Isso serve de "cabeçalho" para saber depois quantos nucleotídeos são válidos.
3. Escreve os bits da sequência logo em seguida, usando `tofile()`.

### `descompactar()`
1. Abre `compactado.bin` e lê a primeira linha (`readline()`) para descobrir a quantidade de nucleotídeos originais.
2. Lê o restante do arquivo (os bits) com `fromfile()` — a leitura continua exatamente de onde o `readline()` parou.
3. Converte cada par de bits de volta na letra correspondente (A, C, G ou T).
4. Corta o resultado no tamanho exato (`resultado[:qtd_nucleotideos]`), descartando qualquer bit de padding extra que o `bitarray` possa ter adicionado ao salvar o arquivo.
5. Escreve o resultado em `descompactado.txt`, quebrando uma linha nova a cada 70 caracteres escritos.

## Por que existe o "cabeçalho" com a quantidade de nucleotídeos?

O método `tofile()` do `bitarray` só grava bytes completos (múltiplos de 8 bits). Se a sequência de bits não for múltipla de 8, ele completa o restante com zeros (padding) para fechar o último byte.

Sem controle disso, esse padding poderia ser interpretado como um nucleotídeo `A` "fantasma" no final do texto descompactado (já que `00` = A). Por isso, o número real de nucleotídeos é salvo no início do próprio arquivo `.bin`, permitindo cortar exatamente o padding na hora de descompactar — sem precisar de arquivos auxiliares ou cálculos de bits.

## Quebra de linha a cada 70 caracteres

Ao escrever o `descompactado.txt`, o código conta quantos caracteres já escreveu. Quando esse total é múltiplo de 70 (`(atual + 1) % 70 == 0`), uma quebra de linha é inserida — resultado em linhas de exatamente 70 caracteres, um formato comum em arquivos de sequências biológicas (como o formato FASTA).

## Como usar

Basta rodar o script. Ele compacta e descompacta em sequência, na mesma execução:

```bash
python nome_do_arquivo.py
```

Isso vai gerar (ou sobrescrever) os arquivos `compactado.bin` e `descompactado.txt` na mesma pasta.
