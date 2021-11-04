"""
TARGET GAME FOR UKRAINIAN LANGUAGE MODULE
"""
import random

def generate_grid():
    alphabet_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',\
               'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю',\
               'я', 'є', 'і', 'ї', 'ґ']
    lst_of_letters = []
    while len(lst_of_letters) < 5:
        new_letter = random.choice(alphabet_letters)
        if new_letter not in lst_of_letters:
            lst_of_letters.append(new_letter)
    return lst_of_letters

def get_words(filename, letters):
    """
    >>> get_words('base.lst', ['є'])
    [('євнух', 'noun'), ('єврей', 'noun'), ('євро', 'noun'), ('єгер', 'noun'), ('єдваб', 'noun'), \
('єзуїт', 'noun'), ('єлей', 'noun'), ('ємний', 'adjective'), ('ємно', 'adverb'), \
('єна', 'noun'), ('єнот', 'noun'), ('єпарх', 'noun'), ('єресь', 'noun'), ('єри', 'noun'), \
('єрик', 'noun'), ('єрик', 'noun'), ('єство', 'noun'), ('єті', 'noun'), ('єхида', 'noun')]
    """
    with open(filename, "r", encoding='utf-8') as file:
        words = []
        for line in file:
            lst_line = line.replace("\n", "").split()
            if lst_line[0][0] in letters and len(lst_line[0]) <= 5:
                if lst_line[1].startswith("/n") or lst_line[1].startswith("noun"):
                    words.append((lst_line[0], "noun"))
                elif lst_line[1].startswith("/v") or lst_line[1].startswith("verb"):
                    words.append((lst_line[0], "verb"))
                elif lst_line[1].startswith("adv"):
                    words.append((lst_line[0], "adverb"))
                elif lst_line[1].startswith("/adj") or lst_line[1].startswith("adj"):
                    words.append((lst_line[0], "adjective"))
    return words
def check_user_words(user_words, language_part, letters, dict_of_words):
    legal_words = []
    right_words = []
    missed_words = []
    for word in user_words:
        word_lst = list(word)
        if word_lst[0] in letters and len(word_lst) <= 5:
            legal_words.append(word)

    for word in legal_words:
        word_lst = list(word)
        if (word, language_part) in dict_of_words:
            right_words.append(word)
    for (word, language_art) in dict_of_words:
        if language_art == language_part:
            if word not in right_words:
                missed_words.append(word)
    return right_words, missed_words