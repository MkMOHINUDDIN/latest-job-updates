from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'Location' : 'Hyderabad',
        'qualification' : 'B.Tech',
        'Experience' : 'Freshers',
        'Batch' : '2023',
        'package' : '7 LPA'

    }, # type: ignore
    {
        'id' : 2,
        'title' : 'SDE',
        'Location' : 'Banglore',
        'qualification' : 'B.Tech',
        'Experience' : 'Freshers',
        'Batch' : '2023',
        'package' : '9 LPA'

    }, # type: ignore
    {
        'id' : 3,
        'title' : 'Data Associate',
        'Location' : 'Chennai',
        'qualification' : 'B.Tech',
        'Experience' : 'Freshers',
        'Batch' : '2023',
        'package' : '7 LPA'

    }, # type: ignore
    {
        'id' : 4,
        'title' : 'Backend Developer',
        'Location' : 'Mumbai',
        'qualification' : 'B.Tech',
        'Experience' : 'Freshers',
        'Batch' : '2023',
        'package' : '7 LPA'

    } # type: ignore
]

@app.route('/')  # decorator function, tells the app to route this url and do something with it when requested by a client (browser)
def First():
    return render_template('index.html',jobs = JOBS,company_name = 'MOBASA')

@app.route('/api/jobs')
def jobs_list():
    return jsonify(JOBS)
if __name__ == '__main__':
    app.run(debug=True)