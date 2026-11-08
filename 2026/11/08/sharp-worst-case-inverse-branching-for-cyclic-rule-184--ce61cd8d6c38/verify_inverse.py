#!/usr/bin/env python3
"""Independent inverse-swap count and cyclic clause-law verification."""
from collections import Counter


def successor(x,n):
    # Simultaneously replace every 10 on the cyclic input by 01.
    bits=[(x>>i)&1 for i in range(n)]
    moved=[bits[i]==1 and bits[(i+1)%n]==0 for i in range(n)]
    after=bits[:]
    for i,t in enumerate(moved):
        if t:
            after[i]=0
            after[(i+1)%n]=1
    return sum(bit<<i for i,bit in enumerate(after))


def swaps(y,n):
    bits=[(y>>i)&1 for i in range(n)]
    possible=[i for i in range(n) if bits[i]==0 and bits[(i+1)%n]==1]
    count=0
    # This is deliberately not based on predecessor enumeration.
    for mask in range(1<<len(possible)):
        chosen={possible[j] for j in range(len(possible)) if (mask>>j)&1}
        valid=True
        for i in range(n):
            if bits[i]==1 and bits[(i+1)%n]==0:
                if (i-1)%n not in chosen and (i+1)%n not in chosen:
                    valid=False
                    break
        if valid:count+=1
    return count


def clause_dp(y,n):
    bits=[(y>>i)&1 for i in range(n)]
    zeros_to_ones=[i for i in range(n) if bits[i]==0 and bits[(i+1)%n]==1]
    ones_to_zeros=[i for i in range(n) if bits[i]==1 and bits[(i+1)%n]==0]
    assert len(zeros_to_ones)==len(ones_to_zeros)
    if not zeros_to_ones:return 1
    t=len(zeros_to_ones)
    constraints=[]
    for v in ones_to_zeros:
        allowed=[]
        if bits[(v-1)%n]==0:
            allowed.append((v-1)%n)
        if bits[(v+2)%n]==1:
            allowed.append((v+1)%n)
        constraints.append(allowed)
    c=0
    for assignment in range(1<<t):
        selected={zeros_to_ones[i] for i in range(t) if (assignment>>i)&1}
        if all(any(i in selected for i in options) for options in constraints):c+=1
    return c

for n in range(1,15):
    true_counts=Counter(successor(x,n) for x in range(1<<n))
    for y in range(1<<n):
        a=true_counts[y]
        b=swaps(y,n)
        c=clause_dp(y,n)
        assert a==b==c,(n,y,a,b,c)
    print('verified_n',n)
print('INVERSE_VERIFY_OK')
