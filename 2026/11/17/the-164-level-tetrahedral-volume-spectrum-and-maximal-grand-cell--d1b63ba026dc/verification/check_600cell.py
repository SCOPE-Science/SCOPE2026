"""Exact 600-cell four-vertex tetrahedron census, Q(phi), phi^2=phi+1.

Run: python verification/check_600cell.py
Requires Python standard library only, plus SPECTRUM.csv in the same directory.
Coordinates and all inner products are exact integers in the basis (1,phi).
"""
from itertools import product, permutations, combinations
from functools import cmp_to_key
from collections import Counter
from pathlib import Path
import csv
from math import comb

Z = (0, 0)

def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y):
    a,b=x; c,d=y
    return (a*c+b*d,a*d+b*c+b*d)
def times(x,k): return (k*x[0],k*x[1])
def sign(x):
    """Exact sign of a+b phi via integer comparisons of (2a+b)+b sqrt(5)."""
    a,b=x; t=2*a+b
    if b==0: return (t>0)-(t<0)
    if t==0: return (b>0)-(b<0)
    if t*b>0: return (t>0)-(t<0)
    diff=t*t-5*b*b
    assert diff != 0
    s=(diff>0)-(diff<0)
    return s if t>0 else -s

def compare(x,y): return sign(sub(x,y))
def dot(a,b):
    z=Z
    for x,y in zip(a,b):z=add(z,mul(x,y))
    return z

def norm2(a):return dot(a,a)

def det3(g00,g11,g22,g01,g02,g12):
    return add(sub(mul(g00,sub(mul(g11,g22),mul(g12,g12))),
                   mul(g01,sub(mul(g01,g22),mul(g02,g12)))),
               mul(g02,sub(mul(g01,g12),mul(g11,g02))))

def det3vectors(a,b,c):
    # Independent alternating three-minor implementation for Cauchy--Binet.
    D=Z
    for ids in combinations(range(4),3):
        i,j,k=ids
        v0=sub(sub(mul(b[j],c[k]),mul(b[k],c[j])),Z)
        v1=sub(mul(b[i],c[k]),mul(b[k],c[i]))
        v2=sub(mul(b[i],c[j]),mul(b[j],c[i]))
        minor=add(sub(mul(a[i],v0),mul(a[j],v1)),mul(a[k],v2))
        D=add(D,mul(minor,minor))
    return D

def vertices():
    V=[]
    for i in range(4):
        for s in (-1,1):
            v=[Z]*4;v[i]=(2*s,0);V.append(tuple(v))
    for signs in product((-1,1),repeat=4):
        V.append(tuple((s,0) for s in signs))
    symbols=(Z,(1,0),(0,1),(-1,1)) # 0,1,phi,phi^-1
    for perm in permutations(range(4)):
        inv=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        if inv%2:continue
        base=[symbols[j] for j in perm]
        nonzero=[i for i in range(4) if base[i]!=Z]
        for signs in product((-1,1),repeat=3):
            v=base.copy()
            for i,s in zip(nonzero,signs):v[i]=times(v[i],s)
            V.append(tuple(v))
    assert len(V)==len(set(V))==120
    assert all(norm2(v)==(4,0) for v in V)
    return V

def solve():
    V=vertices();p=((2,0),Z,Z,Z)
    W=[v for v in V if v!=p]
    X=[tuple(sub(v[k],p[k]) for k in range(4)) for v in W]
    G=[[dot(x,y) for y in X] for x in X]
    spectrum=Counter();maxval=Z;maxima=[]
    # Complete enumeration of all C(119,3)=273819 distinct triples.
    # Independent Cauchy--Binet calculation on EVERY triple.
    for i in range(117):
        for j in range(i+1,118):
            for k in range(j+1,119):
                D=det3(G[i][i],G[j][j],G[k][k],G[i][j],G[i][k],G[j][k])
                assert D==det3vectors(X[i],X[j],X[k]), (i,j,k,D)
                assert sign(D)>=0
                spectrum[D]+=1
                c=compare(D,maxval)
                if c>0: maxval=D; maxima=[(i,j,k)]
                elif c==0:maxima.append((i,j,k))
    assert sum(spectrum.values())==comb(119,3)
    assert len(spectrum)==164, len(spectrum)
    assert maxval==(160,256), maxval
    assert len(maxima)==20,len(maxima)
    assert all(all(dot(tuple(sub(a[m],b[m]) for m in range(4)),
                       tuple(sub(a[m],b[m]) for m in range(4)))==(4,4)
                   for a,b in combinations([p]+[W[t] for t in ids],2))
               for ids in maxima)
    levels=sorted(spectrum, key=cmp_to_key(lambda a,b: -compare(a,b)))
    assert levels[1]==(160,240),levels[1]
    assert spectrum[levels[1]]==120
    # Build graph of all golden-chord edges and independently enumerate K4s.
    nbr=[set() for _ in V]
    for i,j in combinations(range(120),2):
        delta=[sub(V[i][k],V[j][k]) for k in range(4)]
        if norm2(delta)==(4,4): nbr[i].add(j);nbr[j].add(i)
    assert set(map(len,nbr))=={12}
    tetra=set()
    for a in range(120):
        for b in nbr[a]:
            if b<=a:continue
            for c in nbr[a]&nbr[b]:
                if c<=b:continue
                for d in nbr[a]&nbr[b]&nbr[c]:
                    if d>c:tetra.add((a,b,c,d))
    assert len(tetra)==600
    triangles=Counter(tuple(s) for T in tetra for s in combinations(T,3))
    edges=Counter(tuple(s) for T in tetra for s in combinations(T,2))
    assert len(triangles)==1200 and set(triangles.values())=={2}
    assert len(edges)==720 and set(edges.values())=={5}
    # Write only via explicit command, default verifies supplied spectrum file.
    rows=[(d[0],d[1],30*spectrum[d]) for d in levels]
    assert sum(c for _,_,c in rows)==comb(120,4)
    assert rows[0]==(160,256,600)
    path=Path(__file__).with_name('SPECTRUM.csv')
    if path.exists():
        with path.open(newline='',encoding='utf-8') as f:
            r=csv.DictReader(f)
            saved=[(int(x['A']),int(x['B']),int(x['multiplicity'])) for x in r]
        assert rows==saved,(len(rows),len(saved))
    else:
        with path.open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f);w.writerow(('A','B','multiplicity'));w.writerows(rows)
    print('600CELL_TETRA_EXACT_PASS vertices=120 anchored_triples=273819 levels=164 total_subsets=8214570 maxima=600 golden_K4=600 max_det=(160,256) next_det=(160,240) all_Cauchy_Binet=PASS')

if __name__=='__main__':solve()
