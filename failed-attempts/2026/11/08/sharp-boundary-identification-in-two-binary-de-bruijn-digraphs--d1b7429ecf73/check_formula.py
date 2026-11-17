"""Independent, exhaustive in-ball-signature verification of two explicit codebooks.
Usage: python3 check_formula.py
Requires only the Python standard library and witnesses.tsv.
"""
from pathlib import Path


def read_witnesses():
    lines = Path(__file__).with_name('witnesses.tsv').read_text(encoding='utf-8').strip().splitlines()
    records = []
    for line in lines:
        n_text, t_text, hex_text = line.split()
        n, t, f = int(n_text), int(t_text), int(hex_text, 16)
        assert (n, t) in ((7, 4), (9, 5))
        assert f.bit_length() <= 1 << (n - 1)
        records.append((n, t, f))
    assert len(records) == 2 and {r[:2] for r in records} == {(7, 4), (9, 5)}
    return records


def incoming_ball(v, n, t):
    result = {v}
    for steps in range(1, t + 1):
        for prefix in range(1 << steps):
            result.add((prefix << (n - steps)) | (v >> steps))
    return result


def test(n, t, f):
    N = 1 << n
    S = {2 * p + ((f >> p) & 1) for p in range(N // 2)}
    assert len(S) == N // 2
    assert all(len(S & {2 * p, 2 * p + 1}) == 1 for p in range(N // 2))
    signatures = [frozenset(incoming_ball(v, n, t) & S) for v in range(N)]
    assert all(signatures), 'coverage failure'
    assert len(set(signatures)) == N, 'indistinguishable vertices'
    print(f'FORMULA_OK n={n} t={t} N={N} code_size={len(S)} unique_signatures={N}')


if __name__ == '__main__':
    for record in read_witnesses():
        test(*record)
