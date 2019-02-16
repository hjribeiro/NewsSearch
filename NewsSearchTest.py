import unittest
import NewsSearch


class TestStringMethods(unittest.TestCase):
    def test_negative_or(self):
        keyword_list = ['NegativeOrTest']
        expected_reference_list = []
        search_type = 'or'
        search_reference_list = NewsSearch.news_search(keyword_list, search_type)
        self.assertEqual(expected_reference_list, search_reference_list)

    def test_negative_and(self):
        keyword_list = ['Negative', 'and', 'test', 'RANDOMwoRD123']
        expected_reference_list = []
        search_type = 'and'
        search_reference_list = NewsSearch.news_search(keyword_list, search_type)
        self.assertEqual(expected_reference_list, search_reference_list)

    def test_query_Care_Quality_Commission_or(self):
        keyword_list = ['Care', 'Quality', 'Commission']
        expected_reference_list = [0, 1, 2, 3, 4, 5, 6]
        search_type = 'or'
        search_reference_list = NewsSearch.news_search(keyword_list, search_type)
        self.assertEqual(expected_reference_list, search_reference_list)

    def test_query_September_2004_or(self):
        keyword_list = ['September', '2004']
        expected_reference_list = [9]
        search_type = 'or'
        search_reference_list = NewsSearch.news_search(keyword_list, search_type)
        self.assertEqual(expected_reference_list, search_reference_list)

    def test_query_general_population_generally_or(self):
        keyword_list = ['general', 'population', 'generally']
        expected_reference_list = [6, 8]
        search_type = 'or'
        search_reference_list = NewsSearch.news_search(keyword_list, search_type)
        self.assertEqual(expected_reference_list, search_reference_list)

    def test_query_Care_Quality_Commission_admission_and(self):
        keyword_list = ['Care', 'Quality', 'Commission', 'admission']
        expected_reference_list = [1]
        search_type = 'and'
        search_reference_list = NewsSearch.news_search(keyword_list, search_type)
        self.assertEqual(expected_reference_list, search_reference_list)

    def test_query_general_population_Alzheimer_and(self):
        keyword_list = ['general', 'population', 'Alzheimer']
        expected_reference_list = [6]
        search_type = 'and'
        search_reference_list = NewsSearch.news_search(keyword_list, search_type)
        self.assertEqual(expected_reference_list, search_reference_list)


if __name__ == '__main__':
    unittest.main()
