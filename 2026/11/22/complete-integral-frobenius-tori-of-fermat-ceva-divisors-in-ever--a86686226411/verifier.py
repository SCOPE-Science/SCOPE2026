#!/usr/bin/env python3
"""Finite checks of the geometry, Frobenius cycles, torus lattice and point counts of Fermat–Ceva divisors.
No external packages are needed. Finite checks supplement the symbolic argument.
"""
from math import gcd
from collections import Counter


def orbits(n, q, power=1):
    universe = [(i, j) for i in range(n) for j in range(n)] if power == 2 else list(range(n))
    seen, result = set(), []
    for x in universe:
        if x in seen:
            continue
        cyc = []
        y = x
        while y not in seen:
            seen.add(y)
            cyc.append(y)
            if power == 2:
                y = ((y[0]*q)%n, (y[1]*q)%n)
            else:
                y = (y*q)%n
        assert y == x
        result.append(tuple(cyc))
    return result


def graph_test(n, q):
    assert gcd(n,q) == 1
    S = [(i,j) for i in range(n) for j in range(n)]
    # Exactly 3n components, three coordinate points, n^2 triple points.
    A = [('A',i) for i in range(n)]
    B = [('B',i) for i in range(n)]
    C = [('C',i) for i in range(n)]
    Vlines = A+B+C
    centers = [('center',t) for t in 'ABC']
    triples = [('M',i,j) for i,j in S]
    edges=[]
    for family in (A,B,C):
        edges += [(v,('center',v[0])) for v in family]
    for i,j in S:
        edges += [(('A',i),('M',i,j)),(('B',j),('M',i,j)),(('C',(-i-j)%n),('M',i,j))]
    assert len(edges)==3*n*(n+1)
    assert len(set(Vlines+centers+triples)) == 3*n+3+n*n
    assert len(edges)-len(Vlines+centers+triples)+1 == 2*n*n-2
    # Contract the 3n star edges and n^2 A-M edges; leaves 3 family vertices
    # and two n^2-edge bundles. Each contracted edge corresponds to a tree edge.
    parents = {v:v for v in Vlines+centers+triples}
    def root(x):
        while parents[x]!=x:
            x=parents[x]
        return x
    def union(u,v):
        u,v=root(u),root(v)
        assert u!=v
        parents[v]=u
    for u,v in edges[:3*n]:
        union(u,v)
    for u,v in edges[3*n::3]:
        union(u,v)
    assert len({root(x) for x in parents})==3
    assert all(root(('A',i))==root(('A',0)) for i in range(n))
    assert all(root(('B',i))==root(('B',0)) for i in range(n))
    assert all(root(('C',i))==root(('C',0)) for i in range(n))
    assert len(edges[3*n:])==3*n*n
    assert len(edges[3*n+1::3])==n*n
    assert len(edges[3*n+2::3])==n*n
    # Add the two distinguished edges at M_(0,0). The whole set is an
    # invariant spanning tree in the original graph.
    zeroB=(('B',0),('M',0,0))
    zeroC=(('C',0),('M',0,0))
    assert zeroB in edges and zeroC in edges
    union(*zeroB)
    union(*zeroC)
    assert len({root(x) for x in parents})==1
    assert (3*n+n*n+2)==len(parents)-1
    # Frobenius preserves both distinguished edges and every edge type of the tree.
    def frob(v):
        if v[0]=='center':return v
        if v[0]=='M':return ('M',v[1]*q%n,v[2]*q%n)
        return (v[0],v[1]*q%n)
    tree=set(edges[:3*n]+edges[3*n::3]+[zeroB,zeroC])
    assert len(tree)==len(parents)-1
    for u,v in tree:
        assert (frob(u),frob(v)) in tree
    # The two bundles of non-tree edges are permuted by Frobenius.
    chords=set(edges)-tree
    assert len(chords)==2*n*n-2
    for u,v in chords:
        assert (frob(u),frob(v)) in chords
    # Each fundamental cycle for s!=0 is B_s-B_0 or C_s-C_0.
    # Every cycle is sum-zero separately in both edge bundles.
    # Their 2(n^2-1) coefficient columns are independent and integral.
    basis = []
    for k in (0,1):
        for s in S:
            if s!=(0,0):
                vector={(k,s):1,(k,(0,0)):-1}
                basis.append(vector)
    assert len(basis)==2*n*n-2
    for v in basis:
        assert sum(c for (k,s),c in v.items())==0
    # Frobenius takes a basis element to another basis element since (0,0) is fixed.
    basis_enc = {tuple(sorted(v.items())) for v in basis}
    for v in basis:
        fw = {(k,(s[0]*q%n,s[1]*q%n)):c for (k,s),c in v.items()}
        assert tuple(sorted(fw.items())) in basis_enc
    rcycles = Counter(map(len,orbits(n,q)))
    scycles = Counter(map(len,orbits(n,q,2)))
    assert sum(d*c for d,c in rcycles.items()) == n
    assert sum(d*c for d,c in scycles.items()) == n*n
    assert sum(d*(c-(d==1)) for d,c in scycles.items())==n*n-1
    # Frobenius orbit and fixed-point counts match gcd formula.
    period=1
    for cyc in orbits(n,q,2):
        from math import lcm
        period=lcm(period,len(cyc))
    for r in range(1,2*period+1):
        fixedS=sum(d*c for d,c in scycles.items() if r%d==0)
        fixedR=sum(d*c for d,c in rcycles.items() if r%d==0)
        assert fixedS == gcd(n,pow(q,r)-1)**2
        assert fixedR == gcd(n,pow(q,r)-1)
    return rcycles,scycles


def prime_field_points(n,p):
    assert gcd(n,p)==1
    pts=0
    for x in range(p):
        for y in range(p):
            for z in range(p):
                if x==y==z==0: continue
                if next(t for t in (x,y,z) if t!=0)!=1:continue
                a,b,c=(pow(v,n,p) for v in (x,y,z))
                pts+=(a==b or b==c or c==a)
    return pts

# Some small extension fields: monic irreducible defining polynomials.
# e.g. 2:x^2+x+1, 2:x^3+x+1, 3:x^2+1, 5:x^2+2.
IRR={(2,2):(1,1,1),(2,3):(1,1,0,1),(3,2):(1,0,1),(5,2):(2,0,1)}
def ext_add(a,b,p,e):
    x=0
    for j in range(e):x+=(((a//p**j)%p+(b//p**j)%p)%p)*p**j
    return x

def ext_mul(a,b,p,e):
    f=IRR[p,e]
    v=[0]*(2*e-1)
    for i in range(e):
        for j in range(e):v[i+j]+=((a//p**i)%p)*((b//p**j)%p)
    for k in range(2*e-2,e-1,-1):
        for j in range(e):v[k-e+j]-=v[k]*f[j]
    return sum((v[i]%p)*p**i for i in range(e))

def ext_pow(a,n,p,e):
    b=1
    while n:
        if n&1:b=ext_mul(b,a,p,e)
        a=ext_mul(a,a,p,e)
        n//=2
    return b

def ext_points(n,p,e):
    q=p**e
    assert gcd(n,p)==1
    total=0
    # homogeneous normalized projective coordinates (1,a,b),(0,1,b),(0,0,1)
    points=[(1,a,b) for a in range(q) for b in range(q)]
    points += [(0,1,b) for b in range(q)]
    points +=[(0,0,1)]
    for x,y,z in points:
        X,Y,Z=(ext_pow(v,n,p,e) for v in (x,y,z))
        total+=(X==Y or Y==Z or Z==X)
    return total


def main():
    cases=0
    for n in range(3,16):
        for q in (2,3,4,5,7,8,9,11,13,16,17,19,23):
            if gcd(n,q)!=1: continue
            a,b=graph_test(n,q)
            cases+=1
            if n in (3,5,7,8) and q in (2,3,5,7,11):
                print('FROB',n,q,'roots',sorted(a.items()),'triples',sorted(b.items()))
    for p in (2,3,5,7,11,13,17,19,23):
        for n in range(3,20):
            if n%p==0:continue
            expected=3+3*p*gcd(n,p-1)-2*gcd(n,p-1)**2
            actual=prime_field_points(n,p)
            assert actual==expected,(p,n,actual,expected)
    ext_cases=0
    for (p,e) in IRR:
        q=p**e
        for n in range(3,13):
            if n%p==0:continue
            actual=ext_points(n,p,e)
            expected=3+3*q*gcd(n,q-1)-2*gcd(n,q-1)**2
            assert actual==expected,(p,e,n,actual,expected)
            ext_cases+=1
    print('GEOMETRY_ORBIT_TESTS',cases)
    print('EXTENSION_FIELD_TESTS',ext_cases)
    print('ALL_FERMAT_CEVA_TORUS_AND_ZETA_CHECKS_OK')

if __name__=='__main__':main()
