"""
Unit tests for the sentiment analysis function in app.py
"""

from app import analyze_sentiment


def test_analyze_sentiment_positive():
    """
    Test the analyze_sentiment function with positive input.
    """
    result = analyze_sentiment("I love this movie!")
    assert "POSITIVE" in result
    score = float(result.split(":")[-1].strip(")"))
    assert 0 <= score <= 1


def test_analyze_sentiment_negative():
    """
    Test the analyze_sentiment function with negative input.
    """
    result = analyze_sentiment("I hate this movie!")
    assert "NEGATIVE" in result
    score = float(result.split(":")[-1].strip(")"))
    assert 0 <= score <= 1
