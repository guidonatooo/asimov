import json

import streamlit as st
from streamlit_calendar import calendar

with open('calendar_options.json') as f:
    calendar_options = json.load(f)

if not 'ultimo_clique' in st.session_state:
    st.session_state['ultimo_clique'] = ''

def limpar_datas():
    del st.session_state['data_inicio']
    del st.session_state['data_final']

calendar_events = [
    {
        "title": "Férias do Fulano",
        "start": "2024-01-01T08:30:00",
        "end": "2024-02-01T10:30:00",
        "resourceId": "a",
    }
]


calendar_widget = calendar(events=calendar_events, options=calendar_options)
if ('callback' in calendar_widget 
    and calendar_widget['callback'] == 'dateClick'):

    raw_date = calendar_widget['dateClick']['date'].split('T')[0]
    if raw_date != st.session_state['ultimo_clique']:

        st.session_state['ultimo_clique'] = raw_date
        date = calendar_widget['dateClick']['date'].split('T')[0]
        
        if not 'data_inicio' in st.session_state:
            st.session_state['data_inicio'] = date
            st.warning(f'Data de início de férias selecionada {date}')
        else:
            st.session_state['data_final'] = date
            date_inicio = st.session_state['data_inicio']
            cols = st.columns([0.7, 0.3])
            with cols[0]:
                st.warning(f'Data de início de férias selecionada {date_inicio}')
            with cols[1]:
                st.button(
                    'Limpar',
                    use_container_width=True,
                    on_click=limpar_datas
                    )
            cols = st.columns([0.7, 0.3])
            with cols[0]:
                st.warning(f'Data final de férias selecionada {date}')
            with cols[1]:
                st.button(
                    'Adicionar Férias',
                    use_container_width=True
                    )


st.write(calendar_widget)



