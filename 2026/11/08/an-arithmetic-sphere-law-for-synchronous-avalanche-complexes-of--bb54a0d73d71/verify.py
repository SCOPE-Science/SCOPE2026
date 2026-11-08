#!/usr/bin/env python3
"""Finite independent checks for synchronized multi-cycle avalanche spheres."""
from itertools import product
from math import gcd,lcm
from functools import reduce

def orbit(lengths):
    L=lcm(*lengths)
    states=[]
    holes=[0]*len(lengths)
    for _ in range(L):
        states.append(tuple(holes))
        # Binary parallel chip firing, performed literally on each directed cycle.
        for j,n in enumerate(lengths):
            chips=[int(i!=holes[j]) for i in range(n)]
            firing=[int(x>=1) for x in chips]
            advanced=[chips[i]-firing[i]+firing[(i-1)%n] for i in range(n)]
            assert sum(x==0 for x in advanced)==1
            holes[j]=advanced.index(0)
    return set(states),L

def crt_blocks(lengths):
    d=reduce(gcd,lengths)
    return {tuple(row) for r in range(d) for row in product(*[range(r,n,d) for n in lengths])},d

def betti_gf2(lengths,states):
    N=sum(lengths); start=[sum(lengths[:i]) for i in range(len(lengths))]
    facets=set()
    for h in states:
        zeros=sum(1<<(start[j]+h[j]) for j in range(len(h)))
        facets.add(((1<<N)-1)^zeros)
    faces={0}
    for facet in facets:
        sub=facet
        while sub:
            faces.add(sub);sub=(sub-1)&facet
    dim={}
    for f in faces:dim.setdefault(f.bit_count()-1,[]).append(f)
    ranks={};out={}
    for k in range(max(dim)+1):
        low={m:i for i,m in enumerate(dim[k-1])}
        piv={};count=0
        for face in dim[k]:
            vec=0;f=face
            while f:
                b=f&-f;f^=b;vec^=1<<low[face^b]
            while vec:
                v=vec.bit_length()-1
                if v not in piv:piv[v]=vec;count+=1;break
                vec^=piv[v]
        ranks[k]=count
    for k in range(max(dim)+1):
        b=len(dim[k])-ranks.get(k,0)-ranks.get(k+1,0)
        if b:out[k]=b
    return out,len(faces),len(facets)

def main():
    cases=[(3,4,5),(4,6,10),(6,9,15),(6,10,14),(3,5,7,11),(6,9,15,21)]
    for lengths in cases:
        r=len(lengths)
        reach,L=orbit(lengths)
        blocks,d=crt_blocks(lengths)
        assert reach==blocks
        assert len(reach)==L==d*__import__('math').prod(n//d for n in lengths)
        dimension=sum(lengths)-(r-1)*d-2
        if sum(lengths)<=12:
            actual,faces,facets=betti_gf2(lengths,reach)
            assert actual=={dimension:1},(lengths,actual,dimension)
            print('direct full simplicial homology',lengths,'faces',faces,'facets',facets,'betti',actual)
        print('CRT verified',lengths,'common_gcd',d,'orbit_length',L,'sphere_dimension',dimension)
    print('ALL_MULTICYCLE_CHECKS_OK')
if __name__=='__main__': main()
