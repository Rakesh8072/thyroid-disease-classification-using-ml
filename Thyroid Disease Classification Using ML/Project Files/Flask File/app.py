import pickle
pickle.dumb(sv1,open('thyroid_1_model.pk1','wb'))
from flask import flask, render_template, request
import numpy as np
import pickle
import pandas as pd
model = pickle.load(open(r"C:\Users\SmartBridge-PC\Downloads\Thyroid1_model.pkl",'rb'))
le = pickle.load(open("label_encoder.pkl",'rb'))

app = Flask(__name__)
@app.route("/")
def about():
    return render_template('home.html')
@app.route("/pred", methods=['POST','GET'])
def predict():
    x = [[float(x) for x in request.form.values()]]

    print(x)
    col = ['goitre','tumor','hypopituitary','psych','TSH','T3','TT4','T4U','FTI','T&G']

    x= pd.DataFrame(x, columns=col)

    print(x)
    pred = model.predict(x)
    pred = le.inverse_transform(pred)
    print(pred[0])
    return render_template('submit.html',predition_text=str(pred))
if__name__=="__main__":
app.run(debug=False)
