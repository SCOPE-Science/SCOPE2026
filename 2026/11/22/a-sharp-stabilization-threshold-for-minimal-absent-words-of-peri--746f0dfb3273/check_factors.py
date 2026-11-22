"""Independent direct finite test of periodic-prefix antidictionary formula.
No external packages; execute: python check_factors.py
This verifies finite instances, not the all-length theorem.
"""
from itertools import product


def factors(s):
    return [{''}] + [set(s[i:i+k] for i in range(len(s)-k+1))
                     for k in range(1, len(s)+2)]


def minimal_absent(s, alphabet):
    fs = factors(s)
    found = set()
    for k in range(1, len(s)+2):
        for v in fs[k-1]:
            for a in alphabet:
                w = v+a
                if w not in fs[k] and (k == 1 or w[1:] in fs[k-1]):
                    found.add(w)
    return found


def primitive_root(s):
    return next(s[:d] for d in range(1, len(s)+1)
                if len(s) % d == 0 and s[:d]*(len(s)//d) == s)


def circular_maw(root, alphabet):
    p = len(root)
    # All possible periodic factors of length at most p occur among these windows.
    r2 = root + root
    return {x for x in minimal_absent(r2, alphabet) if len(x) <= p}


def main():
    samples = 0
    for q, maximum in [(2, 8), (3, 5), (4, 4)]:
        alphabet = ''.join(str(i) for i in range(q))
        for p in range(1, maximum+1):
            for symbols in product(alphabet, repeat=p):
                w = ''.join(symbols)
                r = primitive_root(w)
                if w != r:
                    continue
                permanent = circular_maw(r, alphabet)
                # Test every allowed linear length, including incomplete final periods.
                d = len(r)
                periodic = r * ((3*d+4)//d+2)
                for n in range(max(1,2*d-2),3*d+3):
                    special = periodic[d-1:n+1]
                    predicted = permanent | {special}
                    actual = minimal_absent(periodic[:n], alphabet)
                    assert predicted == actual, (q, p, n, w, predicted^actual)
                    assert len(permanent) + 1 == len(actual)
                    samples += 1
    print('PASS direct finite factor-set checks:', samples, 'cases')


if __name__ == '__main__':
    main()
