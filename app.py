import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="", layout="centered")
st.title("Welcome to Saher Scientific Calculator")


if "calc_input" not in st.session_state:
    st.session_state.calc_input = ""

user_typed = st.text_input(
    "Type using your keyboard or click the button below:",
    value=st.session_state.calc_input,
    key="keyboard_field"
)

if user_typed != st.session_state.calc_input:
    st.session_state.calc_input = user_typed


def append_to_expression(val):
    st.session_state.calc_input += str(val)


def clear_all():
    st.session_state.calc_input = ""


def delete_last():
    st.session_state.calc_input = st.session_state.calc_input[:-1]


def calculate_result():
    expr = st.session_state.calc_input

    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    expr = expr.replace("sin", "np.sin")
    expr = expr.replace("cos", "np.cos")
    expr = expr.replace("tan", "np.tan")
    expr = expr.replace("log", "np.log10")
    expr = expr.replace("ln", "np.log")
    expr = expr.replace("^", "**")
    expr = expr.replace("√", "np.sqrt")
    expr = expr.replace("π", "np.pi")

    try:
        result = eval(expr)
        st.session_state.calc_input = str(result)

    except:
        st.session_state.calc_input = "Error"



buttons = [
    ["7", "8", "9", "DEL", "AC"],
    ["4", "5", "6", "×", "÷"],
    ["1", "2", "3", "+", "-"],
    ["0", ".", "π", "Ans", "="]
]

for row in buttons:

    cols = st.columns(5)

    for i, button in enumerate(row):

        with cols[i]:

            if button == "DEL":
                st.button(
                    button,
                    on_click=delete_last
                )

            elif button == "AC":
                st.button(
                    button,
                    on_click=clear_all
                )

            elif button == "=":
                st.button(
                    button,
                    on_click=calculate_result
                )

            elif button == "Ans":
                pass

            else:
                st.button(
                    button,
                    on_click=append_to_expression,
                    args=(button,)
                )