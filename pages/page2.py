import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import io 
from datetime import timedelta
import numpy as np
from pytrends.request import TrendReq
import openai
import requests
import time
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import seaborn as sns
from google.oauth2 import service_account
from googleapiclient.discovery import build
import googleapiclient.discovery
from google.oauth2 import service_account
from datetime import datetime, timedelta
import mechanicalsoup
import json
import altair as alt


# Créez un dictionnaire avec vos informations de compte de service
service_account_info = {
  "type": "service_account",
  "project_id": "blog-isagri",
  "private_key_id": "2d5d78070fa70890a5e78ebd62d1dc009521ce36",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCa85UFLnTPTe4t\ntQnBefSqnEdW7P2kosmHSwkuDlWKtvNgUj87c7RBTxvCLOwkDBdl9Nk+aCxPWN+T\nLG6wc6G5QmchexzOqUn7tr+PZz1mLkJB26EMFBH7Q6r0Qb45nIfhyjWi5ueS8KXR\nzljY07eLha4QZ6Q4b6NkisR8RuNAKxQgb7AmA/xVKT+npO39ipO+FMnqvunL91Rm\nv+ocSrg85dSGbORNJwdtAnv4y4k+p9Kriwdq1UKNhcWeYFZ71dNQttb8TtjpJxPN\n4FObVi5pf8RiNcH2rHaVUy70+Xd+SWRlqY9z/iSdCh0eAFPKJUGWwbxDtYUFeeR9\nky+6eP1ZAgMBAAECggEAK6GnNpxMPAt/o9M0egxzPo9e7zUwfulvwe75GMTkhXja\nsya1s3HzMeiqslSf8c6N0CHQAminAXjPC8wZJwqIYXg3PhBCnlbBBGYDLsgtW9Zu\nxcioYpRMM+pr+veALwzKnmOoEsTeNFwa9ScbkYKcTmdICkqEzXdyFN+WUEBNwUVv\n6cOw2NtEJgaRmRDHy30z9tQKBgygLR6BqCwqsYaAo9/1NGNi3xL7+tyfPxZPD8q6\nSZ1+5bl/YJG8HyoXxyJwbZJtKGKFNaLnjXGgYsiBMGYrzIBhW6WdOSzdMSUXQq/S\nvnAzvc2NV7hyMJo0UeJJi+dpA+xk80Qxhedm/zZpeQKBgQDKOlE2e1b/WZ/924iV\nFHomBz4ydzsij8PLVnGUM/PuaGidbBSaAXECmVNjJgnqtvSaEcLn9cGfdziO5bB9\nhqyf9NIziYWh49YPLoU+H+/ma92KaS+7qUKsnzhaz8qeTZdtaNbpIDmXJ6XmeE0Q\nvK2Xp0qNu+gKZ2182nJDuLgYRwKBgQDEJyh0cW/aT8JOJhTYJMja3HzagkQSyZQh\nrXthglVCmOm8xZq/u4YlCmNaP8yMcGzcCi2pRqBtCiJPmI48Um974iM/gDgIYTuj\nX2NTkaNuSylByZPikR/ddHPpZcTGYeYwKmwFDCQPwfEhPdi0VTTrBZCVRzik/PmO\nJTz8rECtXwKBgEpf7lRyQknBhaUQo4fosw/fZBGdZkNMyn6zOSx/evw4rBkRkfYe\nB5kkGNYDPGx1gzpSw/MZoG9sooFzmlhgOobNvK01q88hgy2sN1bk2g9NpnnsO6Dy\nHFJucIR9nZBhCwszHq84qdWcwFgl8HnyWonG/hVogWuqJEth79pWSmarAoGACh0G\nvfI3VSc1mnfmLTrATGB/43hB8EIKbC4YpW9l2/gsXPpHP0l44iIF+1o8vqTxR+sS\nbZ7hmJ2kJTx1YPDTJK0FKjn/KZdxzruVUHK63W3so6K0CEN5RB7D9y2zFpNnneYi\nCaSVm2Zhe1hH+wxFnTR9PuUcK42LhGOxIEn1T7sCgYBPL8I9CzdG5NErzoMDkDut\ngK4+lgrWImlr4fh4+aDGbUaAjFjoSlSpbusqEWoww7ZcVNpXy0HpHe8h9wIwJuIM\nGJqxVvlgYke/IQgIXK0GzHs8Z10mP6PDIDb7yYkv2gWuprkQG13fyr0wA6G51kgv\n6hlrPJdH5ujdGEHxjUPKPQ==\n-----END PRIVATE KEY-----\n",
  "client_email": "isagri@blog-isagri.iam.gserviceaccount.com",
  "client_id": "116347485967402773045",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/isagri%40blog-isagri.iam.gserviceaccount.com"
}

import requests
from bs4 import BeautifulSoup
import mechanicalsoup

@st.cache_data()
def seobserver_volume_motcle(keyword):
    # Informations de connexion
    email = "poledigital@isagri.fr"
    password = "Ojfhzg77Isagri"
    # Vos identifiants
    username = "poledigital@isagri.fr" # Remplacez ceci par votre adresse e-mail
    password = "Ojfhzg77Isagri" # Remplacez ceci par votre mot de passe
    # URL de la page de connexion
    login_url = "https://app.seobserver.com/login"
    # URL de la page à scraper
    page_url = f"https://app.seobserver.com/serpmachine/fr_fr/{keyword}/now"
    # Création d'un navigateur
    browser = mechanicalsoup.StatefulBrowser()
    # Ouverture de la page de connexion
    browser.open(login_url)
    # Récupération du formulaire de connexion
    form = browser.select_form()
    # Remplissage du formulaire avec vos identifiants
    form.input({"data[User][email]": username, "data[User][password]": password})
    # Soumission du formulaire
    browser.submit_selected()
    # Ouverture de la page à scraper
    browser.open(page_url)
    # Récupération du contenu que vous voulez
    content = browser.page.select('.description > span:nth-child(1)')
    # Retourne le contenu
    return [element.text for element in content]

def get_search_console_data(service_account_info, site_url, keyword):
    # Créer un client pour l'API Search Console
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    webmasters_service = build('webmasters', 'v3', credentials=credentials)

    # Calculer les dates de début et de fin
    end_date = datetime.now() - timedelta(days=1)
    start_date = end_date - timedelta(days=365)

    # Convertir les objets datetime en chaînes de caractères au format 'yyyy-mm-dd'
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # Définir la requête pour l'API Search Console
    request = {
        'startDate': start_date_str,
        'endDate': end_date_str,
        'dimensions': ['page', 'query'],
        'dimensionFilterGroups': [
            {
                'filters': [
                    {
                        'dimension': 'query',
                        'expression': keyword
                    }
                ]
            }
        ],
        'rowLimit': 10000  # limitez le nombre de lignes retournées
    }

    # Exécuter la requête
    response = webmasters_service.searchanalytics().query(siteUrl=site_url, body=request).execute()

    # Construire un DataFrame à partir des résultats
    df = pd.DataFrame(response['rows'])
    df['keys'] = df['keys'].apply(lambda x: dict(zip(['page', 'query'], x)))
    df = pd.concat([df.drop(['keys'], axis=1), df['keys'].apply(pd.Series)], axis=1)
    
    return df

# Créez les credentials
credentials = service_account.Credentials.from_service_account_info(service_account_info)

# Construisez le service
service = googleapiclient.discovery.build('searchconsole', 'v1', credentials=credentials)


sns.set(style="whitegrid", rc={"axes.facecolor": ".9"})  #Personnalisation du graphique Tendance
sns.set_context("paper", font_scale=0.8)  #Personnalisation du graphique Tendance

# Fonction pour afficher la page d'accueil
st.set_page_config(
    page_title="iagriX | Outil IA interne | Isagri", 
    page_icon="🚀",
    layout="wide", 
    initial_sidebar_state="expanded", 
    menu_items=None
)

# Définir la clé d'accès API d'OpenAI
openai.api_key = "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"

# 🐱🐱🐱🐱🐱🐱🐱🐱 Fonctions contextuelles pour utiliser GPT 🐱🐱🐱🐱🐱🐱🐱🐱

# Fonction de contextualisation Isagri
@st.cache_data()
def call_openai_api(prompt):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "Tu travailles au sein de la société Isagri, un éditeur de logiciel et de matériel pour le monde agricole. Tes clients sont des agriculteurs. Tu y occupes le poste un redacteur SEO avec 20 années d'expérience. Tu proposes des réponses de qualité et professionnelles en prenant toujours en compte la notion de référencement naturel."},{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content.strip()
    except openai.error.AuthenticationError:
        st.error("Erreur d'authentification OpenAI. Veuillez vérifier votre clé d'accès API.")
        return ""
#🐱🐱🐱 Fonction pour appeler l'API OpenAI avec le contexte des questions
def call_openai_api_question_context(question):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu travailles au sein de la société Isagri, un éditeur de logiciel et de matériel pour le monde agricole. Tes clients sont des agriculteurs, tes réponses doivent donc, dès que c'est logique, être une réponse à une question qu'il peut se poser. Exemple : emploi saisonnier > quelles aides pour recruter un saisonnier, etc. Tu y occupes le poste un redacteur SEO avec 20 années d'expérience. Tu proposes des réponses de qualité et professionnelles en prenant toujours en compte la notion de référencement naturel."},
                {"role": "user", "content": f"Si je te pose cette question : {question} et que tu devais trouver le mot-clé SEO le plus pertinent, lequel serait-il ? Réponds-moi juste par le mot-clé. Exemple : quelle est la meilleure voiture citadine pour Paris ? Réponds-moi avec 5 mots maximum qui forme une requête qu'un utilisateur peut taper naturellement sur Google : \"meilleure voiture citadine paris\"."}
            ]
        )
        return completion.choices[0].message.content.strip()
    except openai.error.AuthenticationError:
        st.error("Erreur d'authentification OpenAI. Veuillez vérifier votre clé d'accès API.")
        return ""
      
#🐱🐱🐱 Fonction qui retient les PAA du keyword pour s'interroger sur de nouvelles questions
def generate_questions_with_gpt(keyword, existing_questions, number_of_questions=15):
    """
    Use the GPT model to generate questions based on a keyword and a list of existing questions.
    The model will try to generate questions that are not in the existing_questions list.
    """
    questions_prompt = "\n".join(existing_questions)
    prompt = f"Sur la base du mot-clé '{keyword}' et des questions déjà posées : \n{questions_prompt}\nQuelles autres questions pertinentes un internaute pourrait-il se poser ?"
    response = openai_api_call(prompt)
    generated_questions = response.split('\n')[:number_of_questions]

    # Return only the questions that are not already in the existing questions
    new_questions = [q for q in generated_questions if q not in existing_questions]
    return new_questions

#🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱🐱

# Fonction pour effectuer la recherche sur Google et parser les résultats
def search_google(keyword):
    api_key = "59895d544d6c19b08d1bee40066a2e09"
    url = "http://api.serpstack.com/search"
    params = {
        "access_key": api_key,
        "query": keyword,
        "google_domain": "google.fr",
        "gl": "fr",
        "hl": "fr"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data


def get_headings(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        h1 = [h1.text for h1 in soup.find_all('h1')]
        h2 = [h2.text for h2 in soup.find_all('h2')]
        return {
            "h1": h1,
            "h2": h2
        }
    except requests.HTTPError as e:
        if e.response.status_code == 403:
            # Gérer l'erreur de statut 403 (Forbidden)
            print("Accès interdit à la ressource :", url)
        else:
            # Gérer d'autres erreurs HTTP
            print("Une erreur HTTP s'est produite pour l'URL", url, ":", e)
        return {
            "h1": [],
            "h2": []
        }
    except Exception as e:
        # Gérer d'autres exceptions
        print("Une erreur s'est produite pour l'URL", url, ":", e)
        return {
            "h1": [],
            "h2": []
        }

def parse_search_results(data):
    search_results = []
    for result in data['organic_results']:
        title = result['title']
        url = result['url']
        headers = get_headings(url)
        h1 = headers['h1']
        h2 = headers['h2']
        search_results.append({
            "title": title,
            "url": url,
            "h1": h1,
            "h2": h2
        })

    return search_results
  
# Récupérer le mot-clé à analyser
keyword = st.sidebar.text_input("Mot-clé à analyser")
if keyword:
    nom_fichier = keyword.replace(" ", "_")
    nom_fichier = nom_fichier.lower()


# Définition de la fonction "google trend"
@st.experimental_memo
def get_data(keyword):
    pytrend = TrendReq()
    
    # Définition du timeframe pour récupérer les données à partir de 2015
    pytrend.build_payload(kw_list=[keyword], timeframe='2015-01-01 ' + datetime.now().strftime('%Y-%m-%d'))
    
    df = pytrend.interest_over_time()
    if df.empty:
        return df
    if 'isPartial' in df.columns:
        df.drop(columns=['isPartial'], inplace=True)
    df.reset_index(inplace=True)
    
    df.columns = ["x", "y"]
    return df

# Interface utilisateur avec Streamlit
st.sidebar.header("Générateur de brief")

# Récupérer la clé d'accès API d'OpenAI
api_key = "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"

# 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 Bouton "Générer le brief"
if st.sidebar.button("Analyser le mot-clé"):
    # Vérifier si la clé d'accès API est fournie
    if api_key:

        # Effacer toutes les valeurs de st.session_state
        st.session_state.clear()

        st.title(f"iagriX analyse : \"{keyword}\"")
        # Définir la clé d'accès API d'OpenAI
        openai.api_key = api_key

# Récupérer les résultats de la SERP de Googlehttp://localhost:8501/
        html = search_google(keyword)
        search_results = parse_search_results(html)

# Extraire les informations des résultats
        table_data = []
        for result in search_results:
            url = result["url"]
            title = result["title"]
            h1 = ", ".join(result["h1"]) if result["h1"] else "-"
            h2 = ", ".join(result["h2"]) if result["h2"] else "-"
            table_data.append([url, title, h1, h2])
          
        #🔎🔎🔎🔎🔎🔎🔎 Volume de recherche
        if keyword:
          # Appel de la fonction avec le mot-clé entré par l'utilisateur
          result = seobserver_volume_motcle(keyword)
          # Vérifier si le résultat est vide
          if not result:
            st.markdown("<h1 style='font-size:22px'>🔎 la base ne contient pas ce mot-clé</h1>", unsafe_allow_html=True)
          else:
            # Remplacer les virgules par des espaces
            parsed_result = result[0].replace(",", " ")
            # Créer le texte à afficher
            display_text = f"<h1 style='font-size:22px; color:#4B7190;'>🔎 <b>{parsed_result}</b> recherches par mois</h1>"
            # Afficher le résultat
            st.markdown(display_text, unsafe_allow_html=True)
         
      
        st.subheader("Tendance depuis 2015")
        if keyword:
          def display_chart(df):
    # Création du graphique avec altair
            chart = alt.Chart(df).mark_line().encode(
              x=alt.X('x:T', axis=alt.Axis(format='%b %Y')),
              y='y:Q'
    )

    # Création des onglets avec les graphiques
            with st.container() :
              st.altair_chart(chart, theme="streamlit", use_container_width=True)
            

# Obtenez les données de Google Trends en utilisant le mot-clé de votre choix
          data = get_data(keyword)

# Affichez le graphique en utilisant les données obtenues
          display_chart(data)

        # PAA + Idée Google PNL
        data = search_google(keyword)
        if 'related_questions' in data:
          existing_questions = data['related_questions']  # Store the existing questions from Google
          st.subheader("PAA Google (Autres questions posées)")
          for question in existing_questions:
            if 'question' in question:
              # Divisez la question en trois en utilisant la fonction split() de Python, et prenez la première partie
              single_question = question['question'].split('?', 1)[0]
              # Appelez l'API OpenAI pour obtenir un mot-clé à partir de la question
              keyword_suggestion = call_openai_api_question_context(single_question)
              # Appelez SEObserver pour obtenir le volume de recherche pour le mot-clé suggéré
              search_volume = seobserver_volume_motcle(keyword_suggestion)
              # Écrivez la question, le mot-clé suggéré et le volume de recherche dans Streamlit
              st.markdown(f'<span style="color:#4B7190;">{single_question}?</span> <br> 🤖 suggère le mot-clé : {keyword_suggestion} - Volume de recherche : {search_volume}', unsafe_allow_html=True)

            else:
              st.write("Une question sans contenu 'question' a été trouvée.")
          else:
            st.write("")
          st.subheader("Autres questions générées par IagriX")
          # Use the ChatGPT model to generate related questions
          openai.api_key = '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'
          model_response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=f"Voici une liste de questions existantes sur le sujet '{keyword}': {existing_questions}. Quelles pourraient être les 10 prochaines questions logiques à poser ? Fais une liste à puce sans saut de ligne avec uniquement les questions", 
            max_tokens=200, 
            temperature=0.8, 
            top_p=1
            )

          generated_questions = model_response.choices[0].text.strip().split('\n')
          
          for gen_question in generated_questions[:10]:  # Limit to top 10 questions
            st.write(gen_question)

     
      
        # Résultats Searh Console (blog pour commencer)     
        st.subheader("Search Console")        
        def display_data(df):
        # Afficher le DataFrame dans Streamlit
                st.write(df)

        # Afficher les résultats de la SERP dans un tableau
        st.subheader("Voici l'analyse de la SERP")
        st.table(table_data)

        # Appeler l'API OpenAI pour obtenir des idées de sujets
        prompt_idee_sujets = f"Propose moi une liste de sujets complémentaires autour de la thématique : {keyword}"
        idee_sujets = call_openai_api(prompt_idee_sujets)
        if idee_sujets not in st.session_state:
            st.session_state["idee_sujets"] = idee_sujets

        # Afficher la liste des idées de sujets
        st.subheader("\nVoici une liste d'idées de sujet :")
        st.write(idee_sujets)

        # Construction de l'intention de recherche
        prompt_search_intent=f"Voici la définition de l'intention de recherche : La recherche informationnelle concerne les internautes ayant un besoin d'information. Ce type d'intention est très large car il concerne des milliers de thématiques allant de la météo aux sites internet d'éducation ou de jardinage. La recherche navigationnelle concerne les internautes qui souhaitent visiter un site web bien particulier. C'est notamment le cas lorsqu'ils tapent le nom du site ou une marque. La recherche transactionnelle concerne les internautes désireux d'acheter sur le web. Ils sont donc à la recherche d'un produit, d'un service ou d'une marque spécifique. En général, les requêtes sont assez courtes et elles ne sont jamais tournées sous forme de question. L'intention de recherche commerciale concerne les personnes en cours de réflexion en vue d'un achat prochain. Ces dernières utilisent le web pour comparer, trouver des bons plans, conseils et avis d'internautes. La recherche commerciale intervient en général juste avant l'intention transactionnelle. Sur la base de cette définition, analyse l'intention de recherche pour le mot-clé '{keyword}' en prenant en compte les title, h1 et h2 des dix premiers résultats sur Google que sont : '{table_data}'. Identifiez l'intention derrière cette requête en tenant compte de ces éléments.\n {idee_sujets}\nQuels sont les sujets connexes ou les termes associés qui peuvent donner des indications sur l'intention de recherche ? Notez-les et considérez leur pertinence par rapport au mot-clé principal.\nTitre : Voici  les titres associés à '{keyword}'.\n {title}\nQuelles sont les informations fournies dans le titre ? Est-ce une question, une demande d'informations, une recherche de comparaison ou autre ? Le titre, le h1 ou les h2 peuvent fournir des indices sur l'intention de recherche.\nNom de domaine de la concurrence : Voici les sites concurrents qui apparaissent dans les résultats de recherche pour '{keyword}'.\n {url}\nQuels types de sites ou d'entreprises sont présents ? S'agit-il de sites de vente en ligne, de blogs d'informations, de sites éducatifs ou d'autres types ? Le type de sites concurrents peut révéler l'intention de recherche.\nEn utilisant ces informations, identifiez l'intention de recherche pour le mot-clé '{keyword}'. Est-ce une intention informative, transactionnelle, navigationelle ou comemrciale ? Expliquez votre raisonnement en prenant en compte les sujets en lien, le titre et le nom de domaine de la concurrence. Adoptez un ton pragamatique, bienveillant et didactique"
        search_intent = call_openai_api(prompt_search_intent)
        if 'search_intent' not in st.session_state:
            st.session_state['search_intent'] = search_intent      

        # Afficher l'intention de recherche
        st.subheader("\nVoici l'intention de recherche du texte :")
        st.write(search_intent)  
       
       # Générer un title et une meta-description
        prompt_title = f"Je souhaite créer une balise <title> efficace sur le sujet {keyword} pour ma page web en me basant sur le TOP10 dont les informations sont : : '{table_data}'. J'aimerais que le titre soit à la fois pertinent, accrocheur et optimisé pour le SEO. Peux-tu m'aider à générer un titre attractif qui incite les utilisateurs à cliquer tout en étant optimisé pour les moteurs de recherche ? Propose moi une liste de 5 titres si possible dans des styles assez differents les uns des autres. Attention, il faut impérativement que le titre ne dépasse pas les 11 mots. Fourni moi directement la liste des titres sans phrases préliminaires"
        prompt_md = f"Je souhaite créer une méta-description convaincante sur le sujet {keyword} pour ma page web. Base-toi sur les title que tu m'as proposé précemment. Attention, il faut impérativement que la meta-description ne dépasse pas les 40 mots. "
        title = call_openai_api(prompt_title)
        metadesc = call_openai_api(prompt_md)
        if 'title' not in st.session_state:
            st.session_state['title'] = title
        if 'metadesc' not in st.session_state:
            st.session_state['metadesc'] = metadesc

        # Afficher le titre et la méta-description
        st.subheader("\nVoici des titres possible :")
        st.write(title)
        st.subheader("\nVoici une meta-description possible :")
        st.write(metadesc)

        # Appeler l'API OpenAI pour générer un plan de site
        prompt_article_plan = f"Je veux que tu fasses un plan complet en français en suivant la méthode MECE avec 1 H1 puis tous les H2 et H3 nécessaires en te basant sur les idées de sujets que je vais te donner, et les titres de mes concurrents. Sous chaque Hn tu dois décrire en 1 à 2 phrases le contenu de la partie et les éléments hors texte à intégrer (tableau, liste à puce, schéma, outil en ligne...). Attention il faut iméprativement effectuer un saut de ligne entre les Hn, la description et les éléments hors contextes afin d'améliorer la visibilité du rendu.\nVoici les titres :\nBalise title : {title}\n\nEt voici les idées de sujets complémentaires : {idee_sujets}"
        article_plan = call_openai_api(prompt_article_plan)
        if 'article_plan' not in st.session_state:
            st.session_state['article_plan'] = article_plan

        # Afficher le plan de site
        st.subheader("\nVoici un plan de site possible :")
        st.write(article_plan)

    else:
        st.error("Veuillez entrer la clé d'accès API OpenAI.")

# Bouton pour modifier les résultats du brief
st.sidebar.subheader("Modifier les résultats du brief")
# Liste des éléments modifiables
elements = ["","Intention de recherche", "Plan de l'article"]
# Sélecteur pour choisir l'élément à modifier
selected_element = st.sidebar.selectbox("Choisissez l'élément à modifier", elements, index=0)
if selected_element =="Intention de recherche" and st.session_state['search_intent']:
    # Vérifier quel élément a été sélectionné
    search_intent = st.session_state['search_intent']
    search_intent_modif = st.text_area(label=f"Intention de recherche actuelle :\n\n {search_intent}")
    if st.button("Modifier"):
        del st.session_state['search_intent']
        st.session_state['search_intent'] = search_intent_modif
        st.experimental_rerun()
elif selected_element =="Plan de l'article" and st.session_state['article_plan']:
    # Vérifier quel élément a été sélectionné
    plan_article = st.session_state['article_plan']
    plan_modif = st.text_area(label=f"Intention de recherche actuelle :\n\n {plan_article}")
    if st.button("Modifier"):
        del st.session_state['article_plan']
        st.session_state['article_plan'] = plan_modif
        st.experimental_rerun()

# Début fonction à coder pour télécharger le brief
if st.sidebar.button("Télécharger le brief"):
    # Obtention des données depuis session_state
    search_intent = st.session_state['search_intent']
    title = st.session_state['title']
    metadesc = st.session_state['metadesc']
    article_plan = st.session_state['article_plan']
    title = st.session_state['title']
    ndd = st.session_state['ndd']
    idee_sujets = st.session_state['idee_sujets']

    # Conversion des données en une chaîne de caractères formatée pour le fichier txt
    txt_content = f"Brief redactionnel pour le mot clé : {keyword}\n\n{search_intent}\n\nVoici une proposition de titres optimisés pour votre article :\n\n{title}\n\nVoici une meta-description possible : \n\n{metadesc}\n\nVoici une proposition de plan pour votre article :\n\n{article_plan}\n\nEnfin voici quelques idées de sujets complémentaires :\n\n{idee_sujets}"
    with st.expander("Voir le rendu de votre brief"):
        st.write(txt_content)
    # Affichage du bouton de téléchargement
    st.download_button("Télécharger les données", data=txt_content, file_name=f"{nom_fichier}.txt", mime="text/plain")
