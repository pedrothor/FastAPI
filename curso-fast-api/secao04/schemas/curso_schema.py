
# para cada model na api, terá que criar um arquivo no schema.

from typing import Optional

from pydantic import BaseModel as SCBaseModel

class CursoSchema(SCBaseModel):
    # o id será criado pelo próprio banco de dados. por isso o Optional.
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
    