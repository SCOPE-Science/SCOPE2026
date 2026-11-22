"""Independent forward exact-rational path/overlap-signature DP."""
from collections import defaultdict
from fractions import Fraction
from itertools import product

WORDS = [''.join(p) for p in product('01', repeat=3)]
EXPECT = {
 (7,0,0): Fraction(1136203,4365900),
 (6,1,0): Fraction(18241309,52390800),
 (5,2,0): Fraction(140831,635040),
 (6,0,1): Fraction(18647,136080),
 (4,3,0): Fraction(41,3920),
 (5,1,1): Fraction(93,7840),
 (4,2,1): Fraction(41,3920),
}

def weight(a,b):
    x,y=WORDS[a],WORDS[b]
    if x[1:] == y[:2]: return 2
    if x[-1] == y[0]: return 1
    return 0

def main():
    initial = tuple((i,) for i in range(8))
    states = {(initial,(0,0,0)): Fraction(1)}
    layers = [len(states)]
    for _ in range(7):
        nxt = defaultdict(Fraction)
        for (paths,sig),prob in states.items():
            val = max(weight(a[-1],b[0]) for i,a in enumerate(paths)
                      for j,b in enumerate(paths) if i!=j)
            ties = [(i,j) for i,a in enumerate(paths) for j,b in enumerate(paths)
                    if i!=j and weight(a[-1],b[0])==val]
            for i,j in ties:
                remaining = [p for z,p in enumerate(paths) if z not in (i,j)]
                child = tuple(sorted(remaining+[paths[i]+paths[j]]))
                new_sig=list(sig);new_sig[2-val]+=1
                nxt[child,tuple(new_sig)] += prob/len(ties)
        states = dict(nxt)
        assert sum(states.values())==1
        layers.append(len(states))
    signatures = defaultdict(Fraction)
    for (paths,sig),p in states.items():
        assert len(paths)==1
        assert len(paths[0])==8 and len(set(paths[0]))==8
        signatures[sig]+=p
    assert dict(signatures)==EXPECT
    lengths=defaultdict(Fraction)
    for sig,p in signatures.items():
        n2,n1,n0=sig
        assert n2+n1+n0==7
        lengths[24-2*n2-n1]+=p
    assert set(lengths)=={10,11,12,13,14}
    assert sum(lengths.values())==1
    assert sum(n*p for n,p in lengths.items())==Fraction(167269939,14968800)
    print('PATH_FORWARD_EXHAUSTIVE_OK')
    print('state_counts_by_level',layers)
    print('signatures',sorted(signatures.items(),reverse=True))
    print('length_distribution',sorted(lengths.items()))
    print('mean',sum(n*p for n,p in lengths.items()))

if __name__=='__main__':main()
