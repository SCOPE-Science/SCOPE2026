"""Exact finite graph/SIR algebra certificate for the two seed objectives.
Requires Python 3 and SymPy (tested with SymPy 1.x).
Run: python check_symbolic.py
"""
import itertools
from functools import lru_cache
import sympy as sp

b=sp.Symbol('b', positive=True)
# Complete representatives of connected simple graphs on at most four vertices.
CATALOG={
 1:[tuple()],
 2:[((0,1),)],
 3:[((0,1),(0,2)),((0,1),(0,2),(1,2))],
 4:[((0,1),(0,2),(0,3)),((0,1),(1,2),(2,3)),
    ((0,1),(0,2),(0,3),(1,2)),((0,1),(1,2),(2,3),(3,0)),
    ((0,1),(0,2),(0,3),(1,2),(1,3)),
    ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))]
}

def values(n,edges,seed):
    adj=[0]*n
    for i,j in edges: adj[i]|=1<<j;adj[j]|=1<<i
    full=(1<<n)-1
    @lru_cache(None)
    def F(S,I,h):
        if not I: return sp.Integer(n-S.bit_count()),sp.Integer(h)
        moves=[(sp.Integer(1),S,I^(1<<u),h)
               for u in range(n) if I>>u&1]
        for u in range(n):
            if (S>>u)&1:
                k=(adj[u]&I).bit_count()
                if k:moves.append((k*b,S^(1<<u),I|(1<<u),max(h,I.bit_count()+1)))
        W=sum(z[0] for z in moves)
        A=B=sp.Integer(0)
        for rate,s,i,peak in moves:
            a,c=F(s,i,peak)
            A+=rate*a; B+=rate*c
        return sp.cancel(A/W),sp.cancel(B/W)
    return F(full^(1<<seed),1<<seed,1)

def nonnegative_coefficients(q):
    num,den=map(sp.expand,sp.fraction(sp.cancel(q)))
    def nonneg(f):return all(x>=0 for x in sp.Poly(f,b).all_coeffs())
    return nonneg(num) and nonneg(den)

def main():
    comparisons=0;distinguished=0
    for n,graphs in CATALOG.items():
        for edges in graphs:
            vals=[values(n,edges,s) for s in range(n)]
            for i,j in itertools.combinations(range(n),2):
                dF=sp.cancel(vals[i][0]-vals[j][0]);dH=sp.cancel(vals[i][1]-vals[j][1])
                if (dF==0)!=(dH==0):raise AssertionError(('different tie sets',n,edges,i,j))
                if dF:
                    distinguished+=1
                    if not nonnegative_coefficients(sp.cancel(dF*dH)):
                        raise AssertionError(('nonpositive or unresolved product',n,edges,i,j,sp.factor(dF*dH)))
                comparisons+=1
        print('connected order',n,':',len(graphs),'isomorphism classes checked')
    print('PASS: 11 connected classes,',comparisons,'root pairs,',distinguished,'strict pairs; all beta>0')

if __name__=='__main__':main()
