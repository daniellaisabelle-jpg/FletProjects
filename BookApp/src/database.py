import os
import sqlite3
from model import Book

# caminho até o arquivo do banco de dados (.db)
DB_PATH = os.path.join(
         os.environ['FLET_APP_STORAGE_DATA'],
         'bookapp.db' 
    )
BOOKAPP_SQL_PATH = os.path.join(
    #nome do diretório em que o arquivo database está
    os.path.dirname(os.path.abspath(__file__)),
    'sql',
    'bookapp.sql'
)

INSERT_BOOK_QUERY = '''
    INSERT INTO books(title, author, desc, price) 
        VALUES (?, ?, ?, ?); 
'''
FETCH_BOOKS_QUERY = '''
    SELECT title, author, desc, price FROM books;
'''

class Database(object):
    def __init__(self):
        self.__create_tables()
    def __connect(self) -> sqlite3.Connection:
        '''abre o arq sqlite para consulta'''
        return sqlite3.connect(DB_PATH)
    def __create_tables(self):
        '''cria tabela do banco de dados, abre conexão 'conn' com o banco sqlte, abre o arquivo 'bookapp.sql' em sqlf, cria tabelas a partir da leitura o script e fecha o 'conn' e fecha sqlf'''
        with self.__connect() as conn:
            with open(BOOKAPP_SQL_PATH, 'r', encoding='utf-8') as sqlf:
                sql_script = sqlf.read()
                conn.executescript(sql_script)
    def insert(self, book:Book):
        '''insere livros na tabela books no banco de dados'''
        with self.__connect() as conn:
            conn.execute(
                INSERT_BOOK_QUERY,
                (book.title, book.author, book.desc, book.price)
            )

    def fetch_all(self) -> list[Book]:
        '''
            fetch_all pega todos os registros de livros do banco de dados e retorna uma lista de objetos Book com os dados de cada registro
        '''
        ret = []
        with self.__connect() as conn:
            cur = conn.cursor()
            cur.execute(FETCH_BOOKS_QUERY)
            # cada valor de rows corresponde a uma tupla contendo os valores do registro de livro
            rows = cur.fetchall()
            for row in rows:
                book = Book(
                    title=str(row[0]),
                    author=str(row[1]),
                    desc=str(row[2]),
                    price=float(row[3])
                )
                ret.append(book)
        return ret