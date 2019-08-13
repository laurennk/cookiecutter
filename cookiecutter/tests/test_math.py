import pytest
import numpy as np

import cookiecutter as cc

@pytest.mark.parametrize('n, answer', [(0, 1), (1, 2), (2, 2.5), (3, 2.6666667)])
def test_euler(n,answer):
    assert cc.math.euler(n) == pytest.approx(answer, abs=1.0e-6)

def test_euler_failures():
    with pytest.raises(ValueError) as exc:
        cc.math.euler(-1)
    
    assert "positive in" in str(exc.value)

def test_pi():
    np.random.seed(0)
    x = cc.math.pi()
    print(x)
    assert x == pytest.approx(3.13304, abs=1.0e-6)

    assert cc.math.pi(1) == 0.0 or 1.0

def test_pi_failures():
    with pytest.raises(ValueError) as exc:
        cc.math.pi(0)
    
    assert "positive in" in str(exc.value)
