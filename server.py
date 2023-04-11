from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(1, 9)

@app.route("/")
def title():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media2.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif?cid=ecf05e47qgqnrkki1r2vyq1pu5dddcvty18jduzr84qe3ctk&rid=giphy.gif&ct=g'>"



@app.route("/<int:number>")
def check_number(number):
    if number > random_num:
        return "<h1 style='color: red'>Too high, try again!</h1>" \
               "<img src='https://media4.giphy.com/media/BKEpUonHHnduM/giphy.gif?cid=ecf05e476zoby36slbvy2wjevunr304rqfvjer7uu1jx2hma&rid=giphy.gif&ct=g'>"
    elif number < random_num:
        return "<h1 style='color: purple'>Too low, try again!</h1>" \
               "<img src='https://media3.giphy.com/media/3NTLIaLazVGH6/giphy.gif?cid=ecf05e471ytssu0vnewthb06l6bjhnix0j8obe9ensdb6e1i&rid=giphy.gif&ct=g'>"
    else:
        return "<h1 style='color: green'>You got it champ!</h1>" \
               "<img src='https://media0.giphy.com/media/26xBubJU1XbjpewPC/giphy.gif?cid=ecf05e474853f6g37jngcoq1jjpau2c7g2ewv56iuqtsm0cv&rid=giphy.gif&ct=g'>"

if __name__ == '__main__':
    app.run(debug=True)