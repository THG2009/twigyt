from flask import Flask, render_template, request
app = Flask(__name__)


def ferblatin_to_english(word: str):
    first_char = word[0]
    word = word[1:]
    final = f'{word}{first_char}erb'
    return final


def english_to_ferblatin(word: str):
    first_character = word[-4]
    entire_word = word[0:-4]
    final = f'{first_character}{entire_word}'
    return final


def translate(word: str):
    words = word.split()

    modified_words = [ferblatin_to_english(word) for word in words]

    modified_sentence = ' '.join(modified_words)
    return modified_sentence


def translate_to_english(word: str):
    words = word.split()

    modified_words = [english_to_ferblatin(word) for word in words]

    modified_sentence = ' '.join(modified_words)
    return modified_sentence


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/english')
def english():
    return render_template('english.html')


@app.route('/english/translated', methods=['POST'])
def english_translated():
    translated_word = request.form['input']
    return render_template('english_translated.html', word=translate_to_english(translated_word))


@app.route('/ferblatin')
def ferblatin():
    return render_template('ferblatin.html')


@app.route('/ferblatin/translated', methods=['POST'])
def ferblatin_translated():
    translated_word = request.form['input']
    return render_template('ferblatin_translated.html', word=translate(translated_word))


if __name__ == '__main__':
    app.run()
