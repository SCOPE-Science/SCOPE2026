"""Reproducible exact checks for commuting singular semigroup endomorphisms.
Run with Python 3; no external dependencies.
"""
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, factorial
from random import Random

@lru_cache(None)
def involutions(m, sign=1):
    return sum(factorial(m)//(2**j * factorial(j)*factorial(m-2*j)) * sign**j
               for j in range(m//2+1))

@lru_cache(None)
def rooted_tripots(s):
    return sum(comb(s-1, h-1)*involutions(h-1)*h**(s-h)
               for h in range(1, s+1))

@lru_cache(None)
def rooted_idems(s):
    return sum(comb(s-1,h-1)*h**(s-h) for h in range(1,s+1))

def compose(f,g):
    return tuple(g[f[i]] for i in range(len(f)))

def parity(f):
    if sorted(f)!=list(range(len(f))):return None
    return (-1)**sum(f[i]>f[j] for i in range(len(f)) for j in range(i+1,len(f)))

def pair_set(n):
    fs=list(product(range(n),repeat=n))
    es=[e for e in fs if compose(e,e)==e]
    ts=[t for t in fs if compose(compose(t,t),t)==t]
    ans=[]
    for e in es:
        for t in ts:
            if compose(t,e)==e and compose(e,t)==e:
                ans.append((t,e))
    return es,ans

def classify(t,e):
    p=parity(t)
    return 'O' if p==-1 else 'E' if p==1 else 'N'

def rank(pair):
    t,e=pair
    return len({t, compose(t,t),e})

def phi_eval(pair,s):
    t,e=pair; p=parity(s)
    return t if p==-1 else compose(t,t) if p==1 else e

def direct_commutes(x,y,reps):
    for r in reps:
        if phi_eval(y,phi_eval(x,r))!=phi_eval(x,phi_eval(y,r)):
            return False
    return True

def core_commutes(x,y):
    t,e=x; u,f=y
    a=classify(t,e); b=classify(u,f)
    ident=tuple(range(len(t)))
    def prod(x,y):
        t,e=x;u,f=y
        typ=classify(t,e)
        if e==ident:return (compose(u,u),compose(u,u))
        if typ=='O':return y
        if typ=='E':return (compose(u,u),f)
        return (f,f)
    return prod(x,y)==prod(y,x)

def partitions(n,m=None):
    if n==0:
        yield ()
        return
    m=n if m is None else min(n,m)
    for k in range(m,0,-1):
        for rest in partitions(n-k,k):yield (k,)+rest

def e_data(parts):
    A=B=C=D=1
    for s in parts:
        A*=rooted_tripots(s)
        B*=involutions(s-1)
        C*=involutions(s-1,-1)
        D*=rooted_idems(s)
    E=(B+C)//2
    O=(B-C)//2
    N=A-B
    assert E>=1 and N>=1 and O>=0 and 1<=D<=A
    return (A,E,O,N,D)

def rankpoly_formula(n):
    result=Counter({(1,1):1})
    for pa in partitions(n):
        if pa==(1,)*n:continue
        mul=factorial(n)
        freq=Counter(pa)
        den=1
        for s,m in freq.items():den*=factorial(s-1)**m*factorial(m)
        assert mul%den==0
        weight=mul//den
        A,E,O,N,D=e_data(pa)
        P={2:1,3:E-1}
        Q={1:1,2:D-2,3:A-D-(E+O)+1}
        for i,ni in P.items():
            for j,nj in P.items():result[i,j]+=weight*ni*nj
        for i,ni in Q.items():
            for j,nj in Q.items():result[i,j]+=weight*ni*nj
        result[3,3]+=weight*O
        result[3,2]+=weight*O;result[2,3]+=weight*O
        result[3,1]+=weight*2*O;result[1,3]+=weight*2*O
        for i,ni in P.items():
            result[1,i]+=weight*2*ni;result[i,1]+=weight*2*ni
    return +result

def weighted_bell(n,weight):
    vals=[1]
    for k in range(1,n+1):
        vals.append(sum(comb(k-1,s-1)*s*weight(s)*vals[k-s] for s in range(1,k+1)))
    return vals[n]

def egf_census(n):
    a=lambda s:rooted_tripots(s)
    b=lambda s:involutions(s-1)
    c=lambda s:involutions(s-1,-1)
    B=lambda f:weighted_bell(n,f)
    numer=4*B(lambda s:a(s)**2)-8*B(lambda s:a(s)*b(s))+5*B(lambda s:b(s)**2)+2*B(lambda s:b(s)*c(s))+B(lambda s:c(s)**2)+22*B(b)-6*B(c)-16
    assert numer%4==0
    return numer//4

def main():
    for n in range(1,9):
        R=rankpoly_formula(n)
        count=sum(R.values())
        assert count==egf_census(n)
        assert all(R[i,j]==R[j,i] for i,j in R)
        print(f'n={n} ordered_commuting={count} rank_cells={dict(sorted(R.items()))}')
        if n>5:continue
        es,ps=pair_set(n)
        assert len(es)==sum(comb(n,r)*r**(n-r) for r in range(1,n+1))
        rng=Random(4125+n)
        reps=[tuple(range(n)),tuple([1,0]+list(range(2,n))) if n>=2 else (0,),tuple([0]*n)]
        if n<=4:
            actual=Counter()
            for a in ps:
                for b in ps:
                    ans=direct_commutes(a,b,reps)
                    assert ans==core_commutes(a,b), ('multiply mismatch',a,b,n)
                    if ans:actual[rank(a),rank(b)]+=1
            assert (+actual)==R,(n,+actual,R)
            print('  independently evaluated phi pair maps:',len(ps),'x',len(ps),'PASS')
        else:
            for _ in range(12500):
                a=ps[rng.randrange(len(ps))];b=ps[rng.randrange(len(ps))]
                assert direct_commutes(a,b,reps)==core_commutes(a,b)
            print('  actual phi pair-map random comparisons: 12,500 PASS; full EGF + partition identity PASS')
    print('COMMUTING_SINGULAR_ENDOMORPHISM_CENSUS_CHECKS_PASSED')

if __name__=='__main__':main()
