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
