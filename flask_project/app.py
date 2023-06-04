from flask import Flask, render_template, request
from mysql.connector import connect, Error


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def call_log_viewer():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        filtered_log = filter_call_log(start_date, end_date)
        return render_template('call_log.html', call_log=filtered_log)
    return render_template('index.html')


def filter_call_log(start_date, end_date):
    select_query = "SELECT * FROM testdb.calls WHERE DATE(date_begin) BETWEEN %s AND %s ORDER BY date_begin"

    try:
        with connect(host='localhost',
                     user='ivan',
                     password='Megaf0n+') as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_query, (start_date, end_date))

                result = []
                for row in cursor.fetchall():
                    result.append({
                        'start_call': row[1],
                        'duration': row[3],
                        'end_call': row[2],
                        'another_number': row[0]
                    })

                return result
    except Error as e:
        print(e)


if __name__ == '__main__':
    app.run()
