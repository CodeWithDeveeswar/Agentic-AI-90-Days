# Day 3 - Python Strings

# AI-Oriented Hands-On Examples

# Example 1 - Build a simple prompt

name = "Devesh"
topic = "Agentic AI"
level = "beginner"

prompt = f"Explain {topic} to {name} at {level} level."
print(prompt)

print() # --------------------------------------------------------------------------------------------

# Example 2 - Clean a user question

user_question = " WHAT IS RAG? "
clean_question = user_question.strip().lower()
print(clean_question)

print() # --------------------------------------------------------------------------------------------

# Example 3 - Detect a keyword

question = "Explain AI agents".lower()
print("agent" in question)

print() # --------------------------------------------------------------------------------------------

# Example 4 - Build a prompt from multiple values

role = "AI tutor"
topic = "LanGraph"
style = "simple"

prompt = f"You are an {role}, Explain {topic} in a {style} way."
print(prompt)

print() # --------------------------------------------------------------------------------------------

# Practice Exercises

# Exercise 1 - Create Strings
# Create variables called name, city, learning_topic, and goal. Print all four values.

name = "Deveeswar"
city = 'Puducherry'
learning_topic = '''Agentic AI'''
goal = "AI Engineer"

print(name+", "+city+", "+learning_topic+", "+goal)

print() # --------------------------------------------------------------------------------------------

# Exercise 2 - type()
# Create topic = "Agentic AI". Print its value and datatype.

topic = "Agentic AI"
print(topic, type(topic))

print() # --------------------------------------------------------------------------------------------

# Exercise 3 - f-string
# Create name and topic. Produce: Hi Sathish, today you are learning Agentic AI.

name = "Devesh"
topic = "Agentic AI"

message = f"Hi {name}, today you are learning {topic}."
print(message)

print() # --------------------------------------------------------------------------------------------

# Exercise 4 - len()
# Find the length of "Agentic AI". Then find the length of your own name.

topic = "Agentic AI"
name = "Deveeswar"

print(len(topic))
print(len(name))

print() # --------------------------------------------------------------------------------------------

# Exercise 5 - Indexing
# Given model = "OpenAI", print the first character, third character, and last character.

model = "OpenAI"

print(model[0])
print(model[2])
print(model[-1])

print() # --------------------------------------------------------------------------------------------

# Exercise 6 - Slicing
# Given course = "Agentic AI Course", extract only Agentic AI.

course = "Agentic AI Course"

print(course[0:10])
print(course[:10])

print() # --------------------------------------------------------------------------------------------

# Exercise 7 - Clean input
# Convert " WHAT IS LANGGRAPH? " to "what is langgraph?".

question = " WHAT IS LANGGRAPH? "
Clean_question =question.strip().lower()
print(Clean_question)

print() # --------------------------------------------------------------------------------------------

# Exercise 8 - Replace
# Change "I am learning Python" into "I am learning Agentic AI" using replace().

text = "I am learning Python"
new_text = text.replace("Python", "Agentic AI")
print(new_text)

print() # --------------------------------------------------------------------------------------------

# Exercise 9 - Split
# Convert "Python,LLM,RAG,Agents" into a list using split().

text = "Python,LLM,RAG,Agents"
words = text.split(",")
print(words)

print() # --------------------------------------------------------------------------------------------

# Exercise 10 - Join
# Join ["Python", "LLM", "RAG", "Agents"] using " -> ".

topics = ["Python", "LLM", "RAG", "Agents"]
result = " -> ".join(topics)
print(result)

print() # --------------------------------------------------------------------------------------------

# Three-Level Challenge

# Level 1 - Easy
# Create name, topic, and day. 
# Use an f-string to print: Hi <name>, this is Day 3 and you are learning <topic>.

name = "Devesh"
topic = "Python Strings"
day = "Day 3"

message = f"Hi {name}, this is {day} and you are learning {topic}."
print(message)

print() # --------------------------------------------------------------------------------------------

# Level 2 - Modify
# Take question = " WHAT IS AN AI AGENT? ". 
# Remove spaces, convert to lowercase, replace ai agent with agentic ai, then print the final string.

question = " WHAT IS AN AI AGENT? "
question = question.strip().lower().replace("ai agent", "agentic ai")
print(question)

print() # --------------------------------------------------------------------------------------------

# Level 3 - AI Prompt Builder
# Create variables topic, audience, and style. Build a prompt using an f-string. 
# Example output: Explain RAG to a beginner using a simple real-world example.

topic = "RAG"
audience = "beginner"
style = "simple real-world example"

prompt = f"Explain {topic} to a {audience} using a {style}."
print(prompt)

print() # --------------------------------------------------------------------------------------------

# Mini Project - Prompt Builder

# Build a small Python program that collects three values and creates an AI prompt.

topic = input("Enter a topic: ")
audience = input("Who is the audience? ")
style = input("Explanation style: ")
prompt = f"Explain {topic} to {audience} in a {style} way."
print("\nGenerated Prompt:")
print(prompt)

# ----------------------------------------------------------------------------------------------------

# Quick Quiz

""" 
    1. What is the datatype of "Agentic AI"?

        Ans: str

    2. What does len("AI") return?

        Ans: 2

    3. What is the first index in a Python string?

        Ans: 0

    4. What does "PYTHON".lower() return?

        Ans: python

    5. Which method removes spaces from both ends?

        Ans: strip()

    6. What does "Python,AI".split(",") return?

        Ans: ["Python", "AI"]

    7. Does input() return an integer automatically when you type 25?

        Ans: No. input() returns str

    8. Are Python strings mutable?

        Ans: No. Strings are immutable

    9. What operator checks whether a substring exists?
    
        Ans: in

    10. Which is cleaner for mixing text and variables: concatenation or f-strings?
    
        Ans: f-strings
"""