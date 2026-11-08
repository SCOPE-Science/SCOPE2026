"""Exact ground sectors via outer-ring enumeration and two independent inner pentagons."""
from itertools import product
from fractions import Fraction

def solve():
    alphabet=range(3)
    pent=[]
    for ext in product(alphabet,repeat=5):
        best=[[10**9,0] for _ in range(6)]
        for inner in product(alphabet,repeat=5):
            k=sum(x==0 for x in inner)
            cost=sum(inner[i]==ext[i] for i in range(5)) + sum(inner[i]==inner[(i+1)%5] for i in range(5))
            if cost<best[k][0]:best[k]=[cost,1]
            elif cost==best[k][0]:best[k][1]+=1
        pent.append(best)
    pow3=[81,27,9,3,1]
    def lookup(x):return pent[sum(v*pow3[i] for i,v in enumerate(x))]
    best=[[10**9,0] for _ in range(21)]
    for outer in product(alphabet,repeat=10):
        outer_cost=sum(outer[i]==outer[(i+1)%10] for i in range(10))
        outer_k=sum(c==0 for c in outer)
        even=lookup([outer[i] for i in (0,2,4,6,8)])
        odd=lookup([outer[i] for i in (1,3,5,7,9)])
        for e,(ce,we) in enumerate(even):
            if we==0:continue
            for o,(co,wo) in enumerate(odd):
                if wo==0:continue
                k=outer_k+e+o
                cost=outer_cost+ce+co
                if cost<best[k][0]:best[k]=[cost,we*wo]
                elif cost==best[k][0]:best[k][1]+=we*wo
    return best

def proper_coloring_profile():
    """Direct proper-color backtracking using an explicit edge list."""
    edges = [(i,(i+1)%10) for i in range(10)]
    edges += [(i,10+i) for i in range(10)]
    edges += [(10+i,10+((i+2)%10)) for i in range(10)]
    adj=[set() for _ in range(20)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    # A fixed order; each edge is checked when its second endpoint is colored.
    values=[-1]*20
    counts=[0]*21
    def dfs(i,k):
        if i==20:
            counts[k]+=1
            return
        for c in (0,1,2):
            if all(values[j]!=c for j in adj[i] if j<i):
                values[i]=c
                dfs(i+1,k+(c==0))
        values[i]=-1
    dfs(0,0)
    return counts

if __name__=='__main__':
    table=solve()
    expected_cost=[6,5,4,3,2,1,0,0,0,2,3,5,6,9,12,15,18,21,24,27,30]
    expected_ways=[250,3000,13800,30400,32760,15840,2720,4160,320,57600,30720,115200,1280,40960,79360,61184,24160,5280,640,40,1]
    assert table==list(map(list,zip(expected_cost,expected_ways)))
    for k,(p,w) in enumerate(table):print(k,p,w)
    profile=proper_coloring_profile()
    assert [(k,v) for k,v in enumerate(profile) if v] == [(6,2720),(7,4160),(8,320)]
    assert table[6][0]==table[7][0]==table[8][0]==0
    assert sum(table[i][1] for i in (6,7,8))==7200
    assert sum(table[i][1] for i in range(7) if table[i][0]+i==6)==98770
    assert sum(table[i][1] for i in range(21) if 2*table[i][0]-3*i==-24)==32320
    assert sum(table[i][1] for i in range(21) if table[i][0]-3*i==-30)==212905
    # Exact rational envelope checks, including every field threshold.
    for x, ground_k, degeneracy in [
        (Fraction(-2), [0],250),
        (Fraction(-1),list(range(7)),98770),
        (Fraction(-1,2),[6],2720),
        (Fraction(0),[6,7,8],7200),
        (Fraction(1),[8],320),
        (Fraction(3,2),[8,10,12],32320),
        (Fraction(2),[12],1280),
        (Fraction(3),list(range(12,21)),212905),
        (Fraction(4),[20],1)]:
        energy=min(p-x*k for k,(p,w) in enumerate(table))
        minimizers=[k for k,(p,w) in enumerate(table) if p-x*k==energy]
        assert minimizers==ground_k
        assert sum(table[k][1] for k in minimizers)==degeneracy
    print('INDEPENDENT_PENTAGON_OK')
