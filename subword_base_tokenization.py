import collections

def get_char_tokens(_texts):
    tokenized_dict = {}
    
    for text in _texts:
        # lower the word
        cur_text = text[:-1].lower()
        for tk in cur_text.split():
            # split the word into characters and add </w> which represent the end of the word
            char_tks = " ".join(list(tk)) + " </w>"
            if char_tks not in tokenized_dict:
                tokenized_dict[char_tks] = 1
            else:
                tokenized_dict[char_tks] += 1
    return tokenized_dict


def get_pairs(_dict):
    pairs = collections.defaultdict(int)
    
    for word, freq in _dict.items():
        tks = word.split()
        for i in range(len(tks)-1):
            pairs[tks[i],tks[i+1]] += freq
    return pairs

def merge_dict(_best_pair, _dict):
    return_dict = {}
    target_pair = " ".join(_best_pair)
    convert_pair = "".join(_best_pair)
    for w in _dict:
        if target_pair in w:
            temp_w = w.replace(target_pair, convert_pair)
            return_dict[temp_w] = _dict[w]
        else:
            return_dict[w] = _dict[w]

    return return_dict
  
def bpe_processing(_listoftext, num_merges):
    num_merges = num_merges

    vocab_freq_dict = get_char_tokens(_listoftext)

    bpe_codes = {}
    bpe_codes_reverse = {}

    for i in range(num_merges):
        pairs = get_pairs(vocab_freq_dict)
        best_pair = max(pairs, key=pairs.get)

        vocab_freq_dict = merge_dict(best_pair, vocab_freq_dict)

        bpe_codes[best_pair] = i
        bpe_codes_reverse[best_pair[0] + best_pair[1]] = best_pair
        
    return bpe_codes
  
def encoding(_text, bpe_codes):
    input_vocab_freq = get_char_tokens([_text])
    pair_freq = get_pairs(input_vocab_freq)

    while True:
        # find the priority merged case of input text
        _pair = min(pair_freq, key = lambda pair: bpe_codes.get(pair, float('inf')))
        if _pair not in bpe_codes:
            break

        input_vocab_freq = merge_dict(_pair, input_vocab_freq)
        pair_freq = get_pairs(input_vocab_freq)

    tokenized_result = []
    for tks in input_vocab_freq.keys():
        temp_tks = tks.split()
        for tk in temp_tks:
            if tk != "</w>":
                if "</w>" in tk:
                    tk = tk.replace("</w>","")
                tokenized_result.append(tk)
                
    return tokenized_result
