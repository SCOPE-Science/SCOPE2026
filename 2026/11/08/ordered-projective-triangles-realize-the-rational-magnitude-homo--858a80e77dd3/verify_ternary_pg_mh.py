#!/usr/bin/env python3
"""Exact integral magnitude-homology check for the 26-vertex incidence graph of PG(2,3).
Uses only the Python standard library. Integer row/column operations use unit pivots,
so the produced boundary ranks and absence of torsion are integral facts.
"""
from collections import defaultdict, Counter
from itertools import product

Q = 3

def graph():
    vecs=set()
    for x in product(range(Q), repeat=3):
        if x==(0,0,0): continue
        a=next(t for t in x if t)
        v=tuple(y*pow(a,-1,Q)%Q for y in x)
        vecs.add(v)
    vecs=sorted(vecs)
    assert len(vecs)==13
    nbr=[set() for _ in range(26)]
    for i,x in enumerate(vecs):
        for j,y in enumerate(vecs):
            if sum(a*b for a,b in zip(x,y))%Q==0:
                nbr[i].add(13+j);nbr[13+j].add(i)
    assert all(len(s)==4 for s in nbr)
    assert sum(map(len,nbr))==104
    return nbr

def distances(nbr):
    D=[]
    for x in range(len(nbr)):
        row=[99]*len(nbr);row[x]=0;front=[x]
        for y in front:
            for z in sorted(nbr[y]):
                if row[z]==99:
                    row[z]=row[y]+1;front.append(z)
        D.append(row)
    assert max(max(row) for row in D)==3
    assert all(D[x][y]==D[y][x] for x in range(26) for y in range(26))
    assert sum(D[x][y]==2 for x in range(26) for y in range(26))==312
    return D

def basis_by_endpoints(D):
    n=len(D);ans=defaultdict(lambda:defaultdict(list))
    def recur(seq,length):
        k=len(seq)-1
        if length==4:
            if 2<=k<=4:ans[(seq[0],seq[-1])][k].append(tuple(seq))
            return
        if k>=4:return
        for y,d in enumerate(D[seq[-1]]):
            if 0<d<=4-length:recur(seq+[y],length+d)
    for x in range(n):recur([x],0)
    return ans

def boundary(cols,rows,D):
    rr={e:i for i,e in enumerate(rows)}
    out=[[0]*len(cols) for _ in rows]
    for j,s in enumerate(cols):
        for i in range(1,len(s)-1):
            if D[s[i-1]][s[i+1]]==D[s[i-1]][s[i]]+D[s[i]][s[i+1]]:
                out[rr[s[:i]+s[i+1:]]][j]+=(-1)**i
    return out

def unit_normal_form(M):
    """Full integer row/column elimination, asserting no nonunit Smith pivots remain."""
    if not M:return 0,0
    a=[r[:] for r in M]; R=len(a);C=len(a[0]);t=0;peak=0
    while t<min(R,C):
        target=next(((i,j) for i in range(t,R) for j in range(t,C) if abs(a[i][j])==1),None)
        if target is None:break
        i,j=target
        a[i],a[t]=a[t],a[i]
        for r in range(R):a[r][j],a[r][t]=a[r][t],a[r][j]
        # First eliminate column t with integer row operations.
        for r in range(t+1,R):
            m=a[r][t]//a[t][t]
            if m:
                for c in range(t,C):a[r][c]-=m*a[t][c]
        # Then eliminate row t with integer column operations.
        for c in range(t+1,C):
            m=a[t][c]//a[t][t]
            if m:
                for r in range(t,R):a[r][c]-=m*a[r][t]
        assert all(a[r][t]==0 for r in range(t+1,R))
        assert all(a[t][c]==0 for c in range(t+1,C))
        t+=1
        peak=max(peak,max((abs(v) for row in a for v in row),default=0))
    remainder=[a[i][j] for i in range(t,R) for j in range(t,C)]
    assert all(v==0 for v in remainder), ('nonunit residual',R,C,t,Counter(remainder))
    return t,peak

def main():
    nbr=graph(); D=distances(nbr); B=basis_by_endpoints(D)
    counts=Counter(); patterns=defaultdict(Counter); peaks=Counter()
    for x in range(26):
        for y in range(26):
            b=B.get((x,y),{})
            c2,c3,c4=(b.get(i,[]) for i in (2,3,4))
            d3=boundary(c3,c2,D);d4=boundary(c4,c3,D)
            # independent check that d3 d4 = 0 on every basis generator
            for k in range(len(c4)):
                if d3:
                    assert all(sum(d3[i][j]*d4[j][k] for j in range(len(c3)))==0 for i in range(len(c2)))
            r3,p3=unit_normal_form(d3);r4,p4=unit_normal_form(d4)
            assert r3+r4<=len(c3)
            beta=len(c3)-r3-r4
            d=D[x][y]
            pat=(len(c2),len(c3),len(c4),r3,r4,beta)
            patterns[d][pat]+=1
            peaks['d3']=max(peaks['d3'],p3);peaks['d4']=max(peaks['d4'],p4)
            for key,val in zip(('C2','C3','C4','rank_d3','rank_d4','H3'),pat):counts[key]+=val
    assert dict(patterns[0])=={(12,36,28,12,24,0):26}
    assert dict(patterns[2])=={(17,45,19,17,19,9):312}
    assert all(set(patterns[d])=={(0,0,0,0,0,0)} for d in (1,3))
    assert counts['H3']==2808
    print('GRAPH: 26 vertices, 52 edges, 13 point nodes and 13 line nodes, diameter 3')
    print('ENDPOINT DISTANCE 0: 26 blocks, C2/C3/C4=12/36/28, ranks=12/24, H3=0')
    print('ENDPOINT DISTANCE 2: 312 blocks, C2/C3/C4=17/45/19, ranks=17/19, H3=9')
    print('ENDPOINT DISTANCES 1 AND 3: zero chain groups of length four')
    print('GLOBAL CHAIN DIMENSIONS AND RANKS:',dict(sorted(counts.items())))
    print('UNIT PIVOT ELIMINATION PEAK:',dict(peaks))
    print('ALL INTEGER NORMAL FORMS: only unit pivots, no nonzero residual')
    print('ALL COMPOSITIONS d3*d4: zero')
    print('CONCLUSION: MH_(3,4)(incidence PG(2,3); Z) = Z^2808')
    print('ENDPOINT-LOCALIZED: Z^9 for every distance-2 ordered pair; zero otherwise')
    print('TERNARY_PROJECTIVE_INCIDENCE_MAGNITUDE_INTEGRAL_VERIFIED')
if __name__=='__main__':main()
