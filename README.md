
# twitter-turkish-preprocess
a light-weight python package to pre-process turkish twitter statuses(tweets).

**note:**
this package is not completely build yet. i'm publishing it for internal use purposes, however you are more than welcome to use it on your own. this package is designed for processing text data fetched from twitter to feed turkish nlp models. if you have any questions or concerns you can reach me from emskaplann@gmail.com.

## installation
on your terminal download the package to your local workspace via pip:
`pip install turkish-twitter-preprocess`

after having the package in your workspace you can simply import it to use it right away!
`import ttp`
`stopwords = ['with', 'are', ...]`
`ttp.preprocess_sentence("Example sentence!", stopwords)`

## functions you can use with the package

### `lower(text)`
this function should lower all the characters given in the string.
### `remove_emoji(text)`
this function should remove every emoji from the given string.
### `resubComma(text)`
this function should replacecommas from the given string with whitespace.
### `vanish_punc(text)`
this function should remove every punctuation from the given string.
### `replace_emoticon(text, positive_str="SMILEYPOSITIVE", negative_str="SMILEYNEGATIVE")`
this function should replace every emoticon from the given string as shown below.
positive emoticon example =>`:D, :), :d` and similars are replaced with `"SMILEYPOSITIVE"` 
negative emoticon example =>` -_-, =(, :(`and similars are replaced with `"SMILEYNEGATIVE"`
### `remove_emoticon(text)`
this function should remove every emoticon from the given string.
### `remove_user_handle(text)`
this function should every word that starts with '@' from the given string. we use this for removing user handles from the twitter data.
### `remove_digits_and_extensions(text)`
this function should remove every digits and their extensions from the string, for example if we have a word like this `"100'de 1 sanslari yok!"`, this function would transform this into `"sanslari yok"`.
### `remove_digits(text)`
this function should remove every digit from the given string.
### `remove_hashtag_and_word(text)`
this function should remove every word that starts with '#' from the given string. we use it to remove hashtags from the twitter data because hashtags does not mean a lot to a nlp model. and hashtags are not really permanent, it can lower your accuracy score in the long run.
### `remove_newline_char(text)`
this function should remove every `"\n"` character from the given string. we use it because it doesn't make any sense to use it in a nlp model.
### `remove_extra_spaces(text)`
this function should remove every extra space from the given string.
### `dup_vanish(text)`
this function should normalize words that contains repeated nonsense characters in it. for example this string `"boyylleeee hukumeetttinnnn gellmiisssini gecmisiniii!"` would be transformed to `"boyle hukumetin gelmisini gecmisini!"`.
### `preprocess_sentence(text, stopwords)`
this function should preprocess the text with stopwords.