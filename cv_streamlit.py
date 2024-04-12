import streamlit as st

def main():
    st.title("Mon CV")

    st.markdown("## Informations personnelles")
    st.text("Nom: Votre nom")
    st.text("Email: votre-email@example.com")

    st.markdown("## Éducation")
    st.text("Université: Votre université")
    st.text("Diplôme: Votre diplôme")
    st.text("Années: Vos années d'études")

    st.markdown("## Expérience professionnelle")
    st.text("Entreprise: Nom de l'entreprise")
    st.text("Rôle: Votre rôle")
    st.text("Années: Période de travail")
    st.text("Responsabilités: Vos responsabilités")

    st.markdown("## Compétences")
    st.text("Python, Streamlit, Machine Learning, etc.")

if __name__ == "__main__":
    main()
