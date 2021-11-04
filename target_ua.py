"""
TARGET GAME FOR UKRAINIAN LANGUAGE
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
    right_words = []
    missed_words = []
    for word in user_words:
        if(word, language_part) in dict_of_words:
            right_words.append(word)
    for word in dict_of_words:
        if word[0] not in right_words:
            missed_words.append(word)
    return right_words, missed_words



