 
import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    word_list = ["lavkush", "learn", "kindness","vikash","hangman"]
    return word_list


def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word



# def get_available_letters(letters_guessed):
#     '''
#     letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
#     returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
#     eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
#     jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
#     '''
#     import string
#     letters_left = string.ascii_lowercase
#     for i in (letters_left):
#         if i!=letters_guessed:
#             return i
# get_available_letters("f")
