import random
from flask import Flask, render_template, request
app = Flask(name)
@app.route('/', methods=['GET', 'POST'])
def play():
if request.method == 'POST':
answer = random.randint(1, 100)
guess = int(request.form['guess'])
attempts = 1
while guess != answer and attempts < 10:
if guess < answer:
result = "Your guess is too low. Guess again."
else:
result = "Your guess is too high. Guess again."
guess = int(request.form['guess'])
attempts += 1
if guess == answer:
result = "Congratulations! You guessed the number in {} attempts.".format(attempts)
else:
result = "Sorry, you did not guess the number within 10 attempts. The number was {}.".format(answer)
return render_template('index.html', result=result)
return render_template('index.html')
if name == 'main':
app.run(debug=True)
