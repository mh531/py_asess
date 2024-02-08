This project introduces a True/False quiz application specifically designed for company assessments, aiming to evaluate potential candidates' alignment with organizational values and general knowledge. The quiz is pre-filled with a variety of questions tailored to gauge various competencies and cultural fit, although the questions within `data.py` can be customized to fit any company's specific assessment criteria.

Built with Python, the application showcases object-oriented programming principles by utilizing classes to model questions (`Question`) and control quiz logic (`QuizBrain`). The project is structured across four main files for clear separation of concerns:

- `data.py`: Contains the quiz questions and answers in a structured format, easily editable to update the quiz content.
- `question_model.py`: Defines the `Question` class, which structures the data for each quiz question.
- `quiz_brain.py`: Implements the `QuizBrain` class, managing quiz functionality such as iterating over questions, checking answers, and keeping score.
- `main.py`: Serves as the entry point for the application, tying together the other components and launching the quiz.

Scoring is transparent, with immediate feedback provided after each question, and a final score presented at the end to reflect the participant's compatibility with the company's values and expectations. The use of the Colorama library enhances the terminal output with colored text, improving the user experience and making the quiz more engaging.

Whether for pre-interview screening, employee onboarding, or simply as a tool for self-assessment, this quiz application offers a flexible and interactive approach to understanding and evaluating company-candidate alignment.
