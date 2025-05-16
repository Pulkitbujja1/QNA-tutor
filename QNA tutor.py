

user_input = input("Ask your computer science question: ").lower()

import wikipedia

try: #if anybody write these kind of words like (jdbnaksjdhnkjld) then Python will try this block, and if something breaks, it jumps to the except block.
    summary = wikipedia.summary(user_input, sentences=2)    
    # A function from the wikipedia module that searches Wikipedia and gives you a short summary of an article
    # user_input - it will search that which page is matching of your question
    # sentences = 2 means it will give result in just 2 sentences — so it's not too long.
    
    print("Professor AI (from Wikipedia):", summary)         
except:
    print("Sorry, I couldn’t find anything.")