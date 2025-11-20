from collections import deque
import heapq
from typing import Optional, List, Tuple
from itertools import count
from .models import Cliente


class QueueManager:
    """Gerencia duas filas: normal (deque) e preferencial (heap).
    Mantém também uma lista de atendidos.
    """

    def __init__(self):
        self.fila_normal: deque[Cliente] = deque()
        # heap stores tuples (priority, counter, cliente)
        self._counter = count()
        self.fila_preferencial: list[Tuple[int, int, Cliente]] = []
        self.atendidos: List[Cliente] = []

    def adicionar_cliente(self, cliente: Cliente) -> None:
        """Adiciona cliente na fila apropriada."""
        if cliente.preferencial:
            # prioridade mais alta = menor número; usamos 0 para preferencial
            heapq.heappush(self.fila_preferencial, (0, next(self._counter), cliente))
        else:
            self.fila_normal.append(cliente)

    def proximo_cliente(self) -> Optional[Cliente]:
        """Retorna e remove o próximo cliente a ser atendido.
        Preferenciais têm prioridade se houver.
        """
        if self.fila_preferencial:
            _, _, cliente = heapq.heappop(self.fila_preferencial)
        elif self.fila_normal:
            cliente = self.fila_normal.popleft()
        else:
            return None

        self.atendidos.append(cliente)
        return cliente

    def listar_fila_normal(self):
        return list(self.fila_normal)

    def listar_fila_preferencial(self):
        # extract Cliente items from heap structure ordered by priority/counter
        return [t[2] for t in sorted(self.fila_preferencial)]

    def listar_atendidos(self):
        return list(self.atendidos)
