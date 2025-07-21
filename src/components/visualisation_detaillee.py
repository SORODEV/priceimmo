
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def show(data):
    st.header("Visualisation Avancée")

    # Graphiques interactifs
    if st.checkbox("Afficher les graphiques interactifs"):
        chart_type = st.selectbox("Sélectionner un type de graphique", ["Histogramme", "Boîte à moustaches", "Nuage de points"], help="Sélectionnez le type de graphique que vous souhaitez afficher.")
        
        if chart_type == "Histogramme":
            column = st.selectbox("Sélectionner une variable", data.columns, key='hist')
            fig = px.histogram(data, x=column)
            st.plotly_chart(fig)

        elif chart_type == "Boîte à moustaches":
            column = st.selectbox("Sélectionner une variable", data.columns, key='box')
            fig = px.box(data, y=column)
            st.plotly_chart(fig)

        elif chart_type == "Nuage de points":
            x_axis = st.selectbox("Sélectionner l'axe X", data.columns, key='scatter_x')
            y_axis = st.selectbox("Sélectionner l'axe Y", data.columns, key='scatter_y')
            fig = px.scatter(data, x=x_axis, y=y_axis)
            st.plotly_chart(fig)

    # Matrice de corrélation interactive
    if st.checkbox("Afficher la matrice de corrélation"):
        # Sélectionner uniquement les colonnes numériques pour la corrélation
        numeric_data = data.select_dtypes(include=['number'])
        corr = numeric_data.corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto")
        st.plotly_chart(fig)
