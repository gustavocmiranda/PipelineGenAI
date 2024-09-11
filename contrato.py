from datetime import datetime
from typing import Tuple
from enum import Enum

from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt


class ProdutoEnum(str, Enum):
    produto1 = 'ZapFlow com Gemini'
    produto2 = 'ZapFlow com ChatGPT'
    produto3 = 'ZapFlow com Llama3.0'


class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    qtd: PositiveInt
    produto: ProdutoEnum

