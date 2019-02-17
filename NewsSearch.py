import argparse


def news_search(keyword_list, search_type):
    keyword_set = set(keyword_list)
    with open("hscic-news", 'r') as news_file:
        line_number = 0
        search_references = []
        for line in news_file:
            line_set = set(line.split())
            if search_type == 'or':  # OR search, match if keyword set and line are not disjont
                if not line_set.isdisjoint(keyword_set):
                    search_references.append(line_number)
            else:
                if keyword_set.issubset(line_set):  # AND search, match if keyword is subset of line
                    search_references.append(line_number)
            line_number += 1
        return search_references


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
