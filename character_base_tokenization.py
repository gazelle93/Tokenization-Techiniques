def character_tokenization(_input_text, _lower=False):
    if _lower == True:
        _input_text = _input_text.lower()
        
    return [x for x in _input_text]
