
import streamlit as st

def show():
    st.sidebar.title("Navigation")
    
    section = st.sidebar.radio(
        "",
        ["Tableau de Bord", "Visualisation Détaillée", "Prédiction"],
        label_visibility="collapsed"
    )
    
    return section
