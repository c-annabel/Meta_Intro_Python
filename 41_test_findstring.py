import findstring
import pytest
import importlib

def test_ispresent():
    assert findstring.ispresent("Al")

def test_nodigit():
    assert findstring.nodigit("N7")