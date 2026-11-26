"""Directly replay every shortest-word witness on all states of the stated DFA."""
import csv
from pathlib import Path

DIRECTORY = Path(__file__).resolve().parent

def run(n, word):
    states = set(range(n))
    for letter in word:
        if letter == 'a':
            states = {(s + 1) % n for s in states}
        elif letter == 'b':
            states = {0 if s == n - 1 else s for s in states}
        else:
            raise AssertionError('invalid letter')
    return states

def verify():
    with (DIRECTORY / 'exact_profile.csv').open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    assert [int(r['n']) for r in rows] == list(range(3, 25))
    for row in rows:
        n = int(row['n'])
        w = row['optimal_word']
        L = int(row['optimal_length'])
        assert w[0] == 'b' and w.endswith('b')
        assert 'aaa' not in w
        assert len(w) == L == (n - 1) * (n - 2) + ((n - 1)**2 + 1)//2
        assert w.count('a') == int(row['a_count'])
        assert w.count('b') == int(row['b_count'])
        assert len(run(n, w)) == 1
        assert int(row['product_graph_distance']) == L
        assert int(row['weighted_graph_distance']) == L
    # Independently replay the constructive all-order witness, not the exact formula.
    for n in range(3, 101):
        w = 'b' + ('aab' + 'ab' * (n - 2)) * (n - 2)
        assert 'aaa' not in w
        assert len(run(n, w)) == 1
    print('VERIFIED exact_profile n=3..24 and constructive witnesses n=3..100')

if __name__ == '__main__':
    verify()
