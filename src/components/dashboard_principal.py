
import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

def show(data):
    st.header("Exploration des Données")

    # Affichage des statistiques descriptives
    if st.checkbox("Afficher les statistiques descriptives"):
        st.write(data.describe())

    # Tables interactives avec filtrage et tri
    if st.checkbox("Afficher la table interactive"):
        st.dataframe(data)

    # Visualisation des données manquantes
    if st.checkbox("Afficher les données manquantes"):
        st.write(data.isnull().sum())

    # Graphiques de distribution des variables clés
    if st.checkbox("Afficher la distribution des variables"):
        column = st.selectbox("Sélectionner une variable", data.columns)
        if data[column].dtype in ['int64', 'float64']:
            st.bar_chart(data[column].value_counts())
        else:
            st.write("La variable sélectionnée n'est pas numérique.")
