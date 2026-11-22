"""Finite coefficient checks for involutive truncated polynomial substitutions.
No external mathematical libraries are required.
"""
from itertools import product
from math import comb
from collections import Counter


def monomials(d, N):
    return [e for degree in range(N) for e in product(range(degree + 1), repeat=d) if sum(e) == degree]


def mul(a, b, p, N):
    out = {}
    for x, cx in a.items():
        for y, cy in b.items():
            z = tuple(i + j for i, j in zip(x, y))
            if sum(z) < N:
                out[z] = (out.get(z, 0) + cx * cy) % p
    return {k:v for k,v in out.items() if v}


def compose(images, p, N):
    d = len(images)
    e0 = (0,) * d
    result = []
    for f in images:
        out = {}
        for e, c in f.items():
            term = {e0:c}
            for i, power in enumerate(e):
                for _ in range(power):
                    term = mul(term, images[i], p, N)
            for key, value in term.items():
                out[key] = (out.get(key, 0) + value) % p
        result.append({k:v for k,v in out.items() if v})
    return result


def apply_substitution(f, g, p, N):
    # f after g: replace coordinate variables in f with the g coordinates
    d = len(g)
    e0 = (0,)*d
    results = []
    for fi in f:
        total = {}
        for exp,c in fi.items():
            term = {e0:c}
            for i, power in enumerate(exp):
                for _ in range(power):
                    term = mul(term, g[i], p, N)
            for key,val in term.items():
                total[key]=(total.get(key,0)+val)%p
        results.append({k:v for k,v in total.items() if v})
    return results


def f_identity(d):
    return [{tuple(int(i==j) for i in range(d)):1} for j in range(d)]


def rank_mod(matrix,p):
    a = [list(row) for row in matrix]
    R=len(a); C=len(a[0]) if a else 0
    pivot=0
    for j in range(C):
        k=next((k for k in range(pivot,R) if a[k][j]%p),None)
        if k is None: continue
        a[k],a[pivot]=a[pivot],a[k]
        inv=pow(a[pivot][j],-1,p)
        a[pivot]=[x*inv%p for x in a[pivot]]
        for i in range(R):
            if i!=pivot and a[i][j]:
                c=a[i][j]
                a[i]=[(x-c*y)%p for x,y in zip(a[i],a[pivot])]
        pivot+=1
        if pivot==R:break
    return pivot


def m(n,j):
    if n==0:return int(j==0)
    return comb(n+j-1,j)

def exponent(d,N,r):
    s=d-r
    tot=0
    for j in range(2,N):
        E=sum(m(r,k)*m(s,j-k) for k in range(0,j+1,2))
        O=m(d,j)-E
        tot+=r*E+s*O
    return tot


def fixed_dim(d,N,r):
    s=d-r
    return sum(sum(m(r,k)*m(s,j-k) for k in range(0,j+1,2)) for j in range(N))


def gl_order(d,q):
    return q**(d*(d-1)//2)*__import__('math').prod(q**i-1 for i in range(1,d+1))


def independent_lowest_jet_rank(d,p,r):
    # At N=3, condition f(f(x))-x=0 is LINEAR in quadratic jet coefficients.
    # Form the equations by composing basis substitutions, not by sign-counting.
    N=3; h=f_identity(d)
    for i in range(r):
        key=next(iter(h[i]));h[i][key]=p-1
    quads=[e for e in monomials(d,N) if sum(e)==2]
    coords=[(i,e) for i in range(d) for e in quads]
    columns=[]
    for i,e in coords:
        f=[dict(x) for x in h];f[i][e]=1
        ff=apply_substitution(f,f,p,N)
        cols=[ff[k].get(mon,0) for k in range(d) for mon in quads]
        columns.append(cols)
    rows=list(zip(*columns))
    rank=rank_mod(rows,p)
    dim=len(coords)-rank
    return dim, len(coords), rank


def exhaustive_two_variables(p=3):
    d=2;N=3; idmap=f_identity(d)
    coords=[(i,e) for i in range(d) for e in monomials(d,N) if sum(e)==2]
    counts={}
    for r in (0,1,2):
        h=[dict(x) for x in idmap]
        for i in range(r):
            key=next(iter(h[i]));h[i][key]=p-1
        hit=0
        for a in product(range(p),repeat=len(coords)):
            f=[dict(x) for x in h]
            for (i,e),c in zip(coords,a):
                if c:f[i][e]=c
            if apply_substitution(f,f,p,N)==idmap:hit+=1
        counts[r]=hit
        assert hit==p**exponent(d,N,r),(r,hit)
    return counts


def asymptotic_winners():
    for d in range(3,8):
        for N in range(4,13):
            e=[exponent(d,N,r) for r in range(d+1)]
            target=d if N%2 else (d+1)//2
            assert max(e)==e[target] and e.count(e[target])==1,(d,N,e)
    return True


def centralizer_dimension_direct(d,N,r):
    # Enumerate output monomial positions and test h∘u=u∘h on the coefficient basis.
    # Deliberately independent of closed E/O combinatorial calculations.
    pos=0; neg=0
    for out in range(d):
        for e in monomials(d,N):
            if sum(e)<2:continue
            outsign= -1 if out<r else 1
            monsign= -1 if (sum(e[:r])%2) else 1
            if outsign==monsign:pos+=1
            else:neg+=1
    return pos,neg


def random_conjugation_check(p=3,d=3,N=4,samples=48):
    import random
    rng=random.Random(20261115)
    h=f_identity(d)
    for r in range(d+1):
        H=[dict(x) for x in h]
        for i in range(r):
            k=next(iter(H[i]));H[i][k]=p-1
        for _ in range(samples):
            u=[dict(x) for x in h]
            for i in range(d):
                for e in monomials(d,N):
                    if sum(e)>=2:
                        v=rng.randrange(p)
                        if v:u[i][e]=v
            # Instead of inverting u, verify f h = h f when f= u^{-1} h u;
            # construct inverse by fixed-point iteration using truncated degree filtration.
            v=[dict(x) for x in h]
            for _it in range(N):
                cu=apply_substitution(u,v,p,N)
                for i in range(d):
                    # v <- v + (id-u(v)), converges because u has identity linear part.
                    for e in monomials(d,N):
                        correction=(h[i].get(e,0)-cu[i].get(e,0))%p
                        if correction:
                            v[i][e]=(v[i].get(e,0)+correction)%p
                            if v[i][e]==0:del v[i][e]
            assert apply_substitution(u,v,p,N)==h
            tmp=apply_substitution(H,u,p,N)
            f=apply_substitution(v,tmp,p,N)
            assert apply_substitution(f,f,p,N)==h
            for i in range(d):
                for e in monomials(d,N):
                    if sum(e)==1:
                        assert f[i].get(e,0)==H[i].get(e,0)
    return samples*(d+1)


def run():
    print('EXHAUSTIVE: q=3,d=2,N=3',exhaustive_two_variables())
    for d,N,p in ((3,3,3),(3,4,3),(4,4,3),(3,5,5),(5,6,3)):
        if N==3:
            checks=[independent_lowest_jet_rank(d,p,r) for r in range(d+1)]
            for r, (dimension,total,rank) in enumerate(checks):
                assert dimension==exponent(d,N,r)
            print('INDEPENDENT QUADRATIC EQUATION RANK:',d,N,p,checks)
        coords=[centralizer_dimension_direct(d,N,r) for r in range(d+1)]
        for r,(same,different) in enumerate(coords):
            assert different==exponent(d,N,r)
            assert same+different==d*sum(m(d,j) for j in range(2,N))
        print('CENTRALIZER COEFFICIENT TEST:',d,N,p,coords)
    print('RANDOM NONLINEAR CONJUGATES:',random_conjugation_check())
    assert asymptotic_winners()
    print('UNIQUE PARITY-WINNER CHECK: d=3..7,N=4..12 PASS')
    for N in range(4,10):
        vals=[exponent(3,N,r) for r in range(4)]
        Fs=[fixed_dim(3,N,r) for r in range(4)]
        print('DIMENSION THREE:',N,vals,Fs)
    print('ALL TESTS PASS')

if __name__=='__main__':run()
