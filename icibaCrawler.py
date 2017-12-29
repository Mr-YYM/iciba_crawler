import requests
import re
import bs4
import warnings

warnings.filterwarnings("ignore")

def check_word(word):
    word_level = []
    word_website = 'http://www.iciba.com/' + word
    res = requests.get(word_website)
    soup = bs4.BeautifulSoup(res.text)
    base_level_tags = soup.select('div[class="base-level"] span')
    for each_level in base_level_tags:
        level_match = re.search('\w+',each_level.get_text())
        if level_match is not None:
            word_level.append(level_match.group())

    return word_level


print(check_word('crawler'))
