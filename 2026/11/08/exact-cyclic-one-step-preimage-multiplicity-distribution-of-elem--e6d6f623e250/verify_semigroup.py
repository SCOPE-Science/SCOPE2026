#!/usr/bin/env python3
"""Exact finite-state certificate for cyclic Rule 30 one-step fibers."""
from collections import Counter, deque

def compose(f,g):
    return tuple(f[g[x]] for x in range(4))

def generators():
    return [tuple(((y ^ ((s>>1) | (s&1)))<<1)|(s>>1) for s in range(4)) for y in (0,1)]

def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def charpoly_coeff(A):
    # Newton identities, coefficient order leading to constant.
    n=len(A); cur=[[int(i==j) for j in range(n)] for i in range(n)]
    sums=[]
    for k in range(1,n+1):
        cur=matmul(cur,A)
        sums.append(sum(cur[i][i] for i in range(n)))
    co=[1]
    for k in range(1,n+1):
        num=sum(co[k-i]*sums[i-1] for i in range(1,k+1))
        assert num%k==0
        co.append(-num//k)
    return co,sums

def poly_product(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out

def main():
    g0,g1=generators()
    assert g0==(0,2,3,3) and g1==(2,0,1,1)
    identity=(0,1,2,3)
    seen={identity:''};queue=deque([identity])
    while queue:
        f=queue.popleft()
        for bit,g in enumerate((g0,g1)):
            nxt=compose(f,g)
            if nxt not in seen:
                seen[nxt]=seen[f]+str(bit);queue.append(nxt)
    assert len(seen)==41
    rank3={w:t for t,w in seen.items() if len(set(t))==3}
    assert set(rank3)=={'0','1','01','11','011','111'}
    assert [sum(t[i]==i for i in range(4)) for t in rank3.values()]==[2,0,1,0,0,3]
    for w,t in rank3.items():
        if w not in ('011','111'):
            assert len(set(compose(t,g0)))<=2
        else:
            assert len(set(compose(t,g0)))<=2
    P=[[0]*16 for _ in range(16)]
    for ab in range(4):
        a,b=ab>>1,ab&1
        for de in range(4):
            d,e=de>>1,de&1
            for c in (0,1):
                for f in (0,1):
                    if (a^(b|c))==(d^(e|f)):
                        dst=((b<<1)|c)*4+((e<<1)|f)
                        P[4*ab+de][dst]+=1
    co,sums=charpoly_coeff(P)
    expected=[1]
    for factor in ([1,-2],[1,-1],[1,-1,0,-2]):
        expected=poly_product(expected,factor)
    expected=expected+[0]*11
    assert co==expected, (co,expected)
    s=[3,1,1]
    for n in range(3,21):s.append(s[-1]+2*s[-3])
    for n in range(1,17):
        delta=int(n%3==0)
        v=(1+s[n]-2*delta)//2
        assert (1+s[n]-2*delta)%2==0
        distribution={0:v,1:2**n-1-s[n]+3*delta,2:v-2*delta,3:delta}
        assert all(x>=0 for x in distribution.values())
        assert sums[n-1]==2**n+1+s[n]
        if n<=12:
            sums_by_output=Counter()
            for y in range(1<<n):
                h=identity
                for i in range(n): h=compose(h,(g0,g1)[(y>>i)&1])
                counts=sum(h[i]==i for i in range(4))
                sums_by_output[counts]+=1
            assert dict(sums_by_output)=={k:v for k,v in distribution.items() if v}
    print('SEMIGROUP_VERIFY_OK',len(seen),'charpoly',co)
    print('CYCLIC_FIBERS_VERIFY_OK n=1..16')

if __name__=='__main__':main()
