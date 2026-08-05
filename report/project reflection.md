# reflection
## Part 1 -- What have I done
I have done several small programs that can run individually that are about what have I learnd, they are embedding(search and similarity), gradient descent, vector search and tfidf search, each one have a separate application and can be also runed in app.py.

## Part 2 -- What error have I got?
Every time I need to text something it cost a very very long time, I didnt created a .json fil so the info is not stored.  
when I am taking screan shot of the programm in app.py, I have to take 3 of them because there are 3 separate pages.
There are too many files in this project and I only have 2 hours to complete it, so I was tring to be very quick but the files is very unkind as they are a bit separated.

## Part 3 -- How to fix it?
- Create a json file to store all the information including the metadata just for incase and run multiple application at a time to prevent running a time each test.
- Make the website 3 titles instead of 3 pages and then change back to 3-page-mode when finish taking the picture or use a picture editor.
- Organize the files better such as creating folder naming Picture for example 1-3.png

## Part 4 -- What will I inprove If I need to do it again?
- label each part of the programm using # for know what does what.
- organise the files better and name files as little words possible.
- Use a better machine for evry application.

## Part 5 -- What is the actual result?
- Current dataset size: 50
- Current embedding backend: sentence-transformers/all-MiniLM-L6-v2 and deterministic fallback
- Average query time: *Copied from stop watch* 00'00'00''786
- Main bottleneck: (For the project)Don't have time to test 20 real examples
- Test failure example: See in examples/ folder or see below
Faiture example:  
```text
Failure Analysis

Expected document 'Machine learning is a field of artificial intelligence.' did not appear in the top-5 results.
Query: Searching machine

Expected: Machine learning is a field of artificial intelligence.

Ranking:

. Embedding: not in top-5
. Cosine: not in top-5
. Euclidean: not in top-5

Reason: The embedding model considers other documents more semantically similar.
Recommendation: Improve dataset quality, add more relevant samples, or fine-tune embeddings.```