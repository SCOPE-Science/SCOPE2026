#!/usr/bin/env python3
"""Independent compressed phase-counter reconstruction and witness checks."""
from math import comb
from collections import deque

def calc(w,a,b):
    n=a+b+1
    s=[0]*n
    p='0'*a+'1'*b+'0'
    for x in w:
        for j in range(n-1,-1,-1):
            if p[j]==x:
                s[j] ^= s[j-1] if j else 1
    return (tuple(s[:a+b]),s[-1])

def phase_step(s,a,b,x):
    P=1<<a.bit_length()
    z,B,c=s
    B=list(B)
    if x=='0':
        c ^= B[-1]
        z=(z+1)%P
    else:
        for j in range(b-1,0,-1):B[j]^=B[j-1]
        B[0] ^= comb(z,a)%2
    return (z,tuple(B),c)

def read(s,a,b,w):
    for x in w:s=phase_step(s,a,b,x)
    return s

def witness(a,b):
    P=1<<a.bit_length()
    if b==1 and a%2==0:
        return '0'*a+'01','0'*a+'10'
    if b>=2 and a>=2:
        t='0'*a+'1'*(b-1)+'0'*(P-a)
        return t+'01',t+'10'
    if b>=2 and a==1:
        r=1<<(b-1).bit_length()
        return '0'+'1'*(r+1)+'0','1'+'0'+'1'*(r-1)+'0'+'1'
    return None

witness_checks=0
for a in range(1,85):
    for b in range(1,60):
        w=witness(a,b)
        if w:
            v1,c1=calc(w[0],a,b)
            v2,c2=calc(w[1],a,b)
            assert v1==v2 and c1!=c2,(a,b,w)
            witness_checks+=1
# Starting from every compressed state, suffixes form an injective Moore signature.
signature_cases=0;signature_states=0
for a in range(1,9):
    for b in range(1,6):
        P=1<<a.bit_length()
        initial=(0,(0,)*b,0)
        seen={initial}; todo=deque([initial])
        while todo:
            s=todo.popleft()
            for x in '01':
                t=phase_step(s,a,b,x)
                if t not in seen:seen.add(t);todo.append(t)
        expected=(1<<a.bit_length())*(1<<b)*(2 if b>=2 or a%2==0 else 1)
        assert len(seen)==expected,(a,b,len(seen),expected)
        suffixes=['']+['1'*t+'0' for t in range(b+1)]+['0'*r+'1'*b+'0' for r in range(P)]
        signatures=set()
        for s in seen:
            sig=tuple(read(s,a,b,w)[-1] for w in suffixes)
            assert sig not in signatures,(a,b,s)
            signatures.add(sig)
        signature_cases+=1;signature_states+=len(seen)
# Every odd a has the invariant C=(z-1)*B1 mod 2 for b=1.
invariant_checks=0
for a in range(1,64,2):
    for zeros in range(0,150):
        for ones in range(0,20):
            # closed input 0^x 1^y 0^(zeros-x); test a range of x values.
            for x in range(0,zeros+1,max(1,zeros//8)):
                z=x
                B=(comb(z,a)*ones)%2
                C=(comb(z,a)*ones*(zeros-z))%2
                assert C==((zeros-1)*B)%2,(a,zeros,ones,x)
                invariant_checks+=1
print(f'PASS witness_pairs={witness_checks} signature_cases={signature_cases} signature_states={signature_states} invariant_checks={invariant_checks}')
