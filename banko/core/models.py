from dataclasses import dataclass
from datetime import datetime


@dataclass
class Cliente:
    nome: str
    preferencial: bool = False
    chegada: datetime = None
    operacao: str = "Não informado"
    tempo_espera: float | None = None
