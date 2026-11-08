#!/usr/bin/env python3
"""Finite independent sanity checks for a valuation-based period-doubling theorem."""
from math import log

def symbol(n):
    z=n+1
    return ((z & -z).bit_length()-1)&1

def test():
    MAX_START=2048
    MAX_PERIOD=128
    v=[symbol(j) for j in range(max(MAX_START+MAX_PERIOD*5+3,1<<16))]
    square_count=0
    dyadic_periods=set()
    for d in range(1,MAX_PERIOD+1):
        # Compute lcp(a,a+d) backward, without assuming the theorem.
        common=0
        for a in range(len(v)-d-1,-1,-1):
            common=(common+1 if v[a]==v[a+d] else 0)
            if a>MAX_START:continue
            if common>=d:
                square_count+=1
                assert d & (d-1)==0,(a,d)
                assert a>=2*d,(a,d)
                # Test maximal periodic continuation from a, using direct comparisons.
                assert common<3*d,(a,d,common)
                dyadic_periods.add(d)
    assert dyadic_periods=={1,2,4,8,16,32,64,128}
    for r in range(1,14):
        endpoint=1<<(r+1)
        for j in range(1,r+1):
            a=1<<j
            h=a//2
            assert v[a:a+h]==v[a+h:2*a],(r,j)
        if r<11:
            a0=2
            # Independently compute shortest repetition factorization by DP
            # over all possible periods, without using the dyadic-period theorem.
            target=endpoint
            dp=[10**9]*(target+1)
            dp[a0]=0
            for a in range(a0,target):
                if dp[a]==10**9:continue
                for d in range(1,(target-a)//2+1):
                    lcp=0
                    while a+d+lcp<target and v[a+lcp]==v[a+d+lcp]:lcp+=1
                    if lcp<d:continue
                    for b in range(a+2*d,min(target,a+d+lcp)+1):
                        dp[b]=min(dp[b],dp[a]+1)
            assert int(r*log(2,3)) + 1 <= dp[target] <=r,(r,dp[target])
            print(f'r={r} length={target-2} shortest_width={dp[target]} lower_bound={int(r*log(2,3))+1}')
    print('VERIFY_OK', 'squares_checked=',square_count,'max_start=',MAX_START,'max_period=',MAX_PERIOD, 'block_scales=',13)
if __name__=='__main__':test()
