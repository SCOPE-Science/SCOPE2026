"""Exact independent verification for k-limited domination on two-level Sierpinski graphs.
No external dependencies; run: python verify_sierpinski_minima.py
"""
from itertools import combinations,product
from math import comb, factorial


def adj(m):
    out=[0]*(m*m)
    for a in range(m):
        for b in range(m):
            x=a*m+b
            for c in range(m):
                if c!=b:out[x]|=1<<(a*m+c)
            if a!=b:out[x]|=1<<(b*m+a)
    return out

def valid(m,k,W,edges):
    N=m*m
    D=((1<<N)-1)^W
    for v in range(N):
        if (W>>v)&1:
            if not(edges[v]&D):return False
        elif (edges[v]&W).bit_count()>k:
            return False
    return True

def regular_symmetric_count(m,k):
    # Brute force symmetric binary matrices on m labels, no graph-domination logic.
    cnt=0
    for pattern in range(1<<(m*(m+1)//2)):
        degrees=[0]*m
        idx=0
        for i in range(m):
            for j in range(i,m):
                if pattern>>idx&1:
                    degrees[i]+=1
                    if i!=j:degrees[j]+=1
                idx+=1
        if all(d==k for d in degrees):cnt+=1
    return cnt

def involutions(m):
    return sum(factorial(m)//(factorial(m-2*j)*factorial(j)*2**j) for j in range(m//2+1))

def paths_cycles_count(m):
    # Labelled assembly recurrence from looped paths and ordinary cycles.
    from math import comb, factorial
    seq=[1]
    for n in range(1,m+1):
        component=lambda s:(factorial(s)//2 if s>=2 else 0)+(factorial(s-1)//2 if s>=3 else 0)
        seq.append(sum(comb(n-1,s-1)*component(s)*seq[n-s] for s in range(1,n+1)))
    return seq[m]

def check():
    for m in range(2,6):
        e=adj(m)
        for k in range(1,m):
            count=0
            for blocks in product(combinations(range(m),k),repeat=m):
                W=sum(1<<(i*m+j) for i,js in enumerate(blocks) for j in js)
                count+=valid(m,k,W,e)
            expected=regular_symmetric_count(m,k)
            assert count==expected,(m,k,count,expected)
            print('MINIMUM_SETS_OK',m,k,'count',count)
        assert regular_symmetric_count(m,1)==involutions(m)
        assert regular_symmetric_count(m,m-1)==involutions(m)
        for k in range(1,m):
            assert regular_symmetric_count(m,k)==regular_symmetric_count(m,m-k)
    for m in range(3,6):
        assert paths_cycles_count(m)==regular_symmetric_count(m,2)
        print('TWO_LIMITED_COMPONENT_ENUM_OK',m,paths_cycles_count(m))
    # check all W for size below m*k for m <= 3: no better k-limited dominating set.
    for m in (2,3):
        e=adj(m)
        for k in range(1,m):
            for W in range(1<<(m*m)):
                if W.bit_count()>m*k:assert not valid(m,k,W,e),(m,k,W)
            print('LOWER_BOUND_FULL_ENUM_OK',m,k)
    print('VERIFY_OK')

if __name__=='__main__':check()
