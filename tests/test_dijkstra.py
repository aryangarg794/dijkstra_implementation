import pytest

from src.dijkstra_algorithm.dijkstra import dijkstra_shortest_path

def test_dijkstra_simple():
    graph = [
        [0, 1, 4],
        [1, 0, 2],
        [4, 2, 0]
    ]
    source = 0
    expected_paths = [0, 1, 3] 
    assert dijkstra_shortest_path(graph, source) == expected_paths, "Test with simple graph failed."

def test_dijkstra_larger_graph():
    graph = [
        [0, 7, 9, 0, 0, 14],
        [7, 0, 10, 15, 0, 0],
        [9, 10, 0, 11, 0, 2],
        [0, 15, 11, 0, 6, 0],
        [0, 0, 0, 6, 0, 9],
        [14, 0, 2, 0, 9, 0]
    ]
    source = 0
    expected_paths = [0, 7, 9, 20, 20, 11]  
    assert dijkstra_shortest_path(graph, source) == expected_paths, "Test with larger graph failed."

def test_dijkstra_disconnected_graph():
    graph = [
        [0, 7, 0],
        [7, 0, 0],
        [0, 0, 0]
    ]
    source = 0
    expected_paths = [0, 7, float('inf')]  
    assert dijkstra_shortest_path(graph, source) == expected_paths, "Test with disconnected graph failed."

def test_dijkstra_single_node():
    graph = [
        [0]
    ]
    source = 0
    expected_paths = [0]  
    assert dijkstra_shortest_path(graph, source) == expected_paths, "Test with single node graph failed."

def test_dijkstra_fully_connected():
    graph = [
        [0, 1, 2],
        [1, 0, 1],
        [2, 1, 0]
    ]
    source = 0
    expected_paths = [0, 1, 2]  
    assert dijkstra_shortest_path(graph, source) == expected_paths, "Test with fully connected graph failed."
