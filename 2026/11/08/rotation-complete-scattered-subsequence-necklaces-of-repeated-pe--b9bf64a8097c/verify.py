#!/usr/bin/env python3
"""Direct finite replay checks for rotation-complete subsequences.
Only standard Python, with bounded finite instances, not a proof for unbounded parameters.
"""
from itertools import combinations, product
from math import comb, gcd


def phi(n):
    return sum(gcd(i,n)==1 for i in range(1,n+1))


def subsequence(u,w):
    j=0
    for x in w:
        if j<len(u) and x==u[j]:j+=1
    return j==len(u)


def rotations(u):
    return [u[i:]+u[:i] for i in range(len(u))]


def canon(u):
    return min(rotations(u))


def weighted_trace(q,h):
    """Coefficient list of tr(M_q(z)^h) by direct weighted-path DP."""
    result=[0]*(h+1)
    for start in range(q):
        # DP state (end, weak-transition number)
        dp={(start,0):1}
        for step in range(h):
            nxt={}
            for (a,c),v in dp.items():
                for b in range(q):
                    z=(b<=a)
                    key=(b,c+z)
                    nxt[key]=nxt.get(key,0)+v
            dp=nxt
        for (end,c),v in dp.items():
            if end==start:result[c]+=v
    return result


def burnside(q,k,h):
    numerator=0
    for d in range(1,h+1):
        if h%d:continue
        t=weighted_trace(q,h//d)
        numerator+=phi(d)*sum(v for c,v in enumerate(t) if c*d<=k-1)
    assert numerator%h==0,(q,k,h,numerator)
    return numerator//h+(q if h==k else 0)


def greedy_cycles(u):
    if not u:return 0
    return 1+sum(u[i]>=u[i+1] for i in range(len(u)-1))


def property_formula(u,k):
    h=len(u)
    c=sum(u[i]>=u[(i+1)%h] for i in range(h))
    return c<=k-1 or (h==k and len(set(u))==1)


def exhaustive(q,k):
    W=tuple(i for _ in range(k) for i in range(q))
    for h in range(1,q*k+2):
        count=0
        for u in product(range(q),repeat=h):
            if u!=canon(u):continue
            direct=all(subsequence(rot,W) for rot in rotations(u))
            theoretical=property_formula(u,k)
            assert direct==theoretical,(q,k,h,u,direct,theoretical)
            if direct:count+=1
        predicted=burnside(q,k,h)
        assert count==predicted,(q,k,h,count,predicted)
    return q*k+1


def near_edge_class(q,d,deficit):
    # all cyclic sorted-run strings of maximal length q*d-deficit
    ans=set()
    for losses in product(range(deficit+1),repeat=d):
        if sum(losses)!=deficit:continue
        sublists=[]
        for loss in losses:
            sublists.append([tuple(x for x in range(q) if x not in missing)
                             for missing in combinations(range(q),loss)])
        for seq in product(*sublists):
            if not all(seq[i][-1]>=seq[(i+1)%d][0] for i in range(d)):
                continue
            w=tuple(c for s in seq for c in s)
            ans.add(canon(w))
    return ans


def edge_formula(q,d,r):
    if r==0:return 1
    if r==1:return q
    if r==2:return comb(q,2)+((d-1)//2)*q*q+(comb(q+1,2) if d%2==0 else 0)
    raise ValueError(r)


def main():
    cases=[(2,k) for k in range(1,6)]+[(3,k) for k in range(1,4)]+[(4,k) for k in range(1,3)]+[(5,1)]
    tested=0
    for q,k in cases:
        tested+=exhaustive(q,k)
    boundary=0
    for q in range(3,7):
        for d in range(2,7):
            for r in (0,1,2):
                seen=near_edge_class(q,d,r)
                want=edge_formula(q,d,r)
                assert len(seen)==want,(q,d,r,len(seen),want)
                for word in seen:
                    assert property_formula(word,d+1)
                boundary+=1
    for q in range(2,7):
        for k in range(1,7):
            for h in range(1,min(q*k+1,16)):
                n=burnside(q,k,h)
                if h<=k:
                    assert n==sum(phi(d)*q**(h//d) for d in range(1,h+1) if h%d==0)//h
                if h>max(k,q*(k-1)):
                    assert n==0,(q,k,h,n)
    print('PASS: exhaustive_qk_cases=',len(cases), 'length_cases=',tested,
          'boundary_cases=',boundary,'transfer_matrix_and_Burnside_exact')

if __name__=='__main__':main()
