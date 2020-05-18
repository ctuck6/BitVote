from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class WalletGeneratorForm(FlaskForm):
	name = StringField("Company name", validators=[DataRequired(), Length(max=50)])
	email = StringField("Email", validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Re-Enter Password", validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Generate Wallet")