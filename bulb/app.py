from flask import Flask,render_template,request
from forms import LoadUrl 
from newsparse import process_article

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'Tt=pS}Rm~jc5Z;6DTauPciO7QAmFv*'

@app.route('/')
def home():
    loadurl = LoadUrl()
    return render_template('home.html',form=loadurl) 


@app.route('/parse')
def parse():
    content_url = request.args['content_url']
    jdata = process_article(url=content_url)
    return render_template('parsed.html',jdata=jdata)


if __name__ == "__main__":
    app.run()