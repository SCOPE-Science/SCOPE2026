#!/usr/bin/env python3
"""Independent exact Eisenstein-integer Fourier transform of Fano weak three-colorings."""
from collections import Counter
from itertools import product

P=7
Q=3
size=Q**P
lines=sorted({tuple(sorted((a-1,b-1,(a^b)-1))) for a in range(1,8) for b in range(a+1,8)})
assert len(lines)==7 and len(set(lines))==7

def digits(z):
    return [(z//3**j)%3 for j in range(7)]

def legal(z):
    d=digits(z)
    return all(not (d[a]==d[b]==d[c]) for a,b,c in lines)

# Exact transform over Z[omega], omega^2+omega+1=0.
A=[(int(legal(z)),0) for z in range(size)]
colorings=sum(x for x,_ in A)
assert colorings==882
for axis in range(P):
    step=3**axis
    for base in range(0,size,3*step):
        for offset in range(step):
            i=base+offset
            a,b,c=A[i],A[i+step],A[i+2*step]
            def add(x,y): return (x[0]+y[0],x[1]+y[1])
            def omega(x): return (-x[1],x[0]-x[1])
            def omega2(x): return (-x[0]+x[1],-x[0])
            A[i]=add(add(a,b),c)
            A[i+step]=add(add(a,omega(b)),omega2(c))
            A[i+2*step]=add(add(a,omega2(b)),omega(c))

C=Counter(A)
expected={(0,0):1458, (882,0):1, (-171,0):14, (-90,0):42,
          (72,0):56, (18,0):252, (-9,0):364}
assert C==expected,(C,expected)
assert sum(a*a-a*b+b*b for a,b in A)==size*colorings
assert all((v==(0,0)) == (sum(digits(i))%3!=0) for i,v in enumerate(A))
assert min(abs(a) for a,b in A if a)!=0
assert min(abs(a) for a,b in A if a)==9
print('DIRECT_PASS', 'colorings',colorings,'full_rank',sum(v!=(0,0) for v in A), 'min_pos',9,'spectrum',sorted(((a,n) for (a,b),n in C.items())))
