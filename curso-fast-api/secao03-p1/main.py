from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Response

# Optional (para deixar campos opcionais)
from typing import Optional, Any, List, Dict

# path parameters
from fastapi import Path

# query parameters
from fastapi import Query

# header (cabeçalho)
from fastapi import Header

# injeção de dependência
from fastapi import Depends

# sleep
from time import sleep

from models import Curso
from models import cursos


def fake_db():
    try:
        print('Abrindo conexão com banco de dados')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados')
        sleep(1)

app = FastAPI(
    title='API de Cursos da Geek University',
    version='0.0.1',
    description='Uma API para estudo do FastAPI',
    )

@app.get('/cursos', 
        description='Retorna todos os cursos ou uma lista vazia.', 
        summary='Retorna todos os cursos.',
        response_model=List[Curso],
        response_description='Cursos encontrados com sucesso!'
        )
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default_factory=None, title='ID do curso', description=f'Deve ser entre 1 e {len(cursos)}', gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id-1]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado')


@app.post('/cursos', 
          status_code=status.HTTP_201_CREATED,
          response_model=Curso,
          )
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o ID {curso_id}')


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe curso com o ID {curso_id}')


# query parameters
@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a + b

    if c:
        soma += c

    print(f'X-GEEK: {x_geek}')
    return {"Resultado": soma}

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)

