from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        lines_to_process = int(request.form['lines_to_process'])
        prompt = request.form['prompt']
        # İşleme mantığını buraya ekleyin
        result = process_prompt(lines_to_process, prompt)
        return render_template('ask.html', result=result)
    return render_template('ask.html')

def process_prompt(lines_to_process, prompt):
    # Örnek işlem: promptu satır sayısı kadar tekrarlamak
    processed_result = (prompt + '\n') * lines_to_process
    return processed_result

if __name__ == '__main__':
    app.run(debug=True)
