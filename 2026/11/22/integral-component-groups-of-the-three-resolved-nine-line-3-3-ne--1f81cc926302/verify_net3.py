"""Exact integral check for the three nine-line (3,3)-net boundaries.

Requires Python 3 and SymPy. No external data or network access is used.
"""
from collections import Counter, defaultdict
from itertools import combinations
from fractions import Fraction as Q
from sympy import Matrix, Rational, Symbol, factor, factorint
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

EXPECTED = {
    0: {
        'triple': 9, 'double': 9, 'vertices': 18, 'genus': 19,
        'invariants': [5, 15, 15, 45, 45, 135],
        'order': 307546875,
        'charpoly': 'z*(z - 6)*(z - 3)**4*(z**2 - 9*z + 15)**6',
        'valuations': {3: Counter({0:12, 1:2, 2:2, 3:1}),
                       5: Counter({0:11, 1:6})},
    },
    1: {
        'triple': 10, 'double': 6, 'vertices': 19, 'genus': 18,
        'invariants': [3, 45, 45, 135, 405],
        'order': 332150625,
        'charpoly': 'z*(z - 3)**3*(z**2 - 9*z + 15)**4*(z**2 - 7*z + 9)**2*(z**3 - 13*z**2 + 51*z - 57)',
        'valuations': {3: Counter({0:13, 1:1, 2:2, 3:1, 4:1}),
                       5: Counter({0:14, 1:4})},
    },
    3: {
        'triple': 12, 'double': 0, 'vertices': 21, 'genus': 16,
        'invariants': [3, 9, 9, 9, 9, 27, 27, 27],
        'order': 387420489,
        'charpoly': 'z*(z - 7)*(z - 3)**3*(z**2 - 7*z + 9)**8',
        'valuations': {3: Counter({0:12, 1:1, 2:4, 3:3}),
                       5: Counter({0:20})},
    }
}

def graph(t):
    """The nine mixed triples, and t coincident within-class triples.

    The Latin square is the addition table of Z/3; its 9 mixed nodes
    meet one line of each of the three classes. A concurrent class
    replaces its three within-class double edges by an exceptional star.
    """
    if t not in (0, 1, 3):
        raise ValueError('Only the three realizable cases are used')
    n = 18 + t
    edges = []
    for a in range(3):
        for b in range(3):
            v = 9 + 3*a + b
            edges += [(a, v), (3+b, v), (6+(a+b) % 3, v)]
    for c in range(3):
        if c < t:
            v = 18 + c
            edges.extend((3*c+i, v) for i in range(3))
        else:
            edges.extend((3*c+i, 3*c+j) for i, j in combinations(range(3), 2))
    L = Matrix.zeros(n)
    for u, v in edges:
        assert u != v
        L[u,u] += 1
        L[v,v] += 1
        L[u,v] -= 1
        L[v,u] -= 1
    return L, edges

def val_p(a, p, bound):
    if a == 0:
        return bound
    e = 0
    while a % p == 0:
        a //= p
        e += 1
    return min(e, bound)

def local_elementary_exponents(A, p, bound=9):
    """Independent elimination over Z/(p^bound), using unit pivots.

    Every pivot is chosen to have minimal p-adic valuation in the remaining
    block. Row and column swaps and unit-modulus additions are invertible,
    hence the list is the prime-local Smith valuation multiset.
    """
    n = A.rows
    assert A.rows == A.cols
    modulus = p**bound
    X = [[int(A[i,j]) % modulus for j in range(n)] for i in range(n)]
    output = []
    for i in range(n):
        e, r, c = min((val_p(X[r][c],p,bound), r, c)
                      for r in range(i,n) for c in range(i,n))
        assert e < bound, ('precision exhausted', p, i)
        X[i], X[r] = X[r], X[i]
        for row in X:
            row[i], row[c] = row[c], row[i]
        pv = p**e
        unit_inverse = pow(X[i][i] // pv, -1, p**(bound-e))
        for r in range(i+1, n):
            assert X[r][i] % pv == 0
            mul = ((X[r][i] // pv)*unit_inverse) % (p**(bound-e))
            for c in range(i, n):
                X[r][c] = (X[r][c]-mul*X[i][c]) % modulus
            assert X[r][i] == 0
        for c in range(i+1, n):
            assert X[i][c] % pv == 0
            mul = ((X[i][c] // pv)*unit_inverse) % (p**(bound-e))
            for r in range(i, n):
                X[r][c] = (X[r][c]-mul*X[r][i]) % modulus
            assert X[i][c] == 0
        output.append(e)
    assert output == sorted(output)
    return Counter(output)

def normalized_point(P):
    for p in P:
        if p:
            return tuple(x/p for x in P)
    raise AssertionError('Coincident lines')

def coordinate_check(b,c, triple_expected, double_expected):
    """Published two-parameter (3,3)-net equation specialized over Q."""
    lines = [
        (0,1,0), (Rational(1,c),1,1), (Rational(b,b-1),0,1),
        (1,0,0), (1,c,1), (0,b,1),
        (1,c*(1-b),0), (1,1,1), (0,0,1),
    ]
    loci = defaultdict(set)
    for i,j in combinations(range(9),2):
        pt = normalized_point(Matrix(lines[i]).cross(Matrix(lines[j])))
        loci[pt].update((i,j))
    mult = Counter(len(s) for s in loci.values())
    assert mult == Counter({2:double_expected,3:triple_expected}), mult
    assert sum(len(s)*(len(s)-1)//2 for s in loci.values()) == 36
    return mult


def ceva_coordinate_check():
    """All 36 line intersections over Q(omega), omega^2+omega+1=0."""
    zero, one, w, w2 = (Q(0),Q(0)), (Q(1),Q(0)), (Q(0),Q(1)), (Q(-1),Q(-1))
    def add(a,b): return (a[0]+b[0],a[1]+b[1])
    def neg(a): return (-a[0],-a[1])
    def sub(a,b): return add(a,neg(b))
    def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
    def inverse(a):
        x,y=a
        n=x*x-x*y+y*y
        assert n != 0
        return ((x-y)/n, -y/n)
    def cross(u,v):
        return tuple(sub(mul(u[(i+1)%3],v[(i+2)%3]),
                         mul(u[(i+2)%3],v[(i+1)%3])) for i in range(3))
    def projective_normalize(pt):
        for a in pt:
            if a != zero:
                inv = inverse(a)
                return tuple(mul(x,inv) for x in pt)
        raise AssertionError('Coincident lines')
    L=[]
    for a in (one,w,w2): L.append((one,neg(a),zero))
    for a in (one,w,w2): L.append((zero,one,neg(a)))
    for a in (one,w,w2): L.append((neg(a),zero,one))
    loci=defaultdict(set)
    for i,j in combinations(range(9),2):
        pt=projective_normalize(cross(L[i],L[j]))
        loci[pt].update((i,j))
    assert Counter(map(len,loci.values())) == Counter({3:12})
    assert sum(len(s)*(len(s)-1)//2 for s in loci.values()) == 36
    return True

def main():
    assert coordinate_check(2,3,9,9) == Counter({2:9,3:9})
    assert coordinate_check(2,2,10,6) == Counter({2:6,3:10})
    assert ceva_coordinate_check()
    z = Symbol('z')
    for t, exp in EXPECTED.items():
        L, edges = graph(t)
        assert L.rows == exp['vertices']
        assert len(edges) == 36
        assert sum(L[i,j] for i in range(L.rows) for j in range(L.cols)) == 0
        assert 36-L.rows+1 == exp['genus']
        assert min(sum(1 for u,v in edges if i in (u,v)) for i in range(L.rows)) >= 3
        assert factor(L.charpoly(z).as_expr() - __import__('sympy').sympify(exp['charpoly'])) == 0
        for root in (0, L.rows-1):
            R = L.copy()
            R.row_del(root)
            R.col_del(root)
            assert R.det() == exp['order']
            S = smith_normal_form(R, domain=ZZ)
            d = [abs(int(S[i,i])) for i in range(S.rows)]
            assert d == sorted(d)
            assert [v for v in d if v>1] == exp['invariants']
            assert factorint(R.det()) == ( {3:9,5:6} if t==0 else {3:12,5:4} if t==1 else {3:18} )
            for p in (3,5):
                local = local_elementary_exponents(R,p)
                assert local == exp['valuations'][p]
                assert local == Counter(val_p(v,p,9) for v in d)
        print(f'case={t} vertices={L.rows} nodes={len(edges)} genus={exp["genus"]} tau={exp["order"]} invariants={exp["invariants"]}')
    print('THREE_NINE_LINE_NET_INTEGRAL_BOUNDARIES_OK')

if __name__ == '__main__':
    main()
