#!/usr/bin/env python3
"""Exact reproducibility checks for edge-diamond sums (standard library only)."""
from itertools import combinations, product
from collections import Counter
from math import factorial

def partitions(n, lower=1):
    if n == 0:
        yield ()
    for k in range(lower, n + 1):
        for tail in partitions(n-k,k): yield (k,) + tail

def graph(parts):
    labels = tuple(i for i,a in enumerate(parts) for _ in range(a))
    edges = [(i,j) for i in range(len(labels)) for j in range(i+1,len(labels)) if labels[i] != labels[j]]
    return labels,edges

def prediction(parts):
    order=sorted(range(len(parts)),key=lambda j:-parts[j])
    partial=0; q=0
    for j in order:
        q += parts[j]*partial**2
        partial += parts[j]
    counts = Counter(parts)
    m=1
    for count in counts.values(): m*=factorial(count)
    contacts = (1 << (sum(parts)-max(parts))) * m
    return q,contacts

def orientation_scan(parts):
    labels, edges=graph(parts); n=len(labels)
    best=-1; bests=set(); num=0
    for bits in product((0,1), repeat=len(edges)):
        degree = [0]*n
        for bit,(u,v) in zip(bits,edges):
            degree[v if bit else u]+=1
        score=sum(t*t for t in degree)
        if score>best:
            best=score; bests={tuple(degree)};num=1
        elif score==best:
            bests.add(tuple(degree));num+=1
    return best,bests,num

def extreme_points_by_signed_endpoints(parts):
    labels, edges=graph(parts); n=len(labels)
    points = {(0,)*n}
    for i,j in edges:
        nxt=set()
        for p in points:
            for k,sgn in [(i,1),(i,-1),(j,1),(j,-1)]:
                pp=list(p);pp[k]+=sgn;nxt.add(tuple(pp))
        points=nxt
    mx=max(sum(v*v for v in x) for x in points)
    return mx,{p for p in points if sum(v*v for v in p)==mx}

def theoretical_contacts(parts):
    vals=set()
    n=sum(parts)
    start=[];o=0
    for size in parts: start.append(tuple(range(o,o+size)));o+=size
    from itertools import permutations
    for order in permutations(range(len(parts))):
        if any(parts[order[k]]<parts[order[k+1]] for k in range(len(order)-1)):continue
        d=[0]*n;ss=0
        for j in order:
            for i in start[j]:d[i]=ss
            ss+=parts[j]
        nz=[i for i,v in enumerate(d) if v]
        for signs in product((-1,1),repeat=len(nz)):
            v=d.copy()
            for i,sgn in zip(nz,signs):v[i]*=sgn
            vals.add(tuple(v))
    return vals

def main():
    partitions_checked=0
    directed_edges_checked=0
    full_endpoint_checked=0
    for n in range(2,7):
        for parts in partitions(n):
            if len(parts)<2:continue
            pred,ct=prediction(parts)
            scan,vecs,num=orientation_scan(parts)
            assert scan==pred, (parts,scan,pred)
            expected=theoretical_contacts(parts)
            assert len(expected)==ct,(parts,len(expected),ct)
            oriented_contacts=set()
            for vec in vecs:
                inds=[i for i,v in enumerate(vec) if v]
                for signs in product((-1,1),repeat=len(inds)):
                    v=list(vec)
                    for j,sgn in zip(inds,signs):v[j]*=sgn
                    oriented_contacts.add(tuple(v))
            assert oriented_contacts==expected,(parts,'orientation/contact mismatch')
            partitions_checked+=1
            _,edges=graph(parts)
            directed_edges_checked+=(1<<len(edges))
            if n<=4:
                full,contacts=extreme_points_by_signed_endpoints(parts)
                assert full==pred and contacts==expected,(parts,full,pred)
                full_endpoint_checked+=1
    # Check a range of balanced and unbalanced high-parameter predictions without exhaustive enumeration.
    for parts in [(1,2,3),(2,2,2),(1,3,4),(2,3,4),(1,1,1,1,1,1,1), (1,2,2,3)]:
        q,ct=prediction(parts)
        assert len(theoretical_contacts(parts))==ct
        assert all(sum(t*t for t in v)==q for v in theoretical_contacts(parts))
    print('OK', 'partitions_exactly_exhausted',partitions_checked,'orientation_assignments',directed_edges_checked,'signed_endpoint_instances',full_endpoint_checked)

if __name__=='__main__': main()
