import pytest
from src.main import factorial, combinatoria, permutacion

@pytest.mark.parametrize(
    "n, result",
    [
        (3, 6),
        (5, 120),
        (7, 5040)
    ]
)

def test_factorial(n, result):
    assert factorial(n) == result

@pytest.mark.parametrize(
    "n_combinatoria, k_combinatoria, result_combinatoria",
    [
        (1, 1, 1),
        (3, 2, 3),
        (5, 3, 10),
        (10, 8, 45)
    ]
)

def test_combinatoria(n_combinatoria, k_combinatoria, result_combinatoria):
    assert combinatoria(n_combinatoria, k_combinatoria) == result_combinatoria

@pytest.mark.parametrize(
    "n_permutacion, k_permutacion, result_permutacion",
    [
        (1, 1, 1),
        (3, 2, 6),
        (9, 3, 504),
        (10, 8, 1814400)
    ]
)

def test_permutacion(n_permutacion, k_permutacion, result_permutacion):
    assert permutacion(n_permutacion, k_permutacion) == result_permutacion