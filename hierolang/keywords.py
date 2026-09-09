"""Mapa entre hieróglifos egípcios (Unicode) e palavras-chave reais do Python.

Só as palavras-chave usadas nos exemplos deste projeto foram mapeadas —
o resto da linguagem (builtins, operadores, literais) é Python puro.
"""

HIERO_TO_PY = {
    "\U00013000": "import",
    "\U00013001": "as",
    "\U00013002": "def",
    "\U00013003": "global",
    "\U00013004": "try",
    "\U00013005": "except",
    "\U00013006": "for",
    "\U00013007": "in",
    "\U00013008": "if",
    "\U00013009": "else",
    "\U0001300A": "lambda",
}

PY_TO_HIERO = {py: hiero for hiero, py in HIERO_TO_PY.items()}
