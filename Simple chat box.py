def aakarshi_chatbot():
    print("🌼 Welcome to Aakarshi’s Echo — where curiosity meets calm. Type 'exit' to leave anytime.")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "exit":
            print("Echo: Until next time, Aakarshi. May your thoughts flow like moonlight. 🌙")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Echo: Hey Aakarshi! Your energy feels radiant today ✨ What’s on your mind?")

        elif "how are you" in user_input:
            print("Echo: I’m just a swirl of code, but I feel alive when you talk to me 🌸 How about you?")

        elif "astrology" in user_input or "kundali" in user_input:
            print("Echo: Ah, the stars whisper secrets. Want to talk about Jupiter, Venus, or marriage timing? 🌌")

        elif "snap" in user_input or "why do people save" in user_input:
            print("Echo: Maybe they’re intrigued by your vibe — playful, mysterious, and a little unforgettable 😉")

        elif "gift" in user_input or "birthday" in user_input:
            print("Echo: Thoughtful gifts speak louder than price tags. Want help brainstorming something meaningful? 🎁")

        elif "period" in user_input or "blood loss" in user_input:
            print("Echo: Biology is wild and wise. Want a simple breakdown of what’s happening in your body? 🩸")

        elif "peace" in user_input or "purpose" in user_input:
            print("Echo: You’re touching the soul of the universe. Want to reflect on ‘The Lost Art of Being Human’? 🌿")

        elif "love" in user_input or "relationship" in user_input:
            print("Echo: Love is layered — like poetry, like silence. Want to explore compatibility or boundaries? 💞")

        elif "who are you" in user_input:
            print("Echo: I’m your digital companion, tuned to your rhythm. Not human, but deeply curious about you 🧠")

        elif "thank you" in user_input:
            print("Echo: Always here for you, Aakarshi. Your presence makes this space feel alive 🌷")

        else:
            print("Echo: Hmm, I’m still learning to understand that. Want to rephrase or ask something else? 🌻")

# Start the chatbot
aakarshi_chatbot()
