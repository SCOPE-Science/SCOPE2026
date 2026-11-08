#!/usr/bin/env python3
"""Independent exhaustive output-fiber histogram for cyclic traffic Rule 184."""
from collections import Counter
from math import comb

def traffic(x, n):
    # Each particle with an empty site immediately to its right moves right.
    occupied = [(x >> j) & 1 for j in range(n)]
    after = occupied[:]
    for j in range(n):
        if occupied[j] == 1 and occupied[(j+1)%n] == 0:
            after[j] = 0
            after[(j+1)%n] = 1
    return sum(bit << j for j, bit in enumerate(after))

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):
            c[i+j]+=u*v
    return c

def add(a,b):
    c=[0]*max(len(a),len(b))
    for i,x in enumerate(a):c[i]+=x
    for i,x in enumerate(b):c[i]+=x
    return c

def scale(a,k):return [k*x for x in a]

def collision_polynomials(N):
    # Newton identities for the quartic eigenvalue power sums.
    a=[1,1]; b=[0,1]; c=[0,1,1]; d=[0,0,2]
    q=[[4],a,add(poly_mul(a,a),scale(b,2))]
    q.append(add(add(poly_mul(a,q[2]),poly_mul(b,q[1])),scale(c,-3)))
    q.append(add(add(add(poly_mul(a,q[3]),poly_mul(b,q[2])),scale(poly_mul(c,q[1]),-1)),scale(d,4)))
    for n in range(5,N+1):
        q.append(add(add(add(poly_mul(a,q[n-1]),poly_mul(b,q[n-2])),scale(poly_mul(c,q[n-3]),-1)),poly_mul(d,q[n-4])))
    for n in range(1,N+1):
        if n%2==0:
            q[n]=add(q[n],[0]*(n//2)+[2*(-1)**(n//2)])
    return q

if __name__=='__main__':
    predicted=collision_polynomials(140)
    for n in range(3,17):
        fibers=Counter(traffic(x,n) for x in range(1<<n))
        histogram=[0]*(n+1)
        for y,mult in fibers.items():
            k=y.bit_count()
            histogram[k]+=mult*mult
        assert len(predicted[n])==n+1,(n,len(predicted[n]))
        assert histogram==predicted[n],(n,histogram,predicted[n])
        assert histogram==histogram[::-1]
        print('DIRECT_OK',n,'total',sum(histogram),'central',histogram[n//2],'outcomes',len(fibers))
    print('DIRECT_EXHAUSTIVE_OK n=3..16, all particle-count sectors')
