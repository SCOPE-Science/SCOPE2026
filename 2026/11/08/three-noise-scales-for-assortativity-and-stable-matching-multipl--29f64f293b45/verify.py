"""Exact finite verification of three-by-three Mallows stable-matching laws.

Run with Python 3 (standard library only): python verify.py
All loops enumerate finite sets exhaustively; integer arithmetic is exact.
"""
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'coefficients.json').read_text(encoding='utf-8'))
P = tuple(itertools.permutations(range(3)))
INV = tuple(sum(p[a] > p[b] for a in range(3) for b in range(a+1,3)) for p in P)
RANK = tuple(tuple(p.index(j) for j in range(3)) for p in P)
PAIRS = P


def stable(male, female, matching):
    """Directly test all six nonassigned pairs for a bilateral block."""
    mate_of_woman = [matching.index(j) for j in range(3)]
    for man in range(3):
        for woman in range(3):
            if woman == matching[man]:
                continue
            if (male[man][woman] < male[man][matching[man]]
                    and female[woman][man] < female[woman][mate_of_woman[woman]]):
                return False
    return True


def convolution(a, b):
    out = [0]*(len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] += ai*bj
    return out


def derivative(a):
    return [i*a[i] for i in range(1, len(a))]


def palin(half):
    d = len(half)-1
    out = [0]*(2*d+1)
    for i,v in enumerate(half):
        out[i] = v
        out[2*d-i] = v
    return out


def same_poly(a,b):
    while len(a)>1 and a[-1]==0:
        a.pop()
    while len(b)>1 and b[-1]==0:
        b.pop()
    return a==b


def sub(a,b):
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))]


def scalar(a,c):
    return [x*c for x in a]


def power(a,n):
    z=[1]
    for _ in range(n): z=convolution(z,a)
    return z


def verify():
    hist = {1:[0]*19,2:[0]*19,3:[0]*19}
    diagonal = [0]*19
    for choice in itertools.product(range(6), repeat=6):
        male = [RANK[choice[i]] for i in range(3)]
        female = [RANK[choice[i+3]] for i in range(3)]
        viable = [m for m in PAIRS if stable(male,female,m)]
        assert 1 <= len(viable) <= 3
        s = sum(INV[c] for c in choice)
        hist[len(viable)][s] += 1
        diagonal[s] += (P[0] in viable)
    expected=DATA['stable_count_histogram_by_total_inversions']
    for k in (1,2,3):
        assert hist[k]==expected[str(k)], (k,hist[k])
    assert diagonal==DATA['identity_stable_by_total_inversions']
    assert sum(sum(h) for h in hist.values()) == DATA['profile_count'] == 6**6
    Z=[1,2,2,1]
    D=convolution(power([1,1],4), power([1,1,1],6))
    poly=DATA['palindromic_polynomials']
    R=palin(poly['R12']); S=palin(poly['S6']); B=palin(poly['B18'])
    U=palin(poly['U14']); V=palin(poly['V8']); H=palin(poly['H18'])
    Nmulti=[hist[2][i]+hist[3][i] for i in range(19)]
    assert same_poly(convolution(Nmulti,D), convolution([0,0]+scalar(R,2), power(Z,6)))
    assert same_poly(convolution(hist[3],D),convolution([0]*5+S,power(Z,6)))
    assert same_poly(diagonal,B)
    # Rational derivative identity: f=A/D implies f'=(A'D-AD')/D^2.
    # Multiply to avoid divisions; check the factorizations in the proof.
    for A,C in (([0,0]+scalar(R,2),[0]+scalar(U,2)),
                ([0]*5+S,[0]*4+scalar(V,2))):
        left = sub(convolution(derivative(A),D),convolution(A,derivative(D)))
        right = convolution(convolution(C,[1,-1]),power([1,1],3))
        right = convolution(right,power([1,1,1],5))
        assert same_poly(left,right)
    left=sub(convolution(derivative(B),Z),scalar(convolution(B,derivative(Z)),6))
    assert same_poly(left,convolution(scalar(H,-2),[1,-1]))
    assert all(c>0 for c in U+V+H)
    assert all(c>=0 for c in R+S+B)
    assert Nmulti[0:2]==[0,0] and Nmulti[2]==4
    assert hist[3][:5]==[0]*5 and hist[3][5]==6
    assert power(Z,6)[1]-diagonal[1]==4
    assert [sum(hist[k]) for k in (1,2,3)]==[34080,11484,1092]
    assert sum(diagonal)==10054
    def stable_list(rank_orders):
        male = [tuple(p.index(j) for j in range(3)) for p in rank_orders[:3]]
        female = [tuple(p.index(j) for j in range(3)) for p in rank_orders[3:]]
        return [m for m in PAIRS if stable(male, female, m)]
    def from_digits(groups):
        return [tuple(int(ch)-1 for ch in word) for group in groups for word in group]
    assert stable_list(from_digits((('123','123','123'),('213','123','123')))) == [(1,0,2)]
    assert stable_list(from_digits((('213','123','123'),('123','213','123')))) == [(0,1,2),(1,0,2)]
    assert stable_list(from_digits((('123','213','132'),('213','312','123')))) == [(0,1,2),(1,0,2),(2,0,1)]
    print('PASS: 46,656 profiles, 6 matchings, all inversion histograms,')
    print('three exact probability rational functions, derivative certificates,')
    print('and sharp inversion costs 1/2/5 (with multiplicities 4/4/6).')


if __name__=='__main__':
    verify()
