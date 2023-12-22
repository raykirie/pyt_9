import psycopg2
from psycopg2 import sql

db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',
    'port': 'your_port'
}

def execute_query(query):
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()
    return results

def create_test_report(query_number, query_description, query_results, errors_warnings, recommendations):
    with open('test_report.txt', 'a') as report_file:
        report_file.write(f'\nЗапрос {query_number}:\n')
        report_file.write(f'- Описание: {query_description}\n')
        report_file.write(f'- Результаты: {query_results}\n')
        report_file.write(f'- Обнаруженные ошибки или предупреждения: {errors_warnings}\n')
        report_file.write(f'- Рекомендации: {recommendations}\n')

if __name__ == "__main__":
    open('test_report.txt', 'w').close()

    query_1 = """
    -- ваш SQL-запрос 1
    """
    results_1 = execute_query(query_1)
    create_test_report(1, 'Выбрать всех клиентов, сделавших заказы в текущем месяце, и отсортировать их по убыванию общей суммы заказов.', results_1, 'Нет ошибок', 'Нет рекомендаций')

    query_2 = """
    -- ваш SQL-запрос 2
    """
    results_2 = execute_query(query_2)
    create_test_report(2, 'Выбрать все продукты, имеющие цену выше средней по категории, и отсортировать их по возрастанию цены.', results_2, 'Нет ошибок', 'Нет рекомендаций')

