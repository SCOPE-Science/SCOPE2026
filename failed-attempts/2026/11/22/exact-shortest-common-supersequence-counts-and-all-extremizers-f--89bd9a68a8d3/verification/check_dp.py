"""Independent recursion and global-extremum census for opposite two-run pairs."""
from functools import lru_cache
from math import comb

@lru_cache(None)
def scs_words(u, v):
    if not u:
        return frozenset((v,))
    if not v:
        return frozenset((u,))
    if u[0] == v[0]:
        return frozenset(u[0] + x for x in scs_words(u[1:], v[1:]))
    a = [u[0] + x for x in scs_words(u[1:], v)]
    b = [v[0] + x for x in scs_words(u, v[1:])]
    k = min(map(len, a + b))
    return frozenset(x for x in a + b if len(x) == k)

def formula(a, b, c, d):
    s, t = min(a, d), min(b, c)
    f0 = comb(b + d - a, b) if a <= d else comb(c + a - d, c)
    f1 = comb(a + c - b, a) if b <= c else comb(d + b - c, d)
    return (f0 if s >= t else 0) + (f1 if t >= s else 0)

def main():
    cases = 0
    for a in range(1, 7):
        for b in range(1, 7):
            for c in range(1, 7):
                for d in range(1, 7):
                    u, v = '0' * a + '1' * b, '1' * c + '0' * d
                    words = scs_words(u, v)
                    assert len(words) == formula(a, b, c, d), (a,b,c,d)
                    assert all(len(w) == len(u) + len(v) - max(min(a, d), min(b,c)) for w in words)
                    cases += 1
    for n in range(4, 55):
        scores = []
        for a in range(1, n - 2):
            for b in range(1, n-a-1):
                for c in range(1, n-a-b):
                    d = n-a-b-c
                    scores.append((formula(a,b,c,d),(a,b,c,d)))
        m = comb(n-2, (n-2)//2)
        winners = {quad for count,quad in scores if count==m}
        expected=set()
        for x in range(1,n-2):
            y=n-2-x
            if abs(x-y)<=1:
                expected.add((1,x,1,y))
                expected.add((x,1,y,1))
        assert max(c for c,_ in scores)==m
        assert winners==expected,(n,winners,expected)
    print(f'DP_AND_EXTREMUM_OK recursive_parameter_tuples={cases} checked_total_lengths=4..54')

if __name__=='__main__':
    main()
