#!/usr/bin/env python3
"""Exact finite verification for Latin-complement 2-complexes (order four).
Python 3 with sympy. All group reductions are exact Tietze transformations.
"""
from itertools import permutations, product
from collections import Counter
from sympy import zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form

Q=4
PERMS=list(permutations(range(Q)))

def original(kind):
    return tuple(tuple((i+j)%Q if kind=='cyclic' else (i^j) for j in range(Q)) for i in range(Q))

def transformed(L,p,q,r):
    S=[[0]*Q for _ in range(Q)]
    for i in range(Q):
        for j in range(Q):
            S[p[i]][q[j]]=r[L[i][j]]
    return tuple(map(tuple,S))

def enumerate_all():
    answer=set()
    def addrow(rows,used):
        if len(rows)==Q:
            answer.add(tuple(rows))
            return
        for p in PERMS:
            if all(not (used[j]>>p[j])&1 for j in range(Q)):
                addrow(rows+[p],[used[j]|(1<<p[j]) for j in range(Q)])
    addrow([], [0]*Q)
    return answer

def faces(L):
    E=sorted((a,b) for a in range(3*Q) for b in range(a+1,3*Q) if a//Q!=b//Q)
    F=sorted((i,Q+j,2*Q+k) for i,j,k in product(range(Q),repeat=3) if k!=L[i][j])
    return E,F

def smith_data(E,F):
    edgeids={e:i for i,e in enumerate(E)}
    D=zeros(len(E),len(F))
    for j,(a,b,c) in enumerate(F):
        D[edgeids[(a,b)],j]=1
        D[edgeids[(a,c)],j]=-1
        D[edgeids[(b,c)],j]=1
    snf=smith_normal_form(D,domain=ZZ)
    diag=Counter(abs(int(snf[i,i])) for i in range(min(snf.rows,snf.cols)) if snf[i,i])
    rank=sum(diag.values())
    return dict(sorted(diag.items())),rank, len(F)-rank, len(E)-(3*Q-1)-rank

def freereduce(w,cyclic=True):
    st=[]
    for x in w:
        if st and st[-1]==-x: st.pop()
        else: st.append(x)
    if cyclic:
        while len(st)>1 and st[0]==-st[-1]: st=st[1:-1]
    return st

def inverse(w):
    return [-z for z in reversed(w)]

def tietze_presentation(E,F):
    # Deterministic union-find spanning tree; every omitted tree edge is null.
    par=list(range(3*Q))
    def root(i):
        while par[i]!=i: i=par[i]
        return i
    tree=[]
    for u,v in E:
        ru,rv=root(u),root(v)
        if ru!=rv:
            par[ru]=rv
            tree.append((u,v))
    assert len(tree)==3*Q-1
    ids={e:i+1 for i,e in enumerate(e for e in E if e not in tree)}
    def path(u,v):
        e=tuple(sorted((u,v)))
        t=ids.get(e)
        return [] if t is None else ([t] if u<v else [-t])
    rel=[freereduce(path(a,b)+path(b,c)+path(c,a)) for a,b,c in F]
    alive=set(ids.values()); trace=[]
    while True:
        rel=[r for r in rel if r]
        moves=[]
        for j,r in enumerate(rel):
            # Occurrence exactly once allows elimination of the generator.
            for letter in r:
                if sum(abs(z)==abs(letter) for z in r)==1:
                    moves.append((len(r),sum(abs(z)==abs(letter) for w in rel for z in w),j,letter))
        if not moves: break
        length,frequency,j,letter=min(moves)
        r=rel.pop(j)
        k=r.index(letter)
        rest=r[k+1:]+r[:k]
        rhs=inverse(rest) if letter>0 else rest
        g=abs(letter)
        assert g in alive
        alive.remove(g)
        trace.append({'step':len(trace)+1,'generator':g,'eliminating_relator':r,'positive_generator_substitution':rhs,'remaining_relators':len(rel)})
        nextrel=[]
        for word in rel:
            new=[]
            for z in word:
                if abs(z)!=g: new.append(z)
                elif z>0: new.extend(rhs if letter>0 else inverse(rhs))
                else: new.extend(inverse(rhs) if letter>0 else rhs)
            nextrel.append(freereduce(new))
        rel=nextrel
    return {'initial_generators':len(ids),'initial_relators':len(F),'elimination_steps':len(trace),'survivors':sorted(alive),'survivor_relators':rel,'trace':trace}

def main():
    all_squares=enumerate_all()
    assert len(all_squares)==576
    orbits={kind:{transformed(original(kind),p,q,r) for p in PERMS for q in PERMS for r in PERMS} for kind in ('cyclic','klein')}
    print('Latin squares enumerated:',len(all_squares))
    print('Isotopy orbit sizes:',{k:len(v) for k,v in orbits.items()})
    assert orbits['cyclic'].isdisjoint(orbits['klein'])
    assert orbits['cyclic']|orbits['klein']==all_squares
    for kind in ('cyclic','klein'):
        L=original(kind)
        E,F=faces(L)
        diag,r,b2,b1=smith_data(E,F)
        pres=tietze_presentation(E,F)
        print(kind,'faces (f0,f1,f2):',(3*Q,len(E),len(F)))
        print(kind,'Smith nonzero factors:',diag,'rank:',r,'Betti H2:',b2,'free H1:',b1)
        print(kind,'Tietze initial generators and relators:',pres['initial_generators'],pres['initial_relators'])
        print(kind,'Tietze steps:',pres['elimination_steps'],'survivors:',pres['survivors'],'relators:',pres['survivor_relators'])
        assert b2==11 and b1==0
        if kind=='cyclic':
            assert diag=={1:37} and pres['survivors']==[] and not pres['survivor_relators']
        else:
            assert diag=={1:36,2:1} and len(pres['survivors'])==1 and pres['survivor_relators']
            g=pres['survivors'][0]
            assert set(tuple(t) for t in pres['survivor_relators'])<= {(g,g),(-g,-g)}
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
