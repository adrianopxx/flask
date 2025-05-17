from flask import Flask, request, render_template_string

app = Flask(__name__)

# Armazena o último nome enviado
last_name = ""

@app.route('/users', methods=['GET'])
def get_users():
    print("hello")
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Users</title>
            <meta http-equiv="refresh" content="5">
        </head>
        <body>
            <h1>Hello</h1>
            <p>Last submitted name: {{ name }}</p>
        </body>
        </html>
    """, name=last_name)

@app.route('/users', methods=['POST'])
def pega():
    global last_name
    data = request.get_json()
    name = data.get("name")
    print(name)
    last_name = name  # Armazena o nome para exibição
    return name

if __name__ == '__main__':
    app.run(debug=True)