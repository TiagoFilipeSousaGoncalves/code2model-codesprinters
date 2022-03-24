# Imports
import streamlit as st
import pandas as pd
import difflib



# Load results .CSV
code_simil_results = pd.read_csv('results/resultados.csv')
prog_lang_results = pd.read_csv('results/resultados_language.csv')



# Create a select box to choose the demo
add_selectbox = st.sidebar.selectbox(
    "What demo would you like to see?",
    ("Code similarity", "Language identification")
)


# The input index of our data
input_number = st.number_input('Select an index', min_value=0, max_value=len(code_simil_results))


# Code similarity
if add_selectbox == 'Code similarity':
    st.write("Code similarity")

    col1, col2, col3 = st.columns(3)

    original = code_simil_results.iloc[input_number][['corpo']].values[0]
    most_similar = code_simil_results.iloc[input_number][['most_similar']].values[0]
    similarity = code_simil_results.iloc[input_number][['most_similar']].values[0]

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

        # st.text(init_text)



# Language identification
elif add_selectbox == 'Language identification':
    st.write("Language identification")

    col1, col2, col3 = st.columns(3)

    original_code = prog_lang_results.iloc[input_number][['corpo']].values[0]
    original_prog_lang = prog_lang_results.iloc[input_number][['platafor']].values[0]
    predicted_prog_lan = prog_lang_results.iloc[input_number][['platafor_predict']].values[0]


    with col1:
        st.text("Original Code")
        st.text(original_code)

    with col2: 
        st.text("Predicted Programming Language")
        st.text(predicted_prog_lan)
    
    with col3:
        st.text("Original Programming Language")
        st.text(original_prog_lang)
