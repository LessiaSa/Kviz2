#От команды редакторов электронного журнала “Такие новости” пришла задача на разработку
# программы для анализа постов.
#Они хотят сократить длину текста, чтобы уменьшить время чтения новостей.
# Для этого нужно во всех новостях найти 10 самых популярных слов, где слово длиннее 6 символов.
import collections
import json


def read_json(file_patch, max_len_word=6, top_words=10): #maxдлину вынесли в параметр функции - чтобы в будущем можно было этот параметр изменять
    with open(file_patch, encoding='utf-8') as news_file:
        news = json.load(news_file)
        description_words = []
        for item in news['rss']['channel']['items']:
            #для итерации по списку использую конструкцию list comprehension
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            description_words.extend(description)
            counter_words = collections.Counter(description_words)
        print(sorted(counter_words.items(), key=lambda x: x[1], reverse=True)[:top_words])#можно так
        print(counter_words.most_common(top_words))#а можно проще и понятней

if __name__ == '__main__':
    read_json('newsafr.json')