import sys
import os
import streamlit as st
import base64
import sqlite3
from datetime import datetime

def fn_lista_opcoes(opcoes, pergunta, texto) :

    # print (f"\n🔢 Questão de numero {pergunta}:")
    # print(f"""\n 📜 {texto} \n""")
    
    text = ""
    # Itera sobre as opções, formatando cada uma
    for i, resposta in enumerate(opcoes, start=1):
        # Adiciona a opção à string acumulada, formatada corretamente
        text += f"{i}) {', '.join(resposta)}\n"
    
    # Retorna o texto formatado
    return text


def fn_valida_resposta(opcoes, resposta_certa):
    # Inicializa a variável para armazenar a escolha do usuário
    escolha_valida = False
    tentativa = 1

    # Loop até que o usuário faça uma escolha válida
    while not escolha_valida:
        # Solicitar ao usuário que faça uma escolha
        escolha = input(f"\nDigite uma das opções de 1 até {len(opcoes)}: ") 

        # Verificar se a escolha é válida
        if escolha.isdigit():  # Verifica se a entrada é um número
            escolha = int(escolha)
            if 1 <= escolha <= len(opcoes):
                escolha_valida = True  # A escolha é válida, saímos do loop
                if escolha == int(resposta_certa):
                    print("\n\u2714 Acertou !! \n")
                    return 1 
                else:
                    print("\n\u2716 Resposta errada !!\n")
            else:
                sys.stdout.write(f"Tentativa {tentativa}: Por favor, digite um número de 1 até {len(opcoes)}.   \r")
                sys.stdout.flush()
                os.system("clear")
                fn_lista_opcoes(opcoes)
                print(f"\n *** Atenção Tentativa {tentativa} de 10 ...")
        else:
            sys.stdout.write(f"Tentativa {tentativa}: Por favor, digite um número de 1 até {len(opcoes)}.   \r")
            sys.stdout.flush()
            os.system("clear")
            fn_lista_opcoes(opcoes)
            print(f"\n *** Atenção Tentativa {tentativa} de 10 ...")

        tentativa += 1
        if tentativa > 3:
            print("\n Excedeu limite de Tentativas \n ")
            return

# Função para desativar o botão após a resposta
def enviar_resposta(pergunta, resposta_certa, resposta_usuario):
    if resposta_usuario == resposta_certa:
        st.write("\n✔ Acertou!")
        st.session_state.pontos += 1
    else:
        st.write("\n✖ Resposta errada!")
    
    # Desativa o botão para a pergunta após o envio
    st.session_state[f'answered_{pergunta}'] = True

def criar_card(titulo, conteudo):
    return f"""
    <div style="
        border: 1px solid #ddd; 
        border-radius: 5px; 
        padding: 15px; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
        background-color: #f9f9f9;
        width: 200px;">
        <h3 style="margin: 0; font-size: 18px; color: #333;">{titulo}</h3>
        <p style="font-size: 24px; color: #007bff; margin-top: 10px;">{conteudo}</p>
    </div>
    """


# Função para adicionar CSS personalizado
def add_css():
    st.markdown(
        """
        <style>
        .header-style {
            position: absolute;
            right: 0;
            top: 0;
            padding: 10px 20px;
            font-size: 16px;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Função para exibir o nome de usuário
def display_username():
    if "username" in st.session_state:
        username = st.session_state["username"]
        st.markdown(
            f'<div class="header-style">Bem-vindo, {username}!</div>',
            unsafe_allow_html=True
        )

def display_username(username):

    # HTML com formatação e estilo CSS para a mensagem de boas-vindas
    welcome_message = f"""
            <style>
                .welcome-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    width: 130%; /* Aumenta a largura do contêiner */
                    margin-left: -100px;
                    max-width: 900px;  Define uma largura máxima para melhor visualização */
                    height: 80px;
                    background-color: #f0f2f6;
                    border-radius: 10px;
                    margin-top: 20px;
                    margin-botton: 30px;
                    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                }}
                .welcome-text {{
                    font-size: 24px;
                    color: #333333;
                    font-family: 'Arial', sans-serif;
                    text-align: center;
                    margin: 0;
                    padding: 10px;
                }}
                .username {{
                    color: #007BFF;
                    font-weight: bold;
                }}
            </style>
            <div class="welcome-container">
                <p class="welcome-text">Bem-vindo(a), <span class="username" style="text-transform: capitalize;">{username}</span></p>
            </div>
        """

    st.html(
        f"<p><span>{welcome_message}</span></p>"
    )

# Função para converter imagem em base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


# Função para inserir novo usuário no banco de dados
def send_result(conn, username):
    try:
        cursor = conn.cursor()
        current_datetime = datetime.now()
        cursor.execute("insert into result (username, datahora) VALUES (?, ?)", (username, current_datetime))
        conn.commit()
        return username 
    
    except sqlite3.IntegrityError:
        return False
    return True


def update_result(conn, username, pergunta, acertos, percentual_acerto):

    cursor = conn.cursor()
    sql = f""" update result 
                set qtd_perguntas = '{pergunta}',
                    qtd_acertos = '{acertos}', 
                    percentual = '{percentual_acerto}' 
                where username = '{username}' """

    # Executar a instrução SQL
    cursor.execute(sql)