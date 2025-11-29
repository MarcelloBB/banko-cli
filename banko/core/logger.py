from datetime import datetime
from .storage import load_data, save_data


class Logger:
    def __init__(self):
        self.load()

    def load(self):
        state = load_data()
        self.eventos = state["eventos"]

    def save(self):
        state = load_data()
        state["eventos"] = self.eventos
        save_data(state)

    def registrar(self, mensagem: str):
        ts = datetime.now().strftime("%H:%M:%S")
        self.eventos.append(f"{ts} - {mensagem}")
        self.save()

    def listar(self):
        return list(self.eventos)
