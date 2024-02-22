import openai


openai.api_key = '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'

def get_fitness_advice(question):
    try:
        response = openai.Completion.create(
          engine="text-davinci-003",
          prompt=question,
          temperature=0.5,
          max_tokens=100,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_user_preferences():
    print("Let's personalize your fitness journey.")
    body_type = input("What is your body type? (e.g., ectomorph, mesomorph, endomorph): ")
    fitness_goals = input("What are your fitness goals? (e.g., weight loss, muscle gain, endurance): ")
    dietary_restrictions = input("Do you have any dietary restrictions?: ")
    
    return "Based on your inputs, we recommend a balanced diet and regular exercise. Please consult a professional for a detailed plan."

def main():
    while True:
        print("\nWelcome to the Fitness Chatbot!")
        print("1. Ask a fitness-related question")
        print("2. Get personalized workout and diet plans")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == "1":
            question = input("\nWhat is your fitness-related question? ")
            print(get_fitness_advice(question))
        elif choice == "2":
            print(get_user_preferences())
        elif choice == "3":
            print("Thank you for using the Fitness Chatbot. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
