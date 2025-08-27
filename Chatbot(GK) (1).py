# space_chatbot.py

def check_answer(user_input, keywords):
    user_input = user_input.lower()
    for keyword in keywords:
        if keyword.lower() in user_input:
            return True
    return False

def main():
    print("🚀 Hello! I’m your Space & Astronomy Chatbot.")
    name = input("👋 What's your name? ")
    print(f"\nNice to meet you, {name}! Let's explore the universe with 20 questions. 🔭")

    questions = [
        ("What is the name of our galaxy?", ["milky way"]),
        ("What is the nearest star to Earth?", ["sun"]),
        ("Which planet is known as the Red Planet?", ["mars"]),
        ("Which planet is the largest in our solar system?", ["jupiter"]),
        ("What do we call a system of millions or billions of stars?", ["galaxy"]),
        ("What force keeps planets in orbit around the sun?", ["gravity"]),
        ("What is the name of the first satellite sent into space?", ["sputnik"]),
        ("Who was the first person to walk on the moon?", ["neil armstrong"]),
        ("What is the name of Earth’s natural satellite?", ["moon"]),
        ("Which planet has rings around it?", ["saturn"]),
        ("What is the name of the telescope launched into space in 1990?", ["hubble"]),
        ("What do we call a star that suddenly increases in brightness?", ["supernova"]),
        ("What is a black hole?", ["collapsed star", "gravitational pull", "space-time", "nothing escapes"]),
        ("What is the term for a rocky object orbiting the sun, mostly between Mars and Jupiter?", ["asteroid"]),
        ("What do we call a frozen ball of gas, dust, and rock that orbits the sun?", ["comet"]),
        ("What planet is known for its giant storm called the Great Red Spot?", ["jupiter"]),
        ("Which planet is closest to the sun?", ["mercury"]),
        ("What is the name of the NASA rover that explored Mars in 2021?", ["perseverance"]),
        ("What do astronauts wear in space?", ["space suit"]),
        ("What is the name of our universe's beginning explosion theory?", ["big bang"]),
    ]

    score = 0

    for i, (question, answers) in enumerate(questions, start=1):
        print(f"\nQ{i}: {question}")
        user_input = input("Your answer: ")

        if check_answer(user_input, answers):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Not quite. One possible correct answer: {answers[0].title()}")

    print(f"\n🎯 Game over, {name}! Your final score: {score}/20")
    if score == 20:
        print("🌟 You're a space genius!")
    elif score >= 15:
        print("🚀 Great job!")
    elif score >= 10:
        print("🪐 Not bad. Keep learning!")
    else:
        print("🌌 It's okay. The universe is vast—keep exploring!")

if __name__ == "__main__":
    main()
