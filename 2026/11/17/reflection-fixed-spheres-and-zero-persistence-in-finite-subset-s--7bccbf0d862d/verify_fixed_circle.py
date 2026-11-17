#!/usr/bin/env python3
"""Exact CW and regular-pair Morse checks for reflection-fixed finite subset spaces of a circle.
Uses only Python's standard library; verifies the prescribed finite cell model and its gradient."""
from fractions import Fraction
from collections import defaultdict

def cells(k):
    return sorted((a,b,j) for a in (0,1) for b in (0,1)
                  for j in range((k-a-b)//2+1)
                  if a+b+2*j<=k and a+b+2*j>=1)

def face_set(cell):
    a,b,j=cell
    return set() if j==0 else {(1,b,j-1),(a,1,j-1),(a,b,j-1)}

def boundary(cell):
    a,b,j=cell
    if j==0: return {}
    faces=[(1,b,j-1)] + [(a,b,j-1)]*(j-1) + [(a,1,j-1)]
    d=defaultdict(int)
    for i,f in enumerate(faces): d[f]+=(-1)**i
    return {f:v for f,v in d.items() if v}

def pairing(k):
    q=k//2
    ans={}
    for j in range(1,q+1): ans[(1,0,j-1)]=(0,0,j)
    for j in range(1,(k-1)//2+1): ans[(1,1,j-1)]=(0,1,j)
    return ans

def rank(matrix):
    a=[[Fraction(x) for x in row] for row in matrix];m=len(a)
    if not m: return 0
    n=len(a[0]);r=0
    for col in range(n):
        pivot=next((i for i in range(r,m) if a[i][col]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        piv=a[r][col]
        for i in range(r+1,m):
            if a[i][col]:
                t=a[i][col]/piv
                for c in range(col,n):a[i][c]-=t*a[r][c]
        r+=1
        if r==m:break
    return r

def check(k):
    cs=cells(k); S=set(cs);d={c:boundary(c) for c in cs}
    for c in cs:
        assert all(f in S and f[2]==c[2]-1 for f in d[c])
        dd=defaultdict(int)
        for f,z in d[c].items():
            for ff,z2 in d[f].items():dd[ff]+=z*z2
        assert all(v==0 for v in dd.values()),('boundary squared',k,c,dd)
    match=pairing(k)
    assert len(match)==len(set(match.values()))
    assert all(low in S and up in S and abs(d[up].get(low,0))==1 for low,up in match.items())
    assert not (set(match)&set(match.values()))
    # Directed Hasse graph; reverse every matched cover relation. Confirm no directed cycles.
    adj={c:[] for c in cs}
    for up in cs:
        for low in (face_set(up) & S):
            if match.get(low)==up:adj[low].append(up)
            else:adj[up].append(low)
    state={c:0 for c in cs}
    def dfs(c):
        state[c]=1
        for w in adj[c]:
            assert state[w]!=1,('gradient cycle',k,c,w)
            if state[w]==0:dfs(w)
        state[c]=2
    for c in cs:
        if state[c]==0:dfs(c)
    critical=[c for c in cs if c not in match and c not in set(match.values())]
    expected=sorted(([(0,1,0),(1,0,0)] if k==1 else
                    [(0,1,0),(1,0,k//2)] if k%2 else
                    [(0,1,0),(1,1,k//2-1)]))
    assert sorted(critical)==expected,(k,critical,expected)
    bydim={i:[c for c in cs if c[2]==i] for i in range(k//2+1)}
    matrices={}
    for i in range(1,k//2+1):
        matrices[i]=[[d[c].get(f,0) for c in bydim[i]] for f in bydim[i-1]]
    ranks={i:rank(mat) for i,mat in matrices.items()}
    betti={i:len(bydim[i])-ranks.get(i,0)-ranks.get(i+1,0) for i in bydim}
    want={0:2 if k<=2 else 1}
    if k>=3:want[(k-1)//2]=1
    assert {i:b for i,b in betti.items() if b}==want,(k,betti,want)
    if k%2:
        q=(k-1)//2
        cap=(0,0,q+1)
        z=boundary(cap) # boundary of the next stage's new cell
        assert all(c in S and c[2]==q for c in z)
        assert z[(1,0,q)]==1
        dz=defaultdict(int)
        for c,v in z.items():
            for cc,vv in d[c].items():dz[cc]+=v*vv
        assert all(v==0 for v in dz.values())
        assert not [c for c in S if c[2]==q+1]
    return f'k={k}: cells={len(cs)}, pairs={len(match)}, critical={sorted(critical)}, betti={betti}'

if __name__=='__main__':
    for k in range(1,17):print(check(k))
    print('REFLECTION_FIXED_SUBSET_CW_MORSE_PASS')
