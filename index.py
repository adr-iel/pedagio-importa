# Instacao de dependencias
!pip install pymysql

# Garantir que a conexão está funcionando
from sqlalchemy import create_engine, text
engine = create_engine('mysql+pymysql://root:minhasenha@localhost:3306/meubanco')
with engine.connect() as conn:
    result = conn.execute(text("SELECT 1"))
    print("Conexão bem-sucedida!" if result.fetchone() else "Falha na conexão.")


import pandas as pd
from sqlalchemy import create_engine, Table, Column, String, Float, MetaData
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import csv

# Configurações
caminho_csv = 'caminho_arquivo.csv'
caminho_log_txt = 'caminho_log.txt'
caminho_banco = 'mysql+pymysql://root:minhasenha@localhost:3306/meubanco'


# Criar engine e metadata
engine = create_engine(caminho_banco)
metadata = MetaData()

# Definir a tabela
transacoes = Table('nome_tabela', metadata,
    Column('coluna_1', String),
    Column('coluna_2', String),
    Column('coluna_3', String),
    Column('coluna_4', String),
    Column('coluna_5', String),
    Column('coluna_6', Float),
    Column('coluna_7', String),
)

# Leitura do CSV
with open(caminho_csv, newline='', encoding='utf-8') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    f.seek(0)
    df = pd.read_csv(caminho_csv, sep=';', encoding='utf-8')

# Abrir log de erros
with open(caminho_log_txt, 'a', encoding='utf-8') as log_file:
    log_file.write(f"\n\n======= Início da execução: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} =======\n")

    with engine.begin() as conn:
        for index, linha in df.iterrows():
            try:
                # Preparar os dados
                insert_stmt = transacoes.insert().values(
                    coluna_1=str(linha['ID Transacao']),
                    coluna_2=str(linha['CPF/CNPJ']),
                    coluna_3=pd.to_datetime(linha['Data de Utilizacao'], dayfirst=True).strftime('%Y-%m-%d'),
                    coluna_4=linha['Hora de Untrada'],
                    coluna_5=str(linha['Placa']),
                    coluna_6=float(str(linha['Valor Cobrado']).replace(',', '.')),
                    coluna_7=str(linha['Endereco do Estabelecimento']),
                    
                )

                conn.execute(insert_stmt)

            except SQLAlchemyError as e:
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_file.write(f"[{timestamp}] Erro na linha {index}:\n")
                log_file.write(f"  Conteúdo da linha: {linha.to_dict()}\n")
                log_file.write(f"  Erro: {str(e)}\n\n")
                print(f"Erro na linha {index} registrado no log.")

print("\nExecução finalizada com SQLAlchemy. Verifique o log em 'log_erros.txt' caso necessário.")
