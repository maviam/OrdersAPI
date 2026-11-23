# FastAPI é uma framework
pip install fastapi uvicorn sqlalchemy passlib[crypt] python-jose[cryptography] python-dotenv python-multipart
# uvicorn - gestor de servidor 
# agsi - gere requisições assíncronas
# python-jose -> gestão dos tokens
# python-dotenv - criar variáveis do ambiente
# python-multipart - dependência do python-jose

# Testar a aplicação
uvicorn main:app --reload

# Criar as nossas rotas
http://127.0.0.1:8000/orders/