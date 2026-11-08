"""Integer-grid tests for quantitative normality and crisp-preorder rounding.

Execute: python checker.py
No external dependencies. Tests corroborate but do not replace the proof.
"""
from itertools import product
from random import Random


def box(R, x, m):
    n = len(R)
    return tuple(m-max(0, max(R[i][j]-x[j] for j in range(n))) for i in range(n))


def formula_defects(R, p, q, m):
    n = len(R)
    bp = box(R,p,m)
    bq = box(R,q,m)
    bi = box(R,tuple(min(m,m-p[j]+q[j]) for j in range(n)),m)
    bbp = box(R,bp,m)
    return (max(0,*(bi[i]+bp[i]-bq[i]-m for i in range(n))),
            max(0,*(bp[i]-p[i] for i in range(n))),
            max(0,*(bp[i]-bbp[i] for i in range(n))))


def predicted(R,m):
    n=len(R)
    K=max(min(v,m-v) for row in R for v in row)
    T=max(m-R[i][i] for i in range(n))
    F=max(0,*(max(0,R[i][j]+R[j][k]-m)-R[i][k]
              for i,j,k in product(range(n),repeat=3)))
    return K,T,F


def direct(R,m):
    n=len(R)
    vals=list(product(range(m+1),repeat=n))
    K=T=F=0
    for p in vals:
        bp=box(R,p,m)
        b2=box(R,bp,m)
        T=max(T,*(max(0,bp[i]-p[i]) for i in range(n)))
        F=max(F,*(max(0,bp[i]-b2[i]) for i in range(n)))
        for q in vals:
            bq=box(R,q,m)
            bi=box(R,tuple(min(m,m-p[i]+q[i]) for i in range(n)),m)
            K=max(K,*(max(0,bi[i]+bp[i]-bq[i]-m) for i in range(n)))
    return K,T,F


def crisp_preorders(n):
    out=[]
    for bits in product((0,1),repeat=n*n):
        P=tuple(bits[i*n:(i+1)*n] for i in range(n))
        if any(P[i][i]!=1 for i in range(n)):continue
        if any(P[i][j] and P[j][k] and not P[i][k]
               for i,j,k in product(range(n),repeat=3)):continue
        out.append(P)
    return out


def distance(R,m,P):
    return max(abs(R[i][j]-m*P[i][j]) for i in range(len(R)) for j in range(len(R)))


def check():
    m=4
    for n in (1,2):
        count=0; prior=crisp_preorders(n)
        for entries in product(range(m+1),repeat=n*n):
            R=tuple(entries[i*n:(i+1)*n] for i in range(n))
            e=predicted(R,m)
            assert direct(R,m)==e,('axiom mismatch',R)
            d=min(distance(R,m,P) for P in prior)
            assert max(e)<=d,('global lower bound',R,e,d)
            if 4*max(e)<m:
                assert d==max(e)==e[0],('local metric identity',R,e,d)
            count+=1
        print('EXHAUSTIVE',n,count)
    gen=Random(1629)
    n=3; prior=crisp_preorders(n)
    assert len(prior)==29
    for j in range(60):
        R=tuple(tuple(gen.randrange(5) for _ in range(n)) for _ in range(n))
        assert direct(R,m)==predicted(R,m)
        e=predicted(R,m)
        d=min(distance(R,m,P) for P in prior)
        assert max(e)<=d
        if 4*max(e)<m:
            assert d==max(e)==e[0]
    print('TESTED_THREE_WORLD_FRAMES',60)
    # Extra perturbative random preorders with mesh 1/8 (sharper than the
    # quarter threshold) and full nearest-preorder comparison.
    m=8
    for j in range(350):
        P=prior[gen.randrange(len(prior))]
        R=tuple(tuple(m-gen.randint(0,1) if P[i][k] else gen.randint(0,1)
                      for k in range(n)) for i in range(n))
        e=predicted(R,m)
        assert max(e)<=1
        d=min(distance(R,m,Q) for Q in prior)
        assert d==e[0]==max(e)
        assert tuple(tuple(int(R[i][k]>m/2) for k in range(n)) for i in range(n))==P
    print('PERTURBED_PREORDERS',350)
    m=4
    R=((4,3,1),(0,4,3),(0,0,4))
    assert predicted(R,m)==(1,0,1)
    assert min(distance(R,m,P) for P in prior)==3
    print('SHARP_THRESHOLD', 'defect=1/4', 'nearest_crisp_preorder_distance=3/4')
    print('QUANTITATIVE_S4_ALL_CHECKS_OK')

if __name__=='__main__':
    check()
