"""Exact finite checks of signed Lefschetz traces and modular homology.

The all-n theorem is proved separately by transfer matrices and the
published homotopy classification; this program checks small cases only.
"""
from math import gcd
from collections import defaultdict


def dimension(n):
    t, a = divmod(n, 4)
    return 2*t-1 if a <= 1 else (2*t if a == 2 else 2*t+1)


def target(n, kind, a):
    d = dimension(n)
    e = (-1)**(d+1)
    if kind == 'r':
        q = gcd(n, a)
        return e * (3 if q%4 == 0 else (-1 if q%4 == 2 else 1))
    L = ((n+1)//2 if n%2 else (n//2+(a%2 == 0)))
    return e * (-1 if L%4 in (2,3) else 1)


def perm(n, kind, a):
    return [(i+a)%n if kind == 'r' else (a-i)%n for i in range(n)]


def valid(n, mask):
    return all(not ((mask>>i)&1 and (mask>>((i+1)%n))&1
                    and (mask>>((i+2)%n))&1) for i in range(n))


def signed_euler(n, p):
    """Trace of reduced action on augmented chains by fixed-face orbits."""
    seen=set(); orbits=[]
    for i in range(n):
        if i not in seen:
            o=[];j=i
            while j not in seen:
                o.append(j);seen.add(j);j=p[j]
            orbits.append(o)
    total=0
    for b in range(1<<len(orbits)):
        mask=0
        for i,o in enumerate(orbits):
            if b>>i&1:
                for v in o: mask|=1<<v
        if valid(n, mask):
            # (-1)^size times sign of restricted permutation = (-1)^#orbits
            total+=(-1)**b.bit_count()
    return -total


def rank_mod(columns, prime):
    """Sparse column reduction; integer entries reduced modulo prime."""
    pivots={}
    for col in columns:
        v={k:(x%prime) for k,x in col.items() if x%prime}
        while v:
            row=max(v)
            if row not in pivots:
                mult=pow(v[row],-1,prime)
                pivots[row]={r:(x*mult)%prime for r,x in v.items()}
                break
            f=v[row]
            for r,x in pivots[row].items():
                nv=(v.get(r,0)-f*x)%prime
                if nv: v[r]=nv
                else: v.pop(r,None)
    return len(pivots)


def homology_ranks(n,prime):
    layers=defaultdict(list)
    for mask in range(1,1<<n):
        if valid(n,mask):layers[mask.bit_count()-1].append(mask)
    ix={d:{v:i for i,v in enumerate(vs)} for d,vs in layers.items()}
    rank={}
    for d,faces in layers.items():
        if d==0:rank[d]=1;continue # reduced C0 -> C-1 augmentation, nonempty
        col=[]
        for face in faces:
            verts=[k for k in range(n) if face>>k&1]
            col.append({ix[d-1][face^(1<<k)]:(-1)**j for j,k in enumerate(verts)})
        rank[d]=rank_mod(col,prime)
    return {d:len(faces)-rank[d]-rank.get(d+1,0) for d,faces in layers.items() if len(faces)-rank[d]-rank.get(d+1,0)}


def main():
    actions=0
    for n in range(4,19):
        for kind in 'rs':
            for a in range(n):
                L=signed_euler(n,perm(n,kind,a))
                actual=(-1)**dimension(n)*L
                expected=target(n,kind,a)
                assert actual==expected, (n,kind,a,actual,expected)
                actions+=1
        print(f'characters n={n:2d}:  {2*n} actions OK; top_rank={target(n,"r",0)}')
    print(f'CHARACTER_CHECK_PASS actions={actions}')
    for p in (101,103):
        for n in range(4,15):
            res=homology_ranks(n,p)
            want={dimension(n):(3 if n%4==0 else 1)}
            assert res==want, (n,p,res,want)
            print(f'homology n={n:2d} mod={p}: {res} OK')
    print('ALL_FINITE_CHECKS_PASS')

if __name__=='__main__':main()
