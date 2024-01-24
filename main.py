from input.parse_pdf import get_pdf_text
from text_processor.text_chunking import get_chunk_text
from text_processor.vector_embed import get_vector_store
from chain_creation.conversationChain import get_conv_chain

def get_chain(input_type, input_files):
    text = ""
    if input_type == "PDF":
        text = get_pdf_text(input_files)

    chunks = get_chunk_text(text)
    vector_store = get_vector_store(chunks)
    chain = get_conv_chain(vector_store)
    return chain


if __name__ == "__main__":
    inp = "PDF"
    pdf_files = [""]
    chain = get_chain(inp, pdf_files)

