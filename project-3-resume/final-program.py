import subprocess
import os
import pandas as pd
import openai

# Call Shane's questionnaire program
os.chdir("./questionnaire")
if not os.path.isfile("user_data.csv"):
    subprocess.call(["g++", "main.cpp", "questionnaire.cpp", "-o", "questionnaire"])
    subprocess.call(["./questionnaire"])

# Turn csv file into txt file
if not os.path.isfile("questionnaire.txt"):
    questionnaire = pd.read_csv('user_data.csv')
    questionnaire = questionnaire.drop(questionnaire.columns[0], axis=1)
    with open("questionnaire.txt", 'w') as f:
        for i in range(questionnaire.shape[0]):
            for j in range(questionnaire.shape[1]):
                f.write(str(questionnaire.iat[i, j]) + '\n')

# Call Celia's skill word extraction program
os.chdir("../BST")
subprocess.call(["g++", "main.cpp", "-o", "BST"])
subprocess.call(["./BST"])

# Load in the data from files
os.chdir("../questionnaire")
with open("questionnaire.txt") as file:
    user_data = file.read()

os.chdir("../BST")
with open("job-post.txt") as file:
    job_post = file.read()

with open("skill-list.txt") as file:
    skill_list = file.read()

# Use chatGPT to find more skill words
print("Enter your Open AI API key:")
openai.api_key = input()

my_message = job_post + "\n Above is a job posting, please extract any relevant skills that you think the employer might be looking for. In particular look for repeated words. Each skill word should be a single item in a comma separated list. Do not provide anything beyond this list of skills."
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user","content": my_message}]
    )
reply = response["choices"][0]["message"]["content"]
final_skill_str = skill_list + reply
rec_skills = [word.strip() for word in final_skill_str.split(',')]

# Go over the list and see which skills the user actually has
user_skills = []

print("Our program has gone through and picked out skills from the job posting that we think the employer might be looking for. Let's go over them. Remember to be generous with yourself as many skill words can be vague, but don't be afraid to say you don't have a skill if you don't have it.")
for skill in rec_skills:
    print(f"Would you say that you have the skill \"{skill}\"? (y/n)")
    line = input()
    if line.strip().lower() == 'y':
        user_skills.append(skill)

user_skills_str = ", ".join(user_skills)

# Make the final resume
print("We're working on your resume. Please wait...")
my_message = "Given the following resume information...\n" + user_data + "\nMake a resume using as many of the following skill words as possible through out the resume...\n" + user_skills_str
response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user","content": my_message}]
            )
reply = response["choices"][0]["message"]["content"]

print("Here is a draft of your resume populated with words that will help it reach a real human:\n")
print(reply)