from app import analyze_sentiment

def test_analyze_sentiment_positive():
    result = analyze_sentiment("I love this movie!")
    assert "POSITIVE" in result
    score = float(result.split(":")[-1].strip(")"))
    assert 0 <= score <= 1

def test_analyze_sentiment_negative():
    result = analyze_sentiment("I hate this movie!")
    assert "NEGATIVE" in result
    score = float(result.split(":")[-1].strip(")"))
    assert 0 <= score <= 1