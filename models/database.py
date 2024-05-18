import databases

# берем параметры БД из переменных окружения
#DB_USER = "russtravel"
#DB_PASSWORD = "russtravel"
#DB_HOST = "localhost"
#DB_NAME = "russtravel"
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    #"postgres://russtravel:CTXnKRp6iwUOMmQf6k33dGta2qFQNNk7@dpg-coilasljm4es739qdp8g-a/russtravel"
)
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)
