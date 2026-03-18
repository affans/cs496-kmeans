import pytest
from kmeans import euclidean_distance
from kmeans import find_closest_centroid
from kmeans import update_centroids
from kmeans import has_converged

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

def test_data_empty():
    with pytest.raises(ValueError):
        update_centroids([], [], 2)

def test_old_empty():
    with pytest.raises(ValueError):
        has_converged([], [], 0.10)

def test_new_empty():
    with pytest.raises(ValueError):
        has_converged([], [], 0.10)

def test_non_numeric():
    with pytest.raises(TypeError):
        update_centroids([1, 'a'], [2, 'b'], 2)

def test_non_numeric_old():
    with pytest.raises(TypeError):
        has_converged([1, 'a'], [2, 'b'], 0.10)

def test_non_numeric_new():
    with pytest.raises(TypeError):
        has_converged([1, 'a'], [2, 'b'], 0.10)