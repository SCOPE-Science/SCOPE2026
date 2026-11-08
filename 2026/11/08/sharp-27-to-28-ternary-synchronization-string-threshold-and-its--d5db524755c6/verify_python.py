"""Exact normalized-squarefree census of ternary synchronization thresholds.

Run: python3 verify_python.py
All arithmetic is integral; fractions are reduced only for output.
"""
from fractions import Fraction
from itertools import permutations

BOUND = 28

def lcs_bitparallel(a, b):
    # Bit-vector LCS recurrence. Bit i represents position i of a.
    masks = [0, 0, 0]
    for i, ch in enumerate(a):
        masks[int(ch)] |= 1 << i
    state = 0
    for ch in b:
        x = masks[int(ch)] | state
        y = 2 * state + 1
        state = x & ~(x - y)
    return state.bit_count()


def cost(word, limit=Fraction(1, 1)):
    highest = Fraction(0)
    for i in range(len(word) - 2):
        for j in range(i + 1, len(word) - 1):
            a = word[i:j]
            for k in range(j + 1, len(word) + 1):
                v = Fraction(2 * lcs_bitparallel(a, word[j:k]), k - i)
                if v > highest:
                    highest = v
                    if highest > limit:
                        return highest
    return highest


def squarefree_extension(word):
    n = len(word)
    return all(word[n - d:] != word[n - 2*d:n - d]
               for d in range(1, n//2 + 1))


def compute():
    layer = ['0']
    table = [(1, 1, '0/1', 1)]
    extremizers = {}
    for n in range(2, BOUND + 1):
        new = []
        for word in layer:
            next_new = str(len(set(word)))
            for c in '012':
                if c not in word and c != next_new:
                    continue
                child = word + c
                if squarefree_extension(child):
                    new.append(child)
        assert len(new) == len(set(new))
        layer = new
        best = Fraction(2)
        optimal = []
        for word in layer:
            value = cost(word, best)
            if value < best:
                best = value
                optimal = [word]
            elif value == best:
                optimal.append(word)
        table.append((n, len(layer), f'{best.numerator}/{best.denominator}', len(optimal)))
        if n in (27, 28):
            extremizers[n] = optimal
    assert table[26] == (27, 2581, '20/23', 1)
    assert table[27] == (28, 3370, '8/9', 13)
    assert extremizers[27] == ['012010212021012102010212012']
    return table, extremizers


def main():
    table, ex = compute()
    for n, num, ratio, cnt in table:
        print(f'{n},{num},{ratio},{cnt}')
    for n in (27, 28):
        for word in ex[n]:
            print(f'EXTREMIZER,{n},{word}')
    print('SYNC_TERNARY_PY_VERIFY_OK')

if __name__ == '__main__':
    main()
