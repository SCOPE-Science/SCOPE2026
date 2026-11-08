"""Directly enumerate four-phase assignments, testing local Greenberg--Hastings constraints."""
from itertools import product
from math import factorial

def is_wave(a, b):
    n=len(a)
    for i,p in enumerate(a):
        # Phase p+2 must be absent in adjacent shore; phase p-1 must be present.
        if any(b[j]==(p+2)%4 for j in range(n) if j!=i):return False
        if not any(b[j]==(p-1)%4 for j in range(n) if j!=i):return False
    for i,p in enumerate(b):
        if any(a[j]==(p+2)%4 for j in range(n) if j!=i):return False
        if not any(a[j]==(p-1)%4 for j in range(n) if j!=i):return False
    return True

def expected(n):
    s=2**n-2
    return 2*s*(s-2*n)+(24 if n==4 else 0)

for n in range(3,6):
    count=0; anomalies=0
    choices=list(product(range(4), repeat=n))
    for a in choices:
        for b in choices:
            if is_wave(a,b):
                count+=1
                if not (set(a).issubset({0,2}) and set(b).issubset({1,3}) or set(a).issubset({1,3}) and set(b).issubset({0,2})):
                    anomalies+=1
    assert count==expected(n),(n,count,expected(n))
    assert anomalies==(24 if n==4 else 0),(n,anomalies)
    print(f'n={n}: phase_waves={count}; exceptional={anomalies}; formula=PASS')
for n in range(3,20):
    assert expected(n)>=0 and expected(n)%4==0
print('all exact formula values divisible by four for n=3..19')
