import streamlit as st

st.set_page_config(
    page_title="Character Counter",
    page_icon=""
)

st.title("Character Counter")
st.write("Find how many times a specific character appears in a sentence.")

sentence = st.text_area("📝 Enter your sentence:")

specific_character = st.text_input(
    "🔎 Enter a character:",
    max_chars=1
)

if st.button("Count Occurrences", use_container_width=True):

    if sentence and specific_character:
        count = sentence.count(specific_character)

        st.subheader("📊 Result")
        st.metric(
            label=f"Occurrences of '{specific_character}'",
            value=count
        )

    else:
        st.warning("Please enter both a sentence and a character.")
