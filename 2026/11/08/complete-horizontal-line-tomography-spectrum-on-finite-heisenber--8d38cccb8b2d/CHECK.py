#!/usr/bin/env python3
"""Direct finite incidence construction and spectral checks for horizontal lines."""
from itertools import product
import numpy as np

checks = 0

def assert_equal(a,b,reason):
    global checks
    assert a == b, (reason,a,b)
    checks += 1

def check_case(q,n):
    """Prime q, actual line incidence on H_n(F_q), without using the Fourier formula."""
    assert q in (3,5,7)
    d = 2*n
    spatial = list(product(range(q), repeat=d))
    points = [(z,t) for z in spatial for t in range(q)]
    point_idx = {p:i for i,p in enumerate(points)}
    directions = set()
    for v in spatial[1:]:
        u = next(t for t in v if t)
        s = pow(u, -1, q)
        directions.add(tuple((s*t)%q for t in v))
    assert_equal(len(directions), (q**d-1)//(q-1), 'directions')
    def omega(z,w):
        return sum(z[j]*w[j+n]-z[j+n]*w[j] for j in range(n)) % q
    all_lines = set()
    for v in directions:
        for z,t in points:
            line = frozenset(point_idx[(tuple((z[j]+s*v[j])%q for j in range(d)),(t+s*omega(z,v))%q)] for s in range(q))
            assert_equal(len(line),q,'each line has q distinct points')
            all_lines.add(line)
    D = (q**d-1)//(q-1)
    assert_equal(len(all_lines),q**d*D,'line number')
    incidence = np.zeros((len(all_lines),len(points)), dtype=np.int64)
    for i,line in enumerate(all_lines):
        for p in line: incidence[i,p]=1
    gram = incidence.T @ incidence
    assert_equal(int(np.trace(gram)),len(points)*D,'Gram trace')
    for i,(z,t) in enumerate(points):
        for j,(w,s) in enumerate(points):
            expected = D if i==j else (int((s-t)%q == omega(z,w)) if z!=w else 0)
            assert_equal(int(gram[i,j]),expected,'pair-line count')
    vals = np.linalg.eigvalsh(gram.astype(float))
    c = D-1
    levels = {(c+q**d):1, c:q**d-1,
              c+q**n:(q-1)*(q**d+q**n)//2,
              c-q**n:(q-1)*(q**d-q**n)//2}
    # All distinct except possible accidental collision, not present here.
    assert_equal(sum(levels.values()),len(points),'spectral dimension')
    theoretical = sorted(v for lam,mult in levels.items() for v in [lam]*mult)
    for expected,actual in zip(theoretical, vals):
        assert abs(expected-actual)<1e-8, (q,n,expected,actual)
        global checks
        checks += 1
    if n==1:
        eta=1
        f = np.array([np.exp(2j*np.pi*eta*t/q)*((1 if all(a==0 for a in z) else 0)-1/q) for z,t in points])
        assert np.linalg.norm(incidence @ f)<1e-9
        checks += 1
    else:
        assert min(vals) > 1e-8
        checks += 1
    print('CASE_OK',q,n,'points',len(points),'lines',len(all_lines),'spectrum',levels)

if __name__ == '__main__':
    for q,n in [(3,1),(5,1),(3,2)]:
        check_case(q,n)
    print('CHECK_OK assertions='+str(checks))
