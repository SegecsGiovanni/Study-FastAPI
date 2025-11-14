from passlib.context import CryptContext
import hashlib


CRIPTO = CryptContext(schemes=['bcrypt_sha256', 'bcrypt'], deprecated='auto')


def _hash_password(senha: str) -> str:
    """
    Função auxiliar que faz hash da senha usando SHA-256 antes de passar para bcrypt.
    Isso garante que a senha nunca exceda 72 bytes (limite do bcrypt).
    """
    return hashlib.sha256(senha.encode()).hexdigest()


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correta comparando a senha em texto puro,
    informada pelo usuário, e o hash da senha que estará salvo no banco de dados durante a criação da conta
    """

    return CRIPTO.verify(_hash_password(senha), hash_senha)

def gerar_hash_senha(senha: str) -> str:
    """
    Função que gera e retorna o hash da senha.
    A senha é primeiramente hasheada com SHA-256 para garantir tamanho consistente,
    depois o resultado é hasheado com bcrypt.
    """

    return CRIPTO.hash(_hash_password(senha))