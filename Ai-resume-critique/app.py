from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Resume Critique App"

if __name__ == "__main__":
    app.run(debug=True)

    print("MY NAME IS JASON")