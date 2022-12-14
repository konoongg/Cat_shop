from flask import Flask, render_template, url_for, request,redirect
import sqlite3
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    conn = sqlite3.connect('shop_project.db')
    cursor = conn.cursor()
    post = ''' SELECT * FROM shop '''
    post= cursor.execute(post).fetchall()
    conn.commit()
    return render_template('index.html', post = post)

@app.route('/<int:code>')
def tov_code (code):
    print(111111111111111111111111111111111111111111111111111111111111111111)
    conn = sqlite3.connect('shop_project.db')
    cursor = conn.cursor()
    post = ''' SELECT * FROM shop where code = ?'''
    post= cursor.execute(post,[code]).fetchall()[0]
    print(post)
    conn.commit()
    return render_template('tov.html', post = post)


if __name__ == "__main__":
    app.run()
