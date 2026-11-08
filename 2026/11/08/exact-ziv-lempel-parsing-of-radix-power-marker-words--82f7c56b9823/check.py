"""Independent finite tests for a closed-form Ziv--Lempel parsing."""
from __future__ import annotations


def markers(b: int, n: int) -> str:
    powers = set()
    p = 1
    while p <= n:
        powers.add(p - 1)
        p *= b
    return ''.join('1' if i in powers else '0' for i in range(n))


def predicted(b: int, max_end: int) -> list[tuple[int, int]]:
    if b == 2:
        phrases = [(0, 1), (1, 2)]
        s = 1
        while 6 * (2 ** (s-1)) <= max_end:
            x = 3 * (2 ** (s-1))
            phrases.append((x, x))
            s += 1
        return phrases
    if b == 3:
        phrases = [(0, 1), (1, 1), (2, 3)]
        s = 1
        while 3 ** (s + 1) <= max_end:
            B = 5 * 3 ** (s - 1)
            A_next = 3 ** (s + 1)
            phrases.append((B, A_next - B))
            next_B = 5 * 3 ** s
            if next_B <= max_end:
                phrases.append((A_next, next_B - A_next))
            s += 1
        return phrases
    phrases = [(0, 1), (1, 1), (2, b-2)]
    s = 1
    while b ** (s + 1) <= max_end:
        A = b ** s
        B = (2*b - 1) * b ** (s-1)
        A_next = b ** (s+1)
        phrases += [(A, B-A), (B, A_next-B)]
        s += 1
    return phrases


def first_new_length(word: str, start: int, upper: int) -> int:
    # The search range includes earlier overlapping occurrences, by definition.
    for length in range(1, upper + 1):
        fragment = word[start:start+length]
        if word.find(fragment, 0, start+length-1) < 0:
            return length
    raise AssertionError(('not-new', start, upper))


def run() -> None:
    checks = 0
    for base in range(2, 13):
        full = markers(base, 24000)
        expected = predicted(base, 12000)
        assert expected[0][0] == 0
        for (start,length), (next_start,_) in zip(expected,expected[1:]):
            assert start + length == next_start, (base,start,length,next_start)
        for start, length in expected:
            assert start + length <= 12000
            actual = first_new_length(full, start, length)
            assert actual == length, (base,start,length,actual)
            # Independent first-occurrence calculation, not using `find`.
            fragment = full[start:start+length]
            earlier = [j for j in range(start) if full[j:j+length] == fragment]
            assert not earlier, (base, start, length, earlier[:2])
            if length > 1:
                fragment = full[start:start+length-1]
                assert any(full[j:j+length-1] == fragment for j in range(start))
            checks += 1
        print(f'base={base}: {len(expected)} consecutive complete phrases tested')
    print(f'PASS {checks} exact phrase-length tests; each has an independent longest-repeat and no-repeat check')


if __name__ == '__main__':
    run()
