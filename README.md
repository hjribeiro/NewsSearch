
<h1>NewsSearch</h1>

Python program that searches for provided keywords on local file [hscic-news](./hscic-news) containing a list of News Articles.

<h2>Usage</h2>

The program can be executed with the following command:

```
python NewsSearch.py [-h] keyword_list [keyword_list ...] {and,or,AND,OR}
```

where `[keyword_list ...\]` is the list of keywords to search, separated by whitespace _( )_, followed by the type of search, `AND` or `OR`. Both lower-case and upper-case versions are valid.  

Running the following
```
NewsSearch.py [-h]
```
will display the usage information on the console.

<h3>Examples</h3>

To search for _September_ _AND_ _2004_:

```commandline
python NewsSearch.py September 2004 AND
```
the output should be the following:
```commandline
[9]
```

to search for the words _June_, _July_ _OR_ _December_:
```commandline
pyton NewsSearch June July December or
```
with the result
```commandline
[0, 1, 2, 3, 4, 8]
```
<h2>Design Considerations</h2>

It was assumed that the search is case-sensitive. This way searching for `september` should return different results than searching for `September`.  

No major performance considerations were taken over code simplicity and readability. It was assumed that the file and set operations have no negative impact on the desired performance.

<h2>Unit tests</h2>

The provided acceptance criteria were implemented as unit tests on the file [NewsSearchTest.py](NewsSearchTest.py). Two extra negative tests were added as first TDD iterations.

To execute the unit tests simply run

```commandline
python NewsSearchTest.py
```
and the output should be:

```commandline
.......
----------------------------------------------------------------------
Ran 7 tests in 0.010s

OK
```
