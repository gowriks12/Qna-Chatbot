from typing import Set

from backend import get_chain, run_llm
import streamlit as st
from streamlit_chat import message

# chain = get_chain("PDF", ["ML concept cheat sheet.pdf"])

# def create_sources_string(source_urls: Set[str]) -> str:
#     if not source_urls:
#         return ""
#     sources_list = list(source_urls)
#     sources_list.sort()
#     sources_string = "sources:\n"
#     for i, source in enumerate(sources_list):
#         sources_string += f"{i+1}. {source}\n"
#     return sources_string


st.header("PDF Helper Bot")
if (
    "chat_answers_history" not in st.session_state
    and "user_prompt_history" not in st.session_state
    and "chat_history" not in st.session_state
    and "chain" not in st.session_state
):
    st.session_state["chat_answers_history"] = []
    st.session_state["user_prompt_history"] = []
    st.session_state["chat_history"] = []
    st.session_state.chain = None

with st.sidebar:
    st.subheader("Upload your Documents Here: ")
    pdf_files = st.file_uploader("Choose your PDF Files and Press OK", type=['pdf'], accept_multiple_files=True)

    if st.button("OK"):
        with st.spinner("Processing your PDFs..."):
            st.session_state.chain = get_chain(pdf_files)
            # chain = get_chain(pdf_files)

prompt = st.text_input("Prompt", placeholder="Ask anything to your PDFs...") or st.button(
    "Submit"
)

if prompt:
    with st.spinner("Generating response..."):
        # generated_response = run_llm(
        #     query=prompt, chat_history=st.session_state["chat_history"]
        # )
        generated_response = st.session_state.chain({"question": prompt, "chat_history": st.session_state.chat_history})
        formatted_response = (
            f"{generated_response['answer']}"
        )

        st.session_state.chat_history.append((prompt, generated_response["answer"]))
        st.session_state.user_prompt_history.append(prompt)
        st.session_state.chat_answers_history.append(formatted_response)

if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(
            user_query,
            is_user=True,
        )
        message(generated_response)
