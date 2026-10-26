# Day 4 - Python Lists

# Hands-On Mini Program

# Build a small learning tracker using a list.

topics = ["Python", "LLM", "Prompting", "Agentic AI"]

print("Current topics:")
for topic in topics:
 print("-", topic)

topics.append("RAG")
topics.append("AI Agent")
topics.append("LangGraph")

print("Total topics:", len(topics))
print("Latest topic:", topics[-1])
print("Last three topics:", topics[-3:])

print()

# Practice Exercises

# Exercise 1 - Create a list
# Create a list containing: Python, LLM, RAG, Agentic AI. Print the full list.

topics = ["Python", "LLM", "RAG", "Agentic AI"]

print(topics)

print()

# Exercise 2 - Indexing
# Print the first item, second item, and last item from your list.

print("First item:", topics[0])
print("Second item:", topics[1])
print("Last item:", topics[-1])

print()

# Exercise 3 - Add items
# Add LangGraph using append(). Then add Prompting at index 1 using insert().

topics.append("LangGraph")
topics.insert(1, "Prompting")
print(topics)

print()

# Exercise 4 - Remove items
# Remove RAG using remove(). Then remove the last item using pop().

topics.remove("RAG")
topics.pop()
print(topics)

print()

# Exercise 5 - Length
# Print the total number of items using len().

print("Total number of items", len(topics))

print()

# Exercise 6 - Loop
# Loop through the list and print each topic on a separate line.

for topic in topics:
 print(topic)

print()

# Exercise 7 - Search
# Check whether "Agentic AI" exists in the list and print the result.

print("Agentic AI" in topics)

print()

# Exercise 8 - Slice
# Print only the first three topics, then print only the last two topics.

print("First three topics:", topics[:3])
print("Last two topics:", topics[-2:])

print()

# Exercise 9 - Sort
# Create scores = [72, 91, 64, 88]. Sort them and print the highest score.

scores = [72, 91, 64, 88]

print("Original scores:", scores)

scores.sort()

print("Sorted scores:", scores)
print("Highest score:", scores[-1])

print()

# Exercise 10 - Copy
# Create one list, copy it using copy(), modify the copied list, 
# and confirm the original list did not change.

original_list = ["Python", "LLM", "RAG"]

copied_list = original_list.copy()
copied_list.append("AI Agent")

print("Original list:", original_list)
print("Copied list:", copied_list) 

# 3-Level Challenge

# Level 1 - Easy

# Create a list named tools with calculator, search, and pdf_search. 
# Print the first and last tool.


