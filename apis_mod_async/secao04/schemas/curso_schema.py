
from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CursoCreateSchema(SCBaseModel):
    titulo: str
    aulas: int
    horas: int

class CursoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    class Config:
        from_attributes = True