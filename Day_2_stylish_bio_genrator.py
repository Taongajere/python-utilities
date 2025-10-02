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


import textwrap

#questions
styles = """
1. Simple lines
2. Vertical flair
3. Emoji sandwich
"""
print(styles)

picked_style = input('choose your style (1, 2, 3): ').strip()

if picked_style not in ['1', '2', '3']:
    print('invalid style, defaulting to style 1')
    picked_style = '1'


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
        print('no custome hundle accepted, hundle created from name')
        optional_answers[key] = place_holder[key]
    else:
        optional_answers[key] = ans

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
    else:
        emoji_answer[key] = ans
    answers.update(emoji_answer)


# bio print
bio_1 = (
    f"{answers['emoji']} {answers['name']} | {answers['profession']}",
    f"{word2emoji('light')} I absolutely love {answers['passion']}",
    f"{word2emoji('link')} {answers['hundle']}"
)

bio_2 = (
    f"{answers['emoji']} {answers['name']}",
    f"{answers['profession']}",
    f"{word2emoji('light')} {answers['passion']}",
    f"{word2emoji('link')} {answers['hundle']}"
)

bio_3 = (
    f"{answers['emoji']} {answers['name']} {answers['emoji']}",
    f"{answers['profession']}",
    f"{word2emoji('light')} {answers['passion']}",
    f"{word2emoji('link')} {answers['hundle']}"
)

def style_picker(style: str) -> str:
    if style == '1':
        return '\n'.join(bio_1)
    elif style == '2':
        return '\n'.join(bio_2)
    else:
        return '\n'.join(bio_3)
    
final_bio = style_picker(picked_style)

print("\nYour stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(final_bio))
print("*" * 50)

# saving file 
save = input("Do you want to save this bio to a text file? (y/n): ").lower()

if save == 'y':
    filename = f"{answers['name'].lower().replace(' ', '_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_bio)
    print("file saved")