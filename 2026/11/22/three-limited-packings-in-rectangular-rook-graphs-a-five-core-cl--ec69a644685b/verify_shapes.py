"""Independent component classification for three-limited rook-board subsets."""
from collections import Counter

def check(m,n,mask):
    selected={(i//n, i%n) for i in range(m*n) if mask>>i&1}
    deg_r=[sum(r==i for r,c in selected) for i in range(m)]
    deg_c=[sum(c==j for r,c in selected) for j in range(n)]
    return all(deg_r[r]+deg_c[c]-((r,c) in selected)<=3 for r in range(m) for c in range(n))

def signature(m,n,mask):
    edges={(i//n, i%n) for i in range(m*n) if mask>>i&1}
    components=[]
    while edges:
        e=next(iter(edges)); rows={e[0]}; cols={e[1]}
        while True:
            rr=rows|{r for r,c in edges if c in cols}
            cc=cols|{c for r,c in edges if r in rows}
            if rr==rows and cc==cols:break
            rows,cols=rr,cc
        cur={(r,c) for (r,c) in edges if r in rows and c in cols}
        edges-=cur
        # vertex degree multiset fully determines these small component kinds
        degrees=sorted([sum(r==rr for r,c in cur) for rr in rows] + [sum(c==cc for r,c in cur) for cc in cols])
        shape=(len(cur),tuple(degrees))
        if shape == (1,(1,1)): name='matching-edge'
        elif shape == (2,(1,1,2)): name='two-star'
        elif shape == (3,(1,1,1,3)): name='three-star'
        elif shape == (3,(1,1,2,2)): name='P4'
        elif shape == (4,(1,1,2,2,2)): name='P5'
        elif shape == (4,(2,2,2,2)): name='C4'
        else: return 'invalid-component'
        if name=='two-star':
            # distinguish which shore contains the center
            name='row-two-star' if any(sum(r==rr for r,c in cur)==2 for rr in rows) else 'col-two-star'
        components.append(name)
    exceptional=[a for a in components if a not in ('matching-edge','row-two-star','col-two-star')]
    if not exceptional:
        stars={a for a in components if a!='matching-edge'}
        return 'star-forest' if len(stars)<=1 else 'invalid-mixed-centers'
    if len(exceptional)!=1 or any(a!='matching-edge' for a in components if a!=exceptional[0]):return 'invalid-mixed'
    if exceptional[0]=='three-star' and len(components)>1:return 'invalid-three-star-plus'
    return exceptional[0]

if __name__=='__main__':
    for m,n in [(2,3),(3,3),(3,4),(3,5),(4,4)]:
        typ=Counter()
        for mask in range(1<<(m*n)):
            if check(m,n,mask): typ[signature(m,n,mask)]+=1
        assert all(not k.startswith('invalid') for k in typ)
        print(f'{m}x{n} valid={sum(typ.values())} classes={dict(sorted(typ.items()))}')
