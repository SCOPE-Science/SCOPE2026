"""Independent finite checks for finite block-character eventual-stabilization enumeration."""
from fractions import Fraction
from itertools import product
from math import factorial


def polynomial_count(block_sizes,chi,height):
    r=len(block_sizes)
    zero=(0,)*r
    one={zero:Fraction(1)}
    def monomial(i):
        d=[0]*r; d[i]=1
        return {tuple(d):Fraction(1)}
    def add(*polys):
        ans={}
        for p in polys:
            for k,v in p.items(): ans[k]=ans.get(k,0)+v
        return {k:v for k,v in ans.items() if v}
    def mul(p,q):
        ans={}
        for u,a in p.items():
            for v,b in q.items():
                w=tuple(x+y for x,y in zip(u,v))
                if all(w[i]<=block_sizes[i] for i in range(r)):
                    ans[w]=ans.get(w,0)+a*b
        return {k:v for k,v in ans.items() if v}
    def exp(p):
        ans=one.copy();term=one.copy()
        for k in range(1,sum(block_sizes)+1):
            term=mul(term,p)
            if not term:break
            ans=add(ans,{m:v/Fraction(factorial(k)) for m,v in term.items()})
        return ans
    T=[monomial(i) for i in range(r)]
    for _ in range(height):
        T=[mul(monomial(j),exp(add(*(T[i] for i in range(r) if chi[i]==j)))) for j in range(r)]
    forest=exp(add(*(T[i] for i in range(r) if chi[i]==i)))
    out=forest.get(tuple(block_sizes),0)
    for n in block_sizes:out*=factorial(n)
    assert out.denominator==1,(block_sizes,chi,height,out)
    return int(out)


def brute_count(block_sizes,chi,height):
    types=[i for i,n in enumerate(block_sizes) for _ in range(n)]
    n=len(types)
    allowed=[tuple(j for j in range(n) if types[j]==chi[types[i]]) for i in range(n)]
    count=0
    for f in product(*allowed):
        for v in range(n):
            w=v
            for _ in range(height): w=f[w]
            if f[w]!=w: break
        else:count+=1
    return count


def min_height(chi):
    r=len(chi); depths=[]
    for i in range(r):
        seen=set();j=i;t=0
        while chi[j]!=j:
            if j in seen:return None
            seen.add(j);j=chi[j];t+=1
        depths.append(t)
    return max(depths)

def max_height(block_sizes,chi):
    r=len(chi)
    depths=[]
    for i in range(r):
        seen=set();j=i;t=0
        while chi[j]!=j:
            if j in seen:return None
            seen.add(j);j=chi[j];t+=1
        depths.append(t+block_sizes[j]-1)
    return max(depths)


def closed_total(sizes,chi):
    if max_height(sizes,chi) is None:return 0
    out=1
    for i,j in enumerate(chi):
        if i!=j:out*=sizes[j]**sizes[i]
        else:out*=(sizes[i]+1)**(sizes[i]-1)
    return out

def run():
    checked=0
    samples=[]
    for r in range(1,4):
        for sizes in product(range(1,4),repeat=r):
            n=sum(sizes)
            if n>6:continue
            for chi in product(range(r),repeat=r):
                H=max_height(sizes,chi)
                for h in range(0, min(n,4)+1):
                    a=polynomial_count(sizes,chi,h)
                    b=brute_count(sizes,chi,h)
                    assert a==b,(sizes,chi,h,a,b)
                    checked+=1
                if H is None:
                    assert polynomial_count(sizes,chi,n)==0
                    assert closed_total(sizes,chi)==0
                else:
                    d=min_height(chi)
                    assert polynomial_count(sizes,chi,H)>0
                    assert polynomial_count(sizes,chi,H)==closed_total(sizes,chi),(sizes,chi,H)
                    for h in range(0,H+1):
                        count=polynomial_count(sizes,chi,h)
                        prev=polynomial_count(sizes,chi,h-1) if h>0 else 0
                        assert (count>prev)==(d<=h<=H),(sizes,chi,h,d,H,count,prev)
                if sizes in ((2,2),(1,1,2),(2,1,1),(1,2,2)) and len(samples)<12:
                    samples.append((sizes,chi,H,[polynomial_count(sizes,chi,h) for h in range(min(n,4)+1)]))
    print('CHARACTER_HEIGHT_EGF_BRUTE_FORCE_PASSED')
    print('profiles_characters_heights',checked)
    for x in samples:print(x)
if __name__=='__main__': run()
