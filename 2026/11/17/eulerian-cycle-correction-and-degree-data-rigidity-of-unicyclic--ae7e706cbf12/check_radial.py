"""Reproduce exact radial-shell data for unicyclic graphical zonotopes.

No third-party packages needed. Run: python check_radial.py
For a graph with n vertices and n edges, the output exponent is 4 times
its squared Euclidean vertex radius in the centered root-coordinate model.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def multiply(p, q):
    ans = Counter()
    for a, va in p.items():
        for b, vb in q.items():
            ans[a+b] += va*vb
    return {e: v for e, v in ans.items() if v}


def F(d):
    assert d >= 0
    p = Counter()
    for j in range(d+1):
        p[(d-2*j)**2] += Fraction(comb(d,j), 2**d)
    return dict(p)


def B(d):
    assert d >= 2
    p = Counter()
    for j in range(d-1):
        t = d-2-2*j
        weight = Fraction(comb(d-2,j), 2**(d-1))
        p[(t+2)**2] += weight
        p[t*t] -= weight
    return {e: v for e, v in p.items() if v}


def predicted(edges, cycle):
    n = max(max(e) for e in edges)+1
    assert len(edges) == n
    degrees = [0]*n
    for u,v in edges:
        degrees[u]+=1
        degrees[v]+=1
    cycle = set(cycle)
    p0={0:Fraction(1)}; pc={0:Fraction(1)}; px={0:Fraction(1)}
    for v,d in enumerate(degrees):
        p0=multiply(p0,F(d))
        pc=multiply(pc, B(d) if v in cycle else F(d))
        px=multiply(px, F(d-2) if v in cycle else F(d))
    ans=Counter()
    for k,v in p0.items():ans[k]+=2**n*v
    for k,v in pc.items():ans[k]+=(-1)**len(cycle)*2**n*v
    for k,v in px.items():ans[k]-=2**(n-len(cycle)+1)*v
    assert all(v.denominator==1 and v>=0 for v in ans.values())
    assert sum(ans.values())==2**n-2**(n-len(cycle)+1)
    return {k:int(v) for k,v in ans.items() if v}


def direct(edges, cycle):
    # Independent enumeration of directed edges, without Fourier coefficients.
    n=max(max(e) for e in edges)+1
    cycle_edges=[(min(i,(i+1)%len(cycle)),max(i,(i+1)%len(cycle))) for i in range(len(cycle))]
    locations={e:i for i,e in enumerate(edges)}
    ans=Counter()
    for signs in product((-1,1),repeat=len(edges)):
        cyclic_signs=[]
        for i,e in enumerate(cycle_edges):
            cyclic_signs.append(signs[locations[e]]*(1 if i < (i+1)%len(cycle) else -1))
        # Exactly the two directed-cycle assignments are not zonotope vertices.
        if len(set(cyclic_signs))==1:
            continue
        totals=[0]*n
        for (u,v),s in zip(edges,signs):
            totals[u]+=s; totals[v]-=s
        ans[sum(w*w for w in totals)]+=1
    return dict(ans)


def graph(c, parents):
    edges={tuple(sorted((i,(i+1)%c))) for i in range(c)}
    for j,parent in enumerate(parents):
        assert 0<=parent<c+j
        edges.add((parent,c+j))
    return sorted(edges)


def main():
    cases=0;orientations=0
    # For every cycle size 3..7 test hundreds of rooted-forest attachments.
    for c in range(3,8):
        for k in range(0,min(4,10-c)+1):
            # Enumerate all attachment choices up to this size (bounded by 320/case).
            count=0
            for parents in product(*[range(c+j) for j in range(k)]):
                edges=graph(c,parents)
                got=direct(edges,list(range(c)))
                want=predicted(edges,list(range(c)))
                assert got==want,(c,parents,got,want)
                cases+=1;orientations+=sum(got.values());count+=1
                if count>=320:break
    a=graph(4,[0,1]);b=graph(4,[0,2])
    assert a!=b
    pa=predicted(a,range(4));pb=predicted(b,range(4))
    assert pa==pb=={4:2,8:16,12:14,16:16,20:6,28:2}
    print('UNICYCLIC_RADIAL_PASS', 'graph_cases='+str(cases),
          'vertices_enumerated='+str(orientations),
          'iso_shell_pairs=1',
          'example='+str(dict(sorted(pa.items()))))

if __name__=='__main__':main()
