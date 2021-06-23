#!/usr/bin/env python

"""Tests for `calc` package."""

import pytest


from calc.calc import Calc



def test_add_two_numbers():
    c  = Calc()
    res = c.add(4,5)
    assert res == 9


def test_add_three_numbers():
    c= Calc()
    res = c.add(12,1,6)
    assert res == 19



def test_add_many_numbers():
    n= range(100)

    res = Calc.add(*n)
    assert res == 4950

def test_subtract_two_numbers():
    c = Calc()
    res = c.sub(10, 3)
    assert res == 7

def test_mul_two_numbers():
    c = Calc()
    res = c.mul(10, 300)
    assert res == 3000


def test_mul_multiple_numbers():
    numbers = range(1,10)
    c=Calc()
    res = c.mul(*numbers)
    assert res == 362880


def test_div_two_numbers_float():
    c = Calc()
    res = c.div(13, 2)
    assert res == 6.5

def test_div_by_zero_returns_infinite():
    c = Calc()
    res = c.div(5, 0)
    assert res == "infinite"

def test_mul_by_zero_raises_exception():
    c = Calc()
    with pytest.raises(ValueError):
        c.mul(3, 0)

def test_avg_correct_average():
    c = Calc()
    res = c.avg([2, 5, 12, 98])
    assert res == 29.25

def test_avg_removes_upper_outliers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=90)
    assert res == pytest.approx(6.333333)

def test_avg_removes_lower_outliers():
    c = Calc()
    res = c.avg([2, 5, 12, 98], lt=10)
    assert res == pytest.approx(55)

def test_avg_uppper_threshold_is_included():
    c = Calc()
    res = c.avg([2, 5, 12, 98], ut=98)
    assert res == 29.25

def test_avg_lower_threshold_is_included():
    c = Calc()
    res = c.avg([2, 5, 12, 98], lt=2)
    assert res == 29.25

def test_avg_empty_list():
    c = Calc()
    res = c.avg([])
    assert res == 0

def test_avg_manages_empty_list_after_outlier_removal():
    c = Calc()
    res = c.avg([12, 98], lt=15, ut=90)
    assert res == 0

def test_avg_manages_empty_list_before_outlier_removal():
    c = Calc()
    res = c.avg([], lt=15, ut=90)
    assert res == 0