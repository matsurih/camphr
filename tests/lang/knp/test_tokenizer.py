import pytest
from bedoner.lang.mecab import Japanese


TOKENIZER_TESTS = [("日本語だよ", ["日本", "語", "だ", "よ"])]
TAG_TESTS = [("日本語だよ", ["名詞/地名", "名詞/普通名詞", "判定詞/*", "助詞/終助詞"])]


@pytest.mark.parametrize("text,expected_tokens", TOKENIZER_TESTS)
def test_knp_tokenizer(knp_tokenizer, text, expected_tokens):
    tokens = [token.text for token in knp_tokenizer(text)]
    assert tokens == expected_tokens


@pytest.mark.parametrize("text,expected_tags", TAG_TESTS)
def test_knp_tokenizer_tags(knp_tokenizer, text, expected_tags):
    tags = [token.tag_ for token in knp_tokenizer(text)]
    assert tags == expected_tags