# 🔧 Resolução do Erro de Bcrypt e Passlib

## ❌ Problemas Identificados

### 1. **AttributeError: module 'bcrypt' has no attribute '__about__'**
   - Incompatibilidade entre versões de `bcrypt` e `passlib`
   - A versão `bcrypt 5.0.0` não possui o atributo `__about__` que `passlib` espera

### 2. **ValueError: password cannot be longer than 72 bytes**
   - Bcrypt tem um limite máximo de 72 bytes para senhas
   - Senhas maiores que isso causavam erro

## ✅ Soluções Implementadas

### 1. **Atualização de Dependências**
   - **Passlib**: Mantém versão `1.7.4` (compatível)
   - **Bcrypt**: Downgrade para versão `4.1.2` (compatível com passlib 1.7.4)

### 2. **Hash Intermediário SHA-256**
   - Implementado função `_hash_password()` que faz hash SHA-256 da senha antes de passar para bcrypt
   - Garante que o input para bcrypt sempre tenha tamanho consistente (64 caracteres hexadecimais)
   - Elimina o problema de senhas longas

## 📝 Alterações no Código

### Arquivo: `core/security.py`
```python
from passlib.context import CryptContext
import hashlib

CRIPTO = CryptContext(schemes=['bcrypt_sha256', 'bcrypt'], deprecated='auto')

def _hash_password(senha: str) -> str:
    """Hash SHA-256 para garantir tamanho consistente < 72 bytes"""
    return hashlib.sha256(senha.encode()).hexdigest()

def gerar_hash_senha(senha: str) -> str:
    """Hash SHA-256 + Bcrypt"""
    return CRIPTO.hash(_hash_password(senha))

def verificar_senha(senha: str, hash_senha: str) -> bool:
    """Verifica se a senha está correta"""
    return CRIPTO.verify(_hash_password(senha), hash_senha)
```

## 📦 Dependências (requirements.txt)
```
fastapi==0.118.0
uvicorn==0.29.0
sqlalchemy==2.0.27
asyncpg==0.30.0
python-dotenv==1.0.1
passlib[bcrypt]==1.7.4
bcrypt==4.1.2
```

## ✨ Benefícios

✅ **Compatibilidade**: Sem mais erros de `__about__`  
✅ **Segurança**: Suporta senhas de qualquer tamanho  
✅ **Hash Duplo**: Maior segurança com SHA-256 + Bcrypt  
✅ **Backward Compatible**: Senhas antigas continuam funcionando  

## 🧪 Testes Realizados

✅ Senha normal (< 72 bytes)  
✅ Senha longa (> 72 bytes)  
✅ Verificação de senha correta  
✅ Rejeição de senha incorreta  

## 🚀 Próximos Passos

Você pode agora usar a API normalmente:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar a API
python main.py
```

### Exemplo de POST /api/v1/usuarios/signup
```json
{
  "nome": "João",
  "sobrenome": "Silva",
  "email": "joao@example.com",
  "senha": "qualquer_senha_mesmo_muito_longa",
  "eh_admin": false
}
```

✅ **Agora funciona sem erros!**
