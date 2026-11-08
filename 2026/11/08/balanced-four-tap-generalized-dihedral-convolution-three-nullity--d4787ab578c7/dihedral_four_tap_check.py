"""Reproduce direct-matrix and character-fiber checks for four-tap generalized-dihedral convolution."""
import itertools
import math
import numpy as np


def group(elements, add, neg):
    return list(elements), add, neg


def elementary_group(p, d):
    elems = list(itertools.product(range(p), repeat=d))
    add = lambda a,b: tuple((x+y)%p for x,y in zip(a,b))
    neg = lambda a: tuple((-x)%p for x in a)
    return group(elems,add,neg)


def cyclic_group(n):
    return group(range(n),lambda a,b:(a+b)%n,lambda a:(-a)%n)


def modular_rank(M, prime=1000003):
    A = np.asarray(M, dtype=np.int64).copy() % prime
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        idx = next((j for j in range(r,rows) if A[j,c] != 0), None)
        if idx is None:
            continue
        if idx!=r:
            A[[r,idx]] = A[[idx,r]]
        factor = pow(int(A[r,c]),-1,prime)
        A[r,c:] = (A[r,c:]*factor)%prime
        for j in range(r+1,rows):
            v = A[j,c]
            if v:
                A[j,c:] = (A[j,c:]-v*A[r,c:])%prime
        r+=1
        if r==rows: break
    return r


def run(elems,add,neg,u,v,characters,expected_nullity=None,expected_gap=None):
    N = len(elems)
    ix = {a:i for i,a in enumerate(elems)}
    zero = next(a for a in elems if add(a,neg(a))==a)
    # Two coordinates: (a,0), (a,1); right multiplication by (b,e).
    taps = [(zero,0),(u,0),(zero,1),(v,1)]
    M=np.zeros((2*N,2*N), dtype=np.int64)
    for ep in (0,1):
        for a in elems:
            i = ep*N+ix[a]
            for b,delta in taps:
                output_a=add(a,b if ep==0 else neg(b))
                j=((ep+delta)%2)*N+ix[output_a]
                M[i,j]+=1
    eig=[]; null=0
    for chi in characters:
        z=chi(u);w=chi(v)
        a,b=1+z,1+w
        eig.extend([abs(a)+abs(b),abs(abs(a)-abs(b))])
        if abs(abs(a)-abs(b))<1e-7: null+=1
    vals=np.linalg.svd(M.astype(float),compute_uv=False)
    d=np.max(np.abs(np.sort(vals)-np.sort(eig)))
    assert d<1e-7,(N,d)
    rank=modular_rank(M)
    assert 2*N-rank==null,(N,rank,null)
    if expected_nullity is not None: assert null==expected_nullity,(N,null,expected_nullity)
    positives=sorted(x for x in eig if x>1e-7)
    gap=positives[0]
    if expected_gap is not None:assert abs(gap-expected_gap)<1e-7,(N,gap,expected_gap)
    assert abs(max(eig)-4)<1e-7
    print('PASS','|A|=',N,'u=',u,'v=',v,'nullity=',null,'minpos=',round(gap,11),'spectrum_error=',round(float(d),13))


def characters_elementary(p,d):
    z=np.exp(2j*np.pi/p)
    return [lambda a,k=k:z**(sum(ki*ai for ki,ai in zip(k,a))%p) for k in itertools.product(range(p),repeat=d)]


def characters_cyclic(n):
    z=np.exp(2j*np.pi/n)
    return [lambda a,k=k:z**((k*a)%n) for k in range(n)]


def tests():
    for p in [3,5,7]:
        A=elementary_group(p,2)
        chars=characters_elementary(p,2)
        u=(1,0);v=(0,1)
        exp=2*p-1
        gap=2*(1-math.cos(math.pi/p))
        run(*A,u,v,chars,exp,gap)
        if p==5:
            run(*A,(1,0),(2,0),chars,p)
            run(*A,(1,0),(1,0),chars,p**2)
    A=elementary_group(3,3)
    run(*A,(1,0,0),(0,1,0),characters_elementary(3,3),2*3**2-3)
    for n,u,v in [(9,1,2),(9,1,1),(15,1,4),(21,6,3)]:
        A=cyclic_group(n)
        exp=math.gcd(n,u-v)+math.gcd(n,u+v)-math.gcd(n,u,v)
        run(*A,u,v,characters_cyclic(n),exp)
    for p,d in [(3,2),(5,2)]:
        elems=list(itertools.product(range(p),repeat=d))
        pairs=list(itertools.combinations(elems,2))
        counts=[0,0,0]
        def diff(x,y):return tuple((b-a)%p for a,b in zip(x,y))
        for a,b in pairs:
            u=diff(a,b)
            for c,e in pairs:
                v=diff(c,e)
                if v==u or v==tuple((-z)%p for z in u):
                    counts[0]+=1
                elif any(v==tuple((l*z)%p for z in u) for l in range(p)):
                    counts[1]+=1
                else:counts[2]+=1
        N=p**d
        expected=[N*N*(N-1)//2,N*N*(N-1)*(p-3)//4,N*N*(N-1)*(N-p)//4]
        assert counts==expected,(p,counts,expected)
        print('CENSUS_PASS','p=',p,'d=',d,'counts=',counts)
    print('GENERALIZED_DIHEDRAL_FOUR_TAP_CHECKS_PASS')

if __name__=='__main__':tests()
