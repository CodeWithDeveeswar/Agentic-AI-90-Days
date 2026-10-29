# Day 6 - Python Conditions

# Practice Exercises

# Exercise 1 - Positive, Negative, or Zero

# Create a variable number. Print Positive, Negative, or Zero using if/elif/else.

number = -1

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 2 - Pass or Fail

# If score is 50 or above, print Pass. Otherwise print Fail.

score = 50

if score >= 50:
    print("Pass")
else:
    print("Fail")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 3 - Even or Odd

# Use number % 2 == 0 to decide whether a number is even or odd.

number = 6

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 4 - Topic Router

# For topic = "RAG": print "Learn Retrieval Augmented Generation". 
# For topic = "Agent": print "Learn AI Agents". 
# Otherwise print "Unknown Topic".

topic = "Agent"

if topic == "RAG":
    print("Learn Retrieval Augmented Generation")
elif topic == "Agent":
    print("Learn AI Agents")
else:
    print("Unknown Topic")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 5 - Access Check

# Allow access only when age >= 18 AND verified is True.

age = 18
verified = True

if age >= 18 and verified:
    print("Access Granted")
else:
    print("Access Denied")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 6 - Tool Allow List

# Create allowed_tools = ["search", "calculator", "weather"]. 
# Check whether selected_tool is allowed.

allowed_tools = ["search", "calculator", "weather"]
selected_tool = "weather"

if selected_tool in allowed_tools:
    print("Tool is allowed")
else:
    print("Tool is not allowed")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 7 - Empty Input

# If user_input is empty after .strip(), print "Please enter a question". 
# Otherwise print the cleaned question.

user_input = input("Ask your question: " ).strip()

if user_input == "":
    print("Please enter a question")
else:
    print("Cleaned question:", user_input)

print() # -------------------------------------------------------------------------------------------------------

# Exercise 8 - Grade Calculator

# 90+ A, 75-89 B, 60-74 C, 50-59 D, below 50 F.

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 9 - Model Selection

# If complexity is "simple", select "small-model". 
# If complexity is "medium", select "standard-model". 
# Otherwise select "large-model".

complexity = "simple"

if complexity == "simple":
    print("small-model")
elif complexity == "medium":
    print("standard-model")
else:
    print("large-model")

print() # -------------------------------------------------------------------------------------------------------

# Exercise 10 - Safe Action

# If action is "send_email" and approved is True, print "Sending email".
# If approval is missing, print "Approval required".

action = "send_email"
approved = True

if action == "send_email" and approved is True:
    print("Sending email")
elif action == "send_email" and approved is not True:
    print("Approval required")

print() # -------------------------------------------------------------------------------------------------------

# Debugging Exercises

# Fix this

# age = 20
# if age = 20:
# print("Age is 20")

age = 20
if age == 20:
    print("Age is 20")

print() # -------------------------------------------------------------------------------------------------------

# Fix this

# score = input("Score: " )

# if score >= 50:
#  print("Pass")

score = int(input("Score: " ))

if score >= 50:
    print("Pass")

print() # -------------------------------------------------------------------------------------------------------

# Think: what is wrong with the logic?

# tool = "search"

# if tool == "search":
#  print("Search")
# if tool == "search":
#  print("Another search branch")

tool = "search"

if tool == "search":
 print("Search")
 print("Another search branch")

print() # -------------------------------------------------------------------------------------------------------

# Three-Level Challenge

# Level 1 - Easy

# Create temperature = 0.7. If it is greater than 0.5, print "Creative mode"; 
# otherwise print "Focused mode".

temperature = 0.7

if temperature > 0.5:
    print("Creative mode")
else:
    print("Focused mode")

print() # -------------------------------------------------------------------------------------------------------

# Level 2 - Modify

# Create user_role and is_verified. 
# Allow access only when the role is admin OR editor, and the user is verified.

user_role = "editor"
is_verified = True

if (user_role == "admin" or user_role == "editor") and is_verified:
    print("Access Granted")
else:
    print("Access Denied")

print() # -------------------------------------------------------------------------------------------------------

# Level 3 - Agent-Style Challenge

# Build a simple router using user_input. 
# Route math-related text to Calculator, weather-related text to Weather, document/PDF-related text to RAG, 
# and everything else to General LLM.

user_input = input("Ask your question: ").strip().lower()

if "calculate" in user_input or "math" in user_input or "sum" in user_input or "multiply" in user_input:
    print("Routing to Calculator")

elif "weather" in user_input or "temperature" in user_input or "forecast" in user_input or "rain" in user_input:
    print("Routing to Weather")

elif "pdf" in user_input or "document" in user_input or "file" in user_input or "report" in user_input:
    print("Routing to RAG")

else:
    print("Routing to General LLM")

print() # -------------------------------------------------------------------------------------------------------

# Mini Project - Rule-Based AI Request Router

# Build a small CLI program that reads one user question and prints the tool that should handle it.

question = input("Ask your question: ").strip().lower()

if not question:
    route = "Invalid Input"

elif "calculate" in question or "math" in question:
    route = "Calculator Tool"

elif "weather" in question or "rain" in question:
    route = "Weather Tool"

elif "pdf" in question or "document" in question:
    route = "RAG Tool"

elif "code" in question or "python" in question or "program" in question:
    route = "Coding Tool"

else:
    route = "General LLM"

print(f"Selected route: {route}")

# ---------------------------------------------------------------------------------------------------------------

# Quick Quiz

""" 
    1. Which operator checks equality: = or == ?

        Ans: ==

    2. What runs when all previous if/elif conditions are False?

        Ans: else

    3. What is the result of 10 > 5 and True?

        Ans: True

    4. What does not False evaluate to? 

        Ans: True

    5. Is an empty list truthy or falsy

        Ans: Falsy

    6. When should you use elif instead of multiple independent if statements?

        Ans: When the branches are alternatives and only one should run

    7. What data type does input() return?

        Ans: str

    8. Why might .lower() be useful before comparing user text?

        Ans: To normalize capitalization so comparisons are more reliable
        
    9. Which keyword checks membership in a list or string?

        Ans: in
        
    10. Why are conditions important for Agentic AI?

        Ans: Because agents need decision and routing logic to choose actions, tools, or next steps.
"""