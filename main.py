from flask import Flask
import random

# Create a variable to store the correct value that will be evaluated against
random_number = random.randint(0, 9)
print(random_number)


app = Flask(__name__)

# This route will be the start of the web page. It will contain the initial question
@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src=https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm1zanN3bTAwM3VieHQ4Zmp0cGJ5NGZ1aWVzNTZ5cGl4eGh4MnVxaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.gif>"



@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
                "<img src=https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGl1ejVkbDhlZjRncG0zczkyMmg3OWMyMTZ5ZmxzeXJwZTRvenJwbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YKroe55zFMIwpmBCu6/giphy.gif>"

    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
                "<img src=https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYm9sd3Q4em04bHR5Ynh6bGY2emhhZGYwd3R4N2oxY245YTZzaHFueiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oEduPoyJdFYgHx7YQ/giphy.gif>"

    else:
        return "<h1 style='color: green'>You found Me</h1>" \
                "<img src=https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXRvNzdoN2h2ZGxpcDUyZWlhN2htb3g0anRhMGoxZTU0MzNlMTB5biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XkGXBa01dxNIvjAJHl/giphy.gif>"


if __name__ == "__main__":
    app.run(debug=True)
