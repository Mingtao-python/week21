from Implementation5.Embedding_Search.embedding_search import search2

def find_failure_cases(query):
    results = search2(query, 5)
    ids = [r[0] for r in results]
    return [{"query": query, "top5": ids}]
