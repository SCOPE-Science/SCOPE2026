#!/usr/bin/env python3
"""Check atomic-extension catalogues of finite Latin hypercube incidence structures.

The computation only checks small examples. The unrestricted theorem is proved
separately by a symbolic completion case analysis.
"""
from itertools import product
from collections import defaultdict

def hypercube(n,q,operation='cyclic'):
    def result(vals):
        if operation=='xor4':
            assert q==4
            v=0
            for x in vals:v ^= x
            return v
        return sum(vals)%q
    return lambda xs:result(xs)

def ptype(n,q,operation, tup):
    sortpos=[[] for _ in range(n+1)]
    for i,v in enumerate(tup):sortpos[v//q].append(i)
    sortseq=tuple(v//q for v in tup)
    eq=tuple((i,j) for i in range(len(tup)) for j in range(i+1,len(tup)) if tup[i]==tup[j])
    rel=[]
    if all(sortpos):
        for indices in product(*sortpos):
            if hypercube(n,q,operation)([tup[indices[j]]%q for j in range(1,n+1)])==tup[indices[0]]%q:
                rel.append(indices)
    return sortseq,eq,tuple(rel)

def catalog(n,q,operation):
    U=range((n+1)*q)
    D=defaultdict(set)
    for base in product(U,repeat=n+1):
        t=ptype(n,q,operation,base)
        for x in U:D[t].add(ptype(n,q,operation,base+(x,)))
    return {k:frozenset(v) for k,v in D.items()}

def intercalates(q,op):
    L=[[hypercube(2,q,op)((i,j)) for j in range(q)] for i in range(q)]
    return sum(L[a][c]==L[b][d] and L[a][d]==L[b][c]
               for a in range(q) for b in range(a+1,q)
               for c in range(q) for d in range(c+1,q))

def main():
    check2={}
    for q,operation in [(2,'cyclic'),(3,'cyclic'),(4,'cyclic'),(4,'xor4'),(5,'cyclic'),(6,'cyclic')]:
        d=catalog(2,q,operation);name=f'{operation}-{q}';check2[name]=d
        print(f'arity=2 {name}: fixed-types={len(d)}, extensions={sum(map(len,d.values()))}')
    for a,b in [('cyclic-4','xor4-4'),('cyclic-4','cyclic-5'),('cyclic-5','cyclic-6')]:
        assert check2[a]==check2[b]
        print(f'arity=2 {a} vs {b}: IDENTICAL exact extension catalogues')
    check3={}
    for op in ('cyclic','xor4'):
        d=catalog(3,4,op);check3[op]=d
        print(f'arity=3 {op}-4: fixed-types={len(d)}, extensions={sum(map(len,d.values()))}')
    assert check3['cyclic']==check3['xor4']
    print('arity=3 cyclic-4 vs xor4-4: IDENTICAL exact extension catalogues')
    for q,op in [(4,'cyclic'),(4,'xor4'),(5,'cyclic'),(6,'cyclic')]:
        print(f'arity=2 {op}-{q}: 2x2 intercalates={intercalates(q,op)}')
    assert intercalates(5,'cyclic')==0 and intercalates(6,'cyclic')>0
    assert intercalates(4,'cyclic')==4 and intercalates(4,'xor4')==12
    print('PASS: local types agree and sharp one-variable-beyond-boundary intercalate witness validated.')
if __name__=='__main__':main()
