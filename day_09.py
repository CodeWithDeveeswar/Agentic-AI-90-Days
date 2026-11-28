# Day 9 - Function Arguments & Return Values

# Debugging practice

# Bug 1 - missing return

# def multiply(a, b):
#     result = a * b

# value = multiply(3, 4)
# print(value) # None

def multiply(a, b):
    result = a * b
    return result

value = multiply(3, 4)
print(value)

print() # ---------------------------------------------------------------------------------------------------------

# Bug 2 - duplicate argument

# def greet(name, topic):
#     return f'{name}: {topic}'

# greet('Sathish', name='Kumar', topic='AI') # TypeError: multiple values for argument 'name'

def greet(name, topic):
    return f"{name}: {topic}"

print(greet("Sathish", "AI"))

print() # ---------------------------------------------------------------------------------------------------------

# Bug 3 - bad default ordering

# Invalid
# def search(top_k=3, query):
    # pass

# Good
def search(query, top_k=3):
    pass

# -----------------------------------------------------------------------------------------------------------------

# Practice exercises

# Exercise 1 - Create full_name(first, last) and return the combined name.

def full_name(first, last):
    return f'{first} {last}'

print(full_name("Deveeswar", "Kandhan"))

print() # ---------------------------------------------------------------------------------------------------------

# Exercise 2 - Create power(number, exponent=2). Call it with and without exponent.

def power(number, exponent=2):
    return number ** exponent

print(power(5))
print(power(5, 3))

print() # ---------------------------------------------------------------------------------------------------------

# Exercise 3 - Create model_config(model, temperature=0.7) returning a dictionary.

def model_config(model, temperature=0.7):
    return {'model': model, 'temperature': temperature}

print(model_config('llama3'))
print(model_config('claude-sonnet-4', 0.5))
print(model_config(temperature=0.3, model='gemini-2.5-pro'))
print(model_config('gpt-4', temperature=0.9))

print() # ---------------------------------------------------------------------------------------------------------

# Exercise 4 - Create is_adult(age) returning True/False.

def is_adult(age):
    return age >= 18

print(is_adult(22))  
print(is_adult(15))  

print() # ---------------------------------------------------------------------------------------------------------

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

print() # ---------------------------------------------------------------------------------------------------------

# Exercise 6 - Create format_message(role, content) returning a dictionary.

def format_message(role, content):
    return {'role': role, 'content': content}

result = format_message("user", "Hello Python")
print(result)

print() # ---------------------------------------------------------------------------------------------------------

# Exercise 7 - Create count_items(*items) returning the number of supplied items.

def count_items(*items):
    return len(items)

print(count_items("LLM", "RAG", "Agentic AI"))
print(count_items(10, 20, 30, 40, 50))
print(count_items())    

print() # ---------------------------------------------------------------------------------------------------------

# Exercise 8 - Create agent_config(**kwargs) returning the config dictionary.

def agent_config(**kwargs):
    return kwargs

config = agent_config(
    name='research-agent', 
    model='llama3', 
    temperature=0.2
)

print(config)

print() # ---------------------------------------------------------------------------------------------------------

# Exercise 9 - Create safe_divide(a, b) handling division by zero.

def safe_divide(a, b):
    if b == 0:
        return 'Cannot divide by zero'
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))

print() # ---------------------------------------------------------------------------------------------------------

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

print() # ---------------------------------------------------------------------------------------------------------

# Three-level challenge

# Level 1 - Easy

# Create introduce(name, topic="Agentic AI") and return a sentence.

def introduce(name, topic="Agentic AI"):
    return f'{name} is learning {topic}'

print(introduce("Devesh"))
print(introduce("Akilan", "RAG"))

print() # ---------------------------------------------------------------------------------------------------------

# Level 2 - Modify

# Create create_user(name, level="Beginner", active=True) and return a dictionary.

def create_user(name, level="Beginner", active=True):
    return {
        'name': name,
        'level': level,
        'active': active
    }

print(create_user("Devesh"))
print(create_user("Akilan", "Advanced", False))

print() # ---------------------------------------------------------------------------------------------------------

# Level 3 - Agentic AI

# Create execute_tool(tool, query, top_k=3). 
# Return a search-style dictionary for search, a message for calculator, and an error dictionary for unknown tools.

def execute_tool(tool, query, top_k=3):
    if tool == 'search':
        return {
            'status': 'success',
            'tool': 'search',
            'query': query,
            'top_k': top_k,
            'message': f'Searching for: {query}'
        }

    elif tool == 'calculator':
        return {
            'status': 'success',
            'tool': 'calculator',
            'message': f'Calculator received input: {query}'
        }

    else:
        return {
            'status': 'error',
            'message': f'Unknown tool: {tool}'
        }

print(execute_tool('search', 'What is RAG?'))
print(execute_tool('calculator', '10 * 5'))
print(execute_tool('weather', 'Coimbatore weather'))

print() # ---------------------------------------------------------------------------------------------------------

# Mini project - Tool Request Builder

def build_tool_request(tool_name, **inputs):
    if not tool_name:
        return {'status': 'error', 'message': 'tool_name is required'}

    return {
        'status': 'ready',
        'tool': tool_name,
        'inputs': inputs
    }

search_request = build_tool_request('search', query='What is RAG?', top_k=3)
print(search_request)

weather_request = build_tool_request('weather', city='Coimbatore', country='India', unit='celsius')
print(weather_request)

calculator_request = build_tool_request('calculator', operation='multiply', num1=10, num2=5)
print(calculator_request)

pdf_request = build_tool_request('', file_name='report.pdf', operation='extract_text', page_number=2)
print(pdf_request)

# -----------------------------------------------------------------------------------------------------------------

# Quick Quiz