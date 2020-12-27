FROM mysql:8.0
# Adicionando os scripts SQL para serem executados na criação do banco
COPY . /docker-entrypoint-initdb.d/