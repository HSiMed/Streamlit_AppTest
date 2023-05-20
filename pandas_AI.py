import pandas as pd
from pandasai import PandasAI
import streamlit as st

st.title('OpenAI')
st.write('PandasAI is a conversational AI that can answer questions about your data. It is powered by OpenAI\'s GPT-3.')

file = st.file_uploader('Upload a CSV file', type=['csv'])

# Sample DataFrame
#df = pd.DataFrame({
#    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia",
#                "Japan", "China"],
#    "gdp": [19294482071552, 2891615567872, 2411255037952, 3435817336832, 1745433788416, 1181205135360, 1607402389504,
#            1490967855104, 4380756541440, 14631844184064],
#    "happiness_index": [6.94, 7.16, 6.66, 7.07, 6.38, 6.4, 7.23, 7.22, 5.87, 5.12]
#})

# Instantiate a LLM
from pandasai.llm.openai import OpenAI

# llm = OpenAI(api_token="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")
llm = OpenAI(api_token="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")

#pandas_ai = PandasAI(llm, conversational=False)
#response = pandas_ai(df, prompt='Which are the 5 saddest countries? ')

#print(response)

question = st.text_input('Ask a question about your data')

if file is not None:
    df = pd.read_csv(file)
    st.write(df)

if st.button('Ask') and file is not None:
    pandas_ai = PandasAI(llm, conversational=False)
    with st.spinner('Thinking......'):
        response=pandas_ai(df,prompt=question)
        st.write(response)