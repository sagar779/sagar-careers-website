from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bangaluru, India',
    'Salary': 'RS.10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'Salary': 'RS.15,00,000 '
  },
  {
    'id': 3,
    'title': 'Frountend Engineer',
    'location': 'Remote',
    'Salary': 'RS.12,00,000 '
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Franscisco,USA',
    'Salary': '$150,000'
  },
]


@app.route("/")
def hello_sagar():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
