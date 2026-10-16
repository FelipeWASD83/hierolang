# HieroLang

Python escrito com hieróglifos egípcios no lugar das palavras-chave.

```
𓀆 n 𓀇 range(3):
    𓀈 n % 2 == 0:
        print(n, "par")
    𓀉:
        print(n, "impar")
```

Isso roda. O interpretador troca cada hieróglifo pela palavra-chave real do
Python e executa o resultado — nada é reimplementado, é Python de verdade por
baixo.

## Como rodar

```powershell
python hierolang\interpreter.py exemplos\calculadora.hiero
```

O exemplo é uma calculadora em Tkinter — abre uma janela, com os botões
funcionando. O arquivo dela tem 45 linhas e não usa nenhuma palavra-chave em
letra latina.

Não precisa instalar nada: só Python. Nenhuma dependência de terceiros.

## O vocabulário

Onze palavras-chave estão mapeadas, na ordem dos hieróglifos Unicode
`U+13000`–`U+1300A`:

| Hieróglifo | Python | | Hieróglifo | Python |
|---|---|---|---|---|
| 𓀀 | `import` | | 𓀆 | `for` |
| 𓀁 | `as` | | 𓀇 | `in` |
| 𓀂 | `def` | | 𓀈 | `if` |
| 𓀃 | `global` | | 𓀉 | `else` |
| 𓀄 | `try` | | 𓀊 | `lambda` |
| 𓀅 | `except` | | | |

Todo o resto — operadores, literais, `print`, `range`, nomes de variável — é
Python normal. `while`, `class`, `return`, `elif`, `with`, `import from` e o
resto da linguagem **não estão mapeados**: usar a palavra em inglês mesmo, que
funciona, ou acrescentar o hieróglifo em `hierolang/keywords.py`.

## Como funciona

`hierolang/interpreter.py` passa o arquivo pelo `tokenize` da biblioteca padrão,
troca todo token do tipo `NAME` que esteja na tabela pela palavra-chave
correspondente, remonta o código com `untokenize` e executa.

Passar pelo tokenizer em vez de dar `str.replace` é o que evita o erro clássico:
um hieróglifo dentro de uma string de texto **não** vira palavra-chave, porque
ali ele é token do tipo `STRING`, não `NAME`.

## Limites conhecidos

- Não existe comando `hierolang` no PATH — roda pelo caminho do arquivo.
- Erro de execução aponta a linha certa do `.hiero`, mas mostra o trecho já
  traduzido para Python, não o hieróglifo original.
- Sem testes automatizados.

## Licença

Código sob a licença MIT (arquivo `LICENSE`).
