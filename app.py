from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True



@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/item/<string:item>',methods=['GET'])
def isbn(item):
    return item
    
if __name__ == "__main__":
    app.run(debug=True)
