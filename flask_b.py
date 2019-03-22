from flask import Flask,render_template
import finder
app = Flask(__name__)

@app.route('/')
def listed():
	hosp=finder.Name
	addr=finder.Address
	return render_template('home.html',list1=hosp,list2=addr)

if __name__=='__main__':
	app.run(debug=True)