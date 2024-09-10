import streamlit as st
# ---------- Home ---------- #
info = {
    "Name": "Julien",
    "Full_name": "Julien MAHIETTE",
    "image": "images/IMG_6849.png",
    "Position": "Data analyst / Data analytics engineer",
    "Intro": """
                👋 Hi, I'm Julien, an enthusiastic and passionate data analyst located in France who enjoys helping people manage their data and get meaningful insights from it.<br>
                With experience in various fields and a successful internship as a data analyst,
                I am seeking unique challenges to broaden my knowledge and expertise.

                🧑‍🦱 After spending 5 years abroad, I decided to advance my career by becoming a data analyst, a field in which I see a lot of potential 
                and a great opportunity to further develop myself.

                👨‍💻 Professional interests: Data quality, data visualization, meaningful insights, data pipelines.

                ✈️ 🥘 Personal interests: I love traveling, cooking & eating good food, and having a nice coffee. I believe that cooking while traveling helps
                people connect with one another and broadens our perspectives.

                💬 Ideal career: Data analyst, data analytics engineer
            """,

    "City": "Annoeullin, 59112, Nord, FRANCE",
    "LinkedIn": "https://www.linkedin.com/in/julienmahiette/",
    "Email": "julien.mahiette@gmail.com"
}



skillset_images = {
    "Python" : "images/python.svg",
    "Sql" : "images/sql.svg",
    "Streamlit" : "images/streamlit.webp",
    "PowerBi" : "images/powerbi.svg",
    "Aws" : "images/aws.svg",
    "Airflow" : "images/airflow.png",
    "Dbt" : "images/dbt.png",
}

# ---------- Education ---------- #
education_info = {
    "wcs": {
        "logo": "images/education/wcs.webp",
        "degree": "Certification Data analyst RNCP 6",
        "school": "Wild Code School",
        "when": "2023",
        "what": """
            A 5 months intensive bootcamp where I gained foundational knwoledge in data alalysis:
            - Understanding the role of the data analyst.
            - Learning Python and Sql.
            - Learning visualization with Power Bi and Streamlit with Plotly.
            - Agile management methods.
            - Introduction to machine learning.
                """
    },
    "iae": {
        "logo": "images/education/iae.png",
        "degree": "Bachelor in economics, law and management",
        "school": "IAE",
        "when": "2016 - 2017",
        "what": """
            A year in which I gained specilized knowledge in the specific requirements of businesses in the retail sector:
            - Management and sociology.
            - Marketing & e-marketing.
            - Economics and finance.
            - Supply chain management.
                """
    },
    "pasteur": {
        "logo": "images/education/pasteur.png",
        "degree": "BTS specialised in sales",
        "school": "Pasteur high school",
        "when": "2014 - 2016",
        "what": """
            Two years spent mastering advanced sales techniques:
            - Sales.
            - Sales management & marketing.
            - Economics & statistics.
                """
    },
    "haut_de_flandres": {
        "logo": "images/education/academie_lille.png",
        "degree": "Profesionnal vocation degree specialised in sales",
        "school": "Haut de flandres vocation school",
        "when": "2012 - 2014",
        "what": """
            Two years spent learning the basics of sales:
            - Sales.
            - Sales management.
            - Economics & statistics.
                """
    },
    "st_marie": {
        "logo": "images/education/ste_marie.png",
        "degree": "Profesionnal vocation degree specialised in catering",
        "school": "Sainte Marie hotel & catering school",
        "when": "2009 - 2012",
        "what": """
            Three years spent learning the basics of catering:
            - Cooking and waiting
            - Cost management & accounting.
            - Local and international specialities.
                """
    },          
}

# ---------- Experiences ---------- #
experience_info = {
    "nhood": {
        "tab": "Data",
        "country": "France",
        "city": "Villeneuve d'Ascq",
        "logo":"images/experience/nhood.png",
        "job": "Data analyst",
        "company": "Nhood",
        "contract": "Intership",
        "period": "September 2023 - September 2024",
        "duration": "1 year",
        "what": """
                Working 1 year as a data analyst on a couple of topics:

                - **Adhoc analysis for the compliance department**:
                    - **Purpose**: Identify customers who received more than 30% discount on their fixed charge within a year. This helps the compliance team identify issues, contact the sales team for explanations, and identify potential corruption.
                    - **How**: I used SQL to retrieve the data and Excel to compile a detailled list of customers.
                    - **Challenge**: Understanding the requirements of compliance.

                <br>

                - **Report for the performance department**:
                    - **Purpose**: Create a report that provied the performance team with meaningful insight, enabling them to better understand their data, make quicker decisions, and reduce repetitive data manipulation in Excel.
                    - **How**: Since all the data was stored in Excel files, I used Python to aggregate historical data and create a clean CSV file. I employed Power Bi to automate the loading of new Excel file added monthly in SharePoint, performed data manipulation, and created a meaningful report. I also used SQL to retrieve additional data for the report.
                    - **Challenge**: The client was uncertain about their needs but required quick results. The Excel files were unclean and inconsistent, making the visialization challenging to create.
                
                <br>

                - **Data quality tool**:
                    - **Purpose**: Develop an easy-to-use tool for the asset management department that helps users check the quality of their CSV and Excel files.
                    - **How**: Building on a personal tool I had already developed, I added quality controls specific to asset management.
                    - **Challenge**: Finding a technical stack that fits the company while adhering to high standards of security and confidentiality.
                """
    },

    "ragt": {
        "tab": "France",
        "country": "France",
        "city": "Annoeullin",
        "logo":"images/experience/ragt.png",
        "job": "Reseach operator",
        "company": "Ragt",
        "contract": "Seasonal",
        "period": "July 2022 - February 2023",
        "duration": "8 months",
        "what": """
                Temporary work I found when I came back from Australia

                - **During the high season**:
                    - Harvesting colza by hand and making sure each section is identified.
                    - Drying Colza.
                    - Collecting the colza seeds and making samples for analysis.

                <br>      

                - **During the low season**:
                    - Preparing the seedlings.
                    - Preparing the plants in the greenhouse.
                    - Managing the colza seed sampling of over 180 000 varieties.

                """
    },
    
    "carte_crepes": {
        "tab": "Abroad",
        "country": "Australia",
        "city": "Melbourne",
        "logo":"images/experience/carte_crepes.png",
        "job": "Restaurant manager",
        "company": "Carte Crepes",
        "contract": "Seasonal",
        "period": "March 2021 - December 2021",
        "duration": "10 months",
        "what": """
                Great hospitality experience has manager / all rounder in a crepe shop in Melbourne University

                - **All rounder**:
                    - Taking orders.
                    - Making crepes and coffees.
                    - Cashing.
                    - Cleaning.

                <br>        

                - **Manager**:
                    - Opening the store.
                    - Controling the stock.
                    - Managing a small team
                    - Teaching new students the job.
                    - Closing the store
                """
    },

    "leeuwin_estate": {
        "tab": "Abroad",
        "country": "Australia",
        "city": "Margaret River",
        "logo":"images/experience/leeuwin.png",
        "job": "Farm hand pruner",
        "company": "Leeuwin Estate",
        "contract": "Seasonal",
        "period": "June 2020 - September 2020",
        "duration": "4 months",
        "what": """
                A great farming experience as pruner in a vineyard.

                - Vine pruning.
                - Taking care of the small vines in the nursery.
                """
    },

    "mr_apple_farmhand": {
        "tab": "Abroad",
        "country": "New Zealand",
        "city": "Hawke's Bay",
        "logo":"images/experience/mr_apple.png",
        "job": "Farm hand",
        "company": "Mr Apple",
        "contract": "Seasonal",
        "period": "Ocotber 2019 - February 2020",
        "duration": "5 months",
        "what": """
                A good farming experience with a large variety of tasks.
                """
    },   

    "thornill": {
        "tab": "Abroad",
        "country": "New Zealand",
        "city": "Hawke's Bay",
        "logo":"images/experience/thornill.png",
        "job": "Farm hand",
        "company": "Thornill",
        "contract": "Seasonal",
        "period": "June 2019 - August 2019",
        "duration": "3 months",
        "what": """
                An interesting farming experience building an orchard from scratch.
                """
    },

    "mr_apple_packing": {
        "tab": "Abroad",
        "country": "New Zealand",
        "city": "Hawke's Bay",
        "logo":"images/experience/mr_apple.png",
        "job": "Packer",
        "company": "Thornill",
        "contract": "Seasonal",
        "period": "April 2019 - June 2019",
        "duration": "3 months",
        "what": """
                A challenging packing experience in a factory.
                """
    },

    "renault_cdi": {
        "tab": "France",
        "country": "France",
        "city": "Englos",
        "logo":"images/experience/renault.png",
        "job": "Car salesman",
        "company": "Renault",
        "contract": "Permanent",
        "period": "December 2017 - February 2019",
        "duration": "1 year and 3 months",
        "what": """
                Developing the car dealership revenue by selling cars, loans, accessories and services.
                """
    },

    "auchan": {
        "tab": "France",
        "country": "France",
        "city": "Villeneuve d'Ascq",
        "logo":"images/experience/auchan.png.webp",
        "job": "Logistical assistant",
        "company": "Auchan",
        "contract": "Contractor",
        "period": "July 2017 - December 2017",
        "duration": "6 months",
        "what": """
                **Stock management focus on automotive and gardening product with at risk suppliers**.
                - Maintaining the stock of products in the warehouses by analyzing the stock history and actual tendency.
                - Verifying reception in the warehouses and dispatch to stores.
                """
    },

    "renault_trainee": {
        "tab": "France",
        "country": "France",
        "city": "Carvin",
        "logo":"images/experience/renault.png",
        "job": "Trainee car salesman",
        "company": "Renault",
        "contract": "Intership",
        "period": "2013 - 2016",
        "duration": "4 years",
        "what": """
                **Car dealership where I have done my intership during my studies, and also my summer and week-end job**.
                - **Intership**
                    - Developing the car dealership revenue by selling cars, loans, accessories and services.
                    - Marketing projects.

                <br>

                - **Week-end job (usually for open house days**):
                    - Welcoming and advising customers.
                    - Assist the customers during the car test drive.

                <br>    
                
                - **Summer job**:
                    - Cleaning up the car for deliveries.
                    - Delivering the car to customers and helping them to go throught the process of getting their new car.
                """
    },
}

# ---------- Contact ---------- #
contact_info = {
    "Full_name": "Julien Mahiette",
    "Phone_number": "0629951418",
    "Email": "julien.mahiette@gmail.com",
    "LinkedIn": "https://www.linkedin.com/in/julienmahiette/"
}

def comp_contact():
    st.sidebar.subheader("Contact", divider=True)
    st.sidebar.write(f"📞 {contact_info["Phone_number"]}")
    st.sidebar.write(f"📧 {contact_info["Email"]}")
    st.sidebar.page_link(
        page="https://www.linkedin.com/in/julienmahiette/",
        label="**LinkedIn**"
        )
    
# --------- LLM Prompt ---------- #
llm_prompt_info = {
    "French orthograph correction": {
        "description": """
                A prompt that:
                - Identify the orthograph and grammatical error in without correcting it ( You have time to think why you have made a mistake).
                - Correct your text.
                - Simple description of the mistakes.
                - Suggestion of rewording.
                - Some stats.
                
                <br>

                The purpose is to correct the user text and help him/her get better.

                """,
        "prompt": """
                Ton rôle est d'identifier et de corriger les fautes d'orthographe, de grammaire et de syntaxe. 
                Dans un premier temps, recopie mon texte entièrement et mets en évidence les fautes d'orthographe, de grammaire et de syntaxe. 
                Les fautes doivent être mises en évidence de cette façon : **fautes**. 
                Ensuite, montre-moi le texte entier et corrigé, en mettant en évidence les corrections apportées avec **correction**. 
                À la fin de ta réponse, je voudrais que tu expliques chaque faute en donnant une description très simple.

                Voici la structure de ta réponse :

                **Erreurs mises en évidence**
                Texte avec les fautes mises en évidence.

                **Texte corrigé**
                Texte corrigé avec les corrections mises en évidence.

                **Contrôle des fautes**
                Description simple des fautes trouvées et corrigées.

                **Suggestions de reformulation**
                Propositions pour améliorer la clarté et la fluidité du texte.

                **Statistiques des fautes**
                Nombre total de fautes trouvées et corrigées par catégorie (orthographe, grammaire, syntaxe).

                Si aucune faute n'est faite, tu devras uniquement répondre : "Quel exploit ! Aucune faute dans ce texte !"

                Tu peux également vérifier le style du texte et proposer des améliorations si nécessaire.

                Es-tu prêt ?
                    """
    },
    "English orthograph correction": {
        "description": """
                A prompt that:
                - Identify the orthograph and grammatical error in without correcting it ( You have time to think why you have made a mistake).
                - Correct your text.
                - Simple description of the mistakes.
                - Suggestion of rewording.
                - Some stats.
                
                <br>

                The purpose is to correct the user text and help him/her get better.

                """,
        "prompt": """
                Your role is to identify and correct spelling, grammar, and syntax errors. 
                First, copy my text entirely and highlight the spelling, grammar, and syntax errors. 
                The errors should be highlighted in this way: **errors**. 
                Then, show me the entire corrected text, highlighting the corrections made with **correction**. 
                At the end of your response, I would like you to explain each error by giving a very simple description.

                Here is the structure of your response:

                **Errors highlighted**:
                Text with the errors highlighted.

                **Corrected text**:
                Corrected text with the corrections highlighted.

                **Error check**:
                Simple description of the errors found and corrected.

                **Suggestions for reformulation**:
                Proposals to improve the clarity and fluidity of the text.

                **Error statistics**:
                Total number of errors found and corrected by category (spelling, grammar, syntax).

                If no error is made, you should only respond: "What an achievement! No errors in this text!"

                You can also check the style of the text and propose improvements if necessary.

                Are you ready?
                """
    }
}

# ---------- Portfolio ---------- #
portfolio_info = {
    "filecheck": {
        "main_page": {"image": "images/portfolio/filecheck/main_page.png",
                      "description": 
                        """
                        Welcome to the **main page** ! <br>
                        In here you can upload you file <br>
                        If you select "xlsx" you can specify which sheet you want to open <br>
                        and if you want to skips rows at the beggining of the sheet.
                        """
        },
        "overview1": {"image": "images/portfolio/filecheck/overview1.png",
                      "description": 
                        """
                        In the **overview** section you can see: <br>
                        - The number of column and rows
                        - The column names
                        - A data sample
                        """
        },
        "duplicates": {"image": "images/portfolio/filecheck/duplicates.png",
                "description": 
                """
                In the **duplicates** section you can: <br>
                - By default check full duplicates. (Entire rows)
                - By using the multiselection tool, check your custom duplicates
                """
        },
        "stats1": {"image": "images/portfolio/filecheck/stats1.png",
                "description": 
                """
                In the first part of the **stats** section you can see: <br>
                - Your columns name
                - Their types
                - Their number of missing values
                - Their number of unique values
                - If they can be considered as a unique key
                - And a data sample
                """
        },

        "stats2": {"image": "images/portfolio/filecheck/stats2.png",
                "description": 
                """
                In the second part of the **stats** section you can see complementary details of the above table: <br>
                - % of missing values
                - % of unique values
                - Minimum, maximum, median and mean for numerical values
                - Minimum and maximum lenght of the values
                - An historam for the numerical values
                - A wordcloud for the sequences of characters
                """
    },
        "graph1": {"image": "images/portfolio/filecheck/graph1.png",
                "description": 
                """
                In the first part of the **graph** section you can see: <br>
                - A visual representation of missing values
                """
    },
        "graph2": {"image": "images/portfolio/filecheck/graph2.png",
                "description": 
                """
                In the second part of the **graph** section you can see: <br>
                - A heatmap that help vizualise the correlation between variables
                """
    },
        "graph3": {"image": "images/portfolio/filecheck/graph3.png",
                "description": 
                """
                In the third part of the **graph** section you can see a box plot: <br>
                - This allow you to vizualise quickly vizualise stats informations
                - Minimum and maximum values
                - Lower and upper fence
                - Median
                - Lower and upper outlier if there is
                """
    },
        "sandbox_uk": {"image": "images/portfolio/filecheck/sandbox_uk.png",
                "description": 
                """
                In the **sandbox uk** section you can: <br>
                - Play with you variables and combine them to find unique combination
                """
    },
},
    "car_sales_performance": {
        "global_car_sales": {
            "image": "images/portfolio/car_sales_performance/global_car_sales_performance.PNG",
            "description": 
            """
            In the **Global car sales performance** page, you have an overview of your nationwide sales. <br>
            You can analyse your performance either year-to-date or by month.
            """
        },
        "global_state_car_sales": {
            "image": "images/portfolio/car_sales_performance/global_state_performance.PNG",
            "description": 
            """
            In the **Global state performance** page, you can analyse your sales performance by state and compare results across states. <br>
            You have detailed insights to refine your analysis, helping you to understand why some states outperform others, <br>
            and you can communicate with the relevant teams if necessary.
            """
        },
        "state_performance" : {
            "image": "images/portfolio/car_sales_performance/state_performance.PNG",
            "description":
            """
            In the **State car sales performance** page, we delve deeper into the details <br>
            to assess how each dealership is performing.
            """
        },
        "data_model": {
            "image": "images/portfolio/car_sales_performance/data_model.PNG",
            "description":
            """
            The dataset is from Kaggle and is fairly basic. I performed some transformations, <br>
            added the states names(as the original dataset only had state codes), <br>
            and inclued a time table.
            """
        },
        "param_model": {
            "image": "images/portfolio/car_sales_performance/param_model.PNG",
            "description":
            """
            To make the dashboard more dynamic, I created several parameter fileds and linked them to a table. <br>
            Depending on my selection (value or count & monthly or YTD), the graphs and values adjust accordingly.
            """
        }
    }
}