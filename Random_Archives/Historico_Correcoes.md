# Histórico de Correções e Ajustes para Funcionamento do Projeto

Este documento lista todas as alterações realizadas para que o projeto FAST_API funcione corretamente com FastAPI, SQLAlchemy e PostgreSQL.


## 1. Correções em dependências e ambiente

- Instalação dos pacotes Python ausentes:
  - `pydantic`
  - `pydantic-settings`
  - `sqlalchemy`
  - `asyncpg`
  - `fastapi`



### Como criar e ativar um ambiente virtual Python (passo a passo detalhado)

1. **Abra o VS Code** e navegue até a pasta raiz do projeto (`FAST_API`).

2. **Verifique se já existe um ambiente virtual**:
   - Procure pela pasta `.venv` ou `venv` na raiz do projeto.
   - Se já existir, pule para o passo de ativação.

3. **Crie um novo ambiente virtual** (caso não exista):
   - No terminal do VS Code, execute:
     ```powershell
     python -m venv .venv
     ```
   - Isso criará uma pasta chamada `.venv` com todos os arquivos do ambiente virtual.
   - Se preferir outro nome, substitua `.venv` por `venv` ou outro de sua escolha.

4. **Ative o ambiente virtual**:
   - No terminal do VS Code, execute:
     ```powershell
     .venv\Scripts\activate
     ```
   - Se o nome da pasta for diferente, ajuste o caminho conforme necessário (ex: `venv\Scripts\activate`).
   - Após ativar, o terminal mostrará o nome do ambiente virtual no início da linha.

5. **Desative o ambiente virtual** (quando terminar de trabalhar):
   - No terminal, execute:
     ```powershell
     deactivate
     ```

---

**Observações importantes:**
- Sempre ative o ambiente virtual antes de instalar pacotes ou rodar scripts do projeto.
- O ambiente virtual garante que as dependências do projeto não afetem outros projetos Python no seu computador.
- Se estiver usando outro sistema operacional:
  - No Linux/Mac, o comando de ativação é:
    ```bash
    source .venv/bin/activate
    ```



### Como instalar os pacotes manualmente (passo a passo detalhado)

1. **Com o ambiente virtual já criado e ativado** (veja instruções acima), instale os pacotes necessários:
   - Execute o comando abaixo para instalar todas as dependências de uma vez:
     ```powershell
     pip install pydantic pydantic-settings sqlalchemy asyncpg fastapi
     ```
   - Aguarde até que todos os pacotes sejam baixados e instalados. Se aparecer algum erro, verifique se o ambiente virtual está ativo e se o comando foi digitado corretamente.

2. **Verifique se os pacotes foram instalados**:
   - Execute:
     ```powershell
     pip list
     ```
   - Confirme que todos os pacotes (`pydantic`, `pydantic-settings`, `sqlalchemy`, `asyncpg`, `fastapi`) aparecem na lista.

3. **Se precisar instalar outros pacotes** (exemplo: `uvicorn` para rodar o servidor FastAPI):
   - Execute:
     ```powershell
     pip install uvicorn
     ```

4. **Sempre mantenha o ambiente virtual ativado** enquanto estiver trabalhando no projeto para garantir que os comandos e dependências funcionem corretamente.

---

**Dica:** Se for compartilhar o projeto, inclua um arquivo `requirements.txt` com todos os pacotes usados. Para gerar:
```powershell
pip freeze > requirements.txt
```
Assim, outros desenvolvedores podem instalar tudo com:
```powershell
pip install -r requirements.txt
```

## 2. Ajustes no código fonte

### 2.1. `core/configs.py`
- Troca do import de `BaseSettings` para o pacote correto:
  - De: `from pydantic import BaseSettings`
  - Para: `from pydantic_settings import BaseSettings`
- Adição de `ClassVar` para o atributo `DBBaseModel`:
  - De: `DBBaseModel = declarative_base()`
  - Para: `DBBaseModel: ClassVar = declarative_base()`

### 2.2. `core/database.py`
- Correção dos imports e uso do SQLAlchemy async:
  - De: `from sqlalchemy.orm import session_key, AsyncEngine, AsyncSession`
  - Para: `from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession`
  - Uso correto de `sessionmaker` para criar sessões assíncronas.

### 2.3. `models/curso_model.py`
- Correção dos imports e definição dos campos:
  - De: `from sqlalchemy import column, Integer, String`
  - Para: `from sqlalchemy import Column, Integer, String`
- Remoção das type annotations dos campos do modelo:
  - De: `id: int = column(...)`
  - Para: `id = Column(...)`

### 2.4. Instalação e configuração do PostgreSQL
- Instalação do PostgreSQL no Windows.
- Criação do usuário `geek` e banco `faculdade`.
- Concessão de permissões ao usuário `geek`:
  - `GRANT ALL PRIVILEGES ON SCHEMA public TO geek;`
  - `ALTER USER geek WITH SUPERUSER;`

## 3. Testes e execução
- Execução do script `criar_tabelas.py` para validar a criação das tabelas.
- Ajuste de permissões no banco até o sucesso da operação.

---

**Todas as alterações acima foram necessárias para garantir o funcionamento do projeto com as versões atuais das bibliotecas e do PostgreSQL.**

Se novas dependências ou mudanças de versão ocorrerem, recomenda-se revisar este documento e atualizar conforme necessário.