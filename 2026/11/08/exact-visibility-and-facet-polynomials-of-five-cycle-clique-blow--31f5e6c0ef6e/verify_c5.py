#!/usr/bin/env python3
"""Direct graph check of visibility, facets, and minimal nonfaces for C5[K_m]."""
import itertools, math
from collections import Counter, defaultdict

def mul(a,b):
    d=Counter()
    for x,c in a.items():
        for y,e in b.items():d[x+y]+=c*e
    return d

def add(*args):
    r=Counter()
    for a in args:r.update(a)
    return r

def scale(a,k):return Counter({j:c*k for j,c in a.items()})
def powpoly(a,k):
    res=Counter({0:1})
    for _ in range(k):res=mul(res,a)
    return res

def polynomials(m):
    A=Counter({i:math.comb(m,i) for i in range(1,m)})
    B=Counter({m:1})
    T=add(Counter({0:1}),A)
    face=add(powpoly(T,5),scale(mul(B,add(Counter({0:1}),scale(A,4),scale(powpoly(A,2),5),scale(powpoly(A,3),2))),5),scale(mul(powpoly(B,2),add(Counter({0:2}),scale(A,4),powpoly(A,2))),5),scale(powpoly(B,3),5))
    facet=add(Counter({3*m:5}),Counter({3*m-1:5*m}),Counter({4*m-2:5*m*m}),Counter({5*m-5:m**5}))
    return face,facet

def main():
    subsets=0;facets_sum=0
    for m in (2,3):
        n=5*m
        adj=[0]*n
        for u in range(n):
            for v in range(n):
                if u!=v and ((u//m-v//m)%5 in (0,1,4)):
                    adj[u]|=1<<v
        witnesses={}
        for u in range(n):
            for v in range(u+1,n):
                if (adj[u]>>v)&1:continue
                mid=adj[u]&adj[v]
                assert mid and mid.bit_count()==m
                witnesses[u,v]=mid
        facepoly=Counter();facetpoly=Counter()
        faces=bytearray(1<<n)
        for mask in range(1<<n):
            sel=[j for j in range(n) if mask>>j&1]
            good=True
            for u,v in itertools.combinations(sel,2):
                w=witnesses.get((u,v))
                if w is not None and not (w & ~mask):good=False;break
            if good:
                faces[mask]=1;facepoly[len(sel)]+=1
        minimal_bad=[]
        for mask in range(1<<n):
            if not faces[mask] and all(faces[mask&~(1<<v)] for v in range(n) if mask>>v&1):
                minimal_bad.append(mask)
        expected_bad=set()
        for i in range(5):
            fi=sum(1<<(i*m+j) for j in range(m))
            for u in range(m):
                for v in range(m):
                    expected_bad.add(fi|(1<<(((i-1)%5)*m+u))|(1<<(((i+1)%5)*m+v)))
        assert set(minimal_bad)==expected_bad and len(expected_bad)==5*m*m
        for mask in range(1<<n):
            if faces[mask] and all(not faces[mask|(1<<v)] for v in range(n) if not (mask>>v&1)):
                facetpoly[mask.bit_count()]+=1
        assert (facepoly,facetpoly)==polynomials(m),(m,facepoly,facetpoly,polynomials(m))
        subsets+=1<<n;facets_sum+=sum(facetpoly.values())
    for m in range(2,30):
        face,facet=polynomials(m)
        assert sum(face.values())>=sum(facet.values())
        assert min(facet)==3*m-1
        assert max(facet)==max(3*m,4*m-2,5*m-5)
    print(f'VERIFY_OK C5_blowups_m=2,3 subsets={subsets} facets={facets_sum} direct_common_neighbors=PASS exact_face_polynomial=PASS exact_facet_polynomial=PASS minimal_nonfaces=PASS symbolic_m2to29=PASS')
if __name__=='__main__':main()
