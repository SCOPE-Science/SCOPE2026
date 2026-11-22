"""Exact finite-ring null-ray spectral verification (standard-library only)."""
from collections import Counter
from itertools import product

def projective_line(p):
    q = p*p
    return [(1,t) for t in range(q)] + [(p*s,1) for s in range(p)]

def directions(p):
    q = p*p
    return list({((a*c)%q,(a*d)%q,(b*c)%q,(b*d)%q)
                 for a,b in projective_line(p) for c,d in projective_line(p)})

def rank_modp(a,b,c,d,p):
    a,b,c,d = (x%p for x in (a,b,c,d))
    if (a*d-b*c)%p: return 2
    return int(any([a,b,c,d]))

def spectral_class(X,p):
    q=p*p
    if not any(X): return 'zero'
    if all(v%p==0 for v in X):
        z=tuple((v//p)%p for v in X)
        return 'p_rank%d'%rank_modp(*z,p)
    r=rank_modp(*X,p)
    if r==2:return 'unit_rank2'
    det=(X[0]*X[3]-X[1]*X[2])%q
    return 'unit_rank1_det0' if det==0 else 'unit_rank1_detp'

def expected(p):
    q=p*p
    return {'zero':q*(p+1)**2,
            'p_rank2':q*(p+1), 'p_rank1':q*(2*p+1),
            'unit_rank2':p*(p+1),
            'unit_rank1_detp':2*q,'unit_rank1_det0':3*q}

def expected_mult(p):
    n1=(p-1)*(p+1)**2
    n2=(p*p-1)*(p*p-p)
    return {'zero':1,'p_rank1':n1,'p_rank2':n2,
            'unit_rank2':n2*p**4,
            'unit_rank1_detp':n1*(p**4-p**3),
            'unit_rank1_det0':n1*p**3}

def inspect(p, full=False):
    q=p*p
    D=directions(p)
    assert len(D)==p*p*(p+1)**2
    expect=expected(p)
    seen=Counter()
    if full:
        Xs=product(range(q),repeat=4)
    else:
        # explicit representatives for the six Smith strata
        Xs=[(0,0,0,0),(p,0,0,0),(p,0,0,p),(1,0,0,0),(1,0,0,p),(1,0,0,1)]
    for X in Xs:
        cl=spectral_class(X,p)
        n=sum((X[0]*Y[0]+X[1]*Y[1]+X[2]*Y[2]+X[3]*Y[3])%q==0 for Y in D)
        assert n==expect[cl], (p,X,cl,n,expect[cl])
        seen[cl]+=1
    assert set(seen)==set(expect)
    if full:
        assert seen==Counter(expected_mult(p)),(p,seen,expected_mult(p))
        orbit={tuple((u*z)%q for z in Y) for Y in D for u in range(q) if u%p}
        primitive_null={X for X in product(range(q),repeat=4)
                        if any(z%p for z in X) and (X[0]*X[3]-X[1]*X[2])%q==0}
        assert orbit==primitive_null
        assert len(orbit)==len(D)*(p*p-p)
    print(f'p={p}, full={full}, direction_count={len(D)}, strata={dict(sorted(seen.items()))}, multipliers={dict(sorted(expect.items()))}')

if __name__=='__main__':
    for p in (2,3):inspect(p,full=True)
    for p in (5,7,11):inspect(p,full=False)
    print('RING_NULL_RAY_EXACT_SPECTRUM_CHECKS_PASS')
