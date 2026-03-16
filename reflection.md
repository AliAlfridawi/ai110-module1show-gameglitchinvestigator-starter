# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?: Simple UI basic quesing game
- List at least two concrete bugs you noticed at the start: 
  (for example: "the hints were backwards").

  The website had a simple UI basic quesing game. There seemed to be an issue with the scoring system where you could get a negative score, and the new game button didn't work. The way the debugger worked was very buggy as well.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?: I used copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).:
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Copilot as my AI tool. I used Copilot to create test and then correct the test. Copilot didn't suggested anything incorrect, or if it did I missed it. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I used a pytest like suggested, and I also tested the app. Manually I played the game multiple times and didn't notice any bugs. AI did design test, I gave Copilot the prompt to test for edge cases and possible bugs. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned to only update the state when the user clicked the button. Streamlit rerun the whole script when you interact with the website. So it can forget when you click a button causing issues. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I started by initializing then asked the agent questions about the repo. I then used the plan feature to plan for edge cases and to fix. I would read through the code base first. It helped me understand how to use testing and its importance in AI development. 
