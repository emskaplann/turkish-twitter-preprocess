# -*- coding: utf-8 -*-

import re
from string import punctuation, digits
import itertools

emoji = __import__('emoji')

def lower(text):
    text=re.sub("İ","i",text)
    text = text.lower()
    return text

#TODO: translate emojis to turkish
def replace_emoji(text):
    return emoji.demojize(text, delimiters=(":", ":"))

def remove_emoji(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def resubComma(text):
    return re.sub(","," ",text)

def vanish_punc(text):
    regex = re.compile('[%s]' % re.escape(punctuation))
    text = regex.sub(' ', text)
    return text

def replace_emoticon(word, positive_str="SMILEYPOSITIVE", negative_str="SMILEYNEGATIVE"):
    check_pos = re.findall(r'(?::\)|:-\)|=\)|:D|:d|<3|\(:|:\'\)|\^\^|;\)|\(-:)', word)
    check_neg = re.findall(r'(:-\(|:\(|;\(|;-\(|=\(|:/|:\\|-_-|\):|\)-:)', word)
    if check_pos:
        #word = ":)"
        word = positive_str
    elif check_neg:
        #word = ":("
        word = negative_str
    return word

def remove_emoticon(text):
    new_text = re.sub(r'(?::\)|:-\)|=\)|:D|:d|<3|\(:|:\'\)|\^\^|;\)|\(-:)', '', text)
    new_text = re.sub(r'(:-\(|:\(|;\(|;-\(|=\(|:/|:\\|-_-|\):|\)-:)', '', new_text)
    return new_text

def remove_user_handle(text):
    return re.sub('@[^\s]+', '', text)

def remove_digits_and_extensions(text):
    return re.sub(r'[0-9][^\s]+', '', text)

def remove_digits(text):
    text = text.strip()
    vanish_digits = str.maketrans('', '', digits)
    text = text.translate(vanish_digits)
    return text

def remove_hashtag_and_word(text):
    return re.sub('#[^\s]+', '', text)

def remove_newline_char(text):
    return re.sub(' +', ' ', text.replace('\n', ' '))

def remove_extra_spaces(text):
    return re.sub(' +', ' ', text)

def dup_vanish(text):
     return (''.join(i for i, _ in itertools.groupby(text)))

def preprocess_sentence(sentence, stopwords):
    sentence = re.sub(r'https?:\/\/.*[\r\n]*', '', sentence)
    sentence = remove_user_handle(sentence)
    sentence = remove_hashtag_and_word(sentence)
    sentence = dup_vanish(sentence)
    sentence = remove_emoticon(sentence)
    sentence = remove_emoji(sentence)
    sentence = lower(sentence)
    sentence = resubComma(sentence)
    sentence = vanish_punc(sentence)
    sentence = remove_digits_and_extensions(sentence)
    sentence = remove_digits(sentence)
    sentence = remove_newline_char(sentence)

    sentence = remove_extra_spaces(sentence)
    # sentence = normalize(sentence)

    return sentence

# remove_emoji('iyi geceler 🙌')
# replace_emoji('iyi geceler 🙌')