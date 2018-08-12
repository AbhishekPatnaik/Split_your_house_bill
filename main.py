from flask import Flask, render_template, request
import datetime
import pandas as pd



app = Flask(__name__)



# creating a dataframe

df = pd.read_csv("data_{}.csv".format(datetime.date.today()))
abhi = list(df['abhishek'])
gajju = list(df['gajendra'])
shu = list(df['shubham'])
amit = list(df['amit'])
gau = list(df['gaurav'])
date = list(df['date'])
obj = list(df['objects'])
print(date)



@app.route('/')
def load_initial_page():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def bills_page():
    if request.form['select_all'] == 'on':
        price = int(request.form['price'])/5
        date.append(str(datetime.date.today()))
        abhi.append(price)
        shu.append(price)
        gajju.append(price)
        gau.append(price)
        amit.append(price)
        obj.append(str(request.form['what_did_u_buy']))
        df = pd.DataFrame({"date":date,'abhishek':abhi,"shubham":shu,"gajendra":gajju,"amit":amit,"gaurav":gau,"object":obj})
        print(df)
        df.to_csv("data_{}.csv".format(datetime.date.today()))
    df.to_csv("data.csv")
    return df.to_html(classes="table .table-bordered")


if __name__ == "__main__":
    app.run(debug=True)