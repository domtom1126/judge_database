import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)


def judge_search():

    display = request.form('autocomp')
    conn = sqlite3.connect('defatty_stats_real.sqlite')
    c = conn.cursor()
    # request.form['judge_statute_text']
    # Gets the total cases for that statute for that atty
    judge_statute_totals = c.execute("SELECT atty_total FROM defatty_stats WHERE atty=? and statute=?",
                                     (display, request.form['judge_statute_text'], )).fetchall()
    # Displays the atty name
    judge_name = c.execute("SELECT atty FROM defatty_stats WHERE atty=?",
                           (display, request.form['judge_text'])).fetchone()
    # Displays the statute
    judge_statute = c.execute("SELECT statute FROM defatty_stats WHERE statute=?",
                              (request.form['judge_statute_text'], )).fetchone()

    return render_template('judge.html',
                           judge_name=judge_name,
                           judge_statute_totals=judge_statute_totals,
                           judge_statute=judge_statute,
                           display=display
                           )
