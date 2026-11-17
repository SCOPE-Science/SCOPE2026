#!/usr/bin/env python3
"""Finite, exhaustive checks for star-fault dissociation complexes; not an infinite proof."""
from itertools import combinations

def check(a,b,t):
    n=a+b
    A=set(range(a)); B=set(range(a,n)); u=0; B0=set(range(a,a+t)); B1=B-B0
    E={(x,y) for x in A for y in B if not (x==u and y in B0)}
    faces={frozenset()}
    for mask in range(1,1<<n):
        S={i for i in range(n) if mask>>i&1}
        deg={v:0 for v in S}
        for x,y in E:
            if x in S and y in S: deg[x]+=1;deg[y]+=1
        if max(deg.values(),default=0)<=1:faces.add(frozenset(S))
    # Independent structural classification using five families.
    model={frozenset()}
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        xa=S&A; yb=S&B
        ok=(not xa or not yb or
             (xa=={u} and len(yb&B1)<=1) or
             (len(xa)==1 and u not in xa and len(yb)==1) or
             (len(xa)==2 and u in xa and len(yb)==1 and yb<=B0))
        if ok:model.add(frozenset(S))
    assert faces==model,(a,b,t,len(faces^model))
    # Pair every 2-face {u,a',b0} with its free opposite edge {a',b0}.
    reduced=faces.copy();pairs=0
    for x in A-{u}:
        for y in B0:
            ed=frozenset({x,y});tri=ed|{u}
            assert tri in reduced and ed in reduced
            cofaces=[z for z in reduced if ed<z]
            assert cofaces==[tri],(a,b,t,ed,cofaces)
            reduced.remove(tri);reduced.remove(ed);pairs+=1
    # The remainder consists of contractible core plus m cross edges.
    core=set()
    for z in reduced:
        if z<=A or z<=B or (u in z and z<={u}|B and len(z&B1)<=1):core.add(z)
    extra=reduced-core
    expected={frozenset({x,y}) for x in A-{u} for y in B1}
    assert extra==expected,(a,b,t,extra^expected)
    # GF(2) reduced Betti numbers of full original complex.
    Fs=[sorted([tuple(sorted(z)) for z in faces if len(z)==k+1]) for k in range(max(map(len,faces),default=0))]
    def rank(mat):
        piv={}
        for x in mat:
            while x:
                j=x.bit_length()-1
                if j not in piv:piv[j]=x;break
                x^=piv[j]
        return len(piv)
    ranks=[]
    for k in range(1,len(Fs)):
        cod={z:i for i,z in enumerate(Fs[k-1])}
        cols=[]
        for face in Fs[k]:
            w=0
            for i in range(len(face)):
                idx=cod[face[:i]+face[i+1:]]
                w^=1<<idx
            cols.append(w)
        ranks.append(rank(cols))
    betti=[]
    for k,seq in enumerate(Fs):
        outgoing=ranks[k-1] if k>0 else 1 # augmentation for reduced H0
        incoming=ranks[k] if k<len(ranks) else 0
        betti.append(len(seq)-outgoing-incoming)
    expected_b1= a*b-1 if t==0 else (a-1)*(b-t)
    assert betti[1] == expected_b1 and all(c==0 for i,c in enumerate(betti) if i!=1),(a,b,t,betti,expected_b1)
    return (a,b,t,len(faces),pairs,betti[1])

if __name__=='__main__':
    data=[]
    for a in range(2,6):
        for b in range(2,6):
            for t in range(b+1):data.append(check(a,b,t))
    print('STAR_DELETION_2_INDEPENDENCE_PASS cases=',len(data))
    for a,b,t,fs,pairs,b1 in data:
        if (a,b) in ((2,3),(3,4),(5,5)):
            print(f'a={a} b={b} t={t} total_faces={fs} free_pairs={pairs} beta1={b1}')
