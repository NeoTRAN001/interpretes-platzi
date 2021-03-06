from typing import (
    NamedTuple,
    Dict,
)
from enum import (
    auto,
    Enum,
    unique,
)

@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    DIV = auto()
    ELSE = auto()
    EOF = auto()
    EQ = auto()
    FALSE = auto()
    FUNCTION = auto()
    GT = auto()
    GT_EQ = auto()
    IDENT = auto()
    IF = auto()
    ILLEGAL = auto()
    INT = auto()
    LBRACE = auto()
    LET = auto()
    LPAREN = auto()
    LT = auto()
    LT_EQ = auto()
    MINUS = auto()
    MULT = auto()
    NOT = auto()
    NOT_EQ = auto()
    PLUS = auto()
    RBRACE = auto()
    RETURN = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE = auto()

class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'\033[94m Type: \033[0m {self.token_type}, \033[92m Literal: \033[0m {self.literal}'

def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'falso': TokenType.FALSE,
        'procedimiento': TokenType.FUNCTION,
        'regresa': TokenType.RETURN,
        'si': TokenType.IF,
        'si_no': TokenType.ELSE,
        'variable': TokenType.LET,
        'verdadero': TokenType.TRUE
    }

    return keywords.get(literal, TokenType.IDENT)