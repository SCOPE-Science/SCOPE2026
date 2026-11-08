"""Independent finite checks of the strong K_{2,n} complex and symmetry traces.
Run: python3 verify.py. Python standard library only.
"""
import itertools
from collections import Counter

def vertices(n):
    return tuple((kind,a,i) for kind in ('x','y') for a in (0,1) for i in range(n))

def true_generators(n):
    # Every total vertex order independently produces a strong gradient.
    graph_vs=[('A',a) for a in (0,1)]+[('B',i) for i in range(n)]
    verts=vertices(n); idx={v:j for j,v in enumerate(verts)}
    gens=set()
    for order in itertools.permutations(graph_vs):
        position={v:j for j,v in enumerate(order)}
        mask=0
        for a in (0,1):
            smaller=[i for i in range(n) if position[('B',i)]<position[('A',a)]]
            if len(smaller)==1:
                mask|=1<<idx[('y',a,smaller[0])]
        for i in range(n):
            smaller=[a for a in (0,1) if position[('A',a)]<position[('B',i)]]
            if len(smaller)==1:
                mask|=1<<idx[('x',smaller[0],i)]
        gens.add(mask)
    return gens

def expected_facets(n):
    idx={v:j for j,v in enumerate(vertices(n))}
    facets=set()
    for a in (0,1):
        facets.add(sum(1<<idx[('x',a,i)] for i in range(n)))
        for i in range(n):
            facets.add((1<<idx[('y',a,i)])+sum(1<<idx[('x',a,j)] for j in range(n) if j!=i))
    for i in range(n):
        for left,right in ((('y',0,i),('y',1,i)),(('y',0,i),('x',1,i)),(('x',0,i),('y',1,i))):
            facets.add((1<<idx[left])|(1<<idx[right]))
    return facets

def allfaces(facets):
    f=set()
    for m in facets:
        s=m
        while s:
            f.add(s)
            s=(s-1)&m
    return f

def permutation_trace(n,faces,swap,sigma):
    vert=vertices(n); idx={v:j for j,v in enumerate(vert)}
    perm=[idx[(kind,a^swap,sigma[i])] for (kind,a,i) in vert]
    trace=0
    for m in faces:
        old=[j for j in range(len(vert)) if m>>j&1]
        new=[perm[j] for j in old]
        if set(new)!=set(old):
            continue
        inversions=sum(new[i]>new[j] for i in range(len(new)) for j in range(i+1,len(new)))
        trace+=(-1 if (len(old)-1+inversions)%2 else 1)
    # In degree one, reduced integral character = 1-Lefschetz, since H_0=Z.
    return 1-trace

def main():
    for n in range(2,7):
        gens=true_generators(n)
        actual=allfaces(gens)
        expected=expected_facets(n)
        want=allfaces(expected)
        assert actual==want,('face mismatch',n,actual^want)
        # Every proposed facet is maximal, and mixed faces are exactly bridge edges.
        for f in expected:
            assert not any(f!=g and f&g==f for g in expected)
        verts=vertices(n)
        mixed=[m for m in actual if any(m>>i&1 and verts[i][1]==0 for i in range(len(verts))) and any(m>>i&1 and verts[i][1]==1 for i in range(len(verts)))]
        assert len(mixed)==3*n and all(m.bit_count()==2 for m in mixed)
        assert len(expected)==5*n+2
        permlist=[tuple(range(n)),tuple(reversed(range(n)))]
        permlist.extend(tuple((i+shift)%n for i in range(n)) for shift in range(1,min(n,4)))
        if n>=4:permlist.append(tuple([1,0]+list(range(2,n))))
        for sigma in set(permlist):
            fixed=sum(sigma[i]==i for i in range(n))
            for swap in (0,1):
                observed=permutation_trace(n,actual,swap,sigma)
                predicted=3*fixed-1 if swap==0 else 1-fixed
                assert observed==predicted,(n,swap,sigma,observed,predicted)
        counts=dict(sorted(Counter(m.bit_count()-1 for m in actual).items()))
        print(f'OK n={n} generators={len(gens)} facets={len(expected)} faces={len(actual)} f_vector={counts} mixed_edges={len(mixed)} character_tests={2*len(set(permlist))}')
    print('ALL_VERIFY_OK')

if __name__=='__main__':main()
