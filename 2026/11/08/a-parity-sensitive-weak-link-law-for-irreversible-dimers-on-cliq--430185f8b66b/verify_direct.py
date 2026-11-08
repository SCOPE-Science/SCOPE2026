"""Exact graph-state test of greedy dimer deposition on two bridged cliques."""
from fractions import Fraction
from functools import lru_cache

def first_edge_probability(a,b, lam=1):
    assert a>=2 and b>=2 and lam>0
    N=a+b
    bridge=(0,a)
    edges=[(i,j,Fraction(1)) for i in range(a) for j in range(i+1,a)]
    edges += [(i,j,Fraction(1)) for i in range(a,N) for j in range(i+1,N)]
    edges += [(bridge[0],bridge[1],Fraction(lam))]
    @lru_cache(None)
    def step(mask):
        if not ((mask>>bridge[0])&1 and (mask>>bridge[1])&1):
            return Fraction(0)
        available=[(u,v,w) for u,v,w in edges if mask&(1<<u) and mask&(1<<v)]
        total=sum((w for _,_,w in available),Fraction(0))
        return sum((w if (u,v)==bridge else w*step(mask & ~(1<<u) & ~(1<<v)) for u,v,w in available),Fraction(0))/total
    return step((1<<N)-1)

@lru_cache(None)
def p_count(a,b, lam):
    c1=a*(a+1)//2
    c2=b*(b+1)//2
    num=Fraction(lam)
    if a>=2: num+=Fraction(a*(a-1)//2)*p_count(a-2,b,lam)
    if b>=2: num+=Fraction(b*(b-1)//2)*p_count(a,b-2,lam)
    return num/(Fraction(lam)+c1+c2)


def full_size_law(a,b,lam):
    N=a+b
    edges=[(i,j,Fraction(1)) for i in range(a) for j in range(i+1,a)]
    edges += [(i,j,Fraction(1)) for i in range(a,N) for j in range(i+1,N)]
    edges += [(0,a,Fraction(lam))]
    @lru_cache(None)
    def go(mask):
        av=[(i,j,w) for i,j,w in edges if mask&(1<<i) and mask&(1<<j)]
        if not av:return {0:Fraction(1)}
        total=sum((w for _,_,w in av),Fraction(0))
        dist={}
        for i,j,w in av:
            for count,p in go(mask&~(1<<i)&~(1<<j)).items():
                dist[count+1]=dist.get(count+1,Fraction(0))+w*p/total
        return dist
    return go((1<<N)-1)

def run():
    tests=0
    for a in range(2,7):
      for b in range(2,7):
        if a+b>11:continue
        for rate in (Fraction(1),Fraction(2,3),Fraction(5,2)):
            direct=first_edge_probability(a,b,rate)
            reduced=p_count(a-1,b-1,rate)
            assert direct==reduced,(a,b,rate,direct,reduced)
            size_dist=full_size_law(a,b,rate)
            size0=a//2+b//2
            size1=1+(a-1)//2+(b-1)//2
            predicted={size0:Fraction(1)-direct}
            predicted[size1]=predicted.get(size1,Fraction(0))+direct
            assert size_dist==predicted,(a,b,rate,size_dist,predicted)
            tests+=1
    print('direct graph DP versus reduced first-edge recurrence:',tests,'exact comparisons PASS')
    for a,b in [(2,2),(3,3),(4,4),(5,6),(7,7)]:
        print(a,b,p_count(a-1,b-1,Fraction(1)))

if __name__=='__main__':run()
