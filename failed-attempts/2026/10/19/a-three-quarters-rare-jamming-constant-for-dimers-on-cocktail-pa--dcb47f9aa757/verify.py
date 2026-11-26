"""Independent finite checks for random sequential dimer adsorption on K_{2n} minus n disjoint forbidden pairs."""
from fractions import Fraction
from functools import lru_cache
from math import comb

@lru_cache(None)
def state_probability(p,s):
    vertices=2*p+s
    if vertices==2:return Fraction(int(p==1))
    if vertices==0:return Fraction(0)
    weights=((s*(s-1)//2,(p,s-2)),(2*p*s,(p-1,s)),(2*p*(p-1),(p-2,s+2)))
    total=sum(w for w,_ in weights)
    assert total==comb(vertices,2)-p
    assert total>0
    return sum((Fraction(w,total)*state_probability(*successor) for w,successor in weights if w),Fraction())

# Independent computation on actual labeled vertex sets, without (p,s) state variables.
def physical_probability(n):
    V=2*n
    initial=(1<<V)-1
    edges=[(u,v) for u in range(V) for v in range(u+1,V) if u//2!=v//2]
    @lru_cache(None)
    def recur(mask):
        valid=[(u,v) for u,v in edges if (mask>>u)&1 and (mask>>v)&1]
        if not valid:
            return Fraction(int(mask.bit_count()==2))
        return sum((recur(mask^(1<<u)^(1<<v)) for u,v in valid),Fraction())/len(valid)
    return recur(initial),recur.cache_info().currsize

for n in range(1,8):
    x=state_probability(n,0)
    y,k=physical_probability(n)
    assert x==y,(n,x,y)
    print('direct subset',n,str(x),'states',k)

# Independently check exact finite intermediary bounds derived from tagged pairs.
from collections import defaultdict
for n in range(5,19):
    dist={(n,0):Fraction(1)}
    for j in range(n-1,1,-1):
        nd=defaultdict(Fraction)
        for (p,s),v in dist.items():
            m=2*p+s; d=comb(m,2)-p
            opts=((s*(s-1)//2,(p,s-2)),(2*p*s,(p-1,s)),(2*p*(p-1),(p-2,s+2)))
            for w,st in opts:
                if w:nd[st]+=v*Fraction(w,d)
        dist=dict(nd)
        assert all(2*p+s==2*j for p,s in dist)
        k=j
        first=sum(Fraction(p)*v for (p,s),v in dist.items())
        second=sum(Fraction(p*(p-1))*v for (p,s),v in dist.items())
        low=Fraction(k*(k-1),n-1)
        high=Fraction(n*(4*k*k-1),4*n*n-1)
        assert low<=first<=high,(n,k,'first',low,first,high)
        assert second<=Fraction(200*k**4,n**2),(n,k,'second',second)
    print('moments',n,'pass')

# A large-n numerical check of the limiting constant.
def numeric_p(nmax=1000):
    old={(0,0):0.,(1,0):1.,(0,2):0.}
    results={}
    for m in range(4,2*nmax+1,2):
        cur={}
        for p in range(m//2+1):
            s=m-2*p
            w1=s*(s-1)//2;w2=2*p*s;w3=2*p*(p-1)
            d=w1+w2+w3
            cur[p,s]=(w1*old.get((p,s-2),0)+w2*old.get((p-1,s),0)+w3*old.get((p-2,s+2),0))/d if d else 0
        old=cur
        if m//2 in (20,100,500,1000):results[m//2]=old[m//2,0]*(m//2)
    return results
print('n*P_n (converges to 0.75):',numeric_p())
print('ALL CHECKS PASSED')
