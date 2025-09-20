from fastapi import APIRouter

router = APIRouter()



@router.get('/api/v1/usuários')
async def get_usuarios():
    return {'info': "Todos os usuários"}
