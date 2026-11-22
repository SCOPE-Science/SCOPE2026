"""Exact finite verification for Markov binary-label permutation parity."""
from fractions import Fraction as F
from itertools import product


def direct(n, p):
    change = (1-p)/2
    stay = (1+p)/2
    total = F(0)
    for bits in product((0,1), repeat=n):
        weight = F(1,2)
        for j in range(1,n):
            weight *= stay if bits[j]==bits[j-1] else change
        inversions = sum(bits[i]>bits[j] for i in range(n) for j in range(i+1,n))
        total += weight * (-1 if inversions%2 else 1)
    return total


def matrix_values(nmax,p):
    states = [(b,z) for b in (0,1) for z in (0,1)]
    stay=(1+p)/2
    flip=(1-p)/2
    dist=[F(1,2),F(0),F(0),F(1,2)]
    result=[None]
    for n in range(1,nmax+1):
        result.append(sum(dist))
        temp=[F(0)]*4
        for i,(prev,one_parity) in enumerate(states):
            for current in (0,1):
                next_parity=(one_parity+current)%2
                pos=states.index((current,next_parity))
                phase = (-1)**one_parity if current==0 else 1
                temp[pos]+=dist[i]*(stay if current==prev else flip)*phase
        dist=temp
    return result


checks=0
for p in [F(0),F(1,6),F(1,3),F(1,2),F(3,4),F(1)]:
    seq=matrix_values(13,p)
    for n in range(1,12):
        assert seq[n]==direct(n,p),(n,p,seq[n],direct(n,p));checks+=1
    a=(1+p)**2/F(2)
    for n in range(1,10):
        assert seq[n+4]==a*seq[n+2]-p*p*seq[n];checks+=1
    assert seq[1]==1 and seq[2]==(1+p)/2
    assert seq[3]==(1+2*p-p*p)/2
    assert seq[4]==(1+3*p-p*p+p**3)/4
    checks+=4

# Independently enumerate 0, 1, 2 switch parity combinatorics.
for n in range(2,31):
    cnt1=0; cnt2=0
    for initial in (0,1):
        for k in range(1,n):
            bits=[initial]*k+[1-initial]*(n-k)
            inv=sum(bits[i]>bits[j] for i in range(n) for j in range(i+1,n))
            cnt1+= inv%2
        for k in range(1,n):
            for l in range(k+1,n):
                bits=[initial]*k+[1-initial]*(l-k)+[initial]*(n-l)
                inv=sum(bits[i]>bits[j] for i in range(n) for j in range(i+1,n))
                cnt2+=inv%2
    if n%2==0:
        assert cnt1==n//2
    else:
        assert cnt1==0 and cnt2==(n*n-1)//4
    checks+=1
print(f"PASS {checks} exact identities / finite enumerations")
