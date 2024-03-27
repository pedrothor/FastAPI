from typing import Optional
from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator('titulo')
    def validar_titulo(cls, value: str):
        palavras = value.split(' ')
        
        # validação 1
        if len(palavras) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavras')
        
        # validação 2
        if value.islower():
            raise ValueError('O título deve ser capitalizado.')
        
        return value
    
    @validator('aulas')
    def validar_aulas(cls, value: int):
        aulas = value

        # validação 3
        if aulas < 12:
            raise ValueError('Deve ter mais de 12 aulas.')
        
        return value
    
    @validator('horas')
    def validar_horas(cls, value: int):
        horas = value

        # validação 4
        if horas < 10:
            raise ValueError('Deve ter mais que 10 horas.')
        
        return value

cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(id=2, titulo= "Algoritmos e Lógica de Programação", aulas=87, horas=67)
]
