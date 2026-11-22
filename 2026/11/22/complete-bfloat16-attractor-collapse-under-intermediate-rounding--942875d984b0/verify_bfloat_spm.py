#!/usr/bin/env python3
"""Exact complete-state certificate for two rounding semantics of a logistic self-parameterized interval map."""
from fractions import Fraction as Q
from bisect import bisect_left
from collections import deque
from hashlib import sha256
import struct

LAST = 0x3f80
MAX = 0x7f80

def bit_value(code):
    # Explicit binary16-width bfloat16 encoding, including subnormals.
    if code < 128:
        return Q(code, 2**133)
    e = (code >> 7) - 127
    m = 128 + (code & 127)
    return Q(m * 2**max(e-7, 0), 2**max(7-e, 0))

VALUES = tuple(bit_value(code) for code in range(MAX))
assert len(VALUES) == 32640 and VALUES[LAST] == 1
assert all(VALUES[i] < VALUES[i+1] for i in range(MAX-1))

def rounded_by_neighbors(x):
    if x < 0 or x > 4: raise ValueError('value outside proof domain')
    k = bisect_left(VALUES, x)
    if k == 0: return 0
    lo = k-1
    if k == MAX: return lo
    dl=x-VALUES[lo]
    dr=VALUES[k]-x
    return lo if dl < dr or (dl == dr and (lo&1)==0) else k

def pow2(e):
    return Q(1<<e,1) if e >= 0 else Q(1,1<<(-e))

def even_int(y):
    a,b = divmod(y.numerator, y.denominator)
    return a+(2*b > y.denominator or (2*b == y.denominator and a%2 == 1))

def rounded_by_exponent(x):
    # Independent exact rounding: determine binade, round scaled integer.
    if x == 0:return 0
    if x < 0 or x > 4: raise ValueError('outside proof domain')
    if x < pow2(-126):
        return even_int(x*pow2(133))
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<pow2(e):e-=1
    assert pow2(e)<=x<pow2(e+1)
    mant=even_int(x/pow2(e-7))
    if mant==256: return (e+128)<<7
    return ((e+127)<<7)+(mant-128)

def maps(rounder):
    # The published self-parameterized logistic map has B=0.975, M=0.01.
    # With C=1 the real transfer function is (197/50 + x/25)*x*(1-x).
    A=[];B=[]
    for i in range(LAST+1):
        x=VALUES[i]
        gain=Q(197,50)+x/25
        kernel=x*(1-x)
        A.append(rounder(gain*kernel))
        B.append(rounder(VALUES[rounder(gain)]*VALUES[rounder(kernel)]))
    return A,B

def classify_walk(edges):
    n=len(edges); marks=[0]*n; labels=[-1]*n; cycles=[]; basins=[]; depth=[-1]*n
    for s in range(n):
        if marks[s]:continue
        trail=[];seen={};v=s
        while not marks[v] and v not in seen:
            seen[v]=len(trail);trail.append(v);v=edges[v]
        if v in seen:
            cyc=trail[seen[v]:]
            id_=len(cycles);cycles.append(tuple(sorted(cyc)));basins.append(len(cyc))
            for w in cyc: labels[w]=id_;marks[w]=1;depth[w]=0
            trail=trail[:seen[v]]
        else:id_=labels[v]
        for w in reversed(trail):
            labels[w]=id_;basins[id_]+=1;marks[w]=1;depth[w]=1+depth[edges[w]]
    return {tuple(c): (basins[i],max(depth[k] for k in range(n) if labels[k]==i)) for i,c in enumerate(cycles)}, labels, depth

def classify_prune(edges):
    n=len(edges);indeg=[0]*n
    for v in edges: indeg[v]+=1
    q=deque(i for i,d in enumerate(indeg) if d==0);removed=[]
    while q:
        i=q.popleft();removed.append(i);j=edges[i];indeg[j]-=1
        if indeg[j]==0:q.append(j)
    labels=[-1]*n; cycles=[]; depths=[-1]*n
    for i in range(n):
        if indeg[i]>0 and labels[i]<0:
            cur=i; cyc=[]
            while labels[cur]<0:
                labels[cur]=len(cycles);depths[cur]=0;cyc.append(cur);cur=edges[cur]
            cycles.append(tuple(sorted(cyc)))
    for i in reversed(removed):
        labels[i]=labels[edges[i]];depths[i]=depths[edges[i]]+1
    counts=[0]*len(cycles); maxdep=[0]*len(cycles)
    for i,k in enumerate(labels):counts[k]+=1;maxdep[k]=max(maxdep[k],depths[i])
    return {cyc:(counts[k],maxdep[k]) for k,cyc in enumerate(cycles)}, labels,depths

def show(label, edges):
    a,labels,dep=classify_walk(edges)
    b,_,dep2=classify_prune(edges)
    assert a==b and dep==dep2
    out=[]
    for cy,(basin,maxdep) in sorted(a.items(),key=lambda z:(len(z[0]),z[0])):
        out.append((len(cy),basin,maxdep,[f'{v:04x}' for v in cy]))
    print(label,'cycle_specs:',out)
    assert sum(x[1] for x in out)==LAST+1
    return out,labels,dep

if __name__=='__main__':
    a,b=maps(rounded_by_neighbors)
    c,d=maps(rounded_by_exponent)
    assert a==c and b==d
    assert max(a)<=LAST and max(b)<=LAST
    o1, labels1,dep1=show('one-final-rounding',a)
    o2, labels2,dep2=show('gain-and-kernel-rounding',b)
    assert [(p,q) for p,q,*_ in o1]==[(1,2),(5,2026),(22,14229)]
    assert [(p,q) for p,q,*_ in o2]==[(1,2),(20,16255)]
    assert sum(v!=w for v,w in zip(a,b))==2205
    assert set(a[i] for i in range(LAST+1)).issubset(set(range(LAST+1)))
    assert set(b[i] for i in range(LAST+1)).issubset(set(range(LAST+1)))
    import json
    report={'state_count':LAST+1,'differing_successors':sum(x!=y for x,y in zip(a,b)),
       'A':o1,'B':o2,
       'sha256_successors_A':sha256(b''.join(i.to_bytes(2,'little') for i in a)).hexdigest(),
       'sha256_successors_B':sha256(b''.join(i.to_bytes(2,'little') for i in b)).hexdigest()}
    print('CERTIFICATE_JSON',json.dumps(report,separators=(',',':')))
    print('PASS exact dual-rounder, dual-decomposition and complete 16257-state graph')
