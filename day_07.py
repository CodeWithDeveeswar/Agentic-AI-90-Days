# Day 7 - Python Loops

# Practice Exercises

# Exercise 1 - Create a list of 5 AI topics and print every topic using a for loop.

topics = ["Python", "LLM", "RAG", "LangGraph", "Agentic AI"]

for topic in topics:
    print(topic)

print() # ------------------------------------------------------------------------------------------------------

# Exercise 2 - Use range() to print numbers 1 to 10.

for num in range(1, 11):
    print(num)

print() # ------------------------------------------------------------------------------------------------------

# Exercise 3 - Use range() to print even numbers from 2 to 20.

for even in range(2, 21, 2):
    print(even)

print() # ------------------------------------------------------------------------------------------------------

# Exercise 4 - Create a while loop that prints Day 1 to Day 5.

day = 1

while day <= 5:
    print("Day", day)
    day += 1

print() # ------------------------------------------------------------------------------------------------------

# Exercise 5 - Loop through the string "AGENT" and print each character.

string = "AGENT"

for char in string:
    print(char)

print() # ------------------------------------------------------------------------------------------------------

# Exercise 6 - Create a tools list and stop the loop when "search" is found.

tools = ["search", "disabled_tool", "calculator"]

for tool in tools:
    if tool == "search":
        print("Search tool found!")
        break
    print(tool)

print() # ------------------------------------------------------------------------------------------------------

# Exercise 7 - Skip "disabled_tool" using continue and print all other tool names.

tools = ["search", "disabled_tool", "calculator"]

for tool in tools:
    if tool == "disabled_tool":
        continue
    print("Available:", tool)

print() # ------------------------------------------------------------------------------------------------------

# Exercise 8 - Use enumerate() to print numbered chat messages.

messages = ["Hello", "Explain RAG", "Explain agents"]

for index, message in enumerate(messages, start=1):
    print(f"Message {index}: {message}")

print() # ------------------------------------------------------------------------------------------------------

# Exercise 9 - Loop through a dictionary containing model, temperature, and max_tokens.

model_config = {
    "model": "llama3",
    "temperature": 0.7,
    "max_tokens": 500
}

for key, value in model_config.items():
    print(key, "=", value)

print() # ------------------------------------------------------------------------------------------------------

# Exercise 10 - Create two lists - agents and tools - and print every agent/tool combination using nested loops.

agents = ["research", "writer"]
tools = ["search", "calculator"]

for agent in agents:
    for tool in tools:
        print(agent, "can use", tool)

print() # ------------------------------------------------------------------------------------------------------

# Three-level challenge

# Level 1 - Easy

# Create a list of four tools and print each tool using a for loop.

tools = ["calculator", "search", "weather", "pdf_search"]

for tool in tools:
    print(tool)

print() # ------------------------------------------------------------------------------------------------------

# Level 2 - Modify

# Print the same tools with numbering using enumerate().

tools = ["calculator", "search", "weather", "pdf_search"]

for index, tool in enumerate(tools, start=1):
    print(f"Tool {index}: {tool}")

print() # ------------------------------------------------------------------------------------------------------

# Level 3 - Challenge

# Build a tiny tool finder. Given a requested tool name, loop through the available tools. 
# If found, print "Tool Found" and stop. If not found after the loop, print "Tool Not Found".

tools = ["calculator", "search", "weather", "pdf_search"]
requested_tool = "search"

for tool in tools:
    if tool == requested_tool:
        print("Tool Found")
        break
else: 
    print("Tool Not Found")

print() # ------------------------------------------------------------------------------------------------------

# Mini project - Message Processor

# Build a program that processes user messages one by one and ignores blank messages.

messages = [
    "What is AI?",
    "",
    "Explain RAG",
    "Explain LangGraph"
]

for message in messages:
    if message == "":
        continue
    print("Processing:", message)

# --------------------------------------------------------------------------------------------------------------

# Quick Quiz

""" 
    1. What does range(3) produce?

        Ans: B) 0,1,2

    2. Which loop runs while a condition is True?

        Ans: B) while

    3. What does break do?

        Ans: B) stops the loop

    4. What does continue do?

        Ans: C) skips current iteration

    5. Why is enumerate() useful?

        Ans: A) gets index and value
"""
