#!/usr/bin/env python3
"""Independent Alexander-dual and finite-field comparison for two SRG(16,6,2,2) graphs."""
from collections import Counter
from itertools import combinations

V = range(16)


def adjacency(kind):
    a = [0] * 16
    for u in V:
        x,y=divmod(u,4)
        for v in V:
            z,w=divmod(v,4)
            if u == v:
                continue
            if kind == 'S':
                edge=((z-x)%4,(w-y)%4) in {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
            else:
                edge=x==z or y==w
            if edge:
                a[u] |= 1<<v
    return a


def dual_faces(a):
    conn=[]
    for t in combinations(V,3):
        edges=sum(bool(a[i]&(1<<j)) for i,j in combinations(t,2))
        if edges>=2:
            conn.append(sum(1<<i for i in t))
    triple_set=set(conn)
    faces={0:[1<<i for i in V],1:[(1<<i)|(1<<j) for i,j in combinations(V,2)],2:conn,3:[]}
    for t in combinations(V,4):
        if all(sum(1<<i for i in q) in triple_set for q in combinations(t,3)):
            faces[3].append(sum(1<<i for i in t))
    assert len(conn)==176
    # There is no 5-vertex face: each 5-set would require all its 4-subsets.
    four=set(faces[3])
    assert all(any(sum(1<<i for i in t) not in four for t in combinations(s,4))
               for s in combinations(V,5))
    return faces


def columns(faces,d):
    lowers={m:i for i,m in enumerate(faces[d-1])}
    for s in faces[d]:
        items=[i for i in V if s&(1<<i)]
        yield {lowers[s^(1<<v)]:(-1 if j%2 else 1) for j,v in enumerate(items)}


def rank(cols,p):
    pivots={}
    for col in cols:
        z={i:v%p for i,v in col.items() if v%p}
        while z:
            row=min(z)
            if row not in pivots:
                factor=pow(z[row],-1,p)
                pivots[row]={k:(v*factor)%p for k,v in z.items() if (v*factor)%p}
                break
            q=pivots[row]; factor=z[row]
            for k,v in q.items():
                vnew=(z.get(k,0)-factor*v)%p
                if vnew:z[k]=vnew
                else:z.pop(k,None)
    return len(pivots)


def main():
    for kind in 'SR':
        a=adjacency(kind)
        assert all(m.bit_count()==6 for m in a)
        assert all((a[i]&a[j]).bit_count()==2 for i,j in combinations(V,2))
        f=dual_faces(a)
        counts=tuple(len(f[i]) for i in range(4))
        assert counts == ((16,120,176,60) if kind=='S' else (16,120,176,44))
        results=[]
        for p in (2,3,5,11):
            rr=tuple(rank(columns(f,d),p) for d in (1,2,3))
            assert rr == (15,105,counts[3])
            betti2=counts[2]-rr[1]-rr[2]
            assert betti2==(11 if kind=='S' else 27)
            results.append((p,rr,betti2))
        print(kind, 'dual f-vector',counts,'(prime, boundary ranks, beta2)',results)
    print('DUAL_COMPARISON_VERIFY_OK')

if __name__ == '__main__':main()
