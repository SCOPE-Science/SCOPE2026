#!/usr/bin/env python3
"""Finite-field exhaustive checks for cyclic Leibniz automorphism order and conjugacy counts."""
import itertools, collections, math

def mul(A,B,p):
    n=len(A); a=A[0]
    Bscaled=[B[j]*pow(a,j,p)%p for j in range(n)]
    return tuple(sum(A[i]*Bscaled[j-i] for i in range(j+1))%p for j in range(n))

def order(A,p):
    n=len(A); unit=(1,)+(0,)*(n-1); cur=unit
    for k in range(1,2*p**math.ceil(math.log(n,p))*(p-1)+1):
        cur=mul(cur,A,p)
        if cur==unit:return k
    raise ValueError('No order')

def formula(p,n):
    out=collections.Counter()
    for d in range(1,p):
        if (p-1)%d:continue
        phi=sum(math.gcd(j,d)==1 for j in range(1,d+1))
        previous=0
        for e in range(0,math.ceil(math.log(max(2,n),p))+2):
            at_most=phi*p**(n-1-(n-1)//(d*p**e))
            value=at_most-previous
            if value:out[d*p**e]+=value
            previous=at_most
    return out

def direct(p,n):
    counts=collections.Counter()
    for a in itertools.product(range(p),repeat=n):
        if a[0]:counts[order(a,p)]+=1
    return counts

if __name__=='__main__':
    for p,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(3,4),(3,5),(5,2),(5,3),(5,4),(7,3)]:
        f=formula(p,n); d=direct(p,n)
        assert f==d,(p,n,f,d)
        print('p=%s n=%s group=%s spectrum=%s'%(p,n,(p-1)*p**(n-1),sorted(d.items())))
    print('NULL_FILIFORM_ORDER_SPECTRA_VERIFIED')

# Independent extension-field enumeration: field elements are base-p encoded pairs.
def field_mul(a,b,p):
    a0,a1=a%p,a//p
    b0,b1=b%p,b//p
    if p==2: # t^2=t+1
        lo=(a0*b0+a1*b1)%p
        hi=(a0*b1+a1*b0+a1*b1)%p
    elif p==3: # t^2=-1
        lo=(a0*b0-a1*b1)%p
        hi=(a0*b1+a1*b0)%p
    else: raise ValueError(p)
    return lo+p*hi

def field_pow(a,k,p):
    r=1
    while k:
        if k&1:r=field_mul(r,a,p)
        a=field_mul(a,a,p);k//=2
    return r

def mul_ext(A,B,p):
    n=len(A);a=A[0]
    bs=[field_mul(B[j],field_pow(a,j,p),p) for j in range(n)]
    return tuple(sum_ext((field_mul(A[i],bs[j-i],p) for i in range(j+1)),p) for j in range(n))

def sum_ext(vals,p):
    return _sum_ext(vals,p)

def _sum_ext(vals,p):
    lo=hi=0
    for x in vals:lo+=x%p;hi+=x//p
    return lo%p+p*(hi%p)

def order_ext(A,p):
    n=len(A);unit=(1,)+(0,)*(n-1);cur=unit;q=p*p
    for k in range(1,(q-1)*p**(n+1)+1):
        cur=mul_ext(cur,A,p)
        if cur==unit:return k
    raise AssertionError(A)

def formula_q(q,n,p):
    out=collections.Counter()
    for d in range(1,q):
        if (q-1)%d:continue
        phi=sum(math.gcd(j,d)==1 for j in range(1,d+1))
        previous=0
        for e in range(0,n+2):
            at_most=phi*q**(n-1-(n-1)//(d*p**e))
            value=at_most-previous
            if value:out[d*p**e]+=value
            previous=at_most
    return out

if __name__=='__main__':
    for p,n in [(2,2),(2,3),(2,4),(3,2),(3,3)]:
        q=p*p;counts=collections.Counter()
        for aa in itertools.product(range(q),repeat=n):
            if aa[0]:counts[order_ext(aa,p)]+=1
        expected=formula_q(q,n,p)
        assert counts==expected,(q,n,counts,expected)
        print('q=%d n=%d spectrum=%s'%(q,n,sorted(counts.items())))
    print('EXTENSION_FIELD_SPECTRA_VERIFIED')

def mat_A(A,p):
    n=len(A);a=A[0]
    M=[[0]*n for _ in range(n)]
    for j in range(n):
        for i in range(j,n):
            M[i][j] = A[i-j]*pow(a,j,p)%p
    return M

def mmul(X,Y,p):
    n=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

if __name__=='__main__':
    for p,n in [(2,4),(3,4),(5,3)]:
        elems=[a for a in itertools.product(range(p),repeat=n) if a[0]]
        for A in elems:
            MA=mat_A(A,p)
            for B in elems:
                assert mmul(MA,mat_A(B,p),p)==mat_A(mul(A,B,p),p),(p,n,A,B)
        print('matrix_composition_checked p=%d n=%d pairs=%d'%(p,n,len(elems)**2))
    print('MATRIX_MODEL_VERIFIED')


def conjugacy_formula(p,n):
    out=collections.Counter()
    for d in range(1,p):
        if (p-1)%d: continue
        phi=sum(math.gcd(j,d)==1 for j in range(1,d+1))
        for t in range(n+1):
            numerator=0
            for e in range(1,p):
                if (p-1)%e: continue
                phi_e=sum(math.gcd(j,e)==1 for j in range(1,e+1))
                l=math.lcm(d,e)
                m=(n-1)//l
                z=p**(m-(n-1)//(l*p**t))
                prev=0 if t==0 else p**(m-(n-1)//(l*p**(t-1)))
                numerator+=phi_e*(z-prev)
            assert phi*numerator%(p-1)==0
            v=phi*numerator//(p-1)
            if v: out[d*p**t]+=v
    return out

def conjugacy_direct(p,n):
    elems=[a for a in itertools.product(range(p),repeat=n) if a[0]]
    N=len(elems); sums=collections.Counter()
    for a in elems:
        center=sum(mul(a,b,p)==mul(b,a,p) for b in elems)
        sums[order(a,p)]+=center
    assert all(v%N==0 for v in sums.values())
    return collections.Counter({k:v//N for k,v in sums.items()})

if __name__=='__main__':
    for p,n in [(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(5,2),(5,3)]:
        assert conjugacy_formula(p,n)==conjugacy_direct(p,n),(p,n)
        print('conjugacy_verified p=%s n=%s'%(p,n))
    print('JOINT_ORDER_CONJUGACY_VERIFIED')
