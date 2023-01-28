from hashlib import sha256
import sqlite3

stored_password = '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'
password_login = input("DIGITE SUAS SENHA:")
hash_password_login = sha256(password_login.encode()).hexdigest()

if hash_password_login == stored_password:
    print("WELCOME TO MY MENU OPÇÃO ❣")
else:
    print('SENHA INVÁLIDA! ENCERRANDO ...')
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
 );
 ''')

def menu():
   print("-*-" * 10)
    print('I: INSERIR NOVA SENHA:')
    print('L: LISTAR SERVIÇOS SALVOS:')
    print('R: RECUPERAR UM SENHA:')
    print('D: DELETAR OS SERVIÇOS:')
    print('S: SAIR')
    print("-*-" * 10)

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
        ''')

    if cursor.rowcount == 0:
        print('SERVIÇO NÃO CADASTRADO, use "L" PARA VERIFICAR OS SERVIÇOS')
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
        ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

def delete():
    cursor.execute(f'''
       DELETE FROM users
        ''')

while True:
    menu()
    op = input("O QUE VOCÊ DESEJA FAZER ?  ")
    if op not in ['I', 'L', 'R', 'S', 'D']:
        print('OPÇAO INVÁLIDA! VERIFIQUE AS opções DISPONÍVEISE DIGITE NOVAMENTE!')
        continue
    if op == 'I':
        service = input('DIGITE O NOME DO SERVIÇO: ')
        username = input('DIGITE O SEU NOME DE USUÁRIO: ')
        password = input('DIGITE A SENHA: ')
        insert_password(service, username, password)

    if op == 'L':
        show_services()

    if op == 'R':
        service = input('QUAL O  SERVIÇO PARA O QUAL VOCÊ DESEJA RECUPERAR A SENHA?')
        get_password(service)

    if op == 'S':
        print('ENCERRANDO O PROGRAMA...')
        break
    if op == 'D':
        print('RESENTANDO OS DADOS...')
        delete()

conn.close()


