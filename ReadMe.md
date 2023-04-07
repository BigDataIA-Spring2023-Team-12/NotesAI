# Assignement 5 : NotesAI

![MarriedShortGalapagossealion-size_restricted](https://user-images.githubusercontent.com/114712818/230681480-13e21bff-e7df-4da2-967d-fedef3d17932.gif)

## About 

Ever revisited the saved messages from different platforms?? Your important data is still out there, yet sitting idle being of no use! <br>

What if there was a smarter way of accessing your data from the past?<br>

What? Seriously?<br>

I want a application that can do that!!!! <br>

Not only that, our application will let you get your data in an ORGANIZED, STRUCTURED, SUMMARIZED and on top of that you can can QUERY random question to get important information which is PRECISE and SUCCINT! <br>

Woah!



This Smart Notes application is designed to help users organize and manage their saved messages from various platforms in a structured and efficient manner. The application allows users to categorize their saved messages may be it anything, a random code you saved, an important article you saved, literraly anything!!



The application utilizes advanced algorithms to extract relevant information from the saved messages and automatically categorize them into different folders based on their content. This makes it easy for users to find and retrieve specific messages quickly.

In addition, the Smart Notes app allows users to add tags and notes to their saved messages, which can further aid in organization and retrieval. The app also provides a search function that enables users to quickly find messages by keyword or tag.

The Smart Notes application is designed to be user-friendly and intuitive, with a simple and clean interface that allows users to navigate and access their saved messages easily. Overall, the app provides a powerful solution for anyone looking to manage their saved messages more efficiently and effectively.
1. Whisper:<br>
(https://openai.com/research/whisper) <br>
The Whisper system is an automatic speech recognition system technology that has been programmed using supervised data collected from the internet. This data comprises over 680,000 hours of multilingual and multitask information. By utilizing this vast and varied dataset, the system has demonstrated an increased ability to accurately transcribe speech regardless of accents, background noise or technical jargon. Additionally, the technology has the capability to transcribe multiple languages and translate them into English.<br><br>
For our service, we will use the whisper API to convert the audio file into processed transcripts which will be utilized by Chatgpt microservice to work upon the textual data.

2. ChatGPT:<br>
(https://platform.openai.com/docs/guides/chat) <br>
ChatGPT API is an API (Application Programming Interface) based on the GPT (Generative Pre-trained Transformer) architecture developed by OpenAI. It allows developers to integrate state-of-the-art natural language processing (NLP) capabilities into their applications, such as chatbots, virtual assistants, and other conversational interfaces. The API can generate human-like responses to a wide variety of prompts, including text-based input and voice-based input, making it a powerful tool for building engaging and intelligent conversational applications.<br><br>
For our service, we will utilize the Chatgpt API which will give answers to pre-defined prompts and user-defined prompts. The API will take the processed audio transcript as produced by whisper and answer general and user-given question based on the provided context. 




## Links
* Codelab Documentation - [Codelab](https://codelabs-preview.appspot.com/?file_id=1vdqyyXWdfmrKZww20KxfUh0Gximydyv3gAmIn1G1pTU/#0)
* GitHub Repository - [GitHub](https://github.com/BigDataIA-Spring2023-Team-12/NotesAI)


## LEARNINGS/TECH USED
Streamlit<br>
AWS<br>
SQLite<br>
WhisperAPI<br>
ChatGPT API<br>
Git (Version Control)<br>
Documentation on Codelabs<br>


## Process Flow

Process Flow :-

1. Browse for an audio file from the system's local files.
2. An upload button will store the audio file to an Amazon S3 bucket's folder.
3. Use Whisper API to process the audio file and convert to a textual transcript.
4. The whisper API will fetch the audio fie from S3 bucket's folder and store the processed file output into another bucket of S3 and SQLite db.
5. Define a generic questionaire for the meetings audio.
6. Use chatgpt API to get answers to these generic questions (send both the transcript and questions to chatgpt).
7. Write the output into a database along with the associated filename.
8. A select box drop-down on the streamlit interface will get list of all the files from the processed folder in the S3 bucket.
9. On selecting a specific file, display the generic questions with answers, and a text box for user questions and a submit button.
10. The submit button should again trigger the chatgpt api to get an answer and write in into the db.
11. Log user activity by storing the question and their responses.
12. Use airflow to automate workflow. Create 2 dags - adhoc process and batch process.
13. Adhoc process will be triggered on the file upload to S3 button.
14. Batch process will run once a day, using cron. The dag will process all the file collectively.



## Project Directory Structure


##### /streamlit
Includes the streamlit application interface for the user to interact with the whisper and chatgpt functionalities. It consists mutiple directories, with the required utilities. Launch the application by running "app.py". The dependent functions and utilities are written and imported from "utils". Also contains the SQLite db file initialized for storing questions data.  




## Run the project
1. Open terminal
2. Browse the location where you want to clone the repository
3. Write the following command and press enter 

````
 git clone https://github.com/BigDataIA-Spring2023-Team-12/Whispers-ChatGPT.git
 ````
 4. Create a virtual environment and activate
 ````
  python -m venv <Virtual_environment_name>
 ````
 5. Install the required dependencies using requirements.txt
 ````
  pip install -r /path/to/requirements.txt
 ````
6. Launch the application by firing up the app.py file in /streamlit




---
## Team Members
1. Harsh Shah - NUID: 002704406 - (shah.harsh7@northeastern.edu)
2. Parva Shah - NUID: 002916822 - (shah.parv@northeastern.edu)
3. Dev Shah - NUID: 002978981 - (shah.devs@northeastern.edu)



## Undertaking

> WE ATTEST THAT WE HAVEN’T USED ANY OTHER STUDENTS’ WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK
**Contribution**: 
*   Harsh Shah &emsp; :`33.33%`
*   Parva Shah &emsp; :`33.33%`
*   Dev Shah &emsp;   :`33.33%`