import requests

apiurl = 'https://superheroapi.com/api/'
token = '2619421814940190'
char_list = ['Hulk', 'Captain America', 'Thanos']


def get_char_by_name(name):
    url = apiurl + token + '/search/' + name
    resp = requests.get(url).json()
    return resp


def who_is_most_intelligent(list_of_char):
    chars_intelligence = dict()

    for char in list_of_char:
        char_info = get_char_by_name(char)
        current_char_intelligence = char_info['results'][0]['powerstats']['intelligence']
        chars_intelligence[char] = int(current_char_intelligence)

    max_intelligence = max(chars_intelligence.values())

    for char, current_intelligence in chars_intelligence.items():
        if current_intelligence == max_intelligence:
            return char


print(who_is_most_intelligent(char_list))