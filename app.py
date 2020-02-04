from flask import Flask, render_template, request, Response
from wtforms import TextField, Form
from statute_search import statute_search
from judge_search import judge_search
import json
import csv


app = Flask(__name__)

# Dropdown
judge_last_name = ["DONNELLY_MP",
                   "ODONNELL_JP",
                   "MCCORMICK_T",
                   "VILLANUEVA_JA",
                   "SUSTER_R",
                   "SHEEHAN_BJ",
                   "MATIA_DT",
                   "TERRY_SJ",
                   "GAUL_D",
                   "BURNSIDE_JR",
                   "MCMONAGLE_RJ",
                   "AMBROSE_D",
                   "FUERST_NA",
                   "RUSSO_JJ",
                   "FRIEDLAND_CB",
                   "GALLAGHER_ET",
                   "MASON_L",
                   "CORRIGAN_PJ",
                   "PROGRAM_D",
                   "SAFFOLD_SS",
                   "SYNENBERG_J",
                   "SUTULA_JD",
                   "SUTULA_KA",
                   "GALLAGHER_EA",
                   "MCGINTY_TJ",
                   "FRIEDMAN_SA",
                   "MCCAFFERTY_BM",
                   "CORRIGAN_BJ",
                   "CALABRESE_DR",
                   "GALLAGHER_HL",
                   "MCDONNELL_NR",
                   "RUSSO_JD",
                   "RUSSO_MJ",
                   "MCCLELLAND_RC",
                   "RUSSO_NM",
                   "MCMONAGLE_TE",
                   "COURT_D",
                   "KOCH_JK",
                   "GALLAGHER_KA",
                   "BUTLER_AG",
                   "GALLAGHER_SM",
                   "KELLY_RP",
                   "Judge_2_NO",
                   "ASTRAB_M",
                   "BARKER_PA",
                   "ROOM_A",
                   "WILLIAMS_CC",
                   "CLANCY_M",
                   "JACKSON_ME",
                   "GALL_SE",
                   "INDERLIED_HF",
                   "SHAUGHNESSY_MP",
                   "MCMONAGLE_MA",
                   "REINBOLD_R",
                   "GREENE_LJ",
                   "TURNER_DM",
                   "MIDAY_S",
                   "HAGAN_E",
                   "MCGINTY_WT",
                   "COSGROVE_P",
                   "JONES_WC",
                   "CRAWFORD_D",
                   "KILBANE_A",
                   "GIBSON_J",
                   "Judge_1_NO", ]

# Gets names and returns list
with open('final_df.csv', 'r') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  for lines in csv_reader:
    new_names = lines[1]


class SearchForm(Form):
  autocomp = TextField('Type last name')


# Landing page
@app.route('/', methods=['GET', 'POST'])
def index():
  form = SearchForm(request.form.get('autocomp'))
  return render_template('home.html', form=form)


# After user inputs statute
@app.route('/statute', methods=['GET', 'POST'])
def statute():
  # orc_totals for database
  # FOR VALIDATION NEED TO KNOW THE TYPE
  return statute_search()


@app.route('/judge', methods=['GET', 'POST'])
def judge():
  # FOR VALIDATION NEED TO KNOW THE TYPE

  return judge_search()


@app.route('/_autocomplete', methods=['GET'])
def autocomplete():
  return Response(json.dumps(new_names), mimetype='application/json')


# GETS THE TOTAL NUMBER OF CASES FOR THAT STATUTE IN THE DATABASE
# judge_statute_totals = c.execute("SELECT atty_total FROM defatty_stats WHERE statute=?", (request.form['judge_statute_text'], ))
# display_judge_totals = len(judge_statute_totals.fetchall())
if __name__ == "__main__":
  app.run()
