import streamlit as st
import pandas as pd

# Give your app a title
st.title("Streamlit Text Elements Demo")

# Header
st.header("This is a Header")

# Subheader
st.subheader("This is a Subheader")

# Markdown
st.markdown("# Header 1")
st.markdown("## Header 2")
st.markdown("### Header 3")

st.markdown("This is some **bold** text and this is *italic* text.")

# Caption
st.caption("This is a caption text.")

# Code block
st.code("print('Hello, Streamlit!')", language='python')
st.code("""def hello():
    return "Hello, Streamlit!\"""", language='python')

# Preformatted text
st.text("Preformatted text\n")

# LaTeX
st.latex("E = mc^2")

# Divider
st.text("Some text above the divider.")
st.divider()
st.text("Some text below the divider.")

#st.write
st.write("This is a simple text using st.write.")
st.write("# This is a header using st.write")
data = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
})
st.write(data)