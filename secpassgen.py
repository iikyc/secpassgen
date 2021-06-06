import streamlit as st
import random
import string

st.title("secpassgen")

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "@", "#", "$", "%", "^", "&"]

allowed_chars = []

password = []

st.sidebar.title("Secure Password Generator")
st.sidebar.subheader("Made By\nKaram - https://github.com/iikyc")

st.header("Options")

include_lowercase = st.checkbox("Include Lowercase Characters (a-z)")
include_uppercase = st.checkbox("Include Uppercase Characters (A-Z)")
include_numbers = st.checkbox("Include Numbers (0-9)")
include_symbols = st.checkbox("Include Symbols (! @ # $ % ^ &...)")

password_length = st.selectbox("Password Length", list(range(6, 29)))

generate_btn = st.button("Generate Password")

def pass_gen():

	if include_lowercase:
		Lowercase = True
		allowed_chars.extend(list(string.ascii_lowercase))
	if include_uppercase:
		Uppercase = True
		allowed_chars.extend(list(string.ascii_uppercase))
	if include_numbers:
		Numbers = True
		allowed_chars.extend(numbers)
	if include_symbols:
		Symbols = True
		allowed_chars.extend(symbols)

	if generate_btn:
		i = 0
		while (i < password_length):
			password.append(random.choice(allowed_chars))
			i += 1
try:
	pass_gen()

except IndexError:
	pass

password = "".join(password)

st.header("Output")

st.info(f"Password: {password}")
