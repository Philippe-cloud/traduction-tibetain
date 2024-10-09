import json
import streamlit as st

# Dictionnaire pour stocker les entités
entities_dict = {
    'entities': []
}

# Fonction pour ajouter une nouvelle entité
def add_entity(name, lang, translation, entity_type, associations, associated_words):
    entities_dict['entities'].append({
        'name': name,
        'language': lang,
        'translation': translation,
        'type': entity_type,
        'associations': associations,
        'associated_words': associated_words
    })

# Interface Streamlit
st.title("Création d'Entités Nommées")
st.write("Ajoutez des entités nommées en tibétain et associez des symboles pour donner une signification littéraire.")

# Ajout d'une nouvelle entité
st.subheader("Ajouter une nouvelle entité")
entity_name = st.text_input("Nom de l'entité (Tibétain)")
entity_language = st.selectbox("Langue de l'entité", ["Tibétain"])
entity_translation = st.text_input("Traduction de l'entité en français")
entity_type = st.selectbox("Type d'entité", ["Personne", "Lieu", "Concept", "Autre"])

# Symboles tibétains
tibetan_symbols = [
    "ཀ", "ཁ", "ག", "ང", "ཅ", "ཆ", "ཇ", "ཉ",
    "ཏ", "ཐ", "ད", "ན", "པ", "ཕ", "བ", "མ",
    "ཙ", "ཚ", "ཛ", "ཝ", "ཞ", "ཟ", "འ", "ཡ",
    "ར", "ལ", "ཤ", "ས", "ཧ", "ཨ"
]
associations = st.multiselect("Associez des symboles tibétains", tibetan_symbols)

# Ajout de mots associés
associated_words = []
with st.form(key='associated_words_form'):
    word = st.text_input("Mot associé")
    word_meaning = st.text_input("Signification du mot associé")
    word_association = st.multiselect("Associez des symboles tibétains pour le mot", tibetan_symbols)
    submit_word = st.form_submit_button("Ajouter le mot associé")
    
    if submit_word and word and word_meaning:
        associated_words.append({
            'word': word,
            'meaning': word_meaning,
            'associations': word_association
        })
        st.success(f"Le mot associé '{word}' avec la signification '{word_meaning}' a été ajouté.")

if st.button("Ajouter l'entité"):
    if entity_name and entity_translation:
        add_entity(entity_name, entity_language, entity_translation, entity_type, associations, associated_words)
        st.success(f"L'entité '{entity_name}' de type '{entity_type}' avec la traduction '{entity_translation}' a été ajoutée.")

# Affichage des entités ajoutées
st.write("Entités ajoutées :")
for entity in entities_dict['entities']:
    st.write(f"Nom : {entity['name']} - Langue : {entity['language']} - Traduction : {entity['translation']} - Type : {entity['type']} - Associations : {', '.join(entity['associations'])}")
    st.write("Mots associés :")
    for word in entity['associated_words']:
        st.write(f"- {word['word']} : {word['meaning']} (Symboles associés : {', '.join(word['associations'])})")

# Générer le fichier JSON pour stocker toutes les entités
output_json_file = 'C:\\Users\\LJDGC\\Philippe Lacassaigne\\output_entities.json'
if st.button("Sauvegarder les entités dans un fichier JSON"):
    with open(output_json_file, 'w', encoding='utf-8') as f:
        json.dump(entities_dict, f, ensure_ascii=False, indent=4)
    st.success("Les entités ont été sauvegardées dans le fichier JSON.")