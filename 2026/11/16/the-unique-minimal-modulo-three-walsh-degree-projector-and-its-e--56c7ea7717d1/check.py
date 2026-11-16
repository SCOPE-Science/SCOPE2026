#!/usr/bin/env python3
"""Independent integer checks for Hamming-mod-3 Walsh frequency projections."""
from math import comb

def A(n):
    return sum(comb(n,2*j)*3**j for j in range(n//2+1))

def predicted(n,r):
    rstar=(2*n)%3
    c=(-1)**((n-2*rstar)//3)
    num=2**n + 2*A(n) + 2*c - 2
    if r!=rstar: num+= 2*A(n-1)+1-3*c
    assert num%3==0,(n,r,num)
    return num//3

def krawtchouk_sum(n,k,r):
    return sum(sum((-1)**j*comb(k,j)*comb(n-k,w-j)
                   for j in range(max(0,w-n+k),min(k,w)+1))
               for w in range(r,n+1,3))

def fwht(a):
    a=a[:]
    h=1
    while h<len(a):
        for start in range(0,len(a),2*h):
            for j in range(start,start+h):
                v=a[j]; w=a[j+h]
                a[j]=v+w; a[j+h]=v-w
        h*=2
    return a

for n in range(3,19):
    a=[]
    for r in range(3):
        if n<=12:
            kernel=fwht([int(x.bit_count()%3==r) for x in range(1<<n)])
            num=sum(abs(x) for x in kernel)
            assert num==sum(comb(n,k)*abs(krawtchouk_sum(n,k,r)) for k in range(n+1))
        else:
            num=sum(comb(n,k)*abs(krawtchouk_sum(n,k,r)) for k in range(n+1))
        assert num==predicted(n,r),(n,r,num,predicted(n,r))
        a.append(num)
    m=(2*n)%3
    assert a[m]<a[(m+1)%3]==a[(m+2)%3],(n,a)
    print(f'n={n} numerator={a} denominator={1<<n} minimizer={m}')
for n in range(3,101):
    m=2*n%3
    c=(-1)**((n-2*m)//3)
    assert 2*A(n-1)+1-3*c>0
    assert A(n+1)==A(n)+3*sum(comb(n,2*j+1)*3**j for j in range((n+1)//2))
print('MOD3_PROJECTION_EXACT_PASS n=3..18; inequality n=3..100')
