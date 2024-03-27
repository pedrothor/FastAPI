from sqlmodel import SQLModel

from core.database import engine

async def create_tables() -> None:
    import models.__all_models
    print('Criando tabelas...')

    async with engine.begin() as conn:
        # se fizesse um drop_all nas tabelas, a tabela "curso", da seção anterior, iria ser excluída. Então preferi mantê-la a fim de estudo.
        #await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

    print('tabelas criadas com sucesso!')


if __name__ == '__main__':
    import asyncio

    asyncio.run(create_tables())