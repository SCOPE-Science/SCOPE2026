"""Independent labelled graph enumeration of asynchronous majority fixation on two-hub books."""
from fractions import Fraction
from functools import lru_cache
from math import comb


def run(s):
    N=s+2
    # Graph from its edge list; leaf labels do not occur in the analytical formula.
    nbr=[set() for _ in range(N)]
    for u,v in [(0,1)]+[(h,l) for h in (0,1) for l in range(2,N)]:
        nbr[u].add(v);nbr[v].add(u)
    @lru_cache(None)
    def p(state):
        if state == 0: return Fraction(0)
        if state == (1<<N)-1: return Fraction(1)
        moves=[]
        for v in range(N):
            ones=sum(bool(state & (1<<w)) for w in nbr[v]);deg=len(nbr[v]);bit=bool(state&(1<<v))
            new=(ones*2>deg) if 2*ones!=deg else bit
            if new!=bit: moves.append(state ^ (1<<v))
        if not moves:raise AssertionError(('non-consensus fixed',s,state))
        return sum((p(next_state) for next_state in moves),Fraction())/len(moves)
    for mask in range(1<<N):
        x=bool(mask&1);y=bool(mask&2);j=sum(bool(mask&(1<<v)) for v in range(2,N))
        r=s//2
        if x and y:
            expect=Fraction(1) if j>=r else Fraction((s-r+2)*(s-r+1),(s-j+2)*(s-j+1))
        elif (not x) and (not y):
            expect=Fraction(0) if s-j>=r else 1-Fraction((s-r+2)*(s-r+1),(j+2)*(j+1))
        else:
            expect=Fraction(1) if 2*j>s else Fraction(0) if 2*j<s else Fraction(1,2)
        got=p(mask)
        assert got==expect,(s,mask,got,expect)
    return 1<<N,p(3)

if __name__=='__main__':
    total=0
    for s in range(1,11):
        n,q=run(s);total+=n
        print(f's={s}, labelled states={n}, P(hubs=11, leaves=00...0)={q}')
    print(f'PASS: all {total} labelled states on books with 1 through 10 leaves.')
