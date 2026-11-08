#!/usr/bin/env python3
"""Direct predecessor calculation from binary ring configurations, n <= 14."""

def image22(x,n):
    y=0
    for i in range(n):
        if ((x>>((i-1)%n))&1)+((x>>i)&1)+((x>>((i+1)%n))&1)==1:
            y |= 1<<i
    return y

T={0:3,1:1,2:1}
for n in range(3,15):T[n]=T[n-1]+T[n-3]
for n in range(1,15):
    freq=[0]*(1<<n)
    for x in range(1<<n):freq[image22(x,n)] += 1
    assert freq[0] == T[n]+1
    assert max(freq)==freq[0] and freq.count(freq[0])==1
print('INDEPENDENT_BRUTE_PASS', 'n=1..14')
