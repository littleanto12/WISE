from flask import Flask

app = flask()

def index():
    return ("Todo List")

if __name__ == '__main__':
    app.run(debug = True)
