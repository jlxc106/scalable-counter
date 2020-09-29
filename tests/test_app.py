# import os
import ast
# import tempfile

# import pytest

from app import create_app

def test_once(client):
    response = client.get('/api/item')
    data = ast.literal_eval(response.data.decode("utf-8"))
    assert "count" in data

#redis-py isn't working with pytest -- returns zero only...
def best_multiple(client):
    response = client.get("/api/item")
    data = ast.literal_eval(response.data.decode("utf-8"))
    assert "count" in data
    initialCount = data["count"]
    n = 100
    for _ in range(n-1):
        response = client.get("/api/item")
    
    response = client.get("/api/item")
    data = ast.literal_eval(response.data.decode("utf-8"))
    assert "count" in data
    finalCount = data["count"]
    diff_count = finalCount - initialCount
    # print(diff_count)
    assert diff_count == n