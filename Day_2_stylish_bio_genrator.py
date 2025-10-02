import emoji
import word2emoji


"""
Challenge: Stylish Bio Generator for Instagram/Twitter

Create a Python utility that asks the user for a few key details and generates a short, stylish bio that could be used for social media profiles like Instagram or Twitter.

Your program should:
1. Prompt the user to enter their:
   - Name
   - Profession
   - One-liner passion or goal
   - Favorite emoji (optional)
   - Website or handle (optional)

2. Generate a stylish 2-3 line bio using the inputs. It should feel modern, concise, and catchy.

3. Add optional hashtags or emojis for flair.

Example:
Input:
  Name: Riya
  Profession: Designer
  Passion: Making things beautiful
  Emoji: 🎨
  Website: @riya.design

Output:
  🎨 Riya | Designer  
  💡 Making things beautiful  
  🔗 @riya.design

Bonus:
- Let the user pick from 2-3 different layout styles.
- Ask the user if they want to save the result into a `.txt` file.
"""

questions = {
    'name': 'What is your name?',
    'profession':'what do you do for a living?',
    'passion':'in one word what are you most passionate about)?',
}


answers = {}



for key, question in questions.items():
    ans = input(question).strip()
    answers[key] = ans


# hundle is optional
optional_questions = {
    'hundle': 'what is your hundle?'
}

place_holder = {
    'hundle': f"iam{answers['name']}"
}

optional_answers = {}
for key, question in optional_questions.items():
    ans = input(question).strip()
    if ans == '':
        optional_answers[key] = place_holder[key]
        answers.update(optional_answers)

# emoji

def emoji_creator (passion: str) -> str:
    return word2emoji(passion.lower())
    ''' this fuction returns the passion in lower case and turns it in an emoji'''

emoji_questions = {'emoji': 'choose custome emoji'}
emoji_placeholder = {'emoji': f"{emoji_creator(answers['passion'])}"}
emoji_answer = {}

for key, emoji_question in emoji_questions.items():
    ans = input(emoji_question).strip()
    if ans == '':
        print('no custrom emoji selected, passion will be turned to emoji')
        emoji_answer[key] = emoji_placeholder[key]
        answers.update(emoji_answer)

print(answers)