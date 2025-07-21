
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def show(data):
    st.header("Prédiction des Prix Immobiliers")

    # Entraîner un modèle simple pour la démonstration
    # Sélectionner uniquement les colonnes numériques
    numeric_data = data.select_dtypes(include=['number'])
    
    # Supprimer les lignes avec des valeurs manquantes dans les colonnes numériques
    numeric_data = numeric_data.dropna()
    
    if not numeric_data.empty and 'Rent' in numeric_data.columns:
        X = numeric_data.drop("Rent", axis=1)
        y = numeric_data["Rent"]
        
        model = LinearRegression()
        model.fit(X, y)

        # Formulaire interactif pour la saisie des caractéristiques
        st.subheader("Saisie manuelle des caractéristiques")
        
        input_data = {}
        for col in X.columns:
            input_data[col] = st.number_input(f"Entrer la valeur pour {col}", value=X[col].mean())
        
        if st.button("Prédire"):
            with st.spinner('Prédiction en cours...'):
                prediction = model.predict(pd.DataFrame([input_data]))
                st.success(f"Le prix prédit ou estimé est de : {prediction[0]:.2f}")

                # Visualisation des facteurs influençant la prédiction
                st.subheader("Facteurs influençant la prédiction")
                
                # Obtenir les coefficients et les noms des fonctionnalités
                coefficients = model.coef_
                feature_names = X.columns
                
                # Créer un DataFrame pour une visualisation facile
                coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
                coef_df = coef_df.sort_values(by='Coefficient', ascending=False)
                
                # Afficher les coefficients dans un graphique à barres
                st.bar_chart(coef_df.set_index('Feature'))

        # Option d'upload de fichier pour des prédictions en masse
        st.subheader("Prédictions en masse à partir d'un fichier")
        uploaded_file = st.file_uploader("Uploader un fichier CSV pour la prédiction", type=["csv"])
        if uploaded_file is not None:
            with st.spinner('Prédiction en cours...'):
                new_data = pd.read_csv(uploaded_file)
                # Assurez-vous que les colonnes correspondent
                new_data_numeric = new_data.select_dtypes(include=['number'])
                predictions = model.predict(new_data_numeric)
                st.write(predictions)

                # Export des résultats
                st.download_button(
                    label="Exporter les prédictions en CSV",
                    data=pd.DataFrame(predictions).to_csv(index=False),
                    file_name="predictions.csv",
                    mime="text/csv",
                )
    else:
        st.warning("Le dataset ne contient pas les colonnes numériques nécessaires ou la colonne 'Rent' est manquante.")
