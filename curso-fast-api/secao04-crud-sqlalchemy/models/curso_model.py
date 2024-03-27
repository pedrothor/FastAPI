from core.configs import Settings
from sqlalchemy import Column, Integer, String


class CursoModel(Settings.DBBaseModel):
    __tablename__ = 'cursos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
    