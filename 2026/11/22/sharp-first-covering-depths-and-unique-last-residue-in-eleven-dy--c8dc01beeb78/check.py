#!/usr/bin/env python3
"""Reproducible finite covering-depth proof for Stern pairs modulo powers of two.

Python >=3.9, standard library.  Run: python check.py
This computes every primitive pair, exact shortest depths and least indices.
For a modulus m=2^k, state (a,b) has children L(a,b)=(a,a+b)
and R(a,b)=(a+b,b), with every coordinate reduced modulo m.
"""
from array import array
import json

RADII = (2,5,8,11,14,18,20,23,26,30,33)
LEAST_INDICES = (2,19,184,1291,10708,140455,676171,5416267,43348660,575329636,4920978067)


def stern_pair(n):
    a,b=0,1
    for digit in bin(n)[2:]:
        if digit=='0': b=a+b
        else: a=a+b
    return a,b


def census(k):
    m=1<<k
    mask=m-1
    distance=bytearray(m*m)  # d+1; zero marks unvisited
    first=array('Q',[0])*(m*m)  # lexicographically first shortest binary word
    distance[1]=1
    queue=array('I',[1])
    count=[1]
    head=0
    while head<len(queue):
        v=queue[head]
        head+=1
        a,b=v>>k,v&mask
        c=(a+b)&mask
        newdepth=distance[v]+1
        prefix=first[v]*2
        for u,word in (((a<<k)|c,prefix),((c<<k)|b,prefix+1)):
            if distance[u]:
                continue
            distance[u]=newdepth
            first[u]=word
            queue.append(u)
            if len(count)<newdepth: count.append(0)
            count[newdepth-1]+=1
    assert len(queue)==3*m*m//4
    assert sum(count)==len(queue)
    # Full-state test proves that every primitive residue pair and ONLY
    # those pairs was reached. For a two-power modulus, primitivity is
    # equivalent to not having both entries even.
    for a in range(m):
        base=a<<k
        for b in range(m):
            assert bool(distance[base|b])==bool((a|b)&1)
    radius=len(count)-1
    final=[v for v in queue if distance[v]==radius+1]
    assert len(final)==count[-1]
    farthest=[(v>>k,v&mask) for v in final]
    target=final[0]
    minimum_index=int(first[target])
    assert 2**(radius-1)<=minimum_index<2**radius
    assert tuple(x%m for x in stern_pair(minimum_index))==farthest[0]
    return dict(exponent=k,modulus=m,number_primitive_pairs=len(queue),
                covering_depth=radius,last_layer_size=len(final),
                last_pair=farthest[0],least_index_for_last_pair=minimum_index,
                distance_histogram=count)


def independent_layer_search(k):
    # Independent recurrence for the SET of points, no BFS visited array.
    m=1<<k
    reached={(0,1)}
    frontier={(0,1)}
    for r in range(1,60):
        frontier={(a,(a+b)%m) for a,b in frontier}|{((a+b)%m,b) for a,b in frontier}
        reached |= frontier
        if len(reached)==3*m*m//4:
            return r
    raise AssertionError('not covered')


def independent_prefix_search(k,least_n):
    # Different algorithm: evaluate the integer Stern sequence by a
    # bottom-up recurrence at EVERY index up through the target.
    m=1<<k
    s=[0,1]
    for n in range(2,least_n+2):
        s.append(s[n//2] if n%2==0 else s[n//2]+s[n//2+1])
    target=(m-1,m-1) if k>1 else (1,0)
    assert (s[least_n]%m,s[least_n+1]%m)==target
    assert all((s[n]%m,s[n+1]%m)!=target for n in range(least_n))


def main():
    rows=[]
    for k in range(1,12):
        row=census(k)
        assert row['covering_depth']==RADII[k-1]
        assert row['least_index_for_last_pair']==LEAST_INDICES[k-1]
        assert row['last_layer_size']==1
        assert row['last_pair']==((1,0) if k==1 else (2**k-1,2**k-1))
        if k<=7:
            assert independent_layer_search(k)==row['covering_depth']
        if k<=6:
            independent_prefix_search(k,row['least_index_for_last_pair'])
        rows.append(row)
        print('k=%2d states=%7d depth=%2d missing_previous=%d least_index=%d' %
              (k,row['number_primitive_pairs'],row['covering_depth'],
               row['last_layer_size'],row['least_index_for_last_pair']),flush=True)
    with open('census.json','w',encoding='utf-8') as f:
        json.dump({'theorem':'first eleven dyadic Stern-pair covering depths',
                   'rows':rows},f,ensure_ascii=False,separators=(',',':'))
        f.write('\n')
    print('EXACT_CENSUS_AND_INDEPENDENT_CROSSCHECKS_PASSED')

if __name__=='__main__': main()
