import datetime as dt

questions = {
    'name': 'what is your name?',
    'age': 'How old are you?',
    'city': 'Where do you live?',
    'profession': 'What do you do for a living?',
    'hobby': 'What is your favourite thing to do?',
}

answers = {}

for key, q in questions.items():
    ans = input(q)
    answers[key] = ans.strip()

self_intro = (
    f'Hello! My name is {answers["name"]}.',
    f"I'm {answers['age']} years old",
    f"and live in {answers['city']}.",
    f"I work as a {answers['profession']},",
    f"and I absolutely enjoy {answers['hobby']} in my free time.",
    f"Nice to meet you!"
)

self_intro = self_intro + (f'Logged on: {dt.date.today()}',)

print('\n'.join(self_intro))