"""Independent finite-word quasiperiod and generating-function checks.

Run with Python 3, no third-party dependencies. The mathematical theorem is
proved for every length; these finite tests are diagnostics, not that proof.
"""
from collections import Counter
from itertools import combinations


def quasiperiod_lengths(word):
    """Direct coverage by every proper prefix, independent of gap criteria."""
    n = len(word)
    result = []
    for m in range(1, n):
        q = word[:m]
        covers = [False] * n
        for start in range(n - m + 1):
            if word[start:start + m] == q:
                for i in range(start, start + m):
                    covers[i] = True
        if all(covers):
            result.append(m)
    return result


def predicates(p, d, e, c):
    one = p < min(d, e) and c < min(d, e) and max(d, e) <= p + c + 1
    two = d == e and p < d and c < d
    return one, two


def brute_counts(max_length=25):
    totals = {}
    tested = 0
    for n in range(3, max_length + 1):
        stats = Counter()
        for p1, p2, p3 in combinations(range(n), 3):
            word = ''.join('1' if i in (p1, p2, p3) else '0' for i in range(n))
            actual = quasiperiod_lengths(word)
            p = p1
            d = p2 - p1
            e = p3 - p2
            c = n - 1 - p3
            has_one, has_two = predicates(p, d, e, c)
            expected = sorted(([p+c+1] if has_one else []) +
                              ([n-d] if has_two else []))
            assert actual == expected, (n, word, expected, actual)
            stats['R1'] += int(has_one)
            stats['R2'] += int(has_two)
            stats['R12'] += int(has_one and has_two)
            stats['F' + str(len(actual))] += 1
            tested += 1
        totals[n] = stats
    return totals, tested


def convolution(a, b, cap):
    c = [0] * (cap + 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:cap-i+1]):
                if y:
                    c[i+j] += x*y
    return c


def unit_geometric(k, cap):
    return [int(n % k == 0) for n in range(cap + 1)]


def shift(a, k, cap):
    if k > cap:
        return [0] * (cap + 1)
    return [0]*k + a[:cap+1-k]


def rational_coefficients(cap):
    """Expand the three displayed rational functions by integer convolution."""
    G1, G2 = unit_geometric(1, cap), unit_geometric(2, cap)
    G3, G4 = unit_geometric(3, cap), unit_geometric(4, cap)
    G5, G6 = unit_geometric(5, cap), unit_geometric(6, cap)
    common = convolution(G1, G1, cap)
    inner1 = [a-2*b+c for a, b, c in zip(G4, shift(G5,1,cap), shift(G6,2,cap))]
    pref1 = convolution(G3, common, cap)
    pref1 = [a+b for a,b in zip(pref1,shift(pref1,3,cap))]
    R1 = shift(convolution(pref1, inner1, cap),3,cap)
    inner2 = [a-2*b+c for a,b,c in zip(shift(G2,2,cap),shift(G3,3,cap),shift(G4,4,cap))]
    R2 = shift(convolution(common,inner2,cap),1,cap)
    R12 = shift(convolution(convolution(G3,G3,cap),G4,cap),3,cap)
    return R1,R2,R12


def direct_parameter_counts(cap):
    R1=[0]*(cap+1);R2=[0]*(cap+1);R12=[0]*(cap+1)
    for a in range(cap//4+1):
        for h in range((cap-4*a-3)//3+1):
            for u in range(a+1):
                for v in range(a+1):
                    n=4*a+3*h+3+u+v
                    if n<=cap:R1[n]+=1 if h==0 else 2
    for d in range(1,(cap-1)//2+1):
        for p in range(d):
            for c in range(d):
                n=2*d+1+p+c
                if n<=cap:R2[n]+=1
    for k in range(1,cap//3+1):
        for h in range((cap-3*k)//4+1):
            R12[3*k+4*h]+=k
    return R1,R2,R12


def main():
    cap=65
    rational=rational_coefficients(cap)
    parameters=direct_parameter_counts(cap)
    assert rational==parameters, [(i,j) for i,j in enumerate(zip(rational,parameters)) if j[0]!=j[1]]
    brute,tested=brute_counts(25)
    for n,row in brute.items():
        assert (row['R1'],row['R2'],row['R12']) == tuple(g[n] for g in rational), n
        assert row['F0']+row['F1']+row['F2']==n*(n-1)*(n-2)//6
        assert row['F2']==rational[2][n]
        assert row['F1']==rational[0][n]+rational[1][n]-2*rational[2][n]
    print('VERIFY_OK', 'words', tested, 'lengths', '3..25', 'GF coefficients', '0..65')
    for n in range(3,16):
        a,b,c=(g[n] for g in rational)
        print(n, 'one_quasiperiod',a+b-2*c, 'two_quasiperiods',c)


if __name__=='__main__':
    main()
