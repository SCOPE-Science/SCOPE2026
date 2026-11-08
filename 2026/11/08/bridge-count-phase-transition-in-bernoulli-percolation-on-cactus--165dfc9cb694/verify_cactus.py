"""Exact independent finite checks for random cactus bridge-count formulas."""
from itertools import combinations
from fractions import Fraction
from math import comb
from collections import defaultdict

def falling(x,k):
    a=1
    for j in range(k): a*=x-j
    return a

def bridge_count(vertices,edges,opened):
    E=[edges[i] for i in opened]
    count=0
    for i,(a,b) in enumerate(E):
        seen={a};front=[a]
        while front:
            v=front.pop()
            for j,(x,y) in enumerate(E):
                if i==j: continue
                nxt=(y if v==x else x if v==y else None)
                if nxt is not None and nxt not in seen:
                    seen.add(nxt);front.append(nxt)
        count+=(b not in seen)
    return count

def test(name, edges, cycles, p):
    m=len(edges); b=m-sum(cycles)
    assert b>=0
    by=defaultdict(lambda: defaultdict(int)); nums=defaultdict(list)
    EX=EB=EXB=Fraction(0)
    for mask in range(1<<m):
        opened=[i for i in range(m) if mask>>i&1]
        x=len(opened); y=bridge_count(None,edges,opened)
        by[x][y]+=1;nums[x].append(y)
        w=p**x * (1-p)**(m-x)
        EX+=w*x;EB+=w*y;EXB+=w*x*y
    assert EX==m*p, (name,'EX')
    assert EB==m*p-sum(c*p**c for c in cycles),(name,'EB')
    cov=EXB-EX*EB
    expected=p*(1-p)*(m-sum(c*c*p**(c-1) for c in cycles))
    assert cov==expected,(name,'cov',cov,expected)
    for e in range(m+1):
        mean=Fraction(sum(nums[e]),len(nums[e]))
        formula=Fraction(e)-sum(Fraction(c*falling(e,c),falling(m,c)) for c in cycles)
        assert mean==formula,(name,e,'conditional',mean,formula)
    # Independent coefficient expansion of claimed joint PGF.
    poly={(0,0): Fraction(1)}
    for c in [1]*b+cycles:
        z=defaultdict(Fraction)
        if c==1:
            z[(0,0)]+=1-p; z[(1,1)]+=p
        else:
            for k in range(c):z[(k,k)]+=comb(c,k)*p**k*(1-p)**(c-k)
            z[(c,0)]+=p**c
        t=defaultdict(Fraction)
        for (x,y),coef in poly.items():
            for (u,v),vcoef in z.items(): t[(x+u,y+v)]+=coef*vcoef
        poly=dict(t)
    assert sum(poly.values())==1
    for x in range(m+1):
        for y in range(m+1):
            actual=Fraction(by[x][y],comb(m,x))*comb(m,x)*p**x*(1-p)**(m-x) if y in by[x] else Fraction(0)
            assert poly.get((x,y),0)==actual,(name,x,y,poly.get((x,y),0),actual)
    return len(nums),sum(map(len,nums.values()))

def main():
    examples=[
      ('tree',[(0,1),(1,2),(2,3),(3,4)],[]),
      ('triangle',[(0,1),(1,2),(2,0)],[3]),
      ('square',[(0,1),(1,2),(2,3),(3,0)],[4]),
      ('triangle_tail',[(0,1),(1,2),(2,0),(2,3),(3,4)],[3]),
      ('bowtie',[(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)],[3,3]),
      ('square_triangle',[(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,3)],[4,3]),
      ('two_cycles_bridge',[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)],[3,3]),
      ('triangle_many_tail',[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9)],[3])
    ]
    count=0
    for name,edges,cycles in examples:
        for p in [Fraction(1,5),Fraction(1,2),Fraction(4,5)]:
            test(name,edges,cycles,p);count+=1
        m=len(edges);f=[Fraction(e)-sum(Fraction(c*falling(e,c),falling(m,c)) for c in cycles) for e in range(m+1)]
        assert all(f[i+2]-2*f[i+1]+f[i]<=0 for i in range(m-1))
        assert (sum(c*c for c in cycles)>m)==(m-sum(c*c for c in cycles)<0)
    print(f'PASS: {count} exact exhaustive Bernoulli-model checks, including joint distribution, mixed covariance and fixed-edge conditional means, plus conditional concavity on {len(examples)} finite cacti')

if __name__=='__main__':main()
