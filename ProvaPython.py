import streamlit as st
from streamlit_option_menu import option_menu
from utils.functions import *
import sqlite3
from datetime import datetime

# Variaveis 

# Configuração da página
st.set_page_config(
    layout="centered",
    page_title="Prova Python",
    page_icon="static/favicon.ico",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': '# Bem-vindo ao teste de conhecimento Python! Este é um aplicativo *muito* útil.'
    }
)

def ProvaPython():

    """Checks whether a password entered by the user is correct."""
    conn = sqlite3.connect('databases/db_producao.db')

    # Configuração do menu horizontal
    selected = option_menu(
        None, ["Home", "registration_page"],
        icons=['house', 'cloud-upload'],
        menu_icon="cast", default_index=0, orientation="horizontal"
)
    # Importar e exibir a página selecionada
    if selected == "registration_page":
        ...
        # Importa e executa o conteúdo do arquivo 'home.py'
        #ProvaPythonPleno.show_page()  # Certifique-se de que o 'home.py' tem uma função 'show_page'
    
    st.title("Teste de conhecimento :blue[Python]") 
    st.divider()

    # Inicialize a pontuação
    if 'pontos' not in st.session_state:
        st.session_state.pontos = 0

    # Inicialize o estado da sessão
    if 'answered' not in st.session_state:
        st.session_state.answered = {}

    # Função para verificar se a pergunta já foi respondida
    def is_answered(pergunta):
        return st.session_state.answered.get(pergunta, False)

    # Função para processar a resposta
    def process_answer(pergunta, resposta_correta, resposta):
        if not is_answered(pergunta):  # Verifica se a pergunta ainda não foi respondida
            if resposta == resposta_correta:
                st.session_state.pontos += 1
            st.session_state.answered[pergunta] = True

    # Layout com colunas para uma apresentação mais responsiva
    col1, col2 = st.columns([3, 1])  # Proporções das colunas podem ser ajustadas

    with col1:

        # Pergunta 1
        pergunta = 1
        opcoes = ['bool, int, float', 'float, int, bool', 'int, float, bool', 'Nenhuma Alternativa está Correta']
        texto = f"""Qual o tipo de dado dos argumentos dentro da função print a seguir: \n
            print(11, 1.1, True)"""

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[2], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()

        # Pergunta 2
        pergunta = 2
        opcoes = ['//', "'#'", '"""e"""', 'Nenhuma Alternativa está Correta']
        texto = "Qual caractere é utilizado para criar comentários no seu código?"

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=is_answered(pergunta))

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[1], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()

        # Pergunta 3
        pergunta = 3
        opcoes = ['Luiz tem 23 anos', '23 tem Luiz anos', 'formato.format(nome,idade)', 'Nenhuma Alternativa está Correta']
        texto = """O que o código abaixo exibe? \n

        nome = "Luiz" 
    idade = 23 
    formato = '{1} tem {0} anos' 
    print(formato.format(nome, idade))"""

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            enviar_resposta(pergunta, opcoes[1], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()

        # Pergunta 4
        pergunta = 4
        opcoes = ['100', '300', '230', 'Nenhuma Alternativa está Correta']
        texto = """Qual o resultado da expressão abaixo (o valor de resultado): \n

        numero_1 = 10 
    numero_2 = 20 
    numero_3 = 30 

    resultado = numero_3 + numero_2 * numero_1
    print(resultado)
        """

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[2], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()

        # Pergunta 5
        pergunta = 5
        opcoes = ["'+'' faz adição para int e float; também faz concatenação entre strs", 
                "'*' faz multiolicação para int e float; também faz repetição quando usamos um int e str", 
                "'+' faz adição para int e float; tambem faz concatenação para int e str", 
                "'/' faz divisão e sempre retorna um numero de ponto flutuante"]
        texto = """Escolha a alternativa incorreta:"""

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio(f"{texto}", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            enviar_resposta(pergunta, opcoes[3], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")


        st.divider()

        # Pergunta 6
        pergunta = 6
        opcoes = ['Não tem como', 
                  'Da pra saber se um número é divisível por 2 usando o resto da divisão (%)',
                  'Da pra saber se um número é divisível por 2 usando a função format', 
                  'Da pra saber se um número é divisível por 2 usando f-strings']
        texto = f"""Como saber se um número é par ou ímpar?"""

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[1], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()
    
        # Pergunta 7
        pergunta = 7
        opcoes = ['11', '01', '10',  '00']
        texto = f"""Qual o resultado do código abaixo? \n
        variavel_a = 1 or 0 
    variavel_b = 0 or 1 
    print(variavel_a, variavel_a)"""

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[0], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()


       # Pergunta 8
        pergunta = 8
        opcoes = ['O nome Maria Carmo não tem espaços', 'O nome Maria Carmo tem espaços']
        texto = """Qual o resultado do código abaixo? \n
        nome = 'Maria Carmo'
    if ' ' in nome: 
        print(f'O nome {nome} tem espaços.') 
    else:  
        print(f'O nome {nome} NÃO tem espaços.')
        """

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[1], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()

       # Pergunta 9
        pergunta = 9
        opcoes = ['Número menor que 2', 
                  'Número menor que 3',
                  'Número maior que 3',
                  'Número menor que 1']
        texto = """É possível adicionar um if dentro de outro fazendo várias condições aninhadas. Com isso em mente, o que você acha que o código abaixo exibe na tela? \n
        numero = 10 
    if numero > 1:
        if numero > 2:
            if numero > 3: 
                print('Número maior que 3') 
            else: 
                print('Número menor que 3') 
        else: 
            print('Número menor que 2') 
    else: 
        print('Número menor que 1')  
        """

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[2], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()

       # Pergunta 10
        pergunta = 10
        opcoes = ['0 1 2 3 4 5 6 7 8 9', 
                  '1 2 3 4 5 6 7 8 9 10',
                  'um erro']
        texto = """O que o código abaixo exibiria na tela? \n
        start = 0 
    end = 10 
    while start < end: 
        print(start) 
        start += 1
        """

        st.write(f"**Questão {pergunta}:**")
        st.write(texto)

        # Verifica se a pergunta já foi respondida
        answered = is_answered(pergunta)

        # Verifica se a pergunta já foi respondida
        resposta = st.radio("Escolha a resposta:", opcoes, key=f"resposta_{pergunta}", disabled=answered)

        # Botão para enviar a resposta
        botao_enviar = st.button("Enviar Resposta", key=f"send_{pergunta}", disabled=answered)

        # Verifique se o botão foi clicado e a pergunta ainda não foi respondida
        if botao_enviar and not answered:
            # Atualiza o estado para indicar que a pergunta foi respondida
            st.session_state.answered[pergunta] = True

            # Processa a resposta
            # Substitua "opcoes[2]" pela lógica correta para identificar a resposta certa
            enviar_resposta(pergunta, opcoes[0], resposta)

            # Exibe uma mensagem de sucesso
            st.success("Resposta enviada com sucesso!")

        st.divider()



        if st.button("Finalizar Prova"):
            
            acertos = st.session_state.pontos
            percentual_acerto = f"{acertos / pergunta * 100:.2f}%"
            
            #update_result(conn, username, pergunta, acertos, percentual_acerto)

            # Exibir resultado da prova
            st.balloons()  # Efeito visual (balões)
            st.success(f"Você acertou {st.session_state.pontos} de {pergunta} questões!")

            # Mensagem condicional baseada no resultado
            if st.session_state.pontos == pergunta:
                st.info(f"Parabéns, você acertou {percentual_acerto} das questões!")
            elif st.session_state.pontos > 2:
                st.warning(f"Bom trabalho, você acertou {percentual_acerto} das questões!")
            else:
                st.error(f"Que pena, você acertou somente {percentual_acerto} das questões!. Tente novamente!")
# # with col2:

    # Exibe o resultado final
    # percentual_acerto = f"{st.session_state.pontos / pergunta * 100:.2f}%"
    # dados = {"Percent Acertos": percentual_acerto}
    # st.button(f"Seu Resultado foi {dados}")

    # Exibindo como um DataFrame
    # st.sidebar.write("Dados de desempenho:")
    # st.sidebar.write(dados)

    if st.button("Logout"):
        st.session_state["current_page"] = "login"
        st.session_state["password_correct"] = False
        st.experimental_set_query_params(page="login_app")
        st.experimental_rerun()  # Recarrega a página para aplicar o redirecionamento


