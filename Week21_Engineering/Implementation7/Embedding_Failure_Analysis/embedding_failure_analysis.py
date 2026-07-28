from Week21_Engineering.Implementation5.Embedding_Search.embedding_search import search2

def find_failure_cases(query, expected_ids=None):
    if expected_ids is None:
        expected_ids = []

    results = search2(query, 5)
    actual_ids = [r[0] for r in results]

    failures = []
    for eid in expected_ids:
        if eid not in actual_ids:
            failures.append({
                "query": query,
                "expected": eid,
                "actual_top5": actual_ids,
                "error_type": "expected_not_in_top5",
                "reason": "expected document missing",
                "improvement": "improve embedding or dataset"
            })

    return failures
