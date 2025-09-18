import streamlit as st

st.title("Valit2 Calculator App")
st.info("In order to use this calculator you need to be of age...!")

name = st.text_input("Please tell me what is your name?")
age = st.number_input("Please enter your age:", min_value=0, step=1)

if name and age:
    st.write("Currently checking and reviewing user's identity files and legal identity...")
    if age >= 13:
        st.success(f"You are {age} years old meaning you are eligible to proceed, {name}!")
    else:
        st.error(f"I am very sorry but you are currently not old enough to proceed, {name}")

    access_code1 = st.radio("Do you have an Admin access code?", ("Yes", "No"))
    if access_code1 == "Yes":
        access_code2 = st.number_input("Please enter your Admin access code:", min_value=0, step=1)
        if access_code2:
            if access_code2 != 1243:
                st.warning("You are not authorized to proceed to the Admin location")
            else:
                st.success("You are now authorized to proceed to the Admin location")
                look = st.text_input("What are you looking for? (one word only!)")
                if look:
                    if look != "Tablet":
                        st.info("I have no idea where it is...")
                    else:
                        st.success(f"It is with Amma! okay {name}?")

    if name != "Suveer" and age >= 13:
        st.info("Alright, we will now proceed to the calculator....!")
        op = st.selectbox("Enter the operation you want to perform:", ["Add", "Subtract", "Multiply", "Divide"])
        n1 = st.number_input("Please enter your first number:")
        n2 = st.number_input("Please enter the second number:")
        if st.button("Calculate"):
            if op == "Add":
                n3 = n1 + n2
                st.success(f"{n1} + {n2} = {n3}")
            elif op == "Multiply":
                n3 = n1 * n2
                st.success(f"{n1} x {n2} = {n3}")
            elif op == "Divide":
                if n2 == 0:
                    st.error("Your answer is 'undefined'")
                else:
                    n3 = n1 / n2
                    st.success(f"{n1} / {n2} = {n3}")
            elif op == "Subtract":
                n3 = n1 - n2
                st.success(f"{n1} - {n2} = {n3}")
