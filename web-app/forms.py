from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, SubmitField, IntegerField,TextAreaField,RadioField,SelectField, DecimalField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import InputRequired
from wtforms.validators import NumberRange


class PredictForm(FlaskForm):
   check_account = SelectField('Check_Account ', choices = ['A11', 'A12', 'A13', 'A14'])
   duration = IntegerField('Duration', [NumberRange(min=0), InputRequired() ])
   credit_history = SelectField('Credit_history', choices = ['A30', 'A31', 'A32', 'A33', 'A34'])
   purpose = SelectField('Purpose', choices = ['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47', 'A48', 'A49', 'A410'])
   credit_amount  = IntegerField('Credit amount ', [NumberRange(min=0), InputRequired() ])
   saving_account = SelectField('Saving_account',  choices = ['A61', 'A62', 'A63', 'A64', 'A65'])
   employment = SelectField('Employment', choices = ['A71', 'A72', 'A73', 'A74', 'A75'])
   install_rate = IntegerField('Install_rate', [NumberRange(min=0), InputRequired() ])
   personal_status = SelectField('Personal_status', choices = ['A91', 'A92', 'A93', 'A94', 'A95'])
   other_debrotors = SelectField('Other_debrotors', choices = ['A101', 'A102', 'A103'])
   present_residence = IntegerField('Present_residence', [NumberRange(min=0), InputRequired() ])
   property = SelectField('Property', choices = ['A121', 'A122', 'A123', 'A124'])
   age = IntegerField('Age', [NumberRange(min=0), InputRequired() ])
   installment_plant = SelectField('Installment_plant', choices = ['A141', 'A142', 'A143'])
   housing = SelectField('Housing', choices = ['A151', 'A152', 'A153'])
   num_credits = IntegerField('Num_credits', [NumberRange(min=0), InputRequired() ])
   job = SelectField('Job', choices = ['A171', 'A172', 'A173', 'A174'])
   num_dependents = IntegerField('Num_dependents', [NumberRange(min=0), InputRequired() ])
   telephone = SelectField('Telephone', choices = ['A191', 'A192'])
   foreign = SelectField('Foreign', choices = ['A201', 'A202'])
   submit = SubmitField('Result')

   abc = "" # this variable is used to send information back to the front page
