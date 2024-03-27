from typing import Optional
from sqlmodel import Field, SQLModel

class CursoModel(SQLModel, table=True):
    # if table=True, ele vai criar tabela e também schema(json) ao mesmo tempo
    # if table=False, ele não vai criar tabela. Vai funcionar apenas como schema(json) na prória aplicação.
    __tablename__: str = 'cursos-sqlmodel'
    
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    aulas: int
    horas: int