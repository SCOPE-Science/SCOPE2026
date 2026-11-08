#!/usr/bin/env python3
"""Self-contained exhaustive finite-factor certificate for a binary fixed point."""

MORPH = {"0": "010011", "1": "1001"}
EXPECTED = {
    1: ("0", "1"),
    2: ("00", "11"),
    3: ("010", "101", "111"),
    4: ("0110", "1001"),
    5: ("01010", "01110"),
    6: ("001100", "110011"),
    7: ("0010100", "0011100"),
    8: ("01100110", "10011001"),
    9: ("100101001", "100111001"),
    10: ("0011001100", "1100110011"),
    11: ("01001110010", "11001010011"),
    12: ("100110011001",),
    13: ("0110010100110", "1010011100101", "1110010100111"),
    15: ("010100111001010", "011100101001110"),
    17: ("00101001110010100", "00111001010011100"),
    19: ("1001010011100101001", "1001110010100111001"),
    21: ("010011100101001110010", "110010100111001010011"),
    23: ("01100101001110010100110", "10100111001010011100101"),
}
MAXIMAL_EXPECTED = {
    "010", "1100110011", "100110011001", "0110010100110",
    "01100101001110010100110", "10100111001010011100101",
}


def image(word):
    return "".join(MORPH[ch] for ch in word)


def all_palindromes(blocks, max_length=25):
    result = {}
    window_count = 0
    for n in range(1, max_length + 1):
        words = set()
        for block in blocks:
            for j in range(len(block) - n + 1):
                w = block[j:j+n]
                window_count += 1
                if w == w[::-1]:
                    words.add(w)
        result[n] = words
    return result, window_count


def main():
    assert set(MORPH["0"][i:i+2] for i in range(len(MORPH["0"])-1)) == {
        "00", "01", "10", "11"
    }
    imgs = {a: a for a in "01"}
    for _ in range(3):
        imgs = {a: image(imgs[a]) for a in "01"}
    assert (len(imgs["0"]), len(imgs["1"])) == (150, 100)
    blocks = {a+b: imgs[a]+imgs[b] for a in "01" for b in "01"}
    assert {k: len(v) for k,v in blocks.items()} == {
        "00": 300, "01": 250, "10": 250, "11": 200
    }
    exhaustive, windows = all_palindromes(blocks.values())
    assert {n: tuple(sorted(v)) for n, v in exhaustive.items() if v} == EXPECTED
    assert exhaustive[24] == exhaustive[25] == set()
    all_words = set().union(*exhaustive.values())
    assert len(all_words) == 37
    maximal = {w for w in all_words if not any(a+w+a in all_words for a in "01")}
    assert maximal == MAXIMAL_EXPECTED
    # Independent prefix construction, not the source of the exhaustive proof.
    prefix = "0"
    for _ in range(6):
        prefix = image(prefix)
    assert len(prefix) == 18750
    sampled, crosscheck_windows = all_palindromes([prefix])
    assert sampled == exhaustive
    # Independent check of two cutoff lengths in each of the four source pairs.
    for block in blocks.values():
        for n in (24, 25):
            assert all(block[i:i+n] != block[i:i+n][::-1]
                       for i in range(len(block)-n+1))
    assert max(map(len, all_words)) == 23
    print("VERIFY_OK pairs=4 n=1..25 palindromes=37 center_maximal=6"
          f" exhaustive_windows={windows} prefix_windows={crosscheck_windows}")


if __name__ == "__main__":
    main()
