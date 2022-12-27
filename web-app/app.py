from flask import Flask, url_for, render_template, redirect
from forms import PredictForm
from flask import request, sessions
import requests
from flask import json
from flask import jsonify
from flask import Request
from flask import Response
import urllib3
import json
# from flask_wtf import FlaskForm

app = Flask(__name__, instance_relative_config=False)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'development key' #you will need a secret key

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')

@app.route('/', methods=('GET', 'POST'))

def startApp():
    form = PredictForm()
    return render_template('index.html', form=form)

@app.route('/predict', methods=('GET', 'POST'))
def predict():
    form = PredictForm()
    if form.submit():

        # NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
        # curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=OQZaBAM5wuy4cUEs2XQrJ8OXBWlJCBkKhRIADXXHYDYE'
        header = {'Content-Type': 'application/json', 'Authorization': 'Bearer '
                 + "eyJraWQiOiIyMDIyMTIxMjA4MjkiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJJQk1pZC02NjQwMDQyRDBVIiwiaWQiOiJJQk1pZC02NjQwMDQyRDBVIiwicmVhbG1pZCI6IklCTWlkIiwianRpIjoiODQ0NDYzNGQtNGE4Ni00YTg2LTkyNTUtYTdlNWI1Njc5MDI0IiwiaWRlbnRpZmllciI6IjY2NDAwNDJEMFUiLCJnaXZlbl9uYW1lIjoiTmFtIiwiZmFtaWx5X25hbWUiOiJIb2FuZyIsIm5hbWUiOiJOYW0gSG9hbmciLCJlbWFpbCI6Im4xOWRjY24xMTRAc3R1ZGVudC5wdGl0aGNtLmVkdS52biIsInN1YiI6Im4xOWRjY24xMTRAc3R1ZGVudC5wdGl0aGNtLmVkdS52biIsImF1dGhuIjp7InN1YiI6Im4xOWRjY24xMTRAc3R1ZGVudC5wdGl0aGNtLmVkdS52biIsImlhbV9pZCI6IklCTWlkLTY2NDAwNDJEMFUiLCJuYW1lIjoiTmFtIEhvYW5nIiwiZ2l2ZW5fbmFtZSI6Ik5hbSIsImZhbWlseV9uYW1lIjoiSG9hbmciLCJlbWFpbCI6Im4xOWRjY24xMTRAc3R1ZGVudC5wdGl0aGNtLmVkdS52biJ9LCJhY2NvdW50Ijp7ImJvdW5kYXJ5IjoiZ2xvYmFsIiwidmFsaWQiOnRydWUsImJzcyI6Ijk4ZDJkMDM3NDkxYzRhODY4ZDVkMjViZTgzODEyZDQ4IiwiZnJvemVuIjp0cnVlfSwiaWF0IjoxNjcyMTMzMjI2LCJleHAiOjE2NzIxMzY4MjYsImlzcyI6Imh0dHBzOi8vaWFtLmNsb3VkLmlibS5jb20vaWRlbnRpdHkiLCJncmFudF90eXBlIjoidXJuOmlibTpwYXJhbXM6b2F1dGg6Z3JhbnQtdHlwZTphcGlrZXkiLCJzY29wZSI6ImlibSBvcGVuaWQiLCJjbGllbnRfaWQiOiJkZWZhdWx0IiwiYWNyIjoxLCJhbXIiOlsicHdkIl19.A6xMbVXFwGVoV24YjdvBZe1eoQsiUSW-sAoYCID8D1csXHmzQzZTCCcA-vo03afjxFKehfonbQ5n8XI5A4jN9QrHCixDbVsFpqXOCs0AlDoH5VWZdzlo6t43bWwjVvU7d3AiexPlrcNwPvOWoTnkneRiqpahoywmSYun5ayPc80djGzvg_AkdfMmDjklQ2wW3SP43ITCGXkcHHt9AQhJBAOIHQz2MA90fgzJu7BqpY6EfzJIEvZUNWgYV7DjrAo1pnrwe8VL_7vduwFsv-LgFa9br2LeYs8No-JvmOSFPGpD7Z_T94a9RF46PLieOow3OKCFVKxSWI346r0stkHlmw"}

        python_object = [form.check_account.data, form.duration.data, form.credit_history.data,
                         form.purpose.data, form.credit_amount.data, form.saving_account.data,
                         form.employment.data, form.install_rate.data, form.personal_status.data,
                         form.other_debrotors.data, form.present_residence.data, form.property.data,
                         form.age.data, form.installment_plant.data, form.housing.data,
                         form.num_credits.data, form.job.data, form.num_dependents.data,
                         form.telephone.data, form.foreign.data]
        userInput = []
        userInput.append(python_object)
        print(userInput)
        # NOTE: manually define and pass the array(s) of values to be scored in the next line
        payload_scoring = {"input_data": [{"fields": ['Check_Account ', 'Duration', 'Credit_history', 'Purpose',
       'Credit amount ', 'Saving_account', 'Employment', 'Install_rate',
       'Personal_status', 'Other_debrotors', 'Present_residence', 'Property',
       'Age', 'Installment_plant', 'Housing', 'Num_credits', 'Job',
       'Num_dependents', 'Telephone', 'Foreign', 'Result'], "values": userInput }]}

        response_scoring = requests.post("https://us-south.ml.cloud.ibm.com/ml/v4/deployments/pipeline_credit_data/predictions?version=2022-12-16", json=payload_scoring, headers=header)
        print(response_scoring)
        output = json.loads(response_scoring.text)
        print(output)
        for key in output:
          ab = output[key]
        
        
        for key in ab[0]:
          bc = ab[0][key]
        
        roundedResult = round(bc[0][0],2)
        print(roundedResult)
  
        form.abc = roundedResult # this returns the response back to the front page
        return render_template('index.html', form=form)