# Day 9 - Function Arguments & Return Values

# Debugging practice

# Bug 1 - missing return

# def multiply(a, b):
#     result = a * b

# value = multiply(3, 4)
# print(value) # None

# Fix: add return result

def multiply(a, b):
    result = a * b
    return result

value = multiply(3, 4)
print(value)

print()

# Bug 2 - duplicate argument

# def greet(name, topic):
#     return f'{name}: {topic}'

# greet('Sathish', name='Kumar', topic='AI') # TypeError: multiple values for argument 'name'

def greet(name, topic):
    return f"{name}: {topic}"

print(greet("Sathish", "AI"))

print()

# Bug 3 - bad default ordering

# Invalid
# def search(top_k=3, query):
    # pass

# Good
def search(query, top_k=3):
    pass

# Practice exercises

# Exercise 1 - Create full_name(first, last) and return the combined name.

def full_name(first, last):
    return f'{first} {last}'

print(full_name("Deveeswar", "Kandhan"))

print()

# Exercise 2 - Create power(number, exponent=2). Call it with and without exponent.

def power(number, exponent=2):
    return number ** exponent

print(power(5))
print(power(5, 3))

print()

# Exercise 3 - Create model_config(model, temperature=0.7) returning a dictionary.

def model_config(model, temperature=0.7):
    return {'model': model, 'temperature': temperature}

print(model_config('llama3'))
print(model_config('claude-sonnet-4', 0.5))
print(model_config(temperature=0.3, model='gemini-2.5-pro'))
print(model_config('gpt-4', temperature=0.9))

print()

# Exercise 4 - Create is_adult(age) returning True/False.

def is_adult(age):
    return age >= 18

print(is_adult(22))  
print(is_adult(15))  

print()

# Exercise 5 - Create min_max(numbers) returning minimum and maximum.

def min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

result = min_max([10, 5, 25, 3, 15])
print(result)

minimum, maximum = min_max([10, 5, 25, 3, 15])
print("Minimum:", minimum)
print("Maximum:", maximum)

print()

# Exercise 6 - Create format_message(role, content) returning a dictionary.

def format_message(role, content):
    return {'role': role, 'content': content}

result = format_message("user", "Hello Python")
print(result)

print()

# Exercise 7 - Create count_items(*items) returning the number of supplied items.

def count_items(*items):
    return len(items)

print(count_items("LLM", "RAG", "Agentic AI"))
print(count_items(10, 20, 30, 40, 50))
print(count_items())    

print()

# Exercise 8 - Create agent_config(**kwargs) returning the config dictionary.

def agent_config(**kwargs):
    return kwargs

config = agent_config(
    name='research-agent', 
    model='llama3', 
    temperature=0.2
)

print(config)

print()

# Exercise 9 - Create safe_divide(a, b) handling division by zero.

def safe_divide(a, b):
    if b == 0:
        return 'Cannot divide by zero'
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))

print()

# Exercise 10 - Create search_tool(query, top_k=3) returning query, top_k, status, and an empty results list.

def search_tool(query, top_k=3):
    return {
        'query': query,
        'top_k': top_k,
        'status': 'success',
        'results': []
    }

result1 = search_tool("What is Python?")
result2 = search_tool("What is Agentic AI?", top_k=5)

print(result1)
print(result2)

print()

# Three-level challenge