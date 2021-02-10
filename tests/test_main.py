from Parens import balanced_parens2 
import pytest

def test__balanced_parens2_1():
    assert balanced_parens2('(()())')

def test__balanced_parens2_2():
    assert balanced_parens2('(()(()((()))))()(())')

def test__balanced_parens2_3():
    assert balanced_parens2('([]{})')

def test__balanced_parens2_4():
    assert balanced_parens2('([]{[][]{{()}}})')

def test__balanced_parens2_5():
    assert not balanced_parens2('([{]})')

def test__balanced_parens2_5b():
    assert not balanced_parens2('([{]}])')

def test__balanced_parens2_6():
    assert not balanced_parens2(')))(((')

def test__balanced_parens2_7():
    assert not balanced_parens2('(()()')

def test__balanced_parens2_8():
    assert not balanced_parens2('(()()))')

def test__balanced_parens2_9():
    n = 10000
    open_parens = '({['*n
    close_parens = open_parens[::-1].translate(open_parens.maketrans('([{',')]}'))
    assert balanced_parens2(open_parens+close_parens)
    assert not balanced_parens2(close_parens+open_parens)
    assert not balanced_parens2(open_parens+'('+close_parens)
    assert not balanced_parens2('('+open_parens+close_parens)
    assert not balanced_parens2(open_parens+close_parens+')')
