"""Finite direct checks of left and two-sided principal-unit actions.

Uses only the Python standard library; q must be prime in these test cases.
"""
from itertools import product
from collections import defaultdict
from math import prod

def matrices(m,q):
    return list(product(range(q), repeat=m*m))

def mult(a,b,m,q):
    return tuple(sum(a[i*m+k]*b[k*m+j] for k in range(m))%q
                 for i in range(m) for j in range(m))

def add(a,b,q):
    return tuple((x+y)%q for x,y in zip(a,b))

def rank(a,m,q):
    rows=[list(a[i*m:(i+1)*m]) for i in range(m)]
    i=0
    for j in range(m):
        piv=next((k for k in range(i,m) if rows[k][j]%q),None)
        if piv is None: continue
        rows[piv],rows[i]=rows[i],rows[piv]
        t=pow(rows[i][j],-1,q)
        rows[i]=[(x*t)%q for x in rows[i]]
        for k in range(m):
            if k!=i:
                t=rows[k][j]
                rows[k]=[(x-t*y)%q for x,y in zip(rows[k],rows[i])]
        i+=1
        if i==m:break
    return i

def prediction_N(m,r,q):
    if not r:return 1
    return prod(q**m-q**i for i in range(r))**2 // prod(q**r-q**i for i in range(r))

def check(m,q):
    mats=matrices(m,q);zero=(0,)*(m*m); bins=defaultdict(lambda: [0,0,0])
    for C in mats:
        r=rank(C,m,q)
        left={mult(A,C,m,q) for A in mats}
        right={mult(C,A,m,q) for A in mats}
        both={add(X,Y,q) for X in left for Y in right}
        assert len(left)==q**(m*r),(m,q,r,len(left))
        assert len(both)==q**(2*m*r-r*r),(m,q,r,len(both))
        assert len(mats)%len(left)==0
        assert len(mats)%len(both)==0
        # Enumerate all actual orbit fibers as cosets in the second component.
        for image, expected in ((left,q**(m*r)),(both,q**(2*m*r-r*r))):
            unseen=set(mats);count=0
            while unseen:
                D=next(iter(unseen)); coset={add(D,X,q) for X in image}
                assert len(coset)==expected and coset.issubset(unseen)
                unseen-=coset;count+=1
            assert count==len(mats)//expected
        bins[r][0]+=1
        bins[r][1]+=q**(m*m-m*r)
        bins[r][2]+=q**((m-r)**2)
    out={r:tuple(bins[r]) for r in range(m+1)}
    for r,(number,left_orb,both_orb) in out.items():
        n=prediction_N(m,r,q)
        assert number==n,(m,q,r,number,n)
        assert left_orb==n*q**(m*(m-r))
        assert both_orb==n*q**((m-r)**2)
    print('case',m,q,'rank triples',out,'totals',sum(x[1] for x in out.values()),sum(x[2] for x in out.values()))

# The further checks use linear generator spans, rather than coset enumeration.
def vec_rank_binary(vectors):
    basis={}
    for v in vectors:
        a=sum((x&1)<<i for i,x in enumerate(v))
        while a:
            i=a.bit_length()-1
            if i not in basis:
                basis[i]=a
                break
            a^=basis[i]
    return len(basis)

def check_binary_m3():
    m,q=3,2
    mats=matrices(m,q)
    z=(0,)*(m*m)
    basis=[]
    for i in range(m*m):
        t=list(z); t[i]=1; basis.append(tuple(t))
    bins=defaultdict(lambda:[0,0,0])
    for C in mats:
        r=rank(C,m,q)
        la=vec_rank_binary([mult(U,C,m,q) for U in basis])
        co=vec_rank_binary([mult(U,C,m,q) for U in basis]+[mult(C,U,m,q) for U in basis])
        assert la==m*r
        assert co==2*m*r-r*r
        bins[r][0]+=1
        bins[r][1]+=2**(m*m-la)
        bins[r][2]+=2**(m*m-co)
    for r in range(m+1):
        n=prediction_N(m,r,q)
        assert bins[r]==[n,n*2**(m*(m-r)),n*2**((m-r)**2)]
    assert sum(x[1] for x in bins.values())==6168
    assert sum(x[2] for x in bins.values())==2052
    print('binary m=3 generator dimension and rank census',dict(bins))


def check_asymptotic_sample():
    # Numerical examples are checks only, not the infinite-dimensional proof.
    q=2; m=60
    P=[1.0]
    for i in range(1,m+1):
        P.append(P[-1]*(1-q**(-i)))
    H=lambda r: P[m]**2/(P[r]*P[m-r]**2)
    Wt=[H(r) for r in range(m+1)]
    Wl=[q**(-((r-m/2)**2))*H(r) for r in range(m+1)]
    pt=[w/sum(Wt) for w in Wt]
    pl=[w/sum(Wl) for w in Wl]
    uniform_tv=sum(abs(p-1/(m+1)) for p in pt)/2
    theta=sum(q**(-j*j) for j in range(-50,51))
    theta_tv=sum(abs(pl[r]-q**(-(r-m/2)**2)/theta) for r in range(m+1))/2
    assert uniform_tv<0.07, uniform_tv
    assert theta_tv<1e-7, theta_tv
    print('asymptotic sample q=2 m=60 two-sided uniform-TV',round(uniform_tv,6),
          'left theta-TV',round(theta_tv,10))

if __name__=='__main__':
    for m,q in [(1,2),(1,3),(2,2),(2,3)]:
        check(m,q)
    check_binary_m3()
    check_asymptotic_sample()
    print('MATRIX_RADICAL_TWO_SIDED_ORBIT_SPECTRA_VERIFIED')
