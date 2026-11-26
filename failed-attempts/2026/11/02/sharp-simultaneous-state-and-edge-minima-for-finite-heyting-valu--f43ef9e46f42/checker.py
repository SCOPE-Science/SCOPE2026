#!/usr/bin/env python3
"""Finite independent checks for the modal-type and optimal-edge formulas.
Public scientific reproducibility script. Requires only Python 3 standard library.
"""
from itertools import product
from collections import defaultdict
from math import prod


def join(a,b,q,kind):
    if kind == 'chain': return max(a,b)
    if kind == 'boolean': return a | b
    raise ValueError(kind)

def meet(a,b,q,kind):
    if kind == 'chain': return min(a,b)
    if kind == 'boolean': return a & b
    raise ValueError(kind)

def impl(a,b,q,kind):
    if kind == 'chain': return q-1 if a <= b else b
    if kind == 'boolean': return ((q-1) ^ a) | b
    raise ValueError(kind)

def bottom(q,kind):return 0

def top(q,kind):return q-1

def all_types(q,k,d):
    t=[tuple(c) for c in product(range(q),repeat=k)]
    out=[t]
    for _ in range(d):
        t=[(c,ws) for c in out[0] for ws in product(range(q),repeat=len(t))]
        out.append(t)
    return out

def truncate(typ,depth,all_levels,kind,q):
    """Semantic projection of a depth-depth type to depth-(depth-1)."""
    if depth==1:return typ[0]
    color,weights=typ
    old=all_levels[depth-1]
    lower=all_levels[depth-2]
    groups={x:i for i,x in enumerate(lower)}
    agg=[0]*len(lower)
    for j,wt in enumerate(weights):
        idx=groups[truncate(old[j],depth-1,all_levels,kind,q)]
        agg[idx]=join(agg[idx],wt,q,kind)
    return (color,tuple(agg))

def projection(typ,from_depth,to_depth,levels,kind,q):
    for h in range(from_depth,to_depth,-1):
        typ=truncate(typ,h,levels,kind,q)
    return typ

def model_check(q,k,d,kind):
    levels=all_types(q,k,d)
    n=[len(t) for t in levels]
    assert n[0]==q**k
    for j in range(1,d+1):assert n[j]==q**k*q**n[j-1]
    highest=levels[d]
    idx={t:i for i,t in enumerate(highest)}
    lower=levels[d-1]
    loweridx={t:i for i,t in enumerate(lower)}
    # Choose one depth-d representative for each depth-(d-1) type.
    section={}
    for i,typ in enumerate(highest):
        t=truncate(typ,d,levels,kind,q)
        if t not in section:section[t]=i
    assert len(section)==len(lower)
    edges=[[] for _ in highest]
    for i,typ in enumerate(highest):
        _,weights=typ
        for j,wt in enumerate(weights):
            if wt:edges[i].append((section[lower[j]],wt))
    observed=[typ[0] for typ in highest]
    for h in range(1,d+1):
        previous={t:i for i,t in enumerate(levels[h-1])}
        nxt=[]
        for i,typ in enumerate(highest):
            agg=[0]*len(levels[h-1])
            for dst,wt in edges[i]:
                z=previous[observed[dst]]
                agg[z]=join(agg[z],wt,q,kind)
            nxt.append((typ[0],tuple(agg)))
        for i,t in enumerate(nxt):
            expected=projection(highest[i],d,h,levels,kind,q)
            assert t==expected,(d,h,i,t,expected)
        observed=nxt
    assert observed==highest
    count=sum(map(len,edges))
    predicted=n[d]*n[d-1]*(q-1)//q
    assert count==predicted
    assert sum(sum(x != 0 for x in typ[1]) for typ in highest)==predicted
    # Formula witnesses: for all depth-d signatures, applying diamond to the
    # Boolean characteristic formula of each (d-1)-type recovers each weight.
    for i,typ in enumerate(highest):
        for j,t in enumerate(lower):
            v=0
            for dst,wt in edges[i]:
                child=projection(highest[dst],d,d-1,levels,kind,q)
                if child==t:v=join(v,wt,q,kind)
            assert v==typ[1][j]
    print(f'UNIVERSAL_OK algebra={kind} values={q} variables={k} depth={d} states={n[d]} edges={count}')


def direct_semantic_law(q,kind):
    # Enumerate weighted branching multisets and valuations for the 1-step
    # aggregation of the box and diamond operators.
    sample_count=0
    for weights in product(range(q),repeat=3):
        for vals in product(range(q),repeat=3):
            grouped=defaultdict(list)
            for r,v in zip(weights,vals):grouped[v].append(r)
            aggregated={v:0 for v in range(q)}
            for v,rs in grouped.items():
                for r in rs:aggregated[v]=join(aggregated[v],r,q,kind)
            # Every possible propositional map on the q truth values.
            for table in product(range(q),repeat=q):
                original_d=0; group_d=0
                original_b=q-1; group_b=q-1
                for r,v in zip(weights,vals):
                    original_d=join(original_d,meet(r,table[v],q,kind),q,kind)
                    original_b=meet(original_b,impl(r,table[v],q,kind),q,kind)
                for v,r in aggregated.items():
                    group_d=join(group_d,meet(r,table[v],q,kind),q,kind)
                    group_b=meet(group_b,impl(r,table[v],q,kind),q,kind)
                assert (original_d,original_b)==(group_d,group_b)
                sample_count+=1
    print(f'AGGREGATION_OK algebra={kind} values={q} exhaustive_tables={sample_count}')


def main():
    direct_semantic_law(3,'chain')
    direct_semantic_law(4,'boolean')
    for args in [(2,1,1,'chain'),(3,1,1,'chain'),(4,1,1,'boolean'),(2,2,1,'chain'),(2,1,2,'chain')]:
        model_check(*args)
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
