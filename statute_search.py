import sqlite3
from flask import request, render_template


def statute_search():
    conn = sqlite3.connect('sample.sqlite')
    c = conn.cursor()
    request.form['statute_text']
    statute_display = c.execute("SELECT statute  FROM final_df WHERE statute=?",
                                (request.form['statute_text'], )).fetchone()
    statute_total = c.execute("SELECT stat_totals FROM final_df WHERE statute=?",
                              (request.form['statute_text'], )).fetchone()
    conn.close()
    return render_template('statute.html',
                           statute_display=statute_display,
                           statute_total=statute_total)
