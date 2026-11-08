#!/usr/bin/env python3
"""Finite corroboration of cycle-independent-set VC and online bounds."""
from itertools import combinations, product
from functools import lru_cache
from math import comb, floor, log2

def fam(n,k):
    return tuple(sum(1 << v for v in sel) for sel in combinations(range(n),k)
                 if all((v+1)%n not in sel for v in sel))

def vc_by_traces(n,k,H):
    mx=0
    for S in range(1<<n):
        d=S.bit_count()
        if d<=mx or (1<<d)>len(H):
            continue
        if len({a&S for a in H})==(1<<d):
            mx=d
    return mx

def ldim(n,H):
    @lru_cache(None)
    def L(indices):
        if len(indices)<2: return 0
        ans=0
        for v in range(n):
            T=tuple(i for i in indices if H[i]>>v&1)
            F=tuple(i for i in indices if not H[i]>>v&1)
            if T and F:
                ans=max(ans,1+min(L(T),L(F)))
        return ans
    return L(tuple(range(len(H))))

def gap_construction(n,k,S,bits):
    # S = {0, 2, ..., 2(t-1)}. For each short 2-edge gap, use
    # 0 as intermediate unless both queried endpoints are 0.
    t=len(S)
    x=[None]*n
    for i,b in enumerate(bits): x[2*i]=b
    m=0
    for i in range(t-1):
        a,b=bits[i],bits[i+1]
        x[2*i+1]=1 if a==b==0 else 0
        m+=int(a!=b)
    extra=n-2*k-m
    L=n-2*(t-1)
    a,b=bits[-1],bits[0]
    # Need a no-11 walk of L edges from a to b with exactly extra 00 edges.
    # A DP on position/last bit/number of 00 edges reconstructs one.
    dp={(a,0):[a]}
    for j in range(L):
        nxt={}
        for (last,c),path in dp.items():
            for bit in (0,1):
                if last and bit: continue
                c2=c+(not last and not bit)
                if c2<=extra:
                    nxt[(bit,c2)]=path+[bit]
        dp=nxt
    assert (b,extra) in dp,(n,k,S,bits,extra,L)
    tail=dp[(b,extra)]
    for j in range(1,L):x[2*(t-1)+j]=tail[j]
    assert all(v in (0,1) for v in x)
    A=sum(v<<i for i,v in enumerate(x))
    assert A.bit_count()==k and not any(x[i] and x[(i+1)%n] for i in range(n))
    assert all(x[2*i]==bits[i] for i in range(t))
    return A

def block(b,j):
    return [v for _ in range(j) for v in (1,0)]+[0]+[v for _ in range(b-j) for v in (1,0)]

def main():
    vc_cases=0
    online_cases=0
    witness_cases=0
    threshold_cases=0
    for n in range(3,15):
        for k in range((n//2)+1):
            H=fam(n,k)
            expected=min(k,n-2*k+1)
            # Skip large trace universe only when too costly, do small n exhaustive.
            if n<=12:
                got=vc_by_traces(n,k,H)
                assert got==expected,(n,k,got,expected)
                vc_cases+=1
            t=expected
            S=tuple(range(0,2*t,2))
            if t:
                assert max(S)<n
                for bits in product((0,1),repeat=t):
                    A=gap_construction(n,k,S,bits)
                    assert A in H
                    witness_cases+=1
            if n<=10:
                L=ldim(n,H)
                r=n-2*k
                if k and r>=1:
                    B=[k//r+(i<k%r) for i in range(r)]
                    lower=sum((b+1).bit_length()-1 for b in B)
                    assert lower<=L<=len(H).bit_length()-1,(n,k,lower,L)
                online_cases+=1
    for k in range(1,35):
        for r in range(1,8):
            n=2*k+r
            bs=[k//r+(i<k%r) for i in range(r)]
            words=[[]]
            for b in bs:
                new=[]
                for w in words:
                    for j in range(b+1):new.append(w+block(b,j))
                words=new
                if len(words)>10000:break
            if len(words)>10000:continue
            for w in words:
                assert len(w)==n and sum(w)==k
                assert not any(w[i] and w[(i+1)%n] for i in range(n))
            for b in bs:
                for j in range(b+1):
                    z=block(b,j)
                    assert all(z[2*q]==int(j>q) for q in range(b))
            threshold_cases+=1
    print('FIXED_WEIGHT_CYCLE_LEARNING_PASS',vc_cases,online_cases,witness_cases,threshold_cases)
if __name__=='__main__':main()
