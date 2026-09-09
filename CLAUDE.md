# CLAUDE.md — hierolang

Instruções para qualquer sessão aberta nesta pasta.
Este arquivo tem prioridade sobre o `CLAUDE.md` da raiz da pasta "Claude Code".

---

## 1. O que é

Python com hieróglifos egípcios no lugar das palavras-chave. O
`hierolang/interpreter.py` passa o arquivo `.hiero` pelo `tokenize` da
biblioteca padrão, troca cada token `NAME` que esteja na tabela pela
palavra-chave real e executa com `exec`.

**É uma linguagem-piada, e a piada é o ponto.** Vale a mesma regra da `larpc`:
não transformar isso numa linguagem séria, não propor gramática própria, AST
própria nem VM. A graça é que por baixo é Python inteiro e sem truque.

**Não confundir com a `larpc`.** São duas linguagens-piada diferentes na mesma
pasta: a `larpc` transpila para C e compila com o MSVC; esta executa Python
direto na memória. Não portar sistema de uma para a outra.

## 2. O vocabulário é a linguagem

`hierolang/keywords.py` tem onze pares hieróglifo→palavra-chave, ocupando os
pontos Unicode `U+13000`–`U+1300A` em ordem. **Mexeu aí, mexeu na linguagem:**
o `README.md` traz a tabela inteira e precisa acompanhar qualquer mudança.

Acrescentar palavra-chave nova é a evolução natural do projeto (`while`,
`class`, `return`, `elif`, `with` ainda não têm hieróglifo). Duas regras:

- **Continuar a sequência Unicode.** O próximo é `U+1300B`, e assim por diante.
  Nada de escolher hieróglifo "que combina com o significado" — a ordem é o
  critério, e ela é o que torna a tabela conferível.
- **Não remover nem renumerar o que já existe.** `exemplos/calculadora.hiero`
  está escrito contra a tabela atual e quebra em silêncio se os pontos mudarem
  de significado.

## 3. Por que passa pelo tokenizer

Substituição por `str.replace` seria mais curta e está **errada**: trocaria
hieróglifo dentro de string de texto e de comentário também. O `tokenize` só
troca token do tipo `NAME`. Se alguém "simplificar" isso, o bug volta e só
aparece quando um programa imprimir um hieróglifo.

## 4. Testar

Não há suíte. Antes de dizer que uma alteração funciona, rodar um `.hiero` de
verdade e mostrar a saída:

```powershell
python hierolang\interpreter.py exemplos\calculadora.hiero
```

Esse exemplo abre janela do Tkinter. Para teste que não depende de janela,
escrever um `.hiero` pequeno na pasta temporária e rodar por lá — não sujar
`exemplos/` com arquivo de teste.

## 5. Encoding

Arquivo `.hiero` é UTF-8 e os hieróglifos são pares surrogados fora do BMP. Ao
criar ou editar um `.hiero` no Windows, gravar em UTF-8 explicitamente — o
padrão ANSI do PowerShell (`Set-Content` sem `-Encoding utf8`) destrói os
caracteres e o arquivo passa a dar `SyntaxError` sem motivo aparente.
