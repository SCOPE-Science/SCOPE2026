#!/usr/bin/env python3
"""Exact integer orbit-chain and cancellation checker for a seven-vertex dihedral action.

Usage: python verify.py certificate.json
Option --generate writes a fresh certificate.json in the current directory.
Only Python standard library is required. All cell counts and differentials are rebuilt.
"""
import json
import sys
from collections import defaultdict
from math import gcd

N = 7
FULL = (1 << N) - 1

def group_maps():
    result = []
    for k in range(N):
        result.append(tuple((i+k) % N for i in range(N)))
        result.append(tuple((k-i) % N for i in range(N)))
    return [tuple(sum(1 << p[i] for i in range(N) if (m >> i) & 1)
                  for m in range(FULL+1)) for p in result]

def full_chains():
    layers = [set() for _ in range(N-1)]
    layers[0] = {(m,) for m in range(1,FULL)}
    for k in range(1,N-1):
        for ch in layers[k-1]:
            remaining = FULL ^ ch[-1]
            extra = remaining
            while extra:
                larger = ch[-1] | extra
                if larger != FULL:
                    layers[k].add(ch+(larger,))
                extra = (extra-1) & remaining
    return layers

def build():
    perms = group_maps()
    C = full_chains()
    def canon(ch):
        return min(tuple(p[x] for x in ch) for p in perms)
    T = [sorted({canon(ch) for ch in layer}) for layer in C]
    ids = [{ch:i for i,ch in enumerate(layer)} for layer in T]
    boundaries = [None]
    for k in range(1,N-1):
        mat = {}
        for c,ch in enumerate(T[k]):
            bd = defaultdict(int)
            for j in range(k+1):
                face = ch[:j]+ch[j+1:]
                bd[ids[k-1][canon(face)]] += (-1)**j
            mat[c] = {r:v for r,v in bd.items() if v}
        boundaries.append(mat)
    fixed = [[sum(all(p[x] == x for x in ch) for ch in layer) for layer in C]
             for p in perms]
    burnside = [sum(z[k] for z in fixed)//len(perms) for k in range(N-1)]
    assert burnside == list(map(len,T))
    assert list(map(len,C)) == [126,1806,8400,16800,15120,5040]
    assert burnside == [16,147,612,1200,1080,360]
    assert all(fixed[2*k] == [0]*6 for k in range(1,N))
    assert all(fixed[2*k+1] == [14,36,24,0,0,0] for k in range(N))
    check_chain(boundaries)
    return boundaries,burnside,list(map(len,C))

def check_chain(D):
    for k in range(2,len(D)):
        for col,bd in D[k].items():
            dd = defaultdict(int)
            for middle,a in bd.items():
                for low,b in D[k-1][middle].items():
                    dd[low] += a*b
            assert all(v == 0 for v in dd.values()), ('d^2 nonzero', k, col)

def rank_mod(cols,p):
    basis={}
    for c in sorted(cols):
        x = {r:v%p for r,v in cols[c].items() if v%p}
        while x:
            row=max(x)
            if row not in basis:
                inv=pow(x[row],-1,p)
                basis[row]={z:(v*inv)%p for z,v in x.items()}
                break
            q=x[row]
            for z,v in basis[row].items():
                nextv=(x.get(z,0)-q*v)%p
                if nextv:x[z]=nextv
                else:x.pop(z,None)
    return len(basis)

def choose_pivot(D):
    best=None
    for k in range(len(D)-1,0,-1):
        byrow=defaultdict(list)
        for c,vec in D[k].items():
            for r,v in vec.items():byrow[r].append((c,v))
        for row,items in byrow.items():
            for c,v in items:
                if abs(v)!=1:continue
                cost=(len(items)-1)*(len(D[k][c])-1)
                if best is None or cost<best[0]:best=(cost,k,row,c,v)
                if cost==0:break
            if best is not None and best[0]==0:break
        if best is not None and best[0]==0:break
    return best[1:] if best else None

def cancel(D,active,k,row,col,piv):
    assert col in active[k] and row in active[k-1]
    assert D[k][col].get(row) == piv and abs(piv)==1
    pivot_column = D[k].pop(col)
    for other,vec in D[k].items():
        if row not in vec:continue
        mult=vec[row] // piv
        for r,v in pivot_column.items():
            result=vec.get(r,0)-mult*v
            if result:vec[r]=result
            else:vec.pop(r,None)
        assert row not in vec
    if k>1: D[k-1].pop(row)
    if k+1<len(D):
        for vec in D[k+1].values():vec.pop(col,None)
    active[k].remove(col)
    active[k-1].remove(row)

def verify(path,generate=False):
    D,fvec,fullvec = build()
    initial_ranks={str(p):[0]+[rank_mod(D[k],p) for k in range(1,N-1)]+[0]
                   for p in (2,3,7,11)}
    if generate: pivots=[]
    else:
        cert=json.load(open(path,encoding='utf-8'))
        pivots=cert['pivots']
    active=[set(range(m)) for m in fvec]
    counts=[0]*len(fvec)
    if generate:
        while True:
            pivot=choose_pivot(D)
            if pivot is None:break
            pivots.append(pivot)
            k,r,c,p=pivot
            cancel(D,active,k,r,c,p)
            counts[k]+=1
    else:
        for k,r,c,p in pivots:
            cancel(D,active,k,r,c,p)
            counts[k]+=1
        assert choose_pivot(D) is None
    check_chain(D)
    remainder = [len(a) for a in active]
    assert counts == [0,15,132,480,719,359],counts
    assert remainder == [1,0,0,1,2,1],remainder
    assert len(D[4])==2 and len(D[5])==1
    r=next(iter(active[3])); c1,c2=sorted(active[4]); c5=next(iter(active[5]))
    a=D[4][c1].get(r,0); b=D[4][c2].get(r,0)
    u=D[5][c5].get(c1,0); v=D[5][c5].get(c2,0)
    order7=gcd(a,b)
    assert order7==7,(a,b)
    ker=(b//order7,-a//order7)
    assert ker[0]*v == ker[1]*u and (ker[0] or ker[1])
    if ker[0]: assert u%ker[0]==0; multiplier=u//ker[0]
    else: assert v%ker[1]==0; multiplier=v//ker[1]
    assert abs(multiplier)==2,(a,b,u,v)
    result = {
        'object':'proper Boolean poset of 7 labels modulo dihedral action, also cyclohedron boundary quotient',
        'full_chain_counts':fullvec,'orbit_cell_counts':fvec,
        'modular_boundary_ranks':initial_ranks,
        'unit_cancellation_counts':counts,'remaining_cell_counts':remainder,
        'remaining_cell_ids':list(map(lambda x:sorted(x),active)),
        'remaining_d4':[a,b],'remaining_d5':[u,v],
        'nonzero_reduced_homology':{'3':'Z/7','4':'Z/2'},
        'pivots':pivots,
    }
    if generate:
        with open(path,'w',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,separators=(',',':'))
    else:
        assert result == cert, 'certificate mismatch'
    print('VERIFY_OK')
    print('orbit cells:',fvec)
    print('modular ranks:',initial_ranks)
    print('unit cancellations:',counts)
    print('remaining differential d4:',[a,b],'d5:',[u,v])
    print('homology: H0=Z H3=Z/7 H4=Z/2; all other H=0')

if __name__=='__main__':
    if len(sys.argv)!=3 or sys.argv[1] not in ('--generate','--verify'):
        raise SystemExit('Usage: python verify.py --generate|--verify certificate.json')
    verify(sys.argv[2],generate=(sys.argv[1]=='--generate'))
