import sqlite3
import hashlib
import streamlit as st
from ProvaPython import ProvaPython

def display_username():
    # Fetch the username safely from session state
    username = st.session_state.get("username", "Guest")
    # Apply initcap (capitalize the first letter of each word)
    username = username.title()
    # Display the username in the header-style div
    st.markdown(
        f'<div style = "padding: 20px "class="header-style">Bem-vindo, {username}!</div>',
        unsafe_allow_html=True
    )

def get_hashed_password(password):
    """Hashes a password with SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password():
    """Returns `True` if the user has provided the correct username and password from the database."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect('databases/db_producao.db')
        cursor = conn.cursor()

        # Obter credenciais do formulário
        username = st.session_state["username"]
        password = st.session_state["password"]
        hashed_password = get_hashed_password(password)

        # Consulta SQL para verificar as credenciais
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        result = cursor.fetchone()

        if result:
            st.session_state["password_correct"] = True
            st.session_state["username"] = username  # Armazena o nome de usuário na sessão
            del st.session_state["password"]  # Não armazene a senha
        else:
            st.session_state["password_correct"] = False

        # Fechar a conexão com o banco de dados
        conn.close()

    # Retorna True se o nome de usuário e senha forem validados.
    if st.session_state.get("password_correct", False):
        return True

    # Exibir entradas para nome de usuário e senha.
    login_form()
    if "password_correct" in st.session_state and not st.session_state["password_correct"]:
        st.error("😕 User not known or password incorrect")
    return False

if not check_password():
    st.stop()

# Main Streamlit app starts here
username = st.session_state.get("username")  # Recupera o nome de usuário do estado da sessão
# Verificação para garantir que o usuário está autenticado
# if username is None:
#     st.error("Usuário não autenticado")
#     st.stop()
display_username()
ProvaPython()