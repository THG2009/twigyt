from flask import Flask, render_template, request
app = Flask(__name__)


def ferblatin(word: str):
    first_char = word[0]
    word = word[1:]
    final = f'{word}{first_char}erb'
    return final


def translate(word: str):
    words = word.split()

    modified_words = [ferblatin(word) for word in words]

    modified_sentence = ' '.join(modified_words)
    return modified_sentence


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/translated', methods=['POST'])
def translated():
    translated_word = request.form['input']
    return render_template('translated.html', word=translate(translated_word))


if __name__ == '__main__':
    app.run()
