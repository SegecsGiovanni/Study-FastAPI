from typing import Optional
from pydantic import BaseModel, field_validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int # mais de 12
    horas: int # mais de 10

    @field_validator('titulo')
    def validar_titulo(cls, value: str):
        # validacao 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos tres palavras!')
        
        # validacao 2
        if value.islower():
            raise ValueError('O titulo deve ser capitalizado!')
        
        return value
    

    @field_validator('aulas')
    def validar_aulas(cls, value: int):
        if value < 12:
            raise ValueError('O curso deve conter mais de 12 aulas.')
        

    @field_validator('horas')
    def validar_horas(cls, value: int):
        if value < 10:
            raise ValueError('O curso deve conter mais de 10 aulas')


cursos = [
    Curso(id=1, titulo="Programação para leigos", aulas=42, horas=56),
    Curso(id=2, titulo="Algoritmos e lógica de programação", aulas=52, horas=66),
]