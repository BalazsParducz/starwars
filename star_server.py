from flask import Flask, render_template


app = Flask('starwas')


@app.route('/')
def main():
    return render_template('star_data.html')



def main():
    app.run(
        host="0.0.0.0",
        port=8888,
        debug=True
    )


if __name__ == '__main__':
    main()