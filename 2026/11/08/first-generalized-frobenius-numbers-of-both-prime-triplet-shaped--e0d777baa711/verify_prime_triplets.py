#!/usr/bin/env python3
"""Exact-integer checks for first generalized Frobenius numbers of triplet-shaped generators.
Only finite corroboration; the accompanying symbolic argument proves all k.
"""

def p_one_frobenius(a,b,c):
    # Count unordered coin combinations (nonnegative coefficient vectors), saturated at 2.
    # A full tail is checked rather than only a proposed exceptional value.
    limit=4*a*a
    dp=[0]*(limit+1)
    dp[0]=1
    for coin in (a,b,c):
        for n in range(coin, limit+1):
            dp[n]=min(2,dp[n]+dp[n-coin])
    return max(n for n in range(limit+1) if dp[n] < 2), dp

def check():
    counts=[0,0]
    for k in list(range(1,61))+[64,71,82,97,113,127]:
        for form in (0,1):
            if form==0:
                a=6*k+5; b=a+2; c=a+6
                target=12*k*k+40*k+23
            else:
                a=6*k+7; b=a+4; c=a+6
                target=12*k*k+50*k+56
            got,dp=p_one_frobenius(a,b,c)
            assert got == target, (k,form,got,target)
            assert dp[target] <= 1 and all(v==2 for v in dp[target+1:]), (k,form)
            counts[form]+=1
    assert p_one_frobenius(5,7,11)[0] == 24
    assert p_one_frobenius(7,11,13)[0] == 45
    print('PASS: exact denumerant DP, 66 parameters per family, full checked tails to 4a^2')
    print('PASS: k=0 boundary exceptions (24 and 45)')
    print('Counts:',counts)

if __name__=='__main__': check()
