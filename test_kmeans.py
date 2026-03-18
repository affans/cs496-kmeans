import pytest
from kmeans import euclidean_distance
from kmeans import find_closest_centroid

def test_euc_empty():
    with pytest.raises(ValueError):
        euclidean_distance([], [])
        
def test_euc_string():
    with pytest.raises(TypeError):
        euclidean_distance(str, str)

def test_euc_onestring():
    with pytest.raises(TypeError):
        euclidean_distance(str, [])


def test_cen_empty():
    with pytest.raises(ValueError):
        find_closest_centroid([], [])
        
def test_cen_string():
    with pytest.raises(TypeError):
        find_closest_centroid(str, str)