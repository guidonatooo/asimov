from time import sleep

import streamlit as st
import pandas as pd

from crud import (
    le_todos_usuarios,
    cria_usurios,
    modifica_usuario,
    deleta_usuario
    )

def login():
    usuarios = le_todos_usuarios()
    usuarios = {usuario.nome: usuario for usuario in usuarios}
    with st.container(border=True):
        st.markdown('Bem-vindos ao AppFerias')
        nome_usuario = st.selectbox(
            'Selecione o seu usuário',
            usuarios.keys()
            )
        senha = st.text_input('Digite sua senha', type='password')
        if st.button('Acessar'):
            usuario = usuarios[nome_usuario]
            if usuario.verifica_senha(senha):
                st.success('Login efetuado com sucesso')
                st.session_state['logado'] = True
                st.session_state['usuario'] = usuario
                sleep(1)
                st.rerun()
            else:
                st.error('Senha incorreta')

def tab_gestao_usuarios():
    tab_vis, tab_cria, tab_mod, tad_del = st.tabs(
        ['Visualizar', 'Criar', 'Moldificar', 'Deletar']
    )
    usuarios = le_todos_usuarios()
    with tab_vis:
        data_usuarios = [{
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'acesso_gestor': usuario.acesso_gestor,
            'inicio_na_empresa': usuario.inicio_na_empresa
        } for usuario in usuarios]
        st.dataframe(pd.DataFrame(data_usuarios).set_index('id'))

    with tab_cria:
        nome = st.text_input('Nome do usuário')
        senha = st.text_input('Senha do usuário')
        email = st.text_input('Email do usuário')
        acesso_gestor = st.checkbox('Tem acesso de gestor?', value=False)
        inicio_na_empresa = st.text_input(
            'Data de início na empresa (formato AAAA-MM-DD)'
            )
        if st.button('Criar'):
            cria_usurios(
                nome=nome,
                senha=senha,
                email=email,
                acesso_gestor=acesso_gestor,
                inicio_na_empresa=inicio_na_empresa,
            )
            st.rerun()
    
    with tab_mod:
        usuarios_dict = {usuario.nome: usuario for usuario in usuarios}
        nome_usuario = st.selectbox(
            'Selecione o usuário para modificar',
            usuarios_dict.keys())
        usuario = usuarios_dict[nome_usuario] 
        nome = st.text_input(
            'Nome do usuário para modificar', 
            value=usuario.nome
            )
        senha = st.text_input('Senha do usuário', value='xxxxx')
        email = st.text_input(
            'Email para modificar', 
            value=usuario.email
            )
        acesso_gestor = st.checkbox('Modificar acesso de gestor?', value=usuario.acesso_gestor)
        inicio_na_empresa = st.text_input(
            'Data de início na empresa (formato AAAA-MM-DD)',
            value=usuario.inicio_na_empresa
            )
        if st.button('Modificar'):
            if senha == 'xxxxx':
                modifica_usuario(
                    id=usuario.id,
                    nome=nome,
                    email=email,
                    acesso_gestor=acesso_gestor,
                    inicio_na_empresa=inicio_na_empresa,
                )
            else:
                modifica_usuario(
                    id=usuario.id,
                    nome=nome,
                    senha=senha,
                    email=email,
                    acesso_gestor=acesso_gestor,
                    inicio_na_empresa=inicio_na_empresa,
                )
            st.rerun()
    with tad_del:
        usuarios_dict = {usuario.nome: usuario for usuario in usuarios}
        nome_usuario = st.selectbox(
            'Selecione o usuário para deletar',
            usuarios_dict.keys())
        usuario = usuarios_dict[nome_usuario]
        if st.button('Deletar'):
            deleta_usuario(usuario.id)
            st.rerun()
        
        


def pagina_calendario():
    st.title('Bem-vindo ao AppFerrias')
    st.divider()

    usuario = st.session_state['usuario']
    if usuario.acesso_gestor:
        cols = st.columns(2)
        with cols[0]:
            if st.button(
                'Acessar Gestão de Usuários',
                use_container_width=True):
                st.session_state['pag_gestao_usuarios'] = True
                st.rerun()
        with cols[1]:
            if st.button(
                'Acessar Calendário',
                use_container_width=True
                ):
                st.session_state['pag_gestao_usuarios'] = False
                st.rerun()
        
    if st.session_state['pag_gestao_usuarios']:
        st.markdown('Página gestão de usuários')
        with st.sidebar:
            tab_gestao_usuarios()
    
    else:
        st.markdown('Calendário')
            


def main():

    if not 'logado' in st.session_state:
        st.session_state['logado'] = False
    if not 'pag_gestao_usuarios' in st.session_state:
        st.session_state['pag_gestao_usuarios'] = False
    
    if not st.session_state['logado']:
        login()
    else:
        pagina_calendario()

if __name__ == '__main__':
    main()


