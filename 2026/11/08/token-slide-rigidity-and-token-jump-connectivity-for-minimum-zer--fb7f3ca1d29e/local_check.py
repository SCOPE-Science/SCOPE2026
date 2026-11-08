"""Independent, template-driven verification of two forcing-triple closures and slides.
It enumerates only the five symbolic pattern orbits, not all four-subsets.
"""
from collections import Counter

def neighbors(n, x):
    row, col = divmod(x, n)
    return ((row*n + (col-1)%n), (row*n + (col+1)%n), ((1-row)*n+col))

def force(n, seed):
    blue = set(seed)
    for _ in range(2*n):
        to_add = set()
        for v in blue:
            other = set(neighbors(n, v)) - blue
            if len(other) == 1:
                to_add |= other
        if not to_add:
            return blue
        blue |= to_add
    return blue

def orbits(n):
    U=lambda x: x%n
    D=lambda x: n+x%n
    bases=((U(0),U(1),U(2),U(3)),(U(0),U(1),U(2),D(0)),
           (U(0),U(1),U(-2),D(0)),(U(0),U(1),D(0),D(1)),
           (U(1),U(2),D(0),D(1)))
    out=[]
    for base in bases:
        states=set()
        for a in range(2):
            for sign in (-1,1):
                for t in range(n):
                    states.add(frozenset(((((p//n)+a)%2)*n +
                                          (sign*(p%n)+t)%n) for p in base))
        out.append(states)
    return out

def main():
    for n in range(5, 61):
        U=lambda x:x%n
        L=lambda x:n+x%n
        three1={U(0),U(1),U(2)}
        three2={U(0),U(1),L(0)}
        assert force(n,three1)==three1|{L(1)}
        assert force(n,three2)==three2|{U(-1)}
        f=orbits(n)
        assert [len(z) for z in f] == [2*n,4*n,4*n,n,2*n]
        allstates=set().union(*f)
        assert len(allstates)==13*n
        for s in allstates:
            assert len(force(n,s))==2*n
            for v in s:
                for w in neighbors(n,v):
                    if w not in s:
                        candidate=frozenset((s-{v})|{w})
                        if n>=6:
                            assert candidate not in allstates, (n,s,v,w)
        # Every symmetry-orbit representative jumps to a consecutive full-rung pair.
        U=lambda x:x%n
        L=lambda x:n+x%n
        D=frozenset((U(0),U(1),L(0),L(1)))
        A1=frozenset((U(0),U(1),U(3),L(1)))
        representatives=[frozenset((U(0),U(1),U(2),U(3))),
                         frozenset((U(0),U(1),U(2),L(0))),
                         frozenset((U(0),U(1),U(-2),L(0))),
                         D, frozenset((U(1),U(2),L(0),L(1)))]
        witnesses=[[representatives[0],A1,D],
                   [representatives[1],D],
                   [representatives[2],D],
                   [D], [representatives[4],D]]
        for chain in witnesses:
            assert all(x in allstates for x in chain)
            assert all(len(a&b)==3 for a,b in zip(chain,chain[1:]))
        E=frozenset((U(1),U(2),L(0),L(1)))
        nextD=frozenset((U(1),U(2),L(1),L(2)))
        assert E in allstates and nextD in allstates
        assert len(D&E)==len(E&nextD)==3
        if n==5:
            deg=[]
            for family in f:
                dset=set()
                for s in family:
                    d=sum(frozenset((s-{v})|{w}) in allstates for v in s
                          for w in neighbors(n,v) if w not in s)
                    dset.add(d)
                deg.append(dset)
            assert deg==[{2},{1},{2},{0},{0}],deg
        if n in (5,6,7,8,12,20,40,60):
            print(f'n={n}, orbit_sizes={[len(z) for z in f]}, sliding_edges='+
                  ('nonzero exceptional' if n==5 else '0'))
    print('LOCAL_CHECK_OK')

if __name__=='__main__':
    main()
