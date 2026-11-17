"""Independent exhaustive small-instance check for two-chord non-matching complexes.
Run with Python 3.10+; uses only the standard library.
"""
import itertools
from collections import Counter

def perfect_matchings(t, x, y):
    n=2*t
    edges=[tuple(sorted((i,(i+1)%n))) for i in range(n)]+[x,y]
    matchings=[]
    for inds in itertools.combinations(range(len(edges)),t):
        verts=[v for i in inds for v in edges[i]]
        if len(set(verts))==n:
            matchings.append(frozenset(inds))
    return matchings

def geometric_case(t,x,y):
    even_x=(x[0]-x[1])%2==0
    even_y=(y[0]-y[1])%2==0
    if not even_x and not even_y:return 'old_sphere'
    if even_x and even_y:
        if x[0]%2==y[0]%2:return 'cone'
        ends=sorted([(z% (2*t), ('x' if z in x else 'y')) for z in x+y])
        if len({z for z,_ in ends})!=4:return 'cone'
        if [a for _,a in ends] in (['x','y','x','y'],['y','x','y','x']):return 'new_sphere'
    return 'cone'

def nerve_f_vector(t,x,y,matchings):
    # Nerve of the dual facets: a matching subfamily is a face iff
    # its union omits at least one of the graph's 2t+2 edges.
    hist=Counter()
    m=2*t+2
    for k in range(1,len(matchings)+1):
        for subset in itertools.combinations(matchings,k):
            if len(set().union(*subset))<m:hist[k]+=1
    return tuple(hist[d] for d in range(1,len(matchings)+1))

def run():
    cases=Counter()
    for t in (3,4,5):
        n=2*t
        chords=[(i,j) for i in range(n) for j in range(i+1,n)
                if j-i not in (1,n-1)]
        for x,y in itertools.combinations(chords,2):
            matchings=perfect_matchings(t,x,y)
            label=geometric_case(t,x,y)
            f=nerve_f_vector(t,x,y,matchings)
            chord_x_index=2*t;chord_y_index=2*t+1
            used_x=any(chord_x_index in p for p in matchings)
            used_y=any(chord_y_index in p for p in matchings)
            if label=='cone':
                assert not(used_x and used_y), (t,x,y,'no cone vertex')
            elif label=='new_sphere':
                assert len(matchings)==3 and f==(3,3,0), (t,x,y,f)
            else:
                assert used_x and used_y
                assert (len(matchings)==4 and f==(4,6,4,0)) or (
                    len(matchings)==5 and f==(5,10,8,1,0)),(t,x,y,f)
            cases[(t,label)]+=1
    for t in (3,4,5):
        for label in ('old_sphere','new_sphere','cone'):
            print(f't={t} {label}: {cases[t,label]} pairs')
    print('TWO_CHORD_NONMATCHING_NERVE_ALL_PAIR_PASS')

if __name__=='__main__':run()
