or my profrom question_model import Question
from quizebrain1 import QuizeBrain
from data import question_data
from colorama import Fore, Style, init

init(autoreset=True)

# Welcoming message with bold and green text
welcoming = print(f"{Fore.GREEN}{Style.BRIGHT}Welcome to Our Company's Assessment Test! 🚀 Congratulations on taking the first step towards becoming part of our team! 🎉\n"
                  "This assessment is designed to help us understand more about you, your skills, and how you align with our company's values and culture. \n"
                  "It's also a great way for you to learn more about what we're looking for in our team members.\n"
                  "We're excited to get to know you better! Good luck!🍀\n")


question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question= Question(question_text,question_answer)
    question_bank.append(new_question)


quize = QuizeBrain(question_bank)

while quize.atill_have_q():
    quize.next_question()


init(autoreset=True)

total_questions = quize.question_number * 2  

print(f"{Style.BRIGHT}Your final score is {Fore.GREEN}{quize.score}/{total_questions}{Style.RESET_ALL}\n")

if quize.score >= 90:
    print(f"{Fore.YELLOW}Congratulations! 🌟 {Fore.CYAN}Your score indicates that you're an exceptional fit for our company culture and values. Your skills and aspirations align closely with what we're looking for in team members. We're excited about the potential of having you on board!{Style.RESET_ALL}")
elif 70 <= quize.score < 90:
    print(f"{Fore.GREEN}Great job! 👍 {Fore.CYAN}Your score shows that you have strong potential and a good alignment with our company's culture and values. There are many areas where you excel, and we believe you could make significant contributions to our team.{Style.RESET_ALL}")
elif 50 <= quize.score < 70:
    print(f"{Fore.BLUE}Well done! {Fore.CYAN}Your score suggests that you're a good fit for our company with some areas for growth. We appreciate your strengths and look forward to discussing how we can support your development in areas where there's room for improvement.{Style.RESET_ALL}")
elif 30 <= quize.score < 50:
    print(f"{Fore.MAGENTA}Thank you for completing our assessment. {Fore.CYAN}Your score indicates a moderate fit with our company's culture and values. While there are areas that align with our needs, there are also opportunities for development. Let's explore how we might bridge those gaps together.{Style.RESET_ALL}")
else:
    print(f"{Fore.RED}We appreciate your interest and the time you've taken to complete our assessment. {Fore.CYAN}Based on your score, it seems there might be some misalignment between your current skills/aspirations and what our company is looking for. This doesn't mean there isn't a place for you here, but we may need to discuss and explore potential paths forward more closely.{Style.RESET_ALL}")
