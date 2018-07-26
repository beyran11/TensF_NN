from xml.sax.saxutils import escape, unescape

import unicodedata


# https://wiki.python.org/moin/EscapingHtml
# escape() and unescape() takes care of "&" , "<" and ">" - we need to handle quotes, so we don't break things
html_attribute_escape_table = {
    '"': "&quot;",
    "'": "&apos;",
}


html_attribute_unescape_table = {v: k for (k, v) in html_attribute_escape_table.items()}


def html_attribute_escape(text):
    return escape(text, html_attribute_escape_table)


def html_attribute_unescape(text):
    return unescape(text, html_attribute_unescape_table)


##

def force_clean_ascii_NFKD(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore')


def force_clean_ascii_NFKC(text):
    return unicodedata.normalize('NFKC', text).encode('ascii', 'ignore')
