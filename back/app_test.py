import app
import pytest

def test_fibo0is0():
    assert app.fibonacci(0) == 0

def test_fibo1is1():
    assert app.fibonacci(1) == 1

def test_fibo2is1():
    assert app.fibonacci(2) == 1

def test_fibonegativeisnegative1():
    assert app.fibonacci(-1) == -1
    assert app.fibonacci(-2) == -1
    assert app.fibonacci(-10) == -1

def test_fibo5is5():
    assert app.fibonacci(5) == 5

def test_fibo10is55():
    assert app.fibonacci(10) == 55

def test_fibo20is6765():
    assert app.fibonacci(20) == 6765
