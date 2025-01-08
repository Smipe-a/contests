# This task can be solved using frequency analysis
# Will find the frequency statistics of the Russian alphabet on the internet
from collections import Counter
from typing import List


SOURCE: List[str] = [
    'о', 'е', 'а', 'и', 'н',
    'т', 'с', 'р', 'в', 'л',
    'к', 'м', 'д', 'п', 'у',
    'я', 'ы', 'ь', 'г', 'з',
    'б', 'ч', 'й', 'х', 'ж',
    'ш', 'ю', 'ц', 'щ', 'э',
    'ф', 'ъ', 'ё'
]
LETTERS: str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


if __name__ == '__main__':
    with open('young_and_yandex\intern_week_offer_analytics_2024\encoded.txt',
              encoding='utf-8') as file:
        text = file.read()

    # Filter the characters, keeping only Cyrillic ones, and count their frequency
    counter = Counter(filter(lambda x: x in LETTERS, text))

    # Check the number of letters obtained from the text and from the original data
    # If any are missing, we will add the missing ones to the counter
    if len(counter) != len(SOURCE):
        unique_letters = Counter(SOURCE) - counter
        for letter, _ in unique_letters.items():
            counter[letter] = 0
    
    # Generate a list of letters sorted by frequency
    counter = sorted(counter, key=lambda x: counter[x], reverse=True)

    # Now the task boils down to permuting the positions of letters in SOURCE
    # At the first run, attention can be paid to words consisting of 1-4 letters
    # and selecting the appropriate variant
    # For example, the letter 'т' can be replaced with (и, в, у, о, к, с),
    # and the word 'зороные' resembles 'золотые'
    # Note: Letters with similar frequency % should be swapped with each other
    solve = {
        'и': 'н', 'н': 'т', 'т': 'и', 'р': 'л',
        'л': 'р', 'к': 'м', 'м': 'к', 'п': 'у',
        'у': 'п', 'я': 'ь', 'ь': 'я', 'г': 'ч',
        'б': 'г', 'ч': 'б', 'й': 'ж', 'х': 'й',
        'ж': 'ш', 'ш': 'х', 'ц': 'щ', 'щ': 'э',
        'э': 'ц', 'ъ': 'ё', 'ё': 'ъ'
    }
    for i in range(len(SOURCE)):
        if SOURCE[i] in solve:
            SOURCE[i] = solve[SOURCE[i]]

    # Match the letters in the lists ordered by decreasing frequency
    translation_table = str.maketrans(
        ''.join(counter),
        ''.join(SOURCE)
    )

    # decoded_text = text.translate(translation_table)
    coded_text = 'уцмуьмвя ъэуопшйв ъэуеэвййацчуь цуцчуач ь чуй, щчу аё ужаоиа мшьузйулму ъэшюневювчд'
    decoded_text = coded_text.translate(translation_table)
    print(decoded_text)
