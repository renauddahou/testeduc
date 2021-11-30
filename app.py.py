from db import *
import streamlit as st
import pandas as pd
import re
import random
import streamlit.components.v1 as components
from streamlit_player import st_player
from PIL import Image
#st.set_page_config(layout="wide")
st.set_page_config( 
layout="wide",  
initial_sidebar_state="auto",
page_title= "EducPython",   
)
#page_icon= "Images/Favicon.png",


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

def style():
    st.markdown("""<style>
    div[data-baseweb="select"]> div {
    background-color: yellow;
    } 
    div[role="listbox"] ul {
    background-color:white;
    }</style>""", unsafe_allow_html=True)

def style2():
    st.markdown(
    """
    <style>
    .reportview-container .markdown-text-container {
        font-family: monospace;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    .Widget>label {
        color: white;
        font-family: monospace;
    }
    [class^="st-b"]  {
        color: white;
        font-family: monospace;
    }
    .st-bb {
        background-color: transparent;
    }
    .st-at {
        background-color: #0c0080;
    }
    footer {
        font-family: monospace;
    }
    .reportview-container .main footer, .reportview-container .main footer a {
        color: #0c0080;
    }
    header .decoration {
        background-image: none;
    }

    </style>
    """,
        unsafe_allow_html=True,
    )

#menu
st.sidebar.title("Navigation 👇")
menu = ["Accueil", "Connexion", "Inscription"]
choice = st.sidebar.selectbox(" ",menu)
    


if choice == "Accueil":

        html_temp = """
        <div class="mySlides fade">
            
        <img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20200707215302/Best-Way-To-Start-Learning-Python-%E2%80%93-A-Complete-Roadmap.png" style="width:100%;border-radius:5px;">  
        </div>
        """
        #components.html(html_temp)
        st.markdown(html_temp, unsafe_allow_html = True)
        # Titre
        html_temp = """
		<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:3px;">
		<h1 style="font-family: 'BadaBoom BB', sans-serif;color:white;text-align:center;"><b>📈 EducPython 📊</b></h1>
		</div>
		"""
        st.markdown(html_temp, unsafe_allow_html = True)
        # Embed a youtube video
        #st_player("https://www.youtube.com/watch?v=idPDzWybHMw")
        app_temp = """
                    <iframe src="https://www.youtube.com/watch?v=idPDzWybHMw" width="100%" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
                    """
        st.markdown(app_temp, unsafe_allow_html = True)
        
        st.sidebar.info(
            """
        👆 Utilisez la barre de navigation ci-dessus pour créer votre compte, vous connecter et vivre cette expérience avec nous !
        """)

elif choice == "Connexion":
    with st.sidebar.beta_expander(""):
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
                st.subheader("")

                # Titre
                title_temp = """
                <div style="background-color:#464e5f;padding:5px;border-radius:5px;margin:5px;">
                <h1 style ="color:white;text-align:center;">📈 EducPython 📊 </h1>
                </div>
                """
                #<i><h2 style ="color:white;text-align:center;"> Start your training 📑</h2></i>
                st.markdown(title_temp, unsafe_allow_html = True)

                ##Rdio button 
                st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center;} </style>', unsafe_allow_html=True)

                st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

                genre = st.radio("",("Python pour les enfants", "Python pour les débutants", "Python Avancé", "Python pour les Datascientist","Python pour les Financiers"))


                
                    
                col1, col2 = st.beta_columns([50,10])
                with col2:
                    st.write("")
                    button1=st.button("SEE ANSWER")
                    button2=st.button("RANDOM EXO")
                    button3=st.button("RDM ANSWER")
                    
                    
                    

                with col1:
                    with open('file.py') as f:
                        Ex01 = f.read()
                    
                    Ex02 = '''print("welcome to Educpython")'''
                    choice = st.selectbox("",["Exo1","Exo2"])
                    if choice== "Exo1":
                        exo=st.code(Ex01, language = 'python')
                    elif choice== "Exo2":
                        exo=st.code(Ex02, language = 'python')

                    if button1:
                        st.write("**Solution"+" "+choice+"👇**")
                        Exo3r=exo
                    
                    if button2:
                        choicex = random.choice(["Ex01","Ex02"])
                        choicelst = globals()[choicex] #tranformation de string en variable

                        st.write("**Random Exercice 👇**")
                        Exo1r=st.code(choicelst, language = 'python')
                    
                        
                    if button3:
                        st.write("**Random Solution 👇**")
                        Exo3r=st.code(Ex02, language = 'python')

                with col1:
                    st.markdown("**Exécutez votre code dans la notebook Jupyter pour plus d'expérience.** 👉 👉 👉[![Foo](https://jupyter.org/assets/main-logo.svg)](https://jupyter.org/try)")

                    app_temp = """
                    <iframe src="https://www.programiz.com/python-programming/online-compiler/" width="100%" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
                    """
                    st.markdown(app_temp, unsafe_allow_html = True)


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

    st.title("10 CONSEILS PRATIQUES POUR DÉCROCHER UN JOB EN DATA SCIENCE MÊME EN ÉTANT DÉBUTANT :sleuth_or_spy:")
    
    image = Image.open('im/im1.jpeg')
    st.image(image, caption='Sunrise by the mountains',width=700)
    
    st.markdown(
        """
        C’est le meilleur moment pour devenir Data Scientist. La matière première en Data Science, c’est-à-dire les données,
            est partout. Les entreprises recherchent de plus en plus des Data Scientists qualifiés qui pourront les aider à tirer
            profit de cette grande masse de données disponible pour améliorer leur compétitivité.\n\n\n

        La moisson est bonne mais il y a peu d’ouvriers. En effet, l’offre en professionnels DATA est faible tandis que la demande 
        s’accroît de manière exponentielle. Il est alors temps que vous saisissiez les plus belles opportunités qu’offre ce secteur. 
        Il est temps que vous décrochiez l’emploi de vos rêves en Data Science.\n\n\n

        Dans cet article, je vous donne 10 conseils pratiques pour décrocher le job de vos rêves en Data Science même en étant débutant. 
        Lisez cet article jusqu’à la fin car le dixième conseil est très précieux mais souvent négligé par les chercheurs d’emploi.\n\n\n
        ## **Identifier le poste/rôle qui vous intéresse vraiment** \n
        """,
                    unsafe_allow_html=True,
                )
    image = Image.open('im/im2.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        La Data Science est un domaine très vaste qui regroupe plusieurs types de métiers comme : Data Analyst, Data Engineer, Business 
        Analyst, Machine Learning Engineer, Research Scientist, Data Scientist, Data Architect, etc. Étant donné, à moins d’être un Ninja, 
        que vous ne pouvez pas être qualifié dans tous ces rôles, il est primordial de choisir le métier qui vous passionne réellement et 
        par conséquent dans lequel vous êtes sûrs de toujours vous épanouir.\n\n\n

        Par exemple, le Data Engineer a un profil de Développeur spécialisé dans la Data tandis que le Data Scientist a plutôt un profil 
        ressemblant à celui d’un Statisticien avec une bonne compréhension des modèles d’apprentissage automatique (ce qui veut dire un peu 
        de Mathématiques).\n\n\n

        ## **Trouvez des offres d’emploi en Data Science** \n
        """,
                    unsafe_allow_html=True,
                )
    image = Image.open('im/im3.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Il existe plusieurs sites où vous pouvez trouver des offres d’emploi en général et particulièrement en Data Science. 
        Les sites les plus populaires sont : Indeed, Linkedin, Glassdoor, et Google Jobs. Lorsque vous êtes sur un site dans 
        le but de rechercher des offres d’emploi sur le métier qui vous intéresse, il est conseillé de ne pas se focaliser sur 
        un seul mot clé. Par exemple, si vous êtes intéressé par un poste de Data Scientist, ne cherchez pas seulement avec le 
        mot clé data scientist ou data science. Vous devez étendre vos recherches en essayant d’autres mots clés. Vous pouvez 
        essayer les noms d’outils que vous aimez bien utiliser. Par exemple : python, Scikit-Learn, Tensor Flow, etc. Vous 
        pouvez aussi essayer d’autres noms de métiers tels que : data analyst, statisticien, etc. En effet, les recruteurs 
        n’ont pas forcément la même conception des métiers que vous et vous pouvez donc être surpris de trouvez le job de 
        vos rêves dans une catégorie que vous n’auriez pas deviné.\n\n\n

        Il est essentiel de toujours lire les descriptifs de poste afin de bien comprendre les tâches assignées à un poste.\n\n\n

        ## **Ne chercher pas à cocher toutes les cases avant de postuler** \n
        """,
                    unsafe_allow_html=True,
                )

    image = Image.open('im/im4.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Certaines personnes lisent les descriptifs de poste en Data Science et se découragent parce-qu’elles ne cochent pas toutes les 
        cases. Croyez-moi, cette attitude est la meilleure façon de ne jamais trouver l’emploi dont vous rêvez.\n\n\n

        Je vais peut-être vous choquer mais sachez qu’une grande partie des descriptifs de poste sont des mensonges. En effet, certains 
        recruteurs mettent la barre très haute histoire de déjà filtrer un bon nombre de personnes. Pour la petite anecdote, une de mes 
        connaissances qui travaille dans une grande entreprise de la place m’a fait remarquer que le descriptif du poste qu’il occupe 
        actuellement était en résumé : Data Scientist maîtrisant Tensor Flow, les frameworks du Big Data et le déploiement de modèles 
        de Machine Learning. Les tâches qu’il fait réellement au quotidien sont : analyse de données provenant de fichiers excel, requêtes 
        SQL et visualisation de données. Quel décalage entre ce qui était mentionné dans le descriptif de poste et ce qu’il fait dans la 
        réalité !!! Je ne dis pas que toutes les entreprises ont cette pratique mais il y en a plusieurs qui le font. En faisant ainsi, 
        elles cherchent non seulement à filtrer les candidatures dès le début du processus mais aussi à impressionner leurs concurrents 
        soit-disant qu’elles sont à la pointe de la technologie : c’est du PIPO :).\n\n\n

        Tout ceci pour vous dire que lorsque la mission vous plaît et que vous sentez que vous en êtes capables, foncez ! Envoyez votre 
        candidature. Vous n’avez rien à perdre. Il est d’ailleurs rare de trouver un candidat qui coche absolument toutes les cases et les 
        recruteurs en sont aussi conscients. Ce serait dommage de rater l’opportunité de votre vie parce-que vous vous êtes dégonflé avant 
        même le début du combat.\n\n\n

        ## **Avoir un Portfolio de projets pour montrer vos compétences** \n
        """,
                    unsafe_allow_html=True,
                )

    image = Image.open('im/im5.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Démontrer ce que vous savez faire aux potentiels employeurs est toujours mieux que de raconter votre vie dans un CV long comme 
        le bras :) Juste pour vous dire qu’il faut toujours être dans la logique de démonstration de vos compétences. La meilleure manière 
        de montrer vos compétences est de disposer d’un portfolio (portefeuille) de projets impressionnants qui montrent que vous avez les 
        compétences requises pour le Job.\n\n\n

        Avant de vous dire comment construire votre Portfolio, je dois d’abord vous expliquer ce qu’est réellement un portfolio en 
        data science. Le Portfolio est la preuve publique de vos compétences. C’est un ensemble de projets réels que vous avez réalisé 
        et qui montrent que vous êtes réellement capables de telle ou telle autre chose. J’insiste sur le terme “preuve publique” car 
        si vos projets réalisés, aussi impressionnant qu’ils soient, sont cachés dans un dossier quelque part dans votre ordinateur 
        alors il ne s’agit pas de Portfolio. Vous devez pouvoir les montrer publiquement. Par ailleurs, en matière de construction de 
        portfolio, ce n’est pas la quantité qui compte mais plutôt la qualité. De plus, les projets dans votre portfolio doivent être 
        en adéquation parfaite avec le métier que vous visez. Une personne qui vise un poste de Data Engineer par exemple n’aura pas le 
        même type de portfolio qu’une personne visant un poste de Business Analyst ou un poste de Formateur en Data Science.\n\n\n

        Pour créer votre portfolio en Data Science, vous avez besoin principalement de deux choses : des **données** et un **problème à résoudre**.\n\n\n

        En ce qui concerne les données, il ne s’agit pas d’aller télécharger un “pauvre” petit fichier Excel sur internet qui ne vous a même pas pris une 
        seconde pour le faire. Les données que vous utilisez pour apprendre la Data Science comme le jeu de données Iris ou Titanic n’intéressent 
        pas les recruteurs. Vous devez chercher de réels jeux de données relatifs à une problématique très intéressante dont l’évocation dans votre 
        projet prouvera votre compétence en matière de collecte, de centralisation, de standardisation et de nettoyage des données. Vous pouvez 
        par exemple chercher des données via des API de réseaux sociaux (Twitter, Facebook, etc.) ou d’autres sites connus, des bases de données SQL, 
        du web scraping, des données financières, des données textuelles que vous avez dû traiter pour les rendre exploitable, ou même construire vos 
        propres ensembles de données par des sondages, enquêtes, expérimentations, etc.\n\n\n

        Après avoir bien réaliser votre projet, vous devez le montrer au monde. Pour cela, plusieurs possibilités s’offrent à vous dont : 
        la publication dans un répertoire GitHub ou dans votre Blog dédié à votre portfolio. GitHub est très connu par la communauté de Data 
        Scientists et donc un excellent moyen de montrer au monde vos compétences. Si vous utilisez ce canal, n’oubliez pas de toujours ajouter 
        un readme à chacun de vos projets afin d’expliquer le contexte, la problématique et la démarche suivie pour résoudre le problème.\n\n\n

        ## **Participer aux compétitions en Data Science** \n
        """,
                    unsafe_allow_html=True,
                )

    image = Image.open('im/im6.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Je m’en voudrai de ne pas vous donner cette autre manière de prouver vos compétences en data Science. Il s’agit des compétitions 
        sur des sites tels que Kaggle et Driven Data. Ces plateformes sont selon moi les plus célèbres en matière de compétitions en Data 
        Science. Les projets mis en compétition sont de réels projets d’entreprises très connues dans le monde entier. Les projets sont de 
        très grande envergure avec des prix allant parfois jusqu’au million de $. Même si vous ne gagnez pas à un prix et que vous avez 
        quand même un bon score (parmi les 10 premiers par exemple), cela va booster considérablement votre employabilité et c’est une 
        solide preuve irréfutable que vous avez des compétences en Data Science. Plusieurs personnes ont été recruté suite à leur brillante 
        participation à ce genre de compétitions. L’idée même des entreprises qui soumettent des projets sur ces plateformes est de pouvoir 
        recruter les gagnants au sein de leur équipe DATA.\n\n\n

        Choisissez la plateforme que vous voulez (j’affectionne particulièrement Driven Data) ainsi que les projets qui vous intéressent et 
        compétissez. Vous y apprendrez beaucoup de nouvelles choses et vous améliorerez positivement votre réputation. Les compétitions sont 
        très bénéfiques.\n\n\n

        Je lancerai bientôt une formation sur Comment participer et gagner à une compétition en Data Science.\n\n\n

        ## **Créer un CV optimisé et adapter au poste recherché** \n
        """,
                    unsafe_allow_html=True,
                )

    image = Image.open('im/im7.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Les recruteurs reçoivent des milliers voir des millions de candidatures pour une seule offre d’emploi. Comprenez qu’ils sont humains
        et ne peuvent donc pas tout lire. Vous devez faire en sorte que votre CV sorte du lot. Voici 5 conseils pour créer un CV optimisé 
        qui attire l’attention du recruteur :\n\n\n

        * Lister vos compétences techniques : dans cette section du CV, il ne s’agit pas d’écrire une page de logiciels et de frameworks que vous prétendez maîtriser comme si vous étiez à vous seul un département informatique :). Il s’agit de lister les outils incontournables pour le poste tout en employant les appellations officielles. Placez les vrais mots clés au bon endroit.\n\n\n
        * Personnaliser votre section “Expériences professionnelles” : Les expériences que vous citez à ce niveau doivent être en accord avec l’offre à laquelle vous postuler. Si vous n’avez pas ou pas assez d’expériences, n’hésitez pas à décrire vos projets réalisés qui cadrent avec l’offre. Les projets sont de très bons substituts à de réelles expériences professionnelles et très appréciés par les vrais recruteurs.\n\n\n
        * Limiter votre CV à une page lorsque vous postulez en entreprise : Il est admis que dans le monde des affaires, les gens n’aiment pas lire des documents trop longs. Il faut être concis et précis. Vous pouvez aller à 2 ou 3 pages lorsque vous postulez dans le domaine de la recherche scientifique (Laboratoire, Université, Institut de recherche, etc.)\n\n\n
        * Lister vos diplômes et certifications en adéquation avec le poste : Les certifications que vous avez obtenu sur des plateformes en ligne montrent aux recruteurs que vous êtes une personne qui continue de se former et de se mettre à jour. Si vous postulez par exemple pour un poste de Machine Learning Engineer, en plus de votre diplôme, vous pouvez ajouter quelques certifications obtenues dans le domaine du Machine Learning.\n\n\n
        * Mettre des liens vers votre profil Linkedin, GitHub et votre blog : Linkedin est un puissant réseau professionnel. Veillez à bien optimiser votre profil. Vous devez avoir le badge “Open to Work”, mettre les bons mots clés au niveau des sections “Expérience” , “Formation” et “Compétence”. Ajoutez aussi à votre profil quelques certifications pertinentes en lien avec le poste visé. Par ailleurs, Linkedin n’est pas Facebook ou Instagram. Vous devez avoir une photo professionnelle et un titre efficace. Vous pouvez aussi réseauter avec des personnes travaillant dans les entreprises qui vous intéressent. Il ne s’agit pas d’harceler les gens. Tout est dans la tactique. Le mot d’ordre est : donner pour recevoir. Soyez naturels et dans le partage.\n\n\n

        En ce qui concerne votre compte GitHub, vous devez sélectionner les projets à partager. C’est la qualité qui compte et non la 
        quantité. Pour chaque projet, il est important d’ajouter un Readme avec les éléments suivants : description du projet, explication
        de la manière dont le code doit être exécuté, liste des potentiels bugs et comment les résoudre, liste des principaux résultats.\n\n\n

        Vous n’êtes pas obligé de créer votre propre site web pour avoir un blog. Vous pouvez créer un compte sur des plateformes telles que 
        medium et y poster vos articles. Pas besoin d’être un expert en écriture. Écrivez simplement sur les sujets qui vous passionnent et 
        partagez vos expériences.\n\n\n

        ## **Développer votre réseau** \n
        """,
                    unsafe_allow_html=True,
                )

    image = Image.open('im/im8.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Trouvez un job de nos jours, ce n’est plus tellement ce que vous connaissez mais beaucoup plus qui vous connaissez. ATTENTION ! 
        Je ne suis pas en train de dire que vous n’avez pas besoin d’avoir des compétences relatives au poste visé, mais je veux attirer 
        votre attention sur le fait de ne pas négliger la puissance des réseaux. Lorsqu’on parle de réseau, il s’agit de relations. 
        Votre réseau doit être constitué non seulement de personnes que vous pensez qu’elles peuvent vous aider mais aussi et surtout 
        de personnes que vous pouvez aider. En aidant une personne, elle peut vous recommander dans son entourage, partager votre CV, 
        votre blog, etc. Pour vous connecter à de nouvelles relations, vous pouvez participer à des conférences, des réunions de groupe 
        sur des thématiques en data science, rechercher des personnes sur les réseaux sociaux, participer à des rencontres d’anciens 
        élèves/étudiants, etc.\n\n\n

        
        Une autre façon, non négligeable, qui vous permettra de développer votre réseau est le volontariat. Vous pouvez consacrer une partie 
        de votre temps à des Associations, des Organisations Non Gouvernementales (ONG), etc. Cela augmente votre visibilité et vous permet 
        d’avoir de nouvelles relations et de développer ainsi votre réseau. Toutes choses utiles dans votre recherche d’emploi.\n\n\n

        ## **Demander des recommandations** \n
        """,
                    unsafe_allow_html=True,
                )

    image = Image.open('im/im9.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Si vous avez un bon réseau et que vous savez parler poliment aux gens alors il vous sera très facile de demander des recommandations. Tout d’abord, il vous 
        faudra identifier les bonnes personnes qui peuvent vous recommander. Vous n’allez pas demander une recommandation à votre copine ou copain ou à un chercheur d’emploi comme vous ! 
        Il vous faut trouver dans votre réseau des personnes qui travaillent dans l’entreprise qui vous intéresse et dans laquelle vous avez postulé à un poste. Une recommandation faite 
        par un employé dans l’entreprise que vous visez est très efficace. Vous pouvez trouver cette personne dans votre réseau Linkedln par exemple. Vous pouvez aussi demander à des anciens 
        employeurs avec qui vous avez de très bonnes relations de vous recommander.\n\n\n

        ## ** Bien se préparer pour un entretien** \n
        """,
                    unsafe_allow_html=True,
                )

    image = Image.open('im/im10.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Certaines entreprises (malheureusement elles sont rares) fournissent aux candidats sélectionnés leurs guides de préparation aux entretiens. Si vous êtes dans ce cas, SUPER ! Utilisez précieusement 
        ce guide pour vous préparer.\n\n\n

        Sinon, vous pouvez demander à la personne qui vous recevra en entretien, les sujets qui seront évoqués, surtout les aspects techniques. Il n’y a pas de mal à demander cela et d’ailleurs cela montre 
        davantage votre intérêt pour le poste. Un recruteur ne va pas annuler votre entretien parce-que vous lui avez demandé des informations pour mieux vous préparer à le rencontrer. Au contraire, les recruteurs 
        apprécient ce genre de candidats. L’idée est de rassembler plusieurs informations pour vous aider à bien vous préparer pour l’entretien.\n\n\n

        Je sortirai bientôt un guide technique pour bien réussir un entretien pour un poste en Data Science. Le guide couvrira les aspects techniques en Statistique, Python, Machine Learning, etc.\n\n\n

        l est très important de bien connaître l’entreprise qui vous reçoit. Vous pouvez aller sur son site web par exemple pour en apprendre davantage sur elle comme son secteur d’activité, ses produits et 
        services, son environnement DATA, ses objectifs, ses types de clients, etc. Toutes ces informations vous donnent déjà des idées sur ce que vous pouvez leur apporter réellement. Vous pouvez aussi trouver 
        des avis sur une entreprise sur des sites comme Glassdoor, Indeed, etc. Gardez les choses positives. Si vous allez à votre entretien avec des préjugés sur la boîte, alors c’est perdu d’avance. Soyez toujours positif.\n\n\n

        Relisez à plusieurs reprises le descriptif de poste. Certaines informations s’y trouvant indiquent déjà les questions que le recruteur est susceptible de vous poser. Il est absolument nécessaire de bien comprendre la 
        mission assignée au poste.\n\n\n

        Pour finir, quelque soit l’issue d’un entretien, vous devez toujours capitaliser sur cette expérience. Si par exemple, la réponse est négative, essayer de toujours garder une bonne relation avec la personne qui vous a 
        reçu en entretien. Vous pouvez par exemple lui envoyer une demande de connexion sur Linkedin. Vous pouvez même lui demander les choses que vous devez améliorer. Ceci vous permettra de ne pas refaire les mêmes erreurs 
        pour d’autres entretiens. Vos retours d’expérience d’entretiens sont une mine d’or pour vous aider à vous améliorer et augmenter votre employabilité.\n\n\n

        ## **Envoyez des candidatures spontanées** \n
        """,
                    unsafe_allow_html=True,
                )


    image = Image.open('im/im11.png')
    st.image(image, caption='Sunrise by the mountains',width=700)
    st.markdown(
        """
        Les candidatures spontanées sont un puissant levier pour trouver un job en général et un job dans la Data Science en particulier. 
        Si cette stratégie est connue par les chercheurs d’emploi, elle est moins utilisée par ces derniers.\n\n\n

        Lorsque vous répondez à une offre d’emploi, vous faites tout pour cadrer aux souhaits de l’entreprise. C’est 
        comme si vous devez vous modeler pour lui plaire : adapter votre CV à son offre d’emploi, réaliser un portfolio 
        qui cadre avec le poste visé, etc. Dans ce contexte, vous êtes (on ne va pas mâcher les mots) en position de demandeur 
        et donc de faiblesse. ATTENTION ! Vous demandez mais vous ne devez pas quémander :)\n\n\n

        Dans le cas d’une candidature spontanée, c’est vous qui avez le contrôle. Vous partez dans un esprit de conquérant. Vous êtes 
        là pour proposer vos services en démontrant dans votre candidature ce que vous pouvez apporter à l’entreprise pour l’aider à 
        augmenter ses performances.\n\n\n

        Il arrive qu’une entreprise, surtout les petites et moyennes, ne sache pas l’utilité de la Data Science pour ses activités et 
        donc ne crée pas de postes pour ça. Mais en recevant des candidatures spontanées, cela peut l’aider à se décider. Très souvent 
        ce genre d’entreprises vous propose une sorte de période d’essai qui peut déboucher sur un CDI.\n\n\n

        Les candidatures spontanées montrent aussi l’intérêt que vous portez à la société. Donc n’hésitez pas à utiliser cette stratégie.\n\n\n

        J’espère que vous avez aimé lire cet article comme moi j’ai aimé l’écrire et vous le partager. Je vous prie de le partager à votre tour
        pour que beaucoup de personnes puissent utiliser ces conseils pratiques afin de décrocher le job de leurs rêves.\n\n\n

        Si vous connaissez d’autres conseils pour décrocher un job en Data Science, merci de les partager en commentaires avec la communauté.\n\n\n

        Vous débutez en Data Science, contactez-moi pour des formations pratiques basées sur des projets et totalement personnalisées : **afouda.josue@gmail.com**\n\n\n
        """,
                    unsafe_allow_html=True,
                )

    
    st.markdown(
        """
        Retrouvez-moi aussi sur ma chaîne YouTube  [**J.A DATATECH CONSULTING**](https://www.youtube.com/channel/UCpd56FfjlkKbkHlbgY6XE3w) et sur ma page [**Amazon KDP **](https://www.amazon.fr/Josu%C3%A9-AFOUDA/e/B08F17S1V8/ref=dp_byline_cont_pop_book_1) où j’ai publié plusieurs livres sur 
        la Data Science, la Statistique, le Machine Learning, la programmation avec Python et R ainsi que le développement d’applications 
        web R Shiny.
        """,
                    unsafe_allow_html=True,
                )






