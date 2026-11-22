"""Independent finite checks for the bridged-cycle homotopy theorem.
All objects and computations use exact integer bitmasks and GF(2) elimination.
The infinite-family theorem requires the separately supplied topological proof.
"""
from itertools import product

def independent_faces(p, q, bridged):
    n = p + q
    edges = [(i,(i+1)%p) for i in range(p)] + [(p+i,p+(i+1)%q) for i in range(q)]
    if bridged:
        edges.append((0,p))
    adjacency = [0]*n
    for u,v in edges:
        adjacency[u] |= 1 << v
        adjacency[v] |= 1 << u
    # Build all independent sets recursively (strictly increasing vertices)
    bydim = [[] for _ in range(n+1)]
    bydim[0] = [0]
    masks=[0]
    for v in range(n):
        additions=[s | (1<<v) for s in masks if not (s & adjacency[v])]
        masks += additions
    for s in masks[1:]:
        bydim[s.bit_count()].append(s)
    return [layer for layer in bydim if layer]

def rank_mod2(columns):
    pivots = {}
    for z in columns:
        while z:
            k = z.bit_length()-1
            if k in pivots:
                z ^= pivots[k]
            else:
                pivots[k] = z
                break
    return len(pivots)

def betti(faces):
    # augmented reduced chain with degree -1 = 1 empty face
    ranks={}
    for k in range(1,len(faces)):
        rows={s:i for i,s in enumerate(faces[k-1])}
        cols=[]
        for mask in faces[k]:
            col=0
            m=mask
            while m:
                bit=m & -m
                m-=bit
                col ^= 1<<rows[mask ^ bit]
            cols.append(col)
        ranks[k]=rank_mod2(cols)
    ranks[0]=1 if faces[1] else 0
    return {k-1:len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in range(1,len(faces))
            if len(faces[k])-ranks.get(k,0)-ranks.get(k+1,0)}

def relative_betti(x, y):
    """Ordinary relative homology H_*(X,Y) over GF(2); Y is nonempty."""
    relative=[]
    for k in range(len(x)):
        yin=set(y[k]) if k<len(y) else set()
        relative.append([mask for mask in x[k] if mask not in yin])
    ranks={}
    for k in range(2,len(relative)):
        rows={s:i for i,s in enumerate(relative[k-1])}
        cols=[]
        for mask in relative[k]:
            col=0; m=mask
            while m:
                bit=m & -m; m-=bit
                i=rows.get(mask^bit)
                if i is not None: col ^= 1<<i
            cols.append(col)
        ranks[k]=rank_mod2(cols)
    ranks[1]=0 if not relative[1] else rank_mod2([0 for _ in relative[1]])
    return {k-1:len(relative[k])-ranks.get(k,0)-ranks.get(k+1,0)
            for k in range(1,len(relative))
            if len(relative[k])-ranks.get(k,0)-ranks.get(k+1,0)}

def expected_relative(p,q):
    a,r=divmod(p,3); b,s=divmod(q,3)
    if r==1 or s==1: return {}
    return {a+b-1+int(r==2)+int(s==2):1}

def expected(p,q,bridged):
    a,r=divmod(p,3); b,s=divmod(q,3)
    d=a+b-1 + int(r==2) + int(s==2)
    if not bridged:
        return {d: (2 if r==0 else 1)*(2 if s==0 else 1)}
    if r==s==2: return {}
    count=3 if r==s==0 else 2 if sorted((r,s))==[0,1] else 1
    return {d:count}

def main():
    total=0
    relative_checks=0
    for p,q in product(range(3,9), repeat=2):
        x=independent_faces(p,q,False)
        y=independent_faces(p,q,True)
        for bridged,faces in ((False,x),(True,y)):
            obs=betti(faces)
            exp=expected(p,q,bridged)
            assert obs==exp, (p,q,bridged,obs,exp)
            total +=1
        obsrel=relative_betti(x,y)
        exprel=expected_relative(p,q)
        assert obsrel==exprel, (p,q,obsrel,exprel)
        relative_checks += 1
    print(f'PASS: {total} exact GF(2) absolute homology checks, all p,q in 3..8, with/without the bridge.')
    print(f'PASS: {relative_checks} exact GF(2) relative homology checks for the bridge inclusion.')
    for p,q in [(3,3),(3,4),(3,5),(4,4),(4,5),(5,5),(6,6),(6,8),(8,8)]:
        A=expected(p,q,False); B=expected(p,q,True)
        print(f'{p:2d},{q:2d}: disjoint {A}; bridged {B}')
    print('The relative cofiber and integral-primitive claims are verified by the written simplicial-pair proof, not by these GF(2) tests.')

if __name__=='__main__':
    main()
