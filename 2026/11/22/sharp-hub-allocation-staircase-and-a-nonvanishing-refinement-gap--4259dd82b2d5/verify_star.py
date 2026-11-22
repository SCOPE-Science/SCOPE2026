#!/usr/bin/env python3
"""Independent rational checks for exact star supported-sign trace probing."""
from fractions import Fraction as Q
from math import comb, factorial
from itertools import product


def bal(t,q):
    assert q>=1 and t>=q
    a,b=divmod(t,q)
    return (q-b)*comb(a,2)+b*comb(a+1,2)


def count_optimal_partitions(m,k,hs):
    total=0
    q=k-1
    for h in hs:
        a,b=divmod(m-h,q)
        total+=comb(m,h)*factorial(m-h)//(factorial(a)**(q-b)*factorial(a+1)**b*factorial(q-b)*factorial(b))
    return total


def formula(m,k,mu):
    R=(1+mu)**2
    values=[Q(h*(h-1),2)+R*h+bal(m-h,k-1) for h in range(m-k+2)]
    best=min(values)
    return best,[h for h,f in enumerate(values) if f==best]


def partitions(n):
    colors=[0]
    def recur(t,maxc):
        if t==n:
            yield tuple(colors);return
        for c in range(maxc+2):
            colors.append(c)
            yield from recur(t+1,max(maxc,c))
            colors.pop()
    yield from recur(1,0)


def actual(m,k,mu):
    R=(1+mu)**2
    best=None;hs=set();number=0
    for c in partitions(m+1):
        if max(c)+1 != k:continue
        counts=[c.count(i) for i in range(k)]
        h=counts[0]-1
        f=Q(h*(h-1),2)+R*h+sum(Q(counts[i]*(counts[i]-1),2) for i in range(1,k))
        if best is None or f<best: best=f;hs={h};number=1
        elif f==best: hs.add(h);number+=1
    return best,hs,number


def inv(A):
    n=len(A)
    B=[[Q(A[i][j]) for j in range(n)]+[Q(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        u=next(i for i in range(j,n) if B[i][j]!=0)
        B[j],B[u]=B[u],B[j]
        z=B[j][j]
        B[j]=[x/z for x in B[j]]
        for i in range(n):
            if i==j:continue
            z=B[i][j]
            B[i]=[x-z*y for x,y in zip(B[i],B[j])]
    return [x[n:] for x in B]


def optimal_class_sizes(m,k,mu):
    f,hs=formula(m,k,mu)
    possibilities=[]
    for h in hs:
        q=k-1
        a,b=divmod(m-h,q)
        possibilities.append((h,[a]*(q-b)+[a+1]*b))
    return f,possibilities


def best_one_split(m,k,mu):
    R=(1+mu)**2
    parent,possibilities=optimal_class_sizes(m,k,mu)
    results=[]
    for h,rs in possibilities:
        if h>=1:
            old=Q(h*(h-1),2)+R*h
            new=min(Q(t*(t-1),2)+R*t+Q((h-t)*(h-t-1),2)
                    for t in range(h))
            results.append(parent-old+new)
        for r in rs:
            if r>=2:
                old=Q(r*(r-1),2)
                new=min(Q(t*(t-1),2)+Q((r-t)*(r-t-1),2) for t in range(1,r))
                results.append(parent-old+new)
    return min(results)


def test():
    count=0
    for m in range(2,9):
        for k in range(2,m+2):
            for mu in [Q(1,5),Q(1,2),Q(1),Q(2)]:
                b,hs=formula(m,k,mu)
                b2,hs2,num=actual(m,k,mu)
                assert (b,set(hs))==(b2,hs2),(m,k,mu,b,b2,hs,hs2)
                assert count_optimal_partitions(m,k,hs)==num,(m,k,mu,num)
                count+=1
                if k>=2 and m>=k:
                    thresh=(m-1)//(k-1)
                    assert (0 in hs) == ((1+mu)**2>=thresh)
                    count+=1
    for m in range(2,8):
        for mu in [Q(1,5),Q(1,2),Q(2)]:
            n=m+1
            A=[[Q(mu)+(m if i==0 else 1) if i==j else Q(-1) if i==0 or j==0 else Q(0) for j in range(n)] for i in range(n)]
            G=inv(A)
            b=Q(1,mu*(mu+m+1)); a=b/(mu+1)
            assert all(G[0][j]==b for j in range(1,n))
            assert all(G[i][j]==a for i in range(1,n) for j in range(1,n) if i!=j)
            count+=2
            for k in range(2,min(n,5)+1):
                bf,_=formula(m,k,mu)
                # direct matrix-entry variance for one minimizing partition
                c=next(c for c in partitions(n) if max(c)+1==k and
                       sum((G[i][j]**2 for i in range(n) for j in range(i+1,n) if c[i]==c[j]),Q())==bf*a*a)
                var=4*sum((G[i][j]**2 for i in range(n) for j in range(i+1,n) if c[i]==c[j]),Q())
                assert var==4*a*a*bf
                count+=1
    # Exact example m=12, mu=1/2, two/three probes
    assert formula(12,2,Q(1,2))==(Q(169,4),[5])
    assert formula(12,3,Q(1,2))==(Q(51,2),[2])
    # Exact minimum from refining the optimal two-class allocation.
    R=Q(9,4)
    # Parent classes: hub+5 leaves and 7 leaves. Split one class.
    refine_hub=min(Q(h*(h-1),2)+R*h+Q((5-h)*(4-h),2)+comb(7,2)
                   for h in range(5)) # exclude empty second split
    refine_leaf=Q(5*4,2)+R*5+min(comb(t,2)+comb(7-t,2) for t in range(1,7))
    assert refine_hub==Q(117,4), (refine_hub,refine_leaf)
    assert min(refine_hub,refine_leaf)/Q(51,2)==Q(39,34)
    count+=4
    for k in [2,3,4]:
        limit=Q(2*k*k+k-1,2*k*k)
        for m in [60,120,240,480]:
            mu=Q(1,2)
            ratio=best_one_split(m,k,mu)/formula(m,k+1,mu)[0]
            # Exact rational closeness, no floating point in comparison.
            assert abs(ratio-limit) < Q(10*k, m)
            count+=1
    print('PASS:',count,'exact-rational comparisons / identities')
    print('Example: m=12, shift=1/2: two-class cost=169/4, three-class cost=51/2, best refinement=117/4, ratio=39/34')
    print('Asymptotic k -> k+1 ratio: 1+(k-1)/(2*k*k), including 9/8 for k=2.')

if __name__=='__main__':test()
