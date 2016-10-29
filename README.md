Simple NLP (Natural Language Processing) on streaming data from Twitter
====

![](http://briank.im/content/images/2015/06/twstream.jpg)

Twitter is a "firehouse" of language. However, most Python demos on the web take a snapshot of Twitter data then process it offline (i.e., batch). This repo is an attempt to demystify stream processing, especially for lightweight NLP. 

Data is moving toward streaming as the default:

>Batch processing is a degenerate version of stream processing.

The modest goals are to connect to the Twitter stream and process what data we can as it flies by. Python is a very good (but not perfect) choice for this paradigm, in particular Python 3 is well suited with its preference for iterators and Unicode.

Check out [Twitter's Streaming API documentation](https://dev.twitter.com/streaming/overview) for more info.
