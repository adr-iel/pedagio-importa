# Importador de Transações de Pedágio para Banco de Dados

Este script realiza a importação de dados de transações de pedágio (neste caso foi utilizado a plataforma Veloe) a partir de um arquivo CSV para uma base de dados MySQL utilizando a biblioteca SQLAlchemy e Pandas.

##Estrutura do Projeto
- `extrato_veloe.csv`: Arquivo CSV contendo os dados de transações de pedágio.
- `log_erros.txt`: Arquivo de log que registra qualquer erro encontrado durante a execução.
- `index.py`: Script Python principal que executa a importação.

##Requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:
```bash
pip install pandas sqlalchemy pymysql
```

##Configurações
As variáveis principais que você pode ajustar:
```python
caminho_csv = 'C:/.../extrato_veloe.csv'
caminho_log_txt = 'C:/.../log_erros.txt'
caminho_banco = 'mysql+pymysql://usuario:senha@host:porta/nome_banco'
```

#Funcionamento
1. **Leitura do CSV:** Lê o arquivo usando `pandas.read_csv`, com separador `;`.
2. **Processamento dos Dados:**
   - Converte a data para o formato ISO (`YYYY-MM-DD`).
   - Converte valores com vírgula para ponto e transforma em float.
3. **Inserção no Banco:**
   - Cada linha é inserida na tabela `nome_tabela`.
   - Campos: `coluna_1`, `coluna_2`, `coluna_3`, `coluna_4`, `coluna_5`, `coluna_6`, `coluna_7`.
4. **Log de Erros:**
   - Caso ocorra erro de banco, ele será salvo no `log_erros.txt` com informações da linha e mensagem de erro.

# Exemplo de Execução
```bash
python index.py
```

Ao final da execução, será exibida a mensagem:

```
Execução finalizada com SQLAlchemy. Verifique o log em 'log_erros.txt' caso necessário.
```

#Licença
Este projeto é de uso interno. Consulte a equipe responsável antes de redistribuir.
