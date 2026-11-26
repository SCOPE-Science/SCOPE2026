"""Exact mod-two simplicial boundary-rank check for small even complete graphs."""
from itertools import combinations
from verify import edges,forest_odd_component

def rank2(cols):
    pivots={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p not in pivots:
                pivots[p]=v
                break
            v^=pivots[p]
    return len(pivots)

def compute(n):
    ed=edges(n)
    faces={k:[] for k in range(n-1)}
    for k in range(n-1):
        for F in combinations(range(len(ed)),k):
            mask=sum(1<<e for e in F)
            if forest_odd_component(n,ed,mask):faces[k].append(F)
    ranks={}
    for k in range(1,n-1):
        rows={F:i for i,F in enumerate(faces[k-1])}
        cols=[]
        for F in faces[k]:
            v=0
            for i in range(k):
                G=F[:i]+F[i+1:]
                v^=1<<rows[G]
            cols.append(v)
        ranks[k]=rank2(cols)
    assert len(faces[n-2])>0
    # Last nonempty faces have size n-2; previous loop includes size n-2.
    print('n',n,'faces',[len(faces[k]) for k in range(n-1)],'boundary_ranks',ranks)
    # reduced H_{n-3} dimension = #top faces - rank top boundary.
    k=n-2
    return len(faces[k])-ranks[k]

if __name__=='__main__':
    for n,b in [(4,7),(6,511)]:
        r=compute(n)
        print('top_Betti',r)
        assert r==b
