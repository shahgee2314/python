import operator
def count(article):
    words = article.split()
    Word_count = len(words)
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1
    var_dict = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
    return var_dict, Word_count