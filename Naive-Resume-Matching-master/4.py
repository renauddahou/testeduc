from db import *
import streamlit as st
import pandas as pd
import re
import random
import streamlit.components.v1 as components
from streamlit_player import st_player
from PIL import Image
import os
import flask
from flask import request, jsonify
from functrans import listToString,read_pdf,docx2txtrans,read_resumes,translator,skill_resumes,get_skjob_resum # skills_doc
#from préprocess import read_r,get_cleaned_words,remove_tags,html_parser,get_cleaned_wordsJ
import os
import io
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
import docx2txt
from docx import Document
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import pandas as pd
import textwrap
from deep_translator import GoogleTranslator
import textwrap
from langdetect import detect
import warnings
import os
warnings.filterwarnings("ignore")
# Import libraries
#import sqlite3 as sql # sql connector
from datetime import datetime
import numpy as np             #for numerical computations like log,exp,sqrt etc
import pandas as pd            #for reading & storing data, pre-processing
import matplotlib.pylab as plt #for visualization
#import matplotlib.pyplot as plt
import re
from Cleaner import *
#from Cleaner import *
import tf_idf
exec(open("functrans.py").read())
exec(open("Cleaner.py").read())
from pyresparser import ResumeParser
import html.parser

import matplotlib.colors as mcolors
import gensim
import gensim.corpora as corpora
from gensim.summarization import keywords
from operator import index
from wordcloud import WordCloud
from pandas._config.config import options
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import Similar
from PIL import Image
import time
import pymysql
from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from ast import literal_eval
import warnings
warnings.filterwarnings("ignore")
from nltk.corpus import stopwords
import re
import regex
#st.set_page_config(layout="wide")
st.set_page_config( 
layout="wide",  
initial_sidebar_state="auto",
page_title= "JobsCVmacther",   
)

my_stop_words= stopwords.words('english') + stopwords.words('french')
#couleur button interne
primaryColor = st.get_option("theme.primaryColor")
s = f"""
<style>
div.stButton > button:first-child {{text-shadow:0px 1px 0px #2f6627;font-size:15px; background-color: #71f9ed;border: 5px solid {primaryColor}; border-radius:5px 5px 5px 5px; }}
<style>
"""
st.markdown(s, unsafe_allow_html=True)

#masquer le menu streamlit
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
@st.cache()
def style():
    st.markdown("""<style>
    div[data-baseweb="select"]> div {
    background-color: yellow;
    } 
    div[role="listbox"] ul {
    background-color:white;
    }</style>""", unsafe_allow_html=True)




############******* SCRIPT 2  de recupération des skills*****####################################
#################################################################################################

    
my_file = open("Foutfile.txt",encoding='utf-8')
content = my_file.read()
content_list = content.split("\n")

keywords1 = [re.sub(' +', ' ', e) for e in content_list]

keywords2 = [e.lower() for e in keywords1]
keywords2[:] = [item for item in keywords2 if item != '']
keywords2=list(map(lambda x: x.lower(), keywords2))

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def listToStringWithoutBrackets(list1):
        return str(list1).replace('[','').replace(']','').replace("'",'')

def skills_doc(dirty):
    clean = str(dirty).lower()
    splitclean=clean.split(' ')
    splitclean2=[x.strip("', /\n") for x in splitclean ]
    wordList = keywords2
    result = regex.findall(r"\L<words>", clean, words=keywords2)
    L1=f7([x for x in result if x in wordList]) #retenir les skills qui sont dans la liste de mot clé
    return f7([x for x in splitclean2 if x in L1])# retenir les skills qui sont dans le text par rapport à L1

#Néttoyage du document comportant les CV
#evité de stcache
def get_cleaned_words(document):
    for i in range(len(document)):
        raw = Cleaner(document[i][1])
        document[i].append(" ".join(raw[0]))
        document[i].append(" ".join(raw[1]))
        document[i].append(" ".join(raw[2]))
        try:
            sentence = tf_idf.do_tfidf(document[i][3].split(" "))
        except:
            sentence=Cleaner(document[i][3])
        document[i].append(sentence)
    return document
#menu
st.sidebar.title("Navigation 👇")
menu = ["Accueil", "Connexion", "Inscription"]
choice = st.sidebar.radio(" ",menu)

if choice == "Accueil":
    image_ren ="""
    <img src="https://avatars.githubusercontent.com/u/85571576?v=4" alt="Avatar" style="vertical-align: middle;width: 100px;height: 100px;border-radius: 50%;" >
    """
    st.sidebar.markdown(image_ren, unsafe_allow_html = True)
    st.sidebar.markdown('**Auteur: Renaud Louis DAHOU**')
    st.sidebar.markdown('Email:dahou.r@yahoo.com')
    st.sidebar.markdown('[Linkedin](https://www.linkedin.com/in/dahou-renaud-louis-8958599a/)')
    # Titre
    html_temp = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:3px;">
    <h1 style="font-family: 'BadaBoom BB', sans-serif;color:white;text-align:center;"><b>📈 Jobs Matcher 📊</b></h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.markdown("## **l'intelligence artificielle au service du recrutement des talents!**")
    st.markdown(''' Cet outil est un modèle analytique qui est embarqué de plusieur algoirythme d'intélligence artificielle (IA) et  de machine  l'earning (ML). Il vous permets de trouver le meilleiur candidat pour un poste **peu importe la langue d'origine du CV candidat ou du descriptif du poste**.
    Son utilisation est simple .Il vous suffit de chargers les CV et le/les descriptifs de poste pour voir la magie s'opérée. ''')
    html_temp = """
    <div class="mySlides fade">
    </div>
    """
    image = Image.open('January-22.png')
    st.image(image)
    #<img src="https://coin.i.ng/wp-content/uploads/2021/03/jobs-1536x632.png" style="width:100%;border-radius:5px;">
    #components.html(html_temp)
    st.markdown(html_temp, unsafe_allow_html = True)

        
        

elif choice == "Connexion":
    with st.sidebar.beta_expander("Connecté"):
        st.subheader("")
        email = st.text_input("Email")
        password = st.text_input("Mot de passe",type='password')
        con=st.checkbox("Connexion")
    if con:
        # if password == '12345':
        create_table()
        hashed_pswd = make_hashes(password)

        result = login_user(email,check_hashes(password,hashed_pswd))
        if result:
            st.success("Connecté en tant que {}".format(email))
            #task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
            task = ""
            if task == "":
                #try:
                st.subheader("")
                col1, col2 = st.beta_columns([10,10])
                with col1:
                    st.markdown("### *CHARGER LES CVs ICI 👇*")
                    uploaded_files = st.file_uploader("", accept_multiple_files=True,type=['docx','doc','pdf'])
                    directory=str(email+"cv")
                    if not os.path.isdir(directory):
                            os.mkdir(directory)
                    button1=st.button("VALIDER",key=1)
                    button2=st.button("VIDER LA LISTE",key=2)
                    resume_dir = str(email+"cv")+"/"
                    resume_names = os.listdir(resume_dir)
                    st.write(pd.DataFrame({'CVs': resume_names}))

                    if button1:
                        for uploaded_file in uploaded_files:
                            if uploaded_file is not None:
                                file_path=os.path.join(directory,uploaded_file.name)
                                bytes_data = uploaded_file.getvalue()
                                with open(file_path, 'wb') as f:
                                    f.write(bytes_data)
                                #st.success("AJOUTÉ AVEC SUCCÈS")
                    if button2:
                        for i in resume_names:
                                os.remove(resume_dir+i)
                    
                    

                    with col2:
                        st.markdown("### *CHARGER LES JOBS ICI 👇*")
                        uploaded_files = st.file_uploader("", accept_multiple_files=True,type=['docx','doc','pdf'],key=1)
                        directory=str(email+"jb")
                        if not os.path.isdir(directory):
                                os.mkdir(directory)
                        button3=st.button("VALIDER",key=3)
                        button4=st.button("VIDER LA LISTE",key=4)
                        jobs_dir = str(email+"jb")+"/"
                        jobs_names = os.listdir(jobs_dir)
                        st.write(pd.DataFrame({'Jobs': jobs_names}))
                        if button3:
                            for uploaded_file in uploaded_files:
                                if uploaded_file is not None:
                                    file_path=os.path.join(directory,uploaded_file.name)
                                    bytes_data = uploaded_file.getvalue()
                                    with open(file_path, 'wb') as f:
                                        f.write(bytes_data)
                                    #st.success("AJOUTÉ AVEC SUCCÈS")
                        if button4:
                            for i in jobs_names:
                                os.remove(jobs_dir+i)
                    
                if len(resume_names)==0 |len(jobs_names)==0:
                    st.warning("Assurez-vous d'avoir uploader les jobs et CVs")
                else:
                    #Accédons au dossier contenant le CV des candidat qui ont postulé à l'offre
                    resume_dir = str(email+"cv")+"/"
                    resume_names = os.listdir(resume_dir)
                    #document = []
                    documentcv = read_resumes(resume_names, resume_dir)
                    # pour filtrer utilisateur dont le CV ne fera pas aumoins 36 mots
                    docselect=[]
                    for i in documentcv:
                        S=i[1]
                        K=S.split()
                        if len(K)>=36:
                            docselect.append(i)

                    Doccv = get_cleaned_words(docselect)

                    Resumes1 = pd.DataFrame(Doccv, columns=["Nom", "Context", "Cleaned", "Selective", "Selective_Reduced", "TF_Based"])
                    #recupération des skills
                    skdict=[]
                    for i in range(0,Resumes1.shape[0]):
                        d=Resumes1['Cleaned'][i]
                        dict_skill=skills_doc(d)
                        skdict.append(dict_skill)
                        
                    
                        
                    #recupération dans une dataframe    
                    dataskill= Resumes1.copy()
                    dataskill['Skills']=pd.DataFrame({'Skills': skdict})
                    dataskill['Skills']=dataskill['Skills'].apply(lambda row: listToStringWithoutBrackets(row))

                    Resumes1.reset_index(drop=True, inplace=True)
                    dataskill.reset_index(drop=True, inplace=True)

                    Resumes=pd.concat( [Resumes1, dataskill[['Skills']]], axis=1) 
                    #Database.to_csv("Resume_Data.csv", index=False)
                    #os.system("rm -rf"+" "+email+"cv")

                    #Accédons au dossier contenant du Job
                    jobs_dir = str(email+"jb")+"/"
                    jobs_names = os.listdir(jobs_dir)
                    #traduction et ajout dans un doc
                    #document = []
                    documentjb = read_resumes(jobs_names, jobs_dir)
                    Docjb= get_cleaned_words(documentjb)

                    Jobs = pd.DataFrame(Docjb, columns=["Nom", "Context", "Cleaned", "Selective", "Selective_Reduced", "TF_Based"])

                    ############################### JOB DESCRIPTION CODE ######################################
                    # Checking for Multiple Job Descriptions
                    # If more than one Job Descriptions are available, it asks user to select one as well.
                    # if len(Jobs['Nom']) <= 1:
                    #     st.write(
                    #         "Il n'y a qu'une seule description de poste. Elle sera utilisée pour créer des scores.")
                    # else:
                    #     st.write("il y a ", len(Jobs['Nom']),
                    #             "Descriptions de poste disponibles. Veuillez en sélectionner une.")


                    # Asking to Print the Job Desciption Names
                    if len(Jobs['Nom']) > 1:
                        option_yn = st.selectbox(
                            "Afficher les noms des descriptions de poste ?", options=['OUI', 'NON'])
                        if option_yn == 'OUI':
                            index = [a for a in range(len(Jobs['Nom']))]
                            fig = go.Figure(data=[go.Table(header=dict(values=["Job No.", "Job Desc. Nom"], line_color='darkslategray',
                                                                    fill_color='lightskyblue'),
                                                        cells=dict(values=[index, Jobs['Nom']], line_color='darkslategray',
                                                                    fill_color='cyan'))
                                                ])
                            fig.update_layout(height=150, margin=dict(t=10, b=10))
                            st.write(fig)


                    # Asking to chose the Job Description
                    if len(Jobs['Nom'])<=1:
                        index=0
                    else:
                        index = st.slider("Quel JD choisir ? : ", 0,
                                    len(Jobs['Nom'])-1, 1)


                    option_yn = st.selectbox("Afficher la description du poste ?", options=['OUI', 'NON'])
                    if option_yn == 'OUI':
                        st.markdown(" ")
                        st.markdown("### Description du poste :")
                        fig = go.Figure(data=[go.Table(
                            header=dict(values=["Description du poste"],
                                        fill_color='#f0a500',
                                        align='center', font=dict(color='white', size=16)),
                            cells=dict(values=[Jobs['Context'][index]],
                                    fill_color='#f4f4f4',
                                    align='left'))])

                        fig.update_layout(height=150, margin=dict(t=10, b=10))
                        st.write(fig)
                        st.markdown(" ")


                    #################################### SCORE CALCUATION ################################
                    @st.cache()
                    def calculate_scores(resumes, job_description):
                        scores = []
                        for x in range(resumes.shape[0]):
                            score = Similar.match(
                                resumes['TF_Based'][x], job_description['TF_Based'][index])
                            scores.append(score)
                        return scores


                    Resumes['Scores'] = calculate_scores(Resumes, Jobs)
                    Ranked_resumes=Resumes

                    Ranked_resumes = Resumes.sort_values(
                        by=['Scores'], ascending=False).reset_index(drop=True)

                    Ranked_resumes['Rang'] = pd.DataFrame(
                        [i for i in range(1, len(Ranked_resumes['Scores'])+1)])

                    

                    

                    ################################### LDA CODE ##############################################

                    ##Comparaisons Skill Job VS Skill candidat
                    job_skill=skills_doc(Jobs['Cleaned'][index])
                    words = job_skill
                    stopwordss =["Email,","Email","email,","email","Gmail,","Gmail","Yahoo,","Yahoo","gmail,","gmail","yahoo,","yahoo","Outlook,","Outlook","outlook,","outlook","Telephone,","Telephone","telephone,","telephone"]
                    wordsf=[]
                    for x in words:
                        if x not in stopwordss:
                            wordsf.append(x)

                    countlstJ=[]
                    interlstJ=[]

                    globalskills=wordsf #skills job
                    globalskills=[x.strip("', /\n") for x in globalskills ]
                    for i in range(0,dataskill.shape[0]):
                        listskills=dataskill['Skills'][i].split()
                        listskills=[x for x in listskills if str(x) != 'nan'] # pour supprimer les valeur nuls
                        listskills=[x.split(',') for x in listskills]
                        listskills = list({x.strip("', /\n") for l in listskills for x in l})
                        loacalskills = [x.replace('\\xa0', '').replace(':', '').replace('"', '') for x in listskills]
                        #inter=set(globalskills).intersection(loacalskills)
                        inter=list(set([x.lower() for x in globalskills]) & set([x.lower() for x in loacalskills]))
                        interlstJ.append(inter)
                        count = len(inter)
                        countlstJ.append(count)
                
                    #Creation de la dataframe Nom et skill

                    comptsklJ = pd.DataFrame({'skills_e': interlstJ,'count': countlstJ})
                    comptsklJ['Noms']=Resumes['Nom']
                    comptsklJ.head()
        


                    stdictJ=[]
                    # convert to string
                    for i in range(0,comptsklJ.shape[0]):
                        input= str(comptsklJ['skills_e'][i]).replace('{','').replace('}','').replace(",'","'")
                        stdictJ.append(input)
                        
                    comptsklJ['skills_e'] = pd.DataFrame({'kills_e':stdictJ})
                    comptsklJ['score']=comptsklJ['count'].astype('int')/len(globalskills)*100
                    #comptsklJ.sort_values(by=['score'], ascending=False,inplace=True)

                    scorer=[]
                    for i in range(0, comptsklJ['score'].shape[0]):
                        values = [int(float(comptsklJ['score'][i])),int(float(Resumes['Scores'][i]))]
                        weights =[70,30]
                        s = 0
                        for x, y in zip(values, weights):
                            s += x * y
                        average = round(s / sum(weights))
                        scorer.append(average)

                    comptsklJ['score']=scorer
                    comptsklJ.sort_values(by=['score'], ascending=False,inplace=True)
                    comptsklJ=comptsklJ.reset_index(drop=True)
                    comptsklJ['Rang'] = pd.DataFrame(
                        [i for i in range(1, len(comptsklJ['score'])+1)])
                    sj_sc=comptsklJ.reset_index()

                    ###################################### SCORE TABLE PLOT ####################################

                    fig3 = go.Figure(data=[go.Table(
                        header=dict(values=["Rang", "Nom", "Scores"],
                                    fill_color='#00416d',
                                    align='center', font=dict(color='white', size=16)),
                        cells=dict(values=[sj_sc.Rang,sj_sc.Noms, sj_sc.score],
                                fill_color='#d6e0f0',
                                align='left'))])
                    st.markdown("### CV les mieux classés")
                    fig3.update_layout(height=150, margin=dict(t=10, b=10))
                    st.write(fig3)

                    fig4 = px.bar(sj_sc,
                                x=sj_sc['Noms'], y=sj_sc['score'], color='score',
                                color_continuous_scale='haline', title="Distribution des scores")
                    fig4.update_layout(width=700, height=700)
                    st.write(fig4)



                    ############################################ TF-IDF Code ###################################


                    @st.cache()
                    def get_list_of_words(document):
                        Document = []

                        for a in document:
                            raw = a.split(" ")
                            Document.append(raw)

                        return Document


                    document = get_list_of_words(Resumes1['Cleaned'])

                    id2word = corpora.Dictionary(document)
                    corpus = [id2word.doc2bow(text) for text in document]


                    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=6, random_state=100,
                                                                update_every=3, chunksize=100, passes=50, alpha='auto', per_word_topics=True)

                    ################################### LDA CODE ##############################################


                    @st.cache  # Trying to improve performance by reducing the rerun computations
                    def format_topics_sentences(ldamodel, corpus):
                        sent_topics_df = []
                        for i, row_list in enumerate(ldamodel[corpus]):
                            row = row_list[0] if ldamodel.per_word_topics else row_list
                            row = sorted(row, key=lambda x: (x[1]), reverse=True)
                            for j, (topic_num, prop_topic) in enumerate(row):
                                if j == 0:
                                    wp = ldamodel.show_topic(topic_num)
                                    topic_keywords = ", ".join([word for word, prop in wp])
                                    sent_topics_df.append(
                                        [i, int(topic_num), round(prop_topic, 4)*100, topic_keywords])
                                else:
                                    break

                        return sent_topics_df

                    ####################### SETTING UP THE DATAFRAME FOR SUNBURST-GRAPH ############################

                    df_topic_sents_keywords = format_topics_sentences(
                        ldamodel=lda_model, corpus=corpus)
                    df_some = pd.DataFrame(df_topic_sents_keywords, columns=[
                                        'Document No', 'Dominant Topic', 'Topic % Contribution', 'Keywords'])
                    df_some['Nom'] = Resumes1['Nom']

                    df = df_some

                    st.markdown("### Modélisation thématique des CV ")
                    st.markdown("Utilisation de LDA pour regrouper les CV par thématique")
                    fig3 = px.sunburst(df, path=['Dominant Topic', 'Nom'], values='Topic % Contribution',
                                    color='Dominant Topic', color_continuous_scale='viridis', width=700, height=700, title="Graphique de distribution des CV selon leur thématique")
                    st.write(fig3)



                    option_2 = st.selectbox(
                            "Afficher les thématique ?", options=['NON', 'OUI'])

                    if option_2 == 'OUI':
                        cols = [color for name, color in mcolors.TABLEAU_COLORS.items()]

                        cloud = WordCloud(stopwords = my_stop_words,background_color='white',
                                        width=2500,
                                        height=1800,
                                        max_words=10,
                                        colormap='tab10',
                                        collocations=False,
                                        color_func=lambda *args, **kwargs: cols[i],
                                        prefer_horizontal=1.0)

                        topics = lda_model.show_topics(formatted=False)

                        fig, axes = plt.subplots(2, 3, figsize=(10, 10), sharex=True, sharey=True)

                        for i, ax in enumerate(axes.flatten()):
                            fig.add_subplot(ax)
                            topic_words = dict(topics[i][1])
                            cloud.generate_from_frequencies(topic_words, max_font_size=300)
                            plt.gca().imshow(cloud)
                            plt.gca().set_title('Topic ' + str(i), fontdict=dict(size=16))
                            plt.gca().axis('off')


                        plt.subplots_adjust(wspace=0, hspace=0)
                        plt.axis('off')
                        plt.margins(x=0, y=0)
                        plt.tight_layout()
                        st.pyplot(plt)
                    ##################################################################################################
                    Ranked_resumes2=pd.merge(sj_sc.rename(columns = {'Noms': 'Nom'}, inplace = False), Ranked_resumes[['Nom','Cleaned']] , how='left',on="Nom")
                    #st.write(Ranked_resumes2)
                    option_3 = st.selectbox("Montrer les CV les mieux assortis ?", options=[
                    'OUI', 'NON'],key=1)
                    if option_3 == 'OUI':
                        if len(Ranked_resumes2['Nom']) <= 1:
                            indx=0
                        else:
                            indx = st.slider("Quel CV afficher ?",
                                        1, Ranked_resumes2.shape[0], 1,key=1)

                        #st.write("Affichage du CV avec le rang : ", indx)
                        st.markdown(" ")
                        st.markdown("## **Curriculum vitae** ")
                        st.markdown("#### "+"Ce candidat occupe le rang : "+str(indx)+" Avec un score de : "+str(Ranked_resumes2.iloc[indx-1, 4]))
                        value = Ranked_resumes2.iloc[indx-1, 6]
                        #st.markdown("#### Le nuage de mots pour le CV")
                        
                        wordcloud = WordCloud(stopwords = my_stop_words,width=700, height=700,
                                            background_color='white',
                                            colormap='viridis', collocations=False,
                                            min_font_size=10).generate(value)
                        plt.figure(figsize=(3, 3), facecolor=None)
                        plt.imshow(wordcloud)
                        plt.axis("off")
                        plt.tight_layout(pad=0)
                        st.pyplot(plt)


                    

                    




elif choice == "Inscription":
    
    st.subheader("Créer un nouveau compte")
    new_user = st.text_input("Email")
    new_password = st.text_input("Mot de passe",type='password')
    

    if st.button("Inscription"):
        #pour valider l'entrée email
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if(re.search(regex, new_user)):
            new_user
        else:
            st.error("Email non valide")
            st.stop()
        create_table()
        add_userdata(new_user,make_hashes(new_password))

