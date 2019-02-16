import argparse


def news_or_search(keyword_set, news_file):
    line_number = 0
    search_references = []
    for line in news_file:
        line_set = set(line.split())
        if not line_set.isdisjoint(keyword_set):
            search_references.append(line_number)
        line_number += 1
    return search_references


def news_and_search(keyword_set, news_file):
    line_number = 0
    search_references = []
    for line in news_file:
        line_set = set(line.split())
        if keyword_set.issubset(line_set):
            search_references.append(line_number)
        line_number += 1
    return search_references


def news_search(keyword_list, search_type):
    keyword_set = set(keyword_list)
    with open("hscic-news", 'r') as news_file:
        if search_type == 'or':
            return news_or_search(keyword_set, news_file)
        else:
            return news_and_search(keyword_set, news_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='''Search news based on Keyword list and type of search. 
                                                 Search is not case sensitive''')
    parser.add_argument('keyword_list', type=str, nargs='+',
                        help='list of keywords to be searched')
    parser.add_argument('search_type', choices=['and', 'or', 'AND', 'OR'],
                        help='type of search executed -- possible values are [AND] or [OR]')

    args = parser.parse_args()
    searchType = args.search_type.lower()
    print(news_search(args.keyword_list, searchType))






