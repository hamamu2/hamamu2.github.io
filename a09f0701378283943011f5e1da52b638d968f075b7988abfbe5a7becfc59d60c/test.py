@app.route("/")
def hello():
    tmp = 1+2
    return render_template('index.html', result = tmp)
