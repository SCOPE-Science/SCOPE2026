#!/usr/bin/env python3
"""Exact finite check for a Fibonacci-block maximum of mixed Beatty representations."""
from math import isqrt

def lower(k):
    assert k >= 1
    return (k + isqrt(5*k*k)) // 2

def upper(k):
    return lower(k) + k

F = [0,1]
for j in range(2,20):
    F.append(F[-1]+F[-2])
N = F[17]
low = []
up = []
for k in range(1,N+1):
    a,b=lower(k),upper(k)
    if a <= N: low.append(a)
    if b <= N: up.append(b)
r=[0]*(N+1)
for a in low:
    for b in up:
        if a+b>N:break
        r[a+b]+=1
assert len(low)==len(set(low)) and len(up)==len(set(up))
assert not (set(low)&set(up))
assert set(low)|set(up)==set(range(1,N+1))
for j in range(5,18):
    t=F[j-2]
    target=F[j]-2
    assert target not in {a+b for a in up if a<target for b in up if b<=target-a}
    assert sum(b<target for b in up)==t-1
for m in range(4,17):
    block=range(F[m], F[m+1]); assert block.stop<=N
    maximum=max(r[n] for n in block)
    winners=[n for n in block if r[n]==maximum]
    assert maximum==F[m-1]-1 and winners==[F[m+1]-2], (m,maximum,winners)
    assert r[F[m+1]-1]==0
print('VERIFY_OK fibonacci_blocks=13 F_m_range=4..16 largest_endpoint=' + str(N) + ' complement_up_to=' + str(N))
