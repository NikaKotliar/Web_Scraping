def filter_by_tag(keywords, text, tags):
    if keywords & tags:
        return True
    for part_text in text:
        stripped_text = part_text.text.strip()
        if len(stripped_text) > 0:
            words_set = set(stripped_text.split(' '))
            if keywords & words_set:
                return True
    return False

