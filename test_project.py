import pytest
from project import generate, check, contents


def test_generate():
    generate("Test Task", "2024/12/15")
    assert len(contents) == 1
    assert contents[0]["Task"] == "Test Task"
    assert contents[0]["Due Date"] == "2024/12/15"
    assert contents[0]["Days Left"] > 0
    assert "Just Chill" in contents[0]["Urgency"]


def test_sort():
    contents.clear()
    generate("Test Task 1", "2024/12/30")
    generate("Test Task 2", "2024/12/15")
    assert contents[0]["Task"] == "Test Task 2"


def test_check():
    contents.clear()
    generate("Test Task 1", "2024/12/30")
    generate("Test Task 2", "2024/12/15")
    check(1)
    assert len(contents) == 1
    assert contents[0]["Task"] == "Test Task 1"
