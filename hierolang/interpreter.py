"""Interpretador do HieroLang: troca os tokens de hieróglifo pelas
palavras-chave do Python de verdade e executa o resultado como Python.
"""

import io
import sys
import tokenize
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from keywords import HIERO_TO_PY


def transpilar(codigo_hiero: str) -> str:
    tokens = tokenize.generate_tokens(io.StringIO(codigo_hiero).readline)
    saida = []
    for tok in tokens:
        tipo, valor = tok[0], tok[1]
        if tipo == tokenize.NAME and valor in HIERO_TO_PY:
            valor = HIERO_TO_PY[valor]
        saida.append((tipo, valor))
    return tokenize.untokenize(saida)


def rodar(caminho: str) -> None:
    codigo_hiero = Path(caminho).read_text(encoding="utf-8")
    codigo_python = transpilar(codigo_hiero)
    exec(compile(codigo_python, caminho, "exec"), {"__name__": "__main__"})


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("uso: python interpreter.py arquivo.hiero")
        sys.exit(1)
    rodar(sys.argv[1])
