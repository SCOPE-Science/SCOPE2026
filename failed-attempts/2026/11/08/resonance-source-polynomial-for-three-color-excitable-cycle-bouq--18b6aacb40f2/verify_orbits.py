"""Exhaustive three-step Greenberg-Hastings checks for bouquets of cycles."""
from itertools import product
from math import prod
from collections import defaultdict


def build_graph(lengths, decorations=()):
    # A bouquet has hub 0 and cycles with pairwise disjoint other vertices.
    adj=[set()]
    cycles=[]
    for length in lengths:
        assert length >= 3
        cyc=[0]
        for _ in range(length-1):
            cyc.append(len(adj)); adj.append(set())
        for x,y in zip(cyc,cyc[1:]+cyc[:1]):
            adj[x].add(y); adj[y].add(x)
        cycles.append(cyc)
    # Decorations (parent vertex, length): attach a path of given length.
    for parent,length in decorations:
        assert 0 <= parent < len(adj) and length>=1
        for _ in range(length):
            child=len(adj); adj.append({parent});adj[parent].add(child);parent=child
    return tuple(tuple(sorted(row)) for row in adj)


def gh_step(x,adj):
    return tuple((1 if any(x[w]==1 for w in adj[v]) else 0)
                 if val==0 else (val+1)%3
                 for v,val in enumerate(x))


def formula(lengths):
    b=[2*(L//3)+1 for L in lengths]
    off=[c-(2 if L%3==0 else 0) for c,L in zip(b,lengths)]
    return 3*(prod(b)-prod(off))


def source_count(x,lengths):
    h=x[0]; cursor=1; total=0
    for L in lengths:
        left=cursor; right=cursor+L-2
        total += int(x[left]==(h+1)%3 or x[right]==(h+1)%3)
        cursor+=L-1
    return total

def expected_histogram(lengths):
    d={0:1}
    for L in lengths:
        b=2*(L//3)+1; a=2 if L%3==0 else 0
        e=defaultdict(int)
        for j,v in d.items():
            e[j]+=(b-a)*v
            e[j+1]+=a*v
        d=dict(e)
    return {j:3*v for j,v in d.items() if j>0 and v}

def brute_count(adj,lengths):
    hist=defaultdict(int)
    for x in product(range(3),repeat=len(adj)):
        y=gh_step(x,adj)
        z=gh_step(y,adj)
        w=gh_step(z,adj)
        if w==x and y!=x: hist[source_count(x,lengths)]+=1
    return dict(hist)

cases=[([3],()),([4],()),([6],()),([3,3],()),([3,4],()),
       ([3,6],()),([4,6],()),([6,6],()),([3,3,3],()),
       ([3,4,5],()),([3,3,6],()),([3,3,3,3],()),
       ([3,3],((0,1),)),([3,3],((1,2),)),
       ([3,4],((0,2),(2,1)))]
checks=0; states=0
for lengths,decorations in cases:
    adj=build_graph(lengths,decorations)
    expected=formula(lengths)
    hist=brute_count(adj,lengths)
    found=sum(hist.values())
    assert found==expected, (lengths,decorations,found,expected)
    assert hist==expected_histogram(lengths),(lengths,hist,expected_histogram(lengths))
    assert found%3==0
    checks+=1; states+=3**len(adj)
    print('PASS',lengths,decorations,'vertices=',len(adj),'primitive3=',found,'source_hist=',hist)
print('PASS exhaustive_cases=',checks,'states_checked=',states)
