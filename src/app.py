
import streamlit as st
import pandas as pd
import plotly.express as px
from components import sidebar, dashboard_principal, visualisation_detaillee, prediction

# configurer la page
st.set_page_config(
    page_title="Tableau de Bord Immobilier",
    page_icon=":house:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Charger le style CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Charger les données
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

def show_main_dashboard(data):
    st.title("Tableau de Bord Principal")
    st.markdown("---")

    # Métriques clés
    col1, col2, col3 = st.columns(3)
    col1.metric("Nombre total de biens", f"{data.shape[0]:,}")
    col2.metric("Loyer moyen", f"₹{data['Rent'].mean():,.0f}")
    col3.metric("Nombre de villes", data['City'].nunique())

    st.markdown("<br>", unsafe_allow_html=True)

    # Graphiques interactifs
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Distribution des loyers")
        fig = px.histogram(data, x='Rent', nbins=50, title="")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Biens par ville")
        city_counts = data['City'].value_counts().reset_index()
        city_counts.columns = ['City', 'Count']
        fig = px.bar(city_counts, x='City', y='Count', title="")
        st.plotly_chart(fig, use_container_width=True)

def main():
    # Sélecteur de thème global
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title(":red[Prix Immobiliers] - :blue[Analyse et Prédiction]")
    with col2:
        theme = st.radio("", ["Clair", "Sombre"], key="theme_selector", label_visibility="collapsed", horizontal=True)

    if theme == "Sombre":
        load_css("assets/style.css")

    st.write("Chargez votre fichier de données pour commencer l'analyse et la prédiction.")

    uploaded_file = st.file_uploader("", type=["csv"])

    if uploaded_file is not None:
        data = load_data(uploaded_file)
        
        section = sidebar.show()

        if section == "Tableau de Bord":
            show_main_dashboard(data)
        elif section == "Visualisation Détaillée":
            visualisation_detaillee.show(data)
        elif section == "Prédiction":
            prediction.show(data)
    else:
        st.info("En attente du chargement d'un fichier CSV.")

if __name__ == "__main__":
    main()
