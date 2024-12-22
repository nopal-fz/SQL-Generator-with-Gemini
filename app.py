import streamlit as st
import os
import google.generativeai as genai
from config import GEMINI_API_KEY

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel('gemini-pro')

content = '''
    <div style="text-align: center;">
        <h1>SQL Generator App 🤖</h1>
        <h4>Makin Cepat Generate Query SQL dengan Bantuan AI ⚡⚡⚡</h3>
        <p>
            Website ini membantu Anda menghasilkan query SQL hanya dengan memberikan deskripsi dalam bahasa alami.
        </p>
        <p style="font-size: 12px; color: #666;">
            Model ini menggunakan <a href="https://cloud.google.com/generative-ai" target="_blank">Gemini AI</a>
        </p>
    </div>
'''

def add_footer():
    footer = '''
    <style>
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            font-size: 12px;
            color: #666;
            text-align: right;
        }
    </style>
    <div class="footer">
        Created by <a href="https://nopal-fz.github.io/Website-Personal/" target="_blank">Naufal Faiz</a>
    </div>
    '''
    st.markdown(footer, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title='SQL Query Generator 🔑', page_icon=':robot:')
    st.markdown(content, unsafe_allow_html=True)
    
    text_input = st.text_area('Enter your Query here:')

    submit = st.button('Generate SQL Query')

    if submit:
        if text_input.strip():
            with st.spinner('Generating SQL Query...'):
                template = '''
                    Buatlah kueri SQL berdasarkan teks berikut. Jika teks tidak relevan, jawab dengan pesan:
                    "Error: Input tidak relevan untuk membuat query SQL."

                    ```
                    {text_input}
                    ```

                    saya hanya ingin generate output nya kueri SQL!
                '''

                generate_template = template.format(text_input=text_input)

                try:
                    response = model.generate_content(generate_template)

                    if response and "Error:" in response.text:
                        st.error(response.text)
                    else:
                        st.success("Generate berhasil!, Hasil Query anda dibwah ini:")
                        sql_query = response.text
                        st.write(sql_query)


                        template_explain = '''
                            Jelaskan kueri SQL dibawah ini:

                            ```
                            {sql_query}
                            ```

                            tolong berikan penjelasan sederhananya dengan singkat dan jelas!
                        '''

                        generate_template_explain = template_explain.format(sql_query=sql_query)
                        response_explaination = model.generate_content(generate_template_explain)

                        st.success('Penjelasan dari hasil Query:')
                        explaination = response_explaination.text
                        st.markdown(explaination)

                except Exception as e:
                    st.error(f"Terjadi kesalahan: {str(e)}")
        else:
            st.error("Masukkan deskripsi Query terlebih dahulu!")

main()
add_footer()