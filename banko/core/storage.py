import json
from pathlib import Path
from datetime import datetime
from .models import Cliente

DATA_FILE = Path.home() / ".banko_queue.json"


def _default_data():
    return {"fila_normal": [], "fila_preferencial": [], "atendidos": [], "eventos": []}


def load_data():
    if not DATA_FILE.exists():
        return _default_data()

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    def parse_client(c):
        return Cliente(
            nome=c["nome"],
            preferencial=c["preferencial"],
            chegada=datetime.fromisoformat(c["chegada"]),
            operacao=c.get("operacao", "Não informado"),
            tempo_espera=c.get("tempo_espera"),
        )

    raw["fila_normal"] = [parse_client(c) for c in raw["fila_normal"]]
    raw["fila_preferencial"] = [parse_client(c) for c in raw["fila_preferencial"]]
    raw["atendidos"] = [parse_client(c) for c in raw["atendidos"]]

    return raw


def save_data(data):
    def encode(c: Cliente):
        return {
            "nome": c.nome,
            "preferencial": c.preferencial,
            "chegada": c.chegada.isoformat(),
            "operacao": c.operacao,
            "tempo_espera": c.tempo_espera,
        }

    serializable = {
        "fila_normal": [encode(c) for c in data["fila_normal"]],
        "fila_preferencial": [encode(c) for c in data["fila_preferencial"]],
        "atendidos": [encode(c) for c in data["atendidos"]],
        "eventos": data["eventos"],
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=4, ensure_ascii=False)
