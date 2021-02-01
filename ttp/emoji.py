import re
unicode_codes = __import__('unicode_codes')

_EMOJI_REGEXP = None
_DEFAULT_DELIMITER = ':'

def get_emoji_regexp(language='en'):

    """Returns compiled regular expression that matches emojis defined in
    ``emoji.UNICODE_EMOJI_ALIAS``. The regular expression is only compiled once.
    """

    global _EMOJI_REGEXP
    # Build emoji regexp once
    EMOJI_UNICODE = unicode_codes.EMOJI_UNICODE[language]
    if _EMOJI_REGEXP is None:
        # Sort emojis by length to make sure multi-character emojis are
        # matched first
        emojis = sorted(EMOJI_UNICODE.values(), key=len, reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)
    return _EMOJI_REGEXP


def demojize(
        string,
        use_aliases=False,
        delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER),
        language='en',
):
    """Replace unicode emoji in a string with emoji shortcodes. Useful for storage.
    :param string: String contains unicode characters. MUST BE UNICODE.
    :param use_aliases: (optional) Return emoji aliases.  See ``emoji.UNICODE_EMOJI_ALIAS``.
    :param delimiters: (optional) User delimiters other than _DEFAULT_DELIMITER
    :param language: Choose language of emoji name
        >>> import emoji
        >>> print(emoji.emojize("Python is fun :thumbs_up:"))
        Python is fun 👍
        >>> print(emoji.demojize(u"Python is fun 👍"))
        Python is fun :thumbs_up:
        >>> print(emoji.demojize(u"Unicode is tricky 😯", delimiters=("__", "__")))
        Unicode is tricky __hushed_face__
    """
    UNICODE_EMOJI = unicode_codes.UNICODE_EMOJI[language]

    def replace(match):
        codes_dict = unicode_codes.UNICODE_EMOJI_ALIAS_ENGLISH if use_aliases else UNICODE_EMOJI
        val = codes_dict.get(match.group(0), match.group(0))
        # Val is the part we want to translate
        return delimiters[0] + val[1:-1] + delimiters[1]

    return re.sub(u'\ufe0f', '', (get_emoji_regexp(language).sub(replace, string)))