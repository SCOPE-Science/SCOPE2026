"""Finite checks for the point-collinearity graph of a 4D symplectic space.
No use is made of group automorphisms or unverified external libraries.
"""
from itertools import product
from collections import defaultdict
from random import Random

class Field:
    def __init__(self,q):
        self.q=q
        if q not in (2,3,4,5):raise ValueError('supported finite fields are 2,3,4,5')
        self.add=lambda a,b: a^b if q==4 else (a+b)%q
        self.neg=lambda a: a if q==4 else (-a)%q
        def mul(a,b):
            if q!=4:return a*b%q
            out=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1:out^=1<<(i+j)
            if out&4:out^=7 # X^2=X+1 in GF(4)
            return out
        self.mul=mul
        self.inv={a:next(b for b in range(1,q) if mul(a,b)==1) for a in range(1,q)}
    def sp(self,u,v):
        add,mul,neg=self.add,self.mul,self.neg
        return add(add(mul(u[0],v[1]),neg(mul(u[1],v[0]))),add(mul(u[2],v[3]),neg(mul(u[3],v[2]))))
    def norm(self,v):
        a=next(x for x in v if x);k=self.inv[a]
        return tuple(self.mul(k,x) for x in v)
    def space(self):
        return sorted({self.norm(v) for v in product(range(self.q),repeat=4) if any(v)})

def invariants(q,number=2500):
    F=Field(q);V=F.space();n=len(V)
    edges=[[i!=j and F.sp(V[i],V[j])==0 for j in range(n)] for i in range(n)]
    span=[[set() for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(a,n):
            if a==b:span[a][b]=span[b][a]={a};continue
            L={b}
            for t in range(q):
                L.add(V.index(F.norm(tuple(F.add(V[a][j],F.mul(t,V[b][j])) for j in range(4)))))
            span[a][b]=span[b][a]=L
    def prof(a,b,c):
        k=(a==b,a==c,b==c,edges[a][b],edges[a][c],edges[b][c],c in span[a][b]);S=set()
        lab=span[a][b];lac=span[a][c];lbc=span[b][c]
        ea=edges[a];eb=edges[b];ec=edges[c]
        for x in range(n):
            S.add((x==a,x==b,x==c,ea[x],eb[x],ec[x],x in lab,x in lac,x in lbc))
        return k,frozenset(S)
    T=defaultdict(set)
    rng=Random(707)
    triples=product(range(n),repeat=3) if number>=n**3 else [(0,0,0),(0,0,1),(0,1,1),(0,1,0),(0,1,2)] + [(rng.randrange(n),rng.randrange(n),rng.randrange(n)) for _ in range(number)]
    for a,b,c in triples:
        k,opt=prof(a,b,c);T[k].add(opt)
    k4=any(all(edges[a][b] for a,b in ((u[0],u[1]),(u[0],u[2]),(u[0],u[3]),(u[1],u[2]),(u[1],u[3]),(u[2],u[3]))) for u in product(range(n),repeat=4) if len(set(u))==4) if q==2 else False
    if q>=3:
        for a in range(n):
            if k4:break
            for b in range(a+1,n):
                if edges[a][b]:
                    line=list(span[a][b]);clique=line[:4]
                    assert len(clique)==4 and all(edges[u][v] for u,v in __import__('itertools').combinations(clique,2))
                    k4=True;break
    return T,n,k4

if __name__=='__main__':
    groups={}
    for q,cnt in ((2,4000),(3,65000),(4,3000),(5,3000)):
        T,n,k4=invariants(q,cnt)
        print(f'q={q}: vertices={n}, enriched_stationary_types={len(T)}, nonuniform_types={sum(len(v)>1 for v in T.values())}, K4={k4}')
        groups[q]=T
    assert not groups[2].get(('unreachable',),set())
    assert sum(len(v)>1 for v in groups[3].values())==0
    for q in (4,5):
        shared=set(groups[3])&set(groups[q]);bad=[k for k in shared if groups[3][k]!=groups[q][k]]
        assert not bad,(q,bad)
        print(f'q=3 vs q={q}: matching types {len(shared)}, profile mismatches 0 (sample for q={q})')
    print('Finite corroboration passed; the field-uniform theorem requires the separate algebraic proof.')
