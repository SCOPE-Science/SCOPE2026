"""Independent finite-state and rational checks for two-hop reachability correlations.
Run: python check.py
"""
from fractions import Fraction as F
from itertools import combinations, product


def no_short_path(a, source, target):
    n=len(a)
    return not a[source][target] and all(not (a[source][w] and a[w][target]) for w in range(n) if w!=source and w!=target)


def exact_probability(n, p, pair1, pair2=None):
    edges=list(combinations(range(n),2)); m=len(edges)
    out=F(0)
    for states in product((0,1,2),repeat=m):
        mat=[[False]*n for _ in range(n)]; present=0
        for (u,v),st in zip(edges,states):
            if st!=0:
                present+=1
                if st==1:mat[u][v]=True
                else:mat[v][u]=True
        if no_short_path(mat,*pair1) and (pair2 is None or no_short_path(mat,*pair2)):
            out+=(p/2)**present*(1-p)**(m-present)
    return out


def predicted(n,p,kind):
    q=1-p*p/4
    r=1-p*p/2
    one=(1-p/2)*q**(n-2)
    if kind=='reverse': return (1-p)*r**(n-2)
    if kind=='chain':return (3*p**3-2*p*p-8*p+8)/8*r**(n-3)
    if kind in ('fork','head'):return (1-p/2)**2*(1-p*p/2+p**3/8)**(n-3)
    if kind=='disjoint':return (p-2)**2*(p**4+2*p**3-8*p*p+8)/32*q**(2*(n-4))
    if kind=='identical':return one
    raise ValueError(kind)


def signcheck(kind, p, n, joint):
    m=(1-p/2)*(1-p*p/4)**(n-2)
    cov=joint-m*m
    sign={'chain':-1,'reverse':-1,'fork':1,'head':1,'disjoint':1,'identical':1}[kind]
    if p>0: assert cov*sign>0,(kind,n,p,cov)
    else:assert cov==0
    return cov


def main():
    checks=0
    pairs={'reverse':((0,1),(1,0)),'chain':((0,1),(1,2)),
           'fork':((0,1),(0,2)),'head':((0,1),(2,1)),
           'disjoint':((0,1),(2,3)), 'identical':((0,1),(0,1))}
    for n in range(2,6):
        for p in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            for kind,(ab,cd) in pairs.items():
                if max(*ab,*cd)>=n:continue
                one=exact_probability(n,p,ab)
                assert one==(1-p/2)*(1-p*p/4)**(n-2),(n,p,ab,one)
                checks+=1
                joint=exact_probability(n,p,ab,cd)
                assert joint==predicted(n,p,kind),(n,p,kind,joint,predicted(n,p,kind))
                checks+=1
                signcheck(kind,p,n,joint)
                checks+=1
    # Independently count allowed orientations with each number of present edges
    def counts(k, pair1, pair2):
        e=list(combinations(range(k),2)); z=[0]*(len(e)+1)
        for states in product((0,1,2),repeat=len(e)):
            a=[[False]*k for _ in range(k)];m=0
            for (u,v),s in zip(e,states):
                if s:
                    m+=1
                    if s==1:a[u][v]=True
                    else:a[v][u]=True
            if no_short_path(a,*pair1) and no_short_path(a,*pair2):z[m]+=1
        return z
    assert counts(3,(0,1),(1,2))==[1,4,3,1];checks+=1
    assert counts(3,(0,1),(0,2))==[1,4,5,2];checks+=1
    assert counts(4,(0,1),(2,3))==[1,10,37,66,62,30,6];checks+=1
    # Critical factor algebra checked at a grid of rationals independent of symbolic engine.
    for j in range(1,101):
        p=F(j,100);q=1-p*p/4
        chain=(3*p**3-2*p*p-8*p+8)/8
        expected=(1-p/2)**2*q*q
        assert expected-chain==p**3*(p**3-4*p*p-4*p+8)/64;checks+=1
        dis=(p-2)**2*(p**4+2*p**3-8*p*p+8)/32
        assert dis-(1-p/2)**2*q**4==p**3*(2-p)**2*(64-64*p+16*p**3-p**5)/1024;checks+=1
    print('PASS',checks,'independent exact rational comparisons and algebraic identities')

if __name__=='__main__': main()
