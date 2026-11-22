"""Direct F_2 simplicial homology for small edge-open-packing complexes.
No symbolic topological assumptions are used. Run: python3 check_topology.py
"""
from itertools import combinations
from math import comb


def rank_f2(columns):
    basis = {}
    for v in columns:
        while v:
            pivot = v.bit_length()-1
            if pivot not in basis:
                basis[pivot] = v
                break
            v ^= basis[pivot]
    return len(basis)


def check(m,n,t):
    edges=[(i,j) for i in range(m) for j in range(n) if not (i==j and i<t)]
    q=len(edges)
    assert q<=12
    bad=[[False]*q for _ in range(q)]
    for a,(i,j) in enumerate(edges):
        for b,(k,l) in enumerate(edges):
            if a>=b: continue
            for c,(x,y) in enumerate(edges):
                if c in (a,b): continue
                e1={('L',i),('R',j)}; e2={('L',k),('R',l)}
                if (('L',x) in e1 and ('R',y) in e2) or (('L',x) in e2 and ('R',y) in e1):
                    bad[a][b]=bad[b][a]=True
                    break
    faces={0: [()]}
    for s in range(1,q+1):
        faces[s]=[f for f in combinations(range(q),s) if all(not bad[a][b] for a,b in combinations(f,2))]
        if not faces[s]: break
    ranks={}
    for s in range(2,len(faces)):
        rows={face:i for i,face in enumerate(faces[s-1])}
        cols=[]
        for face in faces[s]:
            bit=0
            for j in range(s): bit ^= 1<<rows[face[:j]+face[j+1:]]
            cols.append(bit)
        ranks[s]=rank_f2(cols)
    bettis={}
    for s in range(1,len(faces)):
        bettis[s-1]=len(faces[s])-ranks.get(s,0)-ranks.get(s+1,0)
    beta=(m-1)*(n-1)-t+comb(t,2)
    assert bettis.pop(0)==1
    assert bettis.pop(1)==beta
    assert all(x==0 for x in bettis.values()),bettis
    return q,beta

if __name__=='__main__':
    cases=[(3,3,t) for t in range(4)]+[(3,4,t) for t in (2,3)]
    for args in cases:
        print(*args,check(*args))
    print('PASS: all finite simplicial homology groups match a wedge of circles in',len(cases),'cases')
