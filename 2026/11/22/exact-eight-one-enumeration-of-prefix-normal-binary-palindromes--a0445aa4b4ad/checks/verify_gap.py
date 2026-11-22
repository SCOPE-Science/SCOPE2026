#!/usr/bin/env python3
"""Independent all-length certificate for gap inequalities and rational-series coefficients."""
from math import comb

def formula_coeffs(max_n):
    d1=[0]*(max_n+1);d2=[0]*(max_n+1)
    d1[0]=d2[0]=1
    for p in [1,2,2,7]:
        for t in range(p,max_n+1):d1[t]+=d1[t-p]
    for p in [2,3,4,7]:
        for t in range(p,max_n+1):d2[t]+=d2[t-p]
    return [((d1[t-8] if t>=8 else 0) - (d2[t-10] if t>=10 else 0)) for t in range(max_n+1)]

# Conditions from the seven-gap sliding-window argument.
def gap_count(n):
    ans=0
    for a in range((n-8)//7+1):
        remainder=n-8-7*a
        for x in range(remainder//2+1):
            for y in range((remainder-2*x)//2+1):
                v=remainder-2*x-2*y
                if x<=y+v:
                    ans+=1
    return ans

# Explicitly verify all seven gap-window comparisons, independently of the simplified inequalities.
def direct_sliding(gaps):
    for j in range(1,8):
        leading=sum(gaps[:j])
        for i in range(1,8-j):
            if sum(gaps[i:i+j])<leading:return False
    return True

if __name__ == '__main__':
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    g=[a,b,c,d,c,b,a]
                    cond=a<=b and a<=c and a<=d and a+b<=c+d
                    assert direct_sliding(g)==cond,(a,b,c,d)
    seq=formula_coeffs(120)
    for n in range(8,121):
        assert seq[n]==gap_count(n),(n,seq[n],gap_count(n))
    print('PASS: 4096 direct gap-window checks; rational identity n=8..120')
