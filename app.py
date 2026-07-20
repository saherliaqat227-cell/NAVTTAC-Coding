import streamlit as st
import math

st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")
st.title("Welcome to Saher Scientific Calculator")


if "calc_input" not in st.session_state:
    st.session_state.calc_input = ""



def calculate_result():
    expr = st.session_state.calc_input


    expr = expr.replace("×", "*")
    expr = expr.replace("÷", "/")
    expr = expr.replace("^", "**")
    expr = expr.replace("π", "math.pi")
    expr = expr.replace("√(", "math.sqrt(")


    expr = expr.replace("sin(", "math.sin(math.radians(")
    expr = expr.replace("cos(", "math.cos(math.radians(")
    expr = expr.replace("tan(", "math.tan(math.radians(")


    open_radians = expr.count("math.radians(")
    if open_radians > 0:
        expr += ")" * open_radians

    open_sqrt = expr.count("math.sqrt(")
    close_brackets = expr.count(")")
    if open_sqrt > (close_brackets - open_radians):
        expr += ")" * (open_sqrt - (close_brackets - open_radians))

    try:
        if expr.strip() == "":
            return
        result = eval(expr, {"math": math, "__builtins__": {}})
        if isinstance(result, float):
            result = round(result, 10)
        st.session_state.calc_input = str(result)
    except Exception:
        st.session_state.calc_input = "Error"



def append_to_expression(val):
    if st.session_state.calc_input == "Error":
        st.session_state.calc_input = ""

    if val in ["sin", "cos", "tan", "√"]:
        st.session_state.calc_input += f"{val}("
    else:
        st.session_state.calc_input += str(val)


def clear_all():
    st.session_state.calc_input = ""


def delete_last():
    st.session_state.calc_input = st.session_state.calc_input[:-1]



with st.form(key="calculator_form", clear_on_submit=False):

    user_input = st.text_input(
        "Display Screen (Type or use buttons, then click '=' or press Enter):",
        value=st.session_state.calc_input
    )


    submitted = st.form_submit_button("Calculate via Keyboard", help="Or just click '=' button below")

    if submitted:
        st.session_state.calc_input = user_input
        calculate_result()
        st.rerun()


buttons = [
    ["7", "8", "9", "DEL", "AC"],
    ["4", "5", "6", "×", "÷"],
    ["1", "2", "3", "+", "-"],
    ["0", ".", "π", "(", ")"],
    ["sin", "cos", "tan", "√", "="]
]

for r_idx, row in enumerate(buttons):
    cols = st.columns(len(row))
    for c_idx, button in enumerate(row):
        with cols[c_idx]:
            b_key = f"btn_{r_idx}_{c_idx}_{button}"

            if button == "DEL":
                if st.button(button, key=b_key, use_container_width=True):
                    delete_last()
                    st.rerun()
            elif button == "AC":
                if st.button(button, key=b_key, use_container_width=True):
                    clear_all()
                    st.rerun()
            elif button == "=":
                if st.button(button, key=b_key, type="primary", use_container_width=True):

                    st.session_state.calc_input = user_input
                    calculate_result()
                    st.rerun()
            else:
                if st.button(button, key=b_key, use_container_width=True):
                    st.session_state.calc_input = user_input
                    append_to_expression(button)
                    st.rerun()
