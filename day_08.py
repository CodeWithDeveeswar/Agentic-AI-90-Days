# Day 8 - Python Functions

# Practice Exercises

# Exercise 1 - Create a function `say_hello()` that prints "Hello, Agentic AI!".

def say_hello():
    print("Hello, Agentic AI!")

say_hello()

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 2 - Create `greet(name)` that returns `Hello <name>`.

def greet(name):
    return f"Hello {name}"

print(greet("Devesh"))

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 3 - Create `multiply(a, b)` that returns the product.

def multiply(a, b): 
    return a * b

result = multiply(10, 20)
print(result)

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 4 - Create `introduce(name, topic)` that returns a formatted sentence.

def introduce(name, topic):
     return f"Hi {name}, you are learning {topic}"

print(introduce("Devesh", "Agentic AI"))

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 5 - Create `is_even(number)` that returns True if the number is even, otherwise False.

def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(7))

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 6 - Create `clean_text(text)` that strips spaces and converts text to lowercase.

def clean_text(text):
    return text.strip().lower()

print(clean_text("   HELLO AGENTIC AI   "))

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 7 - Create `model_prompt(topic, tone="simple")` using a default argument.

def model_prompt(topic, tone="simple"):
    return f"Explain {topic} in a {tone} way."

print(model_prompt("RAG"))
print(model_prompt("RAG", "technical"))

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 8 - Create `stats(a, b)` that returns both sum and product, then unpack the results.

def stats(a, b):
    sum = a + b
    product = a * b
    return sum, product

result_sum, result_product = stats(10, 20)

print("Sum:", result_sum)
print("Product:", result_product)

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 9 - Create `show_tools(*tools)` and print each received tool.

def show_tools(*tools):
    for tool in tools:
        print(tool)

show_tools("calculator", "search", "weather", "pdf_search")

print() # -----------------------------------------------------------------------------------------------------------------

# Exercise 10 - Create `build_config(**settings)` and return the settings dictionary.

def build_config(**settings):
    return settings

config = build_config(
    model="demo-model",
    temperature=0.7,
    max_tokens=500
)

print(config)

print() # -----------------------------------------------------------------------------------------------------------------

# Debugging Exercises

# Find and fix the problem in each snippet.

# Exercise A

# def greet(name)
#  return f"Hello {name}"

def greet(name):
    return f"Hello {name}"

# -------------------------------------------------------------------------------------------------------------------------

# Exercise B

# def add(a, b):
# return a + b

def add(a, b):
    return a + b

# -------------------------------------------------------------------------------------------------------------------------

# Exercise C

# def square(x):
#  print(x * x)

# result = square(5)
# print(result * 2)

def square(x):
    return x * x

result = square(5)
print(result * 2)

print() # -----------------------------------------------------------------------------------------------------------------

# Three-level challenge

# Level 1 - Easy

# Create `introduce(name, topic)` and return a personalized learning message.

def introduce(name, topic):
    return f"Hi {name}, you are learning {topic}"
    
print(introduce("Deveeswar", "RAG"))

print() # -----------------------------------------------------------------------------------------------------------------

# Level 2 - Modify

# Create `calculator(a, b, operation="add")`. Support add and multiply. 
# Return "Unsupported operation" for anything else.

def calculator(a, b, operation="add"):
    if operation == "add":
        return a + b

    elif operation == "multiply":
        return a * b
    
    else:
        return "Unsupported operation"

print(calculator(10, 20))
print(calculator(10, 20, "multiply"))
print(calculator(10, 20, "divide"))

print() # -----------------------------------------------------------------------------------------------------------------

# Level 3 - Agent-style Challenge

# Create `choose_tool(task)` that examines a task and returns Calculator Tool, Search Tool, Weather Tool, or No Tool Found. 
# Then test it with at least four different inputs.

def choose_tool(task):
    task = task.lower()

    if "calculate" in task:
        return "Calculator Tool"

    elif "search" in task:
        return "Search Tool"

    elif "weather" in task:
        return "Weather Tool"

    else:
        return "No Tool Found"

print(choose_tool("Calculate 100 + 200"))
print(choose_tool("Search for Python tutorials"))
print(choose_tool("What is the weather today?"))
print(choose_tool("Tell me a joke"))

print() # -----------------------------------------------------------------------------------------------------------------

# Mini Project - Tiny Tool Box

# Build three functions and a router. 
# The router should choose which tool function to call based on a simple command.

def calculator(a, b):
    return a + b

def search(query):
    return f"Searching: {query}"

def weather(city):
    return f"Checking weather for: {city}"

def run_tool(tool_name):
    if tool_name == "calculator":
        return calculator(10, 20)
    
    elif tool_name == "search":
        return search("Agentic AI")
    
    elif tool_name == "weather":
        return weather("Chennai")
    
    else:
        return "Unknown tool"

print(run_tool("weather"))

# -------------------------------------------------------------------------------------------------------------------------

# Quick Quiz

""" 
    1. Which keyword is used to define a function?

        Ans: B) def

    2. What is `name` in `def greet(name):`?

        Ans: B) parameter

    3. What does `return` do?

        Ans: B) sends a value back

    4. What does a function return if no explicit return is used?

        Ans: C) None

    5. Which syntax accepts flexible keyword arguments?

        Ans: B) **kwargs
"""