from flask import Flask, render_template, request, send_file
import segno

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')


@app.route('/generate_qr_code', methods=['POST'])
def generate_qr_code():
  input = request.form['input_text']
  qr = segno.make(input)
  qr.save('qr.png', scale=10)
  return  send_file('./qr.png')


if __name__ == '__main__':
  app.run(debug=True)