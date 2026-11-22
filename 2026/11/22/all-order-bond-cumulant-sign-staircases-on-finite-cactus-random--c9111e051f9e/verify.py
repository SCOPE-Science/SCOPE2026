"""Exact-rational, independent enumeration for the cycle-block cumulant theorem.

Run: python3 verify.py
No third-party dependencies. Tests arbitrary rational q>0, positive heterogeneous
edge activities, each distinct-edge joint cumulant, and polynomial sign laws.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial


def eulerian_sign_coeff(k):
    """Coefficients of Q_k(b) for D^k log(1+b)=b Q_k(b)/(1+b)^k."""
    assert k >= 2
    coeff = [1]
    for cur in range(2, k):
        new = [F(0)] * (len(coeff) + 1)
        # Q_(cur+1)=(1-(cur-1)b) Q_cur + b(1+b) Q'_cur
        for i, a in enumerate(coeff):
            new[i] += a
            new[i+1] -= (cur-1)*a
            if i:
                new[i] += i*a
                new[i+1] += i*a
        coeff = new
    return coeff


def evaluate(coeff, x):
    v = F(0)
    for a in reversed(coeff):
        v = v*x+a
    return v


def set_partitions(seq):
    if not seq:
        yield []
        return
    x = seq[0]
    for part in set_partitions(seq[1:]):
        yield [(x,)] + part
        for j in range(len(part)):
            yield part[:j] + [part[j] + (x,)] + part[j+1:]


def component_count(n, edge_list, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for i, (u,v) in enumerate(edge_list):
        if mask >> i & 1:
            a, b = find(u), find(v)
            if a != b:
                parent[a] = b
    return len({find(i) for i in range(n)})


def enumeration(n, edges, q, vs):
    m = len(edges)
    weights = []
    for mask in range(1 << m):
        w = q ** component_count(n, edges, mask)
        for j, v in enumerate(vs):
            if mask >> j & 1:
                w *= v
        weights.append(w)
    z = sum(weights)
    moments = {}
    for mask in range(1 << m):
        moments[mask] = sum(w for a,w in enumerate(weights) if a & mask == mask)/z
    return moments


def cumulant(es, moments):
    es = tuple(es)
    value = F(0)
    for pi in set_partitions(es):
        term = F((-1) ** (len(pi)-1) * factorial(len(pi)-1))
        for block in pi:
            bitmask = sum(1 << e for e in block)
            term *= moments[bitmask]
        value += term
    return value


def expected(es, cycles, q, vs):
    for cycle in cycles:
        if set(es).issubset(cycle):
            p = [v / (q+v) for v in vs]
            P = F(1)
            for j in cycle:
                P *= p[j]
            b = (q-1)*P
            factor = F(1)
            for e in es:
                factor *= (1-p[e])
            k = len(es)
            return factor*b*evaluate(eulerian_sign_coeff(k),b)/(1+b)**k
    return F(0)


def test():
    graphs = [
        (4,[(0,1),(1,2),(2,3),(3,0)],[[0,1,2,3]]),
        (5,[(0,1),(1,2),(2,3),(3,4),(4,0)],[[0,1,2,3,4]]),
        (7,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,3)],[[0,1,2],[4,5,6,7]]),
        (6,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)],[[0,1,2],[4,5,6]]),
    ]
    checked = 0
    qvals = [F(1,2),F(1),F(3,2),F(2),F(6),F(12)]
    for n,edges,cycles in graphs:
        m = len(edges)
        vs = [F((j*3)%11+1,j%3+1) for j in range(m)]
        for q in qvals:
            moments = enumeration(n,edges,q,vs)
            for k in range(2,min(5,m)+1):
                for es in combinations(range(m),k):
                    got = cumulant(es,moments)
                    want = expected(es,cycles,q,vs)
                    assert got == want,(n,q,es,got,want)
                    checked += 1
    assert [eulerian_sign_coeff(k) for k in (2,3,4,5)] == [
        [1],[1,-1],[1,-4,1],[1,-11,11,-1]
    ]
    # Exact sign tests: k=4, q=6, uniform p=1/2, 3/4, 9/10.
    # b=5p^4 crosses both positive zeros 2 +/- sqrt(3).
    vcase=[]
    for p in (F(1,10),F(3,4),F(99,100)):
        b=5*p**4
        val=b*evaluate(eulerian_sign_coeff(4),b)/(1+b)**4
        vcase.append(1 if val>0 else -1 if val<0 else 0)
    assert vcase == [1,-1,1],vcase
    # k=5, q=12, all three sign reversals are reachable as b rises to 11.
    k5=[]
    for b in (F(1,100),F(1,2),F(2),F(21,2)):
        val=b*evaluate(eulerian_sign_coeff(5),b)/(1+b)**5
        k5.append(1 if val>0 else -1 if val<0 else 0)
    assert k5 == [1,-1,1,-1],k5
    print('CYCLE_BLOCK_CUMULANTS_EXACT_OK',checked,'polynomial_orders_2_to_5','cycle4_signs',vcase,'cycle5_signs',k5)

if __name__=='__main__':
    test()
