"""Exact rational checks for priced-cycle resistance-diameter threshold."""
from fractions import Fraction as Q
from itertools import combinations
from random import Random

def diameter(weights):
    """Cycle with m successive path links followed by the closing link.
    Each pair splits into two disjoint arcs with series resistances.
    A zero-conductance arc is assigned infinite resistance.
    """
    n=len(weights)
    if all(w==0 for w in weights): return None
    out=[]
    for i,j in combinations(range(n),2):
        arcs=(weights[i:j],weights[j:]+weights[:i])
        vals=[]
        for arc in arcs:
            vals.append(sum((1/w for w in arc),Q(0)) if all(w>0 for w in arc) else None)
        if vals[0] is None and vals[1] is None: return None
        if vals[0] is None: r=vals[1]
        elif vals[1] is None: r=vals[0]
        else:r=vals[0]*vals[1]/(vals[0]+vals[1])
        out.append(r)
    return max(out)

def trial():
    rng=Random(36647)
    checks=0
    for m in range(2,15):
        for B in [Q(1),Q(7,5),Q(11,2)]:
            c=m*m
            xmax=B/Q(m*(2*m-1))
            for f in [Q(0),Q(1,13),Q(1,2),Q(10,13),Q(1)]:
                x=f*xmax;y=(B-c*x)/m
                w=[y]*m+[x]
                assert c*x+sum(w[:-1])==B
                assert diameter(w)==Q(m*m)/B,(m,B,f,diameter(w))
                checks+=1
            for f in [Q(14,13),Q(3,2)]:
                x=f*xmax
                if c*x>=B:continue
                y=(B-c*x)/m
                assert diameter([y]*m+[x])>Q(m*m)/B
                checks+=1
            y=B/m
            assert diameter([y]*m+[Q(0)])==Q(m*m)/B
            checks+=1
            for c_hi in [Q(m*m+1),Q(m*m)+Q(7,3)]:
                for _ in range(32):
                    raw=[Q(rng.randrange(1,100)) for _ in range(m+1)]
                    scale=B/(sum(raw[:-1])+c_hi*raw[-1])
                    w=[z*scale for z in raw]
                    assert diameter(w)>=Q(m*m)/B
                    checks+=1
            for c_lo in [Q(m*m-1,2),Q(m*m-1,1)]:
                if c_lo<=0:continue
                x=B/Q(1000*m*m)
                y=(B-c_lo*x)/m
                assert diameter([y]*m+[x])<Q(m*m)/B,(m,c_lo)
                checks+=1
    print('VERIFY_OK exact_rational_tests=',checks)

if __name__=='__main__':trial()
