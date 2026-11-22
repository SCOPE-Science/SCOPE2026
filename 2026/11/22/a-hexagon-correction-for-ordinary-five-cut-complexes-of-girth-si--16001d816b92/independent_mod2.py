"""Independent finite mod-two cut-complex chain ranks (Python 3 standard library)."""
from itertools import combinations
from verify import examples, connected
from math import comb


def check(name,a,want):
    n=len(a)
    faces=[[] for _ in range(n-5)]
    verts=range(n)
    for k in range(1,n-4):
        for s in combinations(verts,k):
            complement=tuple(set(verts)-set(s))
            if any(not connected(a,T) for T in combinations(complement,5)):
                faces[k-1].append(s)
    prev=0; ranks=[]
    for d in range(len(faces)):
        if d==0:
            ranks.append(0);continue
        row={s:i for i,s in enumerate(faces[d-1])}
        pivots={}
        for simplex in faces[d]:
            vector=0
            for t in combinations(simplex,d):
                vector^=1<<row[t]
            while vector:
                pos=vector.bit_length()-1
                if pos not in pivots:
                    pivots[pos]=vector
                    break
                vector^=pivots[pos]
        ranks.append(len(pivots))
    betti=[]
    for d,cells in enumerate(faces):
        rank_in=ranks[d+1] if d+1<len(ranks) else 0
        betti.append(len(cells)-ranks[d]-rank_in-(1 if d==0 else 0))
    assert betti == [0]*(n-6)+[want],(name,betti,want)
    print('mod2',name,'ranks',ranks,'betti',betti)

for name,a,c6,b in examples():
    if len(a)<=12:
        from itertools import combinations
        cnt=sum(connected(a,S) for S in combinations(range(len(a)),5))
        want=comb(len(a)-1,4)-cnt+c6
        check(name,a,want)
print('MOD2_INDEPENDENT_PASS')
