from datetime import datetime
from typing import List


class Logger:
    def __init__(self):
        self.eventos: List[str] = []

    def registrar(self, mensagem: str) -> None:
        ts = datetime.now().strftime("%H:%M:%S")
        self.eventos.append(f"{ts} - {mensagem}")

    def listar(self):
        return list(self.eventos)

    def exportar_csv(self, path: str) -> None:
        import csv

        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["timestamp", "evento"])
            for linha in self.eventos:
                if " - " in linha:
                    ts, msg = linha.split(" - ", 1)
                else:
                    ts, msg = "", linha
                writer.writerow([ts, msg])
