import pickle
import streamlit as st
import pandas as pd

st.set_page_config(page_title='DNA Kingdom prediction')
st.title('DNA Kingdom prediction 👨‍🔬🧬')
st.subheader('Using Codon of diverse organisms 🔎 ')
 
upload_file=st.file_uploader('Choose a csv')
if upload_file is not None :
    data=pd.read_csv(upload_file)
    st.write(data)
    model = pickle.load(open("model/model.pkl", 'rb'))
    result=pd.DataFrame(model.predict(data))
    st.dataframe(result)

download=st.button('Download prediction')
if download:
  'Download Started!'
  csv = result.to_csv(index=False)
  b64 = base64.b64encode(csv.encode()).decode()  # some strings
  linko= f'<a href="data:file/csv;base64,{b64}" download="mushrooms_prediction.csv">Download csv file</a>'
  st.markdown(linko, unsafe_allow_html=True)
  st.text('--------------------Created By : Sabarinath K --------------------😊')
