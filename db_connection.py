import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="villa_masses",
            user="your_username",
            password="your_password"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None