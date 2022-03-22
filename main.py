import streamlit as st
import pandas as pd
import difflib

data = pd.read_csv('resultados.csv')



add_selectbox = st.sidebar.selectbox(
    "What demo would you like to see?",
    ("Code similarity", "Language identification")
)

input_number = st.number_input('Seleciona um indice', min_value=0, max_value=len(data))

if add_selectbox == 'Code similarity':

    col1, col2, col3, col4 = st.columns(4)

    original = data.iloc[input_number][['corpo']].values[0]
    most_similar = data.iloc[input_number][['most_similar']].values[0]
    similarity = data.iloc[input_number][['most_similar']].values[0]

    with col1:
        st.text("Original Code")
        st.text(original)

    with col2: 
        st.text("Most similar code")
        st.text(most_similar)

    with col3:
        st.text("Diff between code")
        init_text = ''
        for text in difflib.unified_diff(original.split("\n"), most_similar.split("\n")):
            if text[:3] not in ('+++', '---', '@@ '):

                if '+' in text[0]:
                    text = f"<p style='color: green'> {text} </p>"
                elif '-' in text[0]:
                    text = f"<p style='color: red'> {text} </p>"
        
                init_text = init_text + '\n' + text

        st.markdown(init_text, unsafe_allow_html=True)

        #st.text(init_text)

elif add_selectbox == 'Language identification':
    st.write("Language ID demo")