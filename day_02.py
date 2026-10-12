# Day 2 - Python Variables & Data Types

# Hands-on: Build a Small AI Configuration Program

student_name = "Deveeswar"
learning_topic = "Agentic AI"
day = 2
completed = True
model_name = "llama3"
temperature = 0.7
max_tokens = 500
is_agent_active = True

print("Student:", student_name)
print("Topic:", learning_topic)
print("Day:", day)
print("Completed:", completed)
print("Model:", model_name)
print("Temperature:", temperature)
print("Max Tokens:", max_tokens)
print("Agent Active:", is_agent_active)
print(type(student_name))
print(type(day))
print(type(temperature))
print(type(is_agent_active))

print() # -----------------------------------------------------------------------------------------

# Exercise A - Easy

# 1. Create a variable called name and store your name.
# 2. Create a variable called age and store a whole number.
# 3. Create a variable called course and store "Agentic AI".
# 4. Create a variable called completed and store True.
# 5. Print all four variables.

name = "Devesh"
age = 24
course = "Agentic AI"
completed = True

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Completed:", completed)

print() # -----------------------------------------------------------------------------------------

# Exercise B - Identify the datatype

# Write the datatype for each value before running the code.

a = "Python"           # str
b = 90                 # int
c = 0.5                # float
d = False              # bool
e = ["RAG", "Agent"]   # list
f = {"role": "user"}   # dict
g = None               # NoneType

# -------------------------------------------------------------------------------------------------

# Exercise C - Use type()

# Use type() to verify your answers from Exercise B.

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

print() # -----------------------------------------------------------------------------------------

# Exercise D - Fix the code

# model = llama3
# temperature = "0.7"
# active = true
# 2day = 2

model = "llama3"
temperature = "0.7"
active = True
day = 2

# -------------------------------------------------------------------------------------------------

# Exercise E - Type conversion

# tokens = "500"
# extra_tokens = 100
# # Make this print 600
# print(tokens + extra_tokens)

# Modify the code so it works correctly.

tokens = "500"
extra_tokens = 100
print(int(tokens) + extra_tokens)

print() # -----------------------------------------------------------------------------------------

# Day 2 Challenges

# Level 1 - Easy

# Create four variables: student_name, learning_topic, day, completed. 
# Print the values and their datatypes.

student_name = "DEVEESWAR K"
learning_topic = "Agentic AI"
day = 2
completed = True

print(student_name, type(student_name))
print(learning_topic, type(learning_topic))
print(day, type(day))
print(completed, type(completed))

print() # -----------------------------------------------------------------------------------------

# Level 2 - Modify

# Create your own AI model configuration using model_name, temperature, max_tokens, and is_active. 
# Change the values and run the program again.

model_name = ""
temperature = 0
max_tokens = 0
is_active = False

model_name = "GPT"
temperature = 0.5
max_tokens = 4096
is_active = True

print("Model Name:", model_name)
print("Temperature:", temperature)
print("Max Tokens:", max_tokens)
print("Is Active:", is_active)

print() # -----------------------------------------------------------------------------------------

# Level 3 - Challenge

# Ask the user for their name and age using input(). 
# Convert age to an integer. 
# Print a message showing their name, their current age, and their age next year.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello,", name, "! You are", age, "years old.")
print("Next year, you will be", age + 1, "years old.")

# -------------------------------------------------------------------------------------------------

# Quick Quiz

""" 
    1. What datatype is 0.8? A) str B) int C) float D) bool

        Ans: C) float

    2. Which is a valid variable name? A) 2model B) model-name C) model_name D) model name

        Ans: C) model_name

    3. What datatype is True? A) str B) bool C) int D) float

        Ans: B) bool

    4. What does type("Agent") return?

        Ans: <class 'str'>

    5. What datatype does input() return by default?

        Ans: str

    6. Convert "500" to an integer using one Python function.

        Ans: int("500")

    7. Which datatype is most suitable for a model temperature such as 0.7?

        Ans: float

    8. Which datatype is most suitable for whether an agent is running or not?

        Ans: bool
"""
