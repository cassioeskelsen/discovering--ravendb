import datetime
from typing import Optional

from fastapi import FastAPI
from pyravendb.store.document_store import DocumentStore
from src.models import Romaneio, Destinatario, Transportador, Item

app = FastAPI(title="Romaneios")
server = "http://192.168.0.156:8080"  # altere para o seu servidor
store = None


@app.on_event("startup")
async def on_startup():
    global store
    store = DocumentStore(urls=[server], database="romaneios")
    store.initialize()


@app.get("/romaneios/")
async def romaneios(numero_romaneio: Optional[int] = None):
    with store.open_session() as session:
        if numero_romaneio is None:
            query_result = list(session.query(object_type=Romaneio))
        else:
            query_result = list(session.query(object_type=Romaneio).where(numero=numero_romaneio))
        return query_result


@app.post("/romaneios/", status_code=201)
async def romaneio(numero: int, data_hora_carga: datetime.datetime, nome_destinatario: str, endereco: str, cidade: str,
                   uf: str, nome_transportadora, nome_motorista, placa):
    with store.open_session() as session:
        romaneio = Romaneio(numero, data_hora_carga, destinatario=Destinatario(nome_destinatario, endereco, cidade, uf),
                     transportador=Transportador(nome_transportadora, nome_motorista, placa), itens=[], updates=[])
        session.store(romaneio)
        session.save_changes()
        return romaneio


@app.post("/romaneios/{numero_romaneio}/adiciona_item/{qt_item}/{descricao}")
async def romaneios(numero_romaneio: int, qt_item: int, descricao: str):
    with store.open_session() as session:
        romaneio = list(session.query(object_type=Romaneio).where(numero=numero_romaneio))[0]
        romaneio.itens.append(Item(qt_volume=qt_item, descricao=descricao))
        session.store(romaneio)
        session.save_changes()
        return romaneio
