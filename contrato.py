from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt


class ProdutoEnum(str, Enum):
    produto1 = 'ZapFlow com Gemini'
    produto2 = 'ZapFlow com ChatGPT'
    produto3 = 'ZapFlow com Llama3.0'


class Vendas(BaseModel):
    """

    Modelo de dados para as vendas. teste

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositveFloat): valor da compra
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto

    """


    email: EmailStr
    data: datetime
    valor: PositiveFloat
    qtd: PositiveInt
    produto: ProdutoEnum

