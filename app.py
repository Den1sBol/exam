from flask import Flask
app = Flask(__name__)

@app.route('/')

def program(a0, d, n):
    if n == 1:
        return a0
    else:
        return program(a0, d, n - 1) + d

def prog(a0, d, n):
    if n == 1:
        return a0
    else:
        return program(a0, d, n) + prog(a0, d, n - 1)

print(program(1, 4, 5))
print(prog(1, 4, 5))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')