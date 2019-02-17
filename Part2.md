<h1>Part 2 - Riak Tasks</h1>
<h2>Riak version</h2>
Exercise was executed with no Riak installation. I have a Windows machine that is not compatible with Riak or even Docker.

<h2>Common query caching</h2>

It was assumed that it is expected to obtain the whole news article as response.  
Keywords are sorted alphabetically and concatenated to search type to create one unique key per Common Query. For example:

|Query|Type of search|Key 
|  -- | --  |  -- 
| Care Quality Commission | or | Care_Commission_Quality_or

The data is stored as a JSON array containing the full news article.

<h3>Creating Cache Entries</h3>
This results the following PUT requests to setup the cache:

```commandline
curl -XPUT \
  -H "Content-Type: application/json" \
  -d '["June 5 , 2013 : The majority of carers..." ,\
        "July 9 , 2013 : The HSCIC has...", \
        "June 19 , 2013 : New figures...", \
        "June 13 , 2013 : Almost one...", \
        "June 5 , 2013 : The majority ...", \
        "April 15 , 2013 Thousands...", \
        "February 19 , 2013 : Mortality..."]'\
  http://localhost:8098/types/news/buckets/cache/keys/Care_Commission_Quality_or
```

```commandline
   curl -XPUT \
     -H "Content-Type: application/json" \
     -d '["September 26 , 2012 : Income before..."]'\
     http://localhost:8098/types/news/buckets/cache/keys/2004_September_or
```
   
```commandline
curl -XPUT \
  -H "Content-Type: application/json" \
  -d '["February 19 , 2013 : Mortality...",\
       "December 12 , 2012 : The proportion..."]'\
  http://localhost:8098/types/news/buckets/cache/keys/general_generally_population_or
```

```commandline
   curl -XPUT \
     -H "Content-Type: application/json" \
     -d '["July 9 , 2013 : The HSCIC..."]'\
     http://localhost:8098/types/news/buckets/cache/keys/admission_Care_Commission_Quality_and
```
   
```commandline
   curl -XPUT \
     -H "Content-Type: application/json" \
     -d '["February 19 , 2013 : Mortality"]'\
     http://localhost:8098/types/news/buckets/cache/keys/general_population_Alzheimer_and
```

<h3>Retrieving Cache Entries</h3>

To query the cache, the same key creation formula should be followed:

|Query|Type of search|Key   
|  -- | --  |  --   
| Care Quality Commission | or | Care_Commission_Quality_or

and executing the following command:

```commandline
curl http://localhost:8098/types/news/buckets/cache/keys/Care_Commission_Quality_or
```

This should return the JSON Array stored with the news articles.

<h2>Monthly Indexes</h2>
To allow filtering by month and year, it is suggested to add a secondary index that it's the concatenation of year and month on the form YYYYMM.
This allows searching not only for an exact month of a year, but also for a range of months.
Example `201601` would retrieve results from January 2016, and `201701 to 201712` would retrieve all results from the year 2017.

<h3>Setting Up indexes</h3>

As per riak's latest documentation, it is recommended to implement this with secondary indexes instead of Riak search:

`2i is thus recommended when your use case requires an easy-to-use search mechanism that does not require a schema (as does Riak Search) and a basic query interface, i.e. an interface that enables an application to tell Riak things like “fetch all objects tagged with the string Milwaukee_Bucks” or “fetch all objects tagged with numbers between 1500 and 1509.”`  

To create the secondary Indexes on the first reference in the file we should run the following command:

```commandline
curl -XPUT H "Content-Type: text/plain"  \
            -H 'x-riak-index-yearmonth_int: 201307' \
             -d "June 5 , 2013 : The majority ..." \
             http://localhost:8098/buckets/hscicNews/keys/RESULT:1
```

were the header `-H 'x-riak-index-yearmonth_int: 201307'` sets the secondary index `yearmonth_int` as an integer for July 2013.

The remaining PUT commands are skipped, but they should be created using the appropriate key and secondary index.

<h3>Query for secondary indexes</h3>

To Query for secondary indexes for July 2013, the following CURL must be executed:

```curl localhost:8098/types/indexes/buckets/hscicNews/index/yearmonth_int/201307```

This command should return the list of Keys  from July 2013.

It is also possible to query for a range, the whole 2013 for example, and even return the associated News Articles associated with each key.
To do that the following CURL should be executed:

```commandline
curl localhost:8098/types/indexes/buckets/hscicNews/index/yearmonth_int/201301/201312?return_terms=true

```