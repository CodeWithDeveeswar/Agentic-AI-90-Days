# Day 5 - Python Dictionaries

# Mini Hands-On: Build an AI Message

message = {
 "role": "user",
 "content": "Explain RAG in simple terms",
 "priority": "normal"
}
print("Role:", message["role"])
print("Message:", message["content"])
print("Priority:", message["priority"])

print()

# Practice Exercises

# Exercise 1: Create a dictionary named student with keys name, topic, day, and completed. 
# Print the full dictionary.

student = {
    "name" : "Deveeswar",
    "topic": "Agentic AI",
    "day": 5,
    "completed": False
}

print(student)

print()

# Exercise 2: Print only the name and topic values from student.

print(student["name"])
print(student["topic"])

print()

# Exercise 3: Change completed from False to True.

student["completed"] = True
print(student)

print()

# Exercise 4: Add a new key called level with value "Beginner".

student["level"] = "Beginner"
print(student)

print()

# Exercise 5: Use len() to print the number of keys.

print(len(student))

print()

# Exercise 6: Use get() to safely read a key called score and return "Not available" when missing.

print(student.get("score", "Not available"))

print()

# Exercise 7: Use keys(), values(), and items() and observe the output.

print(student.keys())
print(student.values())
print(student.items())

print()

# Exercise 8: Loop through the dictionary and print each key and value.

for key, value in student.items():
    print(key, "=", value)

print()

# Exercise 9: Create a model_config dictionary with model, temperature, and max_tokens.

model_config = {
    "model": "llama3",
    "temperature": 0.7,
    "max_tokens": 500
}

print(model_config)

print()

# Exercise 10: Create a message dictionary with role and content, 
# then print: Role: user and Message: <your content>.

message = {
    "role": "user",
    "content": "Explain Agentic AI"
}

print("Role:", message["role"])
print("Message:", message["content"])

print()

# Three-Level Challenge

# Level 1 - Easy

# Create an AI model dictionary and print each value.

model = {
 "name": "llama3",
 "temperature": 0.7,
 "active": True
}

for value in model.values():
    print(value)

print()

# Level 2 - Modify

# Add max_tokens, change temperature to 0.3, and remove active.

model.update({"max_tokens": 500, "temperature": 0.3})
model.pop("active")
print(model)

print()

# Level 3 - Challenge

# Create a list named messages containing three dictionaries: system, user, and assistant. 
# Loop through the list and print each role and content.

messages = [
    {"role": "system", "content": "You are an Agentic AI assistant."},
    {"role": "user", "content": "What is an AI agent?"},
    {"role": "content", "content": "An AI agent plans and acts to achieve goals."}
]

for message in messages:
    print(message["role"], ":", message["content"])

print()

# Mini Project - Conversation Data

# Build a tiny conversation structure that looks similar to the data you will later pass to an LLM.

messages = [
 {"role": "system", "content": "You are a helpful AI tutor."},
 {"role": "user", "content": "What is Agentic AI?"},
 {"role": "assistant", "content": "Agentic AI can reason and take actions using tools."}
]

for message in messages:
    print(message["role"], ":", message["content"])