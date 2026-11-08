"""Independent absorbing-chain computation of edge-addition effect on polarized two-hub systems."""
from fractions import Fraction
from functools import lru_cache


def win_probability(s, edge):
    N=s+2
    adj=[[0]*N for _ in range(N)]
    for i in (0,1):
        for leaf in range(2,N): adj[i][leaf]=adj[leaf][i]=1
    if edge:adj[0][1]=adj[1][0]=1
    @lru_cache(None)
    def win(mask):
        if mask==0:return Fraction(0)
        if mask==(1<<N)-1:return Fraction(1)
        changes=[]
        for i in range(N):
            ones=sum(adj[i][j] for j in range(N) if mask&(1<<j))
            degree=sum(adj[i]);old=(mask>>i)&1
            new=1 if 2*ones>degree else 0 if 2*ones<degree else old
            if old!=new:changes.append(mask^(1<<i))
        if not changes:
            # For the polarized start all reachable absorbing states are consensus.
            raise AssertionError(('nonconsensus',s,edge,mask))
        return sum((win(nxt) for nxt in changes),Fraction())/len(changes)
    return win(3)

if __name__=='__main__':
    for s in range(1,12):
        P=win_probability(s,True);Q=win_probability(s,False)
        expected=Fraction(s+3,(s+2)*(s+1)) if s%2 else Fraction(0)
        assert P-Q==expected,(s,P,Q,expected)
        print(f'leaves={s}: book={P}, bipartite={Q}, edge_gain={P-Q}')
    print('PASS: exact labelled Markov-chain edge comparison for every s from 1 through 11.')
