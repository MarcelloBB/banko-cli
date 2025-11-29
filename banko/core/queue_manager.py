from collections import deque
import heapq
from itertools import count
from .models import Cliente
from .storage import load_data, save_data
from datetime import datetime


class QueueManager:
    def __init__(self):
        self._counter = count()
        self.load()

    def load(self):
        state = load_data()

        self.fila_normal = deque(state["fila_normal"])
        self.fila_preferencial = [
            (0, next(self._counter), c) for c in state["fila_preferencial"]
        ]
        heapq.heapify(self.fila_preferencial)

        self.atendidos = state["atendidos"]
        self.eventos = state["eventos"]

    def save(self):
        data = {
            "fila_normal": list(self.fila_normal),
            "fila_preferencial": [c for _, _, c in self.fila_preferencial],
            "atendidos": self.atendidos,
            "eventos": self.eventos,
        }
        save_data(data)

    def adicionar_cliente(self, cliente: Cliente):
        if cliente.preferencial:
            heapq.heappush(self.fila_preferencial, (0, next(self._counter), cliente))
        else:
            self.fila_normal.append(cliente)
        self.save()

    def proximo_cliente(self):
        if self.fila_preferencial:
            _, _, cliente = heapq.heappop(self.fila_preferencial)
        elif self.fila_normal:
            cliente = self.fila_normal.popleft()
        else:
            return None

        agora = datetime.now()
        cliente.tempo_espera = (agora - cliente.chegada).total_seconds()

        self.atendidos.append(cliente)
        self.save()
        return cliente

    def listar_fila_normal(self):
        return list(self.fila_normal)

    def listar_fila_preferencial(self):
        return [c for _, _, c in sorted(self.fila_preferencial)]

    def listar_atendidos(self):
        return list(self.atendidos)
