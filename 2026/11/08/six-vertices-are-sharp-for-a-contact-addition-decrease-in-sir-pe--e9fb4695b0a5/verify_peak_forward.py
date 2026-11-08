"""Independent subset-only rational absorption calculation for the six-site SIR peak witness."""
from fractions import Fraction as Q
from functools import lru_cache

N=6
E=((0,4),(0,5),(1,3),(2,3),(3,4))

def all_infected_before_recovery(edges,seed=1,rate=50):
    neighbors=[0]*N
    for a,b in edges:
        neighbors[a]|=1<<b; neighbors[b]|=1<<a
    @lru_cache(None)
    def success(infected):
        if infected==(1<<N)-1:return Q(1)
        rates=[(v,rate*(infected & neighbors[v]).bit_count()) for v in range(N) if not(infected>>v&1)]
        total=infected.bit_count()+sum(w for v,w in rates)
        return sum((Q(w)*success(infected|(1<<v)) for v,w in rates),Q(0))/total
    return success(1<<seed)

if __name__=='__main__':
    a=all_infected_before_recovery(E)
    b=all_infected_before_recovery(E+((1,2),))
    assert a==Q(14289062500,18273931533)
    assert b==Q(1946796875000,2491078937193)
    assert a-b==Q(24352320312500,56704429847324259)>0
    print('INDEPENDENT_SUBSET_PASS',a,b,a-b)
