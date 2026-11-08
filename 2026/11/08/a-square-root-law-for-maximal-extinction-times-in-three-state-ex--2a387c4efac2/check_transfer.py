#!/usr/bin/env python3
"""Independent positive-Markov-meander DP; compare with differential-series coefficients."""
from collections import defaultdict

def coeffs(N):
    a=[1,2]
    for n in range(2,N):
        numerator=2*n*a[n-1]+3*(n-2)*a[n-2]
        assert numerator%n==0
        a.append(numerator//n)
    return a[:N]

def change(a,b):
    return (a==1 and b==0)-(a==0 and b==1)

# A right-end strict record has reversed initial letters (1,0) and height 1.
d={(0,1):1}
A=coeffs(102)
for n in range(2,102):
    ways=sum(d.values())
    assert 2*ways==A[n-1],(n,ways,A[n-1])
    if n<14:
        print(f'n={n}: one-end strict records={ways}; both ends={2*ways}; OK')
    new=defaultdict(int)
    for (state,height),count in d.items():
        for next_state in (0,1,2):
            h=height+change(state,next_state)
            if h>0:
                new[(next_state,h)]+=count
    d=new
print('TRANSFER_100_OK')
