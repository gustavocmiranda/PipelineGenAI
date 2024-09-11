import streamlit as st
from contrato import Vendas
from datetime import datetime
from pydantic import ValidationError
from database import salvar_no_postgres

def main():

    st.title('Sistema de CRM e Vendas da ZapFlow - Frontend simples')

    email = st.text_input('Email do vendedor')
    data = st.date_input('Data em que a venda foi realizada', value='today')
    hora = st.time_input('Hora em que a venda foi realizada')
    valor = st.number_input('Valor da venda')
    qtd = st.number_input('Quantidade de produtos')
    produto = st.selectbox('Produto vendio', options=['ZapFlow com Gemini', 'ZapFlow com ChatGPT', 'ZapFlow com Llama3.0'])


    if st.button('Salvar'):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                qtd = qtd,
                produto = produto)
            
            st.write('**Dados da Venda:**')
            st.write(venda)
            salvar_no_postgres(venda)

        except ValidationError as e:
            st.error(e)

            


if __name__=='__main__':
    main()