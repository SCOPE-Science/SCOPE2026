"""Independent finite-field enumeration for truncated-node algebra endomorphisms.

Enumerates generator images and tests the original relations, without
using the counting formula to filter candidates. Supports prime fields and F4.
"""
from itertools import product
from math import ceil

def plus(a,b,q):
    return (a^b) if q==4 else ((a+b)%q)

def times(a,b,q):
    if q!=4:return (a*b)%q
    z=0
    for j in range(2):
        if (b>>j)&1:z ^= (a<<j)
    if z&8:z^=0b1100   # X^3 = X^2+X over F2[X]/(X^2+X+1)
    if z&4:z^=0b0111
    return z

def mul(a,b,m,n,q):
    # [constant,x,...,x^(m-1),y,...,y^(n-1)]
    z=[0]*(m+n-1)
    z[0]=times(a[0],b[0],q)
    for i in range(1,m):
        for j in range(i+1):
            z[i]=plus(z[i],times(a[j],b[i-j],q),q)
    for i in range(1,n):
        for j in range(i+1):
            aj=a[0] if j==0 else a[m-1+j]
            bj=b[0] if i-j==0 else b[m-1+(i-j)]
            z[m-1+i]=plus(z[m-1+i],times(aj,bj,q),q)
    return tuple(z)

def power(a,t,m,n,q):
    v=(1,)+(0,)*(m+n-2)
    for _ in range(t):v=mul(v,a,m,n,q)
    return v

def formula(m,n,q):
    return q**(m+n-2)*(1+(m-ceil(m/n))*(q-1))*(1+(n-ceil(n/m))*(q-1))

def components(m,n):
    return ([(a,m-a) for a in range(1,m-ceil(m/n)+1)],
            [(a,n-a) for a in range(1,n-ceil(n/m)+1)])

def val(seq):
    return next((i for i,x in enumerate(seq,1) if x),len(seq)+1)

def direct(m,n,q):
    d=m+n-1
    zero=(0,)*d
    images=[(0,)+v for v in product(range(q),repeat=d-1)]
    cx=[x for x in images if power(x,m,m,n,q)==zero]
    cy=[y for y in images if power(y,n,m,n,q)==zero]
    Lx,Ly=components(m,n)
    count=0
    automorphisms=0
    for x in cx:
        for y in cy:
            if mul(x,y,m,n,q)!=zero:continue
            count+=1
            if m==n:
                diagonal=times(x[1],y[m],q)
                offdiagonal=times(x[m],y[1],q)
                determinant=plus(diagonal,offdiagonal,q) if q==4 else (diagonal-offdiagonal)%q
                automorphisms+=(determinant!=0)
            vx,vy=val(x[1:m]),val(y[1:m]); uy,ux=val(y[m:]),val(x[m:])
            assert any(vx>=a and vy>=b for a,b in Lx)
            assert any(uy>=a and ux>=b for a,b in Ly)
    assert count==formula(m,n,q),(m,n,q,count,formula(m,n,q))
    if m==n:
        expected=((q*q-1)*(q*q-q) if m==2 else
                  2*(q-1)**2*q**(2*m-2))
        assert automorphisms==expected,(m,n,q,automorphisms,expected)
    return count,len(Lx)*len(Ly)

def main():
    cases=[(2,2,2),(2,3,2),(3,2,2),(3,3,2),(3,4,2),
           (4,3,2),(4,4,2),(2,5,2),(3,3,3),(2,3,3),
           (3,4,3),(2,2,4),(2,3,4)]
    for m,n,q in cases:
        count,comp=direct(m,n,q)
        print(f'm={m} n={n} q={q}: maps={count}, geometric_components={comp}')
    print('TRUNCATED_NODE_ENDOMORPHISM_COUNTS_OK')

if __name__=='__main__':main()
