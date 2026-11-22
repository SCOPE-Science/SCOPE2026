#!/usr/bin/env python3
"""Standalone exhaustive check of two invariant reconstruction on seven-point blow-ups.
Uses two independent descriptions: (A) Frobenius fixed subsets/cycles;
(B) direct permutation of divisor classes and bitangent pairs.
"""
from itertools import combinations, permutations
from math import comb
import csv
import sys

N=7

def partitions(n, minimum=1):
    if n==0:
        yield ()
    else:
        for k in range(minimum,n+1):
            for rest in partitions(n-k,k):
                yield (k,)+rest

def standard_perm(partition):
    p=list(range(N)); offset=0
    for cycle_length in partition:
        for j in range(cycle_length):
            p[offset+j]=offset+(j+1)%cycle_length
        offset+=cycle_length
    assert offset==N
    return tuple(p)

def iterate(p,k):
    out=tuple(range(N))
    for _ in range(k): out=tuple(p[i] for i in out)
    return out

def cycle_lengths(p):
    seen=set();lens=[]
    for x in range(N):
        if x in seen:continue
        z=x;k=0
        while z not in seen:
            seen.add(z);z=p[z];k+=1
        lens.append(k)
    return lens

def pairwise_bitangent_indices():
    # The 56 exceptional curves are paired by the Geiser involution into
    # 28 bitangents: seven (E_i,cubic_i) and 21 (line_ij,conic_ij).
    return [('one', (i,)) for i in range(N)]+[('two',(i,j)) for i,j in combinations(range(N),2)]

def conic_bundle_classes():
    # D=aH - sum(b_i E_i), D^2=0, -K.D=2 and 0<=b_i<=2.
    # Classes are all nef (checked against the 56 (-1)-curves below).
    out=set()
    for a in range(1,6):
        for b in __import__('itertools').product(range(3),repeat=N):
            if sum(b)!=3*a-2 or sum(x*x for x in b)!=a*a:continue
            out.add((a,b))
    return out

def exceptional_classes():
    out=set()
    for i in range(N):
        b=[0]*N;b[i]=-1;out.add((0,tuple(b)))
    for ij in combinations(range(N),2):
        b=[int(i in ij) for i in range(N)];out.add((1,tuple(b)))
    for ij in combinations(range(N),2):
        b=[int(i not in ij) for i in range(N)];out.add((2,tuple(b)))
    for i in range(N):
        b=[1]*N;b[i]=2;out.add((3,tuple(b)))
    return out

def intersection(x,y):
    return x[0]*y[0]-sum(a*b for a,b in zip(x[1],y[1]))

def fixed_bitangents(p):
    return sum(all(p[i] in idx for i in idx) for _,idx in pairwise_bitangent_indices())

def fixed_conic_classes(p, conics):
    return sum(all(b[i]==b[p[i]] for i in range(N)) for a,b in conics)

def formula(p):
    cycles=cycle_lengths(p)
    f,t,u=(cycles.count(j) for j in (1,2,3))
    bit=f+comb(f,2)+t
    con=2*f+2*(comb(f,3)+f*t+u)+f*(f-1)
    return bit,con

def main(outpath=None):
    conics=conic_bundle_classes();exceptionals=exceptional_classes()
    assert len(conics)==126 and len(exceptionals)==56
    assert all(intersection(c,e)>=0 for c in conics for e in exceptionals)
    assert all(c[0]**2==sum(b*b for b in c[1]) and 3*c[0]-sum(c[1])==2 for c in conics)
    assert len(pairwise_bitangent_indices())==28
    classes=sorted(partitions(N)); rows=[];keys=set();bkeys=set();ckeys=set()
    for part in classes:
        p=standard_perm(part)
        direct=(fixed_bitangents(p),fixed_conic_classes(p,conics))
        algebraic=formula(p)
        assert direct==algebraic,(part,direct,algebraic)
        assert direct not in keys,(part,direct)
        keys.add(direct);bkeys.add(direct[0]);ckeys.add(direct[1])
        # All extension counts are fixed counts of powers of this same action.
        for k in range(1,22):
            pk=iterate(p,k)
            assert (fixed_bitangents(pk),fixed_conic_classes(pk,conics))==formula(pk)
        rows.append({'partition':','.join(map(str,part)),'bitangents':direct[0],
                     'conic_bundles':direct[1], 'rational_base_points':cycle_lengths(p).count(1)})
    assert len(keys)==15 and len(bkeys)==10 and len(ckeys)==11
    if outpath:
        with open(outpath,'w',newline='',encoding='utf-8') as fp:
            writer=csv.DictWriter(fp,fieldnames=['partition','bitangents','conic_bundles','rational_base_points'],lineterminator='\n');writer.writeheader();writer.writerows(rows)
    print('CHECKED_56_EXCEPTIONAL_126_CONIC_CLASSES_28_BITANGENTS_15_UNIQUE_PAIRS_B10_C11')
    for row in rows: print(row)
    return rows
if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else None)
