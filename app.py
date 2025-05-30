from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Global state (for demo only)
food_log = []
total_calories = 0

@app.route("/")
def index():
    return render_template("index.html", food_log=food_log, total_calories=total_calories)

@app.route("/add", methods=["POST"])
def add():
    global total_calories
    food = request.form.get("food")
    calories = request.form.get("calories")

    try:
        cal = int(calories)
        food_log.append({"food": food, "calories": cal})
        total_calories += cal
    except ValueError:
        pass

    return redirect(url_for("index"))

@app.route("/reset")
def reset():
    global food_log, total_calories
    food_log = []
    total_calories = 0
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
