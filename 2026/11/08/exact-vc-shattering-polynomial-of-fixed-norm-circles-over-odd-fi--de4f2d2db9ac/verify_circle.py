#!/usr/bin/env python3
"""Exact trace verifier for fixed nonzero quadratic circles over finite fields.

For prime fields, tests both norms 1 and 2; for selected extension fields,
tests norm 1. Never treats a finite check as a universal proof.
"""
from itertools import combinations
from math import comb

class Field:
    def __init__(self,p,polynomial):
        self.p=p; self.mod=polynomial; self.k=len(polynomial)-1; self.q=p**self.k
        assert polynomial[-1]==1
        self.vec=[tuple((a//(p**j))%p for j in range(self.k)) for a in range(self.q)]
        self.invvec={v:a for a,v in enumerate(self.vec)}
        self.add=[[self.invvec[tuple((x+y)%p for x,y in zip(a,b))] for b in self.vec] for a in self.vec]
        self.neg=[self.invvec[tuple((-x)%p for x in a)] for a in self.vec]
        self.sub=[[self.add[a][self.neg[b]] for b in range(self.q)] for a in range(self.q)]
        self.mul=[]
        for a in self.vec:
            row=[]
            for b in self.vec:
                prod=[0]*(2*self.k-1)
                for i,ai in enumerate(a):
                    for j,bj in enumerate(b):prod[i+j]=(prod[i+j]+ai*bj)%p
                for deg in range(len(prod)-1,self.k-1,-1):
                    coefficient=prod[deg]
                    for j in range(self.k):prod[deg-self.k+j]=(prod[deg-self.k+j]-coefficient*polynomial[j])%p
                row.append(self.invvec[tuple(prod[:self.k])])
            self.mul.append(row)
        for a in range(1,self.q):assert len(set(self.mul[a]))==self.q
        self.chi=[0]+[(-1) for _ in range(self.q-1)]
        for a in range(1,self.q):self.chi[self.mul[a][a]]=1

def verify(F,t):
    q=F.q
    pairs=[(x,y) for x in range(q) for y in range(q)]
    idx={v:i for i,v in enumerate(pairs)}
    norm=lambda v:F.add[F.mul[v[0]][v[0]]][F.mul[v[1]][v[1]]]
    t=int(t)
    C=[v for v in pairs if norm(v)==t]
    S=q-F.chi[F.neg[1]]
    assert len(C)==S,(q,S,len(C))
    diffs={v:norm(v) for v in pairs}
    # Membership circles around arbitrary centers using translation invariance.
    def incident(p,c):return diffs[(F.sub[p[0]][c[0]],F.sub[p[1]][c[1]])]==t
    center_masks=[]
    for c in pairs:
        m=0
        for j,p in enumerate(C):
            if incident(p,c):m|=1<<j
        center_masks.append(m)
    centered_triples=0
    for i,j,k in combinations(range(S),3):
        traces={((m>>i)&1)|(((m>>j)&1)<<1)|(((m>>k)&1)<<2) for m in center_masks}
        seen=(len(traces)==8)
        expected=(C[i]!=(F.neg[C[j][0]],F.neg[C[j][1]]) and
                  C[i]!=(F.neg[C[k][0]],F.neg[C[k][1]]) and
                  C[j]!=(F.neg[C[k][0]],F.neg[C[k][1]]))
        assert seen==expected,(q,t,i,j,k,seen,expected)
        centered_triples+=int(seen)
    assert centered_triples==8*comb(S//2,3) if S>=6 else centered_triples==0
    # Exact check every nonzero displacement's two-point trace, and common-center count.
    shattering_displacements=0
    for v in pairs[1:]:
        centers=[c for c in pairs if incident((0,0),c) and incident(v,c)]
        traces={(int(incident((0,0),c)) | (int(incident(v,c))<<1)) for c in pairs}
        assert (len(traces)==4)==bool(centers),(q,t,v)
        assert len(centers)<=2
        shattering_displacements+=bool(centers)
    assert shattering_displacements==S*S//2,(q,shattering_displacements,S*S//2)
    # In any 4-point shattered support, a three-point subset must be
    # contained in two distinct circles, impossible for a nondegenerate conic.
    print('PASS',f'q={q}',f't={t}',f'S={S}',f'centered_triples={centered_triples}',
          f'displacements={shattering_displacements}',
          f's2={q*q*shattering_displacements//2}',f's3={q*q*centered_triples}')

if __name__=='__main__':
    for p in (3,5,7,11,13,17):
        f=Field(p,[0,1])
        for t in (1,2):verify(f,t)
    for p,pol in ((3,[1,0,1]), (5,[2,0,1]), (3,[1,2,0,1])):
        verify(Field(p,pol),1)
    print('ALL_FINITE_FIELD_CIRCLE_TRACES_PASS 15 fields/radii')
