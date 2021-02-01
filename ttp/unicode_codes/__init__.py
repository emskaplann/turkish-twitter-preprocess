# -*- coding: utf-8 -*-
unicodes_en = __import__('en_emoji')


__all__ = [
    'EMOJI_UNICODE', 'UNICODE_EMOJI',
    'EMOJI_UNICODE_ENGLISH', 'UNICODE_EMOJI_ENGLISH',
    'EMOJI_ALIAS_UNICODE_ENGLISH', 'UNICODE_EMOJI_ALIAS_ENGLISH',
]


EMOJI_UNICODE = {
    'en': unicodes_en.EMOJI_UNICODE_ENGLISH,
}

UNICODE_EMOJI = {
    'en': unicodes_en.UNICODE_EMOJI_ENGLISH,
}
