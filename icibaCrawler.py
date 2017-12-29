import requests
import re
import bs4
import warnings

warnings.filterwarnings("ignore")


def lookup_word_mean(word):
    words_dict = {}
    word_website = 'http://www.iciba.com/' + word
    res = requests.get(word_website)
    soup = bs4.BeautifulSoup(res.text)
    word_means = soup.select('li[class="clearfix"]')
    for each_property_mean in word_means:
        word_property = each_property_mean.select('span[class="prop"]')[0].get_text()
        pep_word_means = [each_dec.get_text() for each_dec in each_property_mean.select('p span')]
        words_dict[word_property] = pep_word_means
    return words_dict


def lookup_word_level(word):
    word_level = []
    word_website = 'http://www.iciba.com/' + word
    res = requests.get(word_website)
    soup = bs4.BeautifulSoup(res.text)
    base_level_tags = soup.select('div[class="base-level"] span')
    for each_level in base_level_tags:
        level_match = re.search(r'\w+', each_level.get_text())
        if level_match is not None:
            word_level.append(level_match.group())

    return word_level


def lookup_word(word):
    word_meaning = word + '\n'
    for k, v in lookup_word_mean(word).items():
        word_meaning += "%-4s" % k
        for ev in v:
            word_meaning += "%s" % ev
        word_meaning += "\n"
    for each_level in lookup_word_level(word):
        word_meaning += "%s " % each_level
    return word_meaning


print(lookup_word("cheat sheet"))
