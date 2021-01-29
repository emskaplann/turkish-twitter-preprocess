import re
import emoji

def lower(text):
    text=re.sub("İ","i",text)
    text = text.lower()
    return text

def replace_emoji(text):
    return emoji.demojize(text, delimiters=(" ", " "))

def resubComma(text):
    text = re.sub(","," ",texts)
    return text

def vanish_punc(text):
    regex = re.compile('[%s]' % re.escape(punctuation))
    text = regex.sub(' ', text)
    return text

def vanish_digits(text):
    text=text.strip()
    vanish_digits = str.maketrans('', '', digits)
    text=text.translate(vanish_digits)
    return text

def replace_emoticon(text):
    check_pos = re.findall(r'(?::\)|:-\)|=\)|:D|:d|<3|\(:|:\'\)|\^\^|;\)|\(-:)', text)
    check_neg = re.findall(r'(:-\(|:\(|;\(|;-\(|=\(|:/|:\\|-_-|\):|\)-:)', text)
    if check_pos:
        #text = ":)"
        text = "SMILEYPOSITIVE"
    elif check_neg:
        #text = ":("
        text = "SMILEYNEGATIVE"
    return text

def remove_url(text):
    return re.sub(r'https?:\/\/.*[\r\n]*', '', text)

def remove_handle(text):
    return re.sub('@[^\s]+', '', text)

def preprocess_sentence(sentence, stopwords):
    sentence = remove_url(sentence)
    sentence = remove_handle(sentence)
    sentence = replace_emoji(sentence)
    sentence = lower(sentence)
    sentence = resubComma(sentence)
    sentence = vanish_punc(sentence)
    sentence = vanish_digits(sentence)
    sentence = re.sub(' +', ' ', sentence)

    new_sentence = list()
    for word in sentence.split(' '):
      if word in stopwords:
        continue
      new_sentence.append(replace_emoticon(word))
    
    return " ".join(new_sentence)