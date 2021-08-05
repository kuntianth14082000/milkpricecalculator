from flask import Flask,request,render_template

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('webpage.html')

@app.route('/math',methods=['get','post'])
def cal():
    type=str(request.form['operation'])
    quantity=float(request.form['num1'])
    fat=float(request.form['num2'])
    if type=='Cow':
        import cow
        result=cow.cow(quantity,fat)
    else:
        import BUFFALO
        result=BUFFALO.BUFFALO(quantity,fat)
    return render_template('result.html',result=result)


if __name__=='__main__':
    app.run(debug=True)