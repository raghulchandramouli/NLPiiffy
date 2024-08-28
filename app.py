### Backend pKgs
import streamlit as st

### NLP Pkgs
import spacy
from textblob import TextBlob

### Text_analyzer (used for Tokens & Lemmas):
def text_analyzer(my_text):
    nlp = spacy.load('en_core_web_sm')  # Use the correct model name
    docx = nlp(my_text)
    allData = [('"Token": {},\n"Lemma": {}'.format(token.text, token.lemma_)) for token in docx]
    return allData

### Entity Analyzer (NER):
def entity_analyzer(my_text):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(my_text)
	tokens = [ token.text for token in docx]
	entities = [(entity.text,entity.label_)for entity in docx.ents]
	allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
	return allData

def main():
    """NLP APPS STARTS HERE"""
    st.title("NLPiffy it")
    st.subheader("A toolkit for Natural Processing on the Go!!!")

    # Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize Your Text")

        message = st.text_area("Enter Text", "Type Here ..")
        if st.button("Analyze"):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)

    # Named Entity Recognition:
    if st.checkbox("Show Named Entities"):
        st.subheader("Analyze Your Text")

        message = st.text_area("Enter Text", "Type Here ..")
        if st.button("Extract"):
            entity_result = entity_analyzer(message)
            st.json(entity_result)
    
    
    # Sentiment Analysis
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Show Sentiment present in your Text")
        
        message = st.text_area("Enter your Text", "Type Here")
        if st.button("Analyze"):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)
        
        
if __name__ == '__main__':
    main()
