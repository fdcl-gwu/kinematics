"""This will test our functions on the n-sphere

"""
from .. import sphere
import numpy as np

def test_two_sphere_random_vector_norm():
    vec = sphere.sphere_rand(3)
    np.testing.assert_almost_equal(np.linalg.norm(vec), 1)

def test_two_sphere_tangent_vector():
    vec = sphere.sphere_rand(3)
    vecd = sphere.sphere_tan_rand(vec)

    np.testing.assert_almost_equal(np.dot(vec, vecd), 0)
