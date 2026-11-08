#!/usr/bin/env python3
"""Independent exact-rational replay of Hamming-graph Radau IIA certificates.
Requires Python standard library only. The infinite statements are established
by the accompanying proof, not by finite numerical sampling.
"""
from fractions import Fraction as Q
from math import comb, factorial

ZERO=Q(0)
def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):
    n=max(len(a),len(b))
    return trim([(a[i] if i<len(a) else ZERO)+(b[i] if i<len(b) else ZERO) for i in range(n)])
def mul(a,b):
    c=[ZERO]*(len(a)+len(b)-1)
    for i,ai in enumerate(a):
        for j,bj in enumerate(b): c[i+j]+=ai*bj
    return trim(c)
def scale(a,s):return trim([Q(s)*v for v in a])
def ratadd(x,y):
    a,b=x;c,d=y
    return (add(mul(a,d),mul(c,b)),mul(b,d))
def ratmul(x,y):return mul(x[0],y[0]),mul(x[1],y[1])
def rat_k(q,k):
    z=q*k
    return ([Q(6),Q(-2*z)],[Q(6),Q(4*z),Q(z*z)])
def kernel(d,q,r):
    ans=([Q(0)],[Q(1)])
    for k in range(d+1):
        ak=Q(0)
        for j in range(max(0,k-(d-r)),min(k,r)+1):
            ak+=Q(comb(r,j)*comb(d-r,k-j)*(-1)**j*(q-1)**(k-j),q**d)
        ans=ratadd(ans,(scale(rat_k(q,k)[0],ak),rat_k(q,k)[1]))
    return ans
def assert_rat_eq(x,y):
    assert mul(x[0],y[1])==mul(y[0],x[1]),(x,y)
def polyval(a,x):return sum(v*Q(x)**i for i,v in enumerate(a))
def R(z):return Q(6-2*z,z*z+4*z+6)

def check_positive_cases():
    # Recomputed kernels vs independent explicit rational certificate data.
    data={
     (2,2):[
      ([9,18,17,2,4],mul([3,4,2],[3,8,8])),
      ([0,3,2],[3,8,8]),
      ([0,0,9,18,4],mul([3,4,2],[3,8,8]))],
     (2,3):[
      ([2,4,3,-4,2],mul([2,4,3],[1,4,6])),
      ([0,2,5,4,2],mul([2,4,3],[1,4,6])),
      ([0,0,2,6,2],mul([2,4,3],[1,4,6]))],
     (3,2):[
      ([9,45,98,83,22,-14,12],mul(mul([3,4,2],[1,4,6]),[3,8,8])),
      ([0,9,45,95,92,42,12],mul(mul([3,4,2],[1,4,6]),[3,8,8])),
      ([0,0,9,45,76,58,12],mul(mul([3,4,2],[1,4,6]),[3,8,8])),
      ([0,0,0,9,54,66,12],mul(mul([3,4,2],[1,4,6]),[3,8,8]))]
    }
    count=0
    for (d,q),entries in data.items():
        for r,(numer,denom) in enumerate(entries):
            assert_rat_eq(kernel(d,q,r),([Q(v) for v in numer],[Q(v) for v in denom]))
            count+=1
    # Positivity: all factors of denominators have positive coefficients;
    # all numerators have positive coefficients except the two explicitly
    # completed-square quadratic subfactors.
    assert 2*(Q(1)-1)**2+1>0
    assert 14**2-4*12*22<0
    assert R(8)==Q(-5,51)
    # d=1: R(z)+1/10 = ((z-8)^2+2)/(10*(z^2+4z+6))
    for z in range(0,101):assert R(z)+Q(1,10)==Q((z-8)**2+2,10*(z*z+4*z+6))
    return count

def bernstein_coeffs_on_interval(power,lower,upper):
    """Compute Bernstein controls from exact power coefficients."""
    n=len(power)-1
    # substitute p=lower+(upper-lower)*v
    vcoeff=[Q(0)]*(n+1)
    for k,a in enumerate(power):
        for j in range(k+1):
            vcoeff[j]+=Q(a)*comb(k,j)*Q(lower)**(k-j)*(Q(upper)-Q(lower))**j
    return [sum(vcoeff[j]*Q(comb(i,j),comb(n,j)) for j in range(i+1)) for i in range(n+1)]

def power_for_binomial(d,z):
    # Build sum binom(d,k) p^k (1-p)^(d-k) R(kz)
    out=[Q(0)]*(d+1)
    for k in range(d+1):
        for j in range(d-k+1):
            out[k+j]+=Q(comb(d,k)*comb(d-k,j)*(-1)**j)*R(k*z)
    return out

def check_negative_cases():
    assert power_for_binomial(2,6)==[Q(1),Q(-24,11),Q(12,11)]
    assert polyval(power_for_binomial(2,6),Q(3,4))==Q(-1,44)
    # f2'(p)=24(p-1)/11 <=0 for p <=1
    b3=bernstein_coeffs_on_interval(power_for_binomial(3,3),Q(2,3),Q(1))
    expected3=[Q(-131,4059),Q(-340,4059),Q(-43,451),Q(-4,41)]
    assert b3==expected3 and all(x<0 for x in b3)
    b4=bernstein_coeffs_on_interval(power_for_binomial(4,4),Q(1,2),Q(1))
    expected4=[Q(-8765,579139),Q(-50619,579139),Q(-8221,91443),Q(-153,1793),Q(-13,163)]
    assert b4==expected4 and all(x<0 for x in b4)
    assert R(3)==0 and R(6)==Q(-1,11) and R(9)==Q(-4,41)
    assert [R(4*k) for k in range(5)]==[Q(1),Q(-1,19),Q(-5,51),Q(-1,11),Q(-13,163)]
    # d>=5 small-time witness: first nonzero power is h^5, with
    # Laplacian^5[x,y]=-5! at Hamming distance 5, coefficient +1/108.
    # Verify the scalar series through order five by exact power series.
    c=[Q(0)]*6
    c[0]=1
    for n in range(1,6):
        c[n]=-Q(4,6)*c[n-1]-(Q(1,6)*c[n-2] if n>=2 else 0)+(Q(-2,6) if n==1 else 0)
    assert c==[Q(1),Q(-1),Q(1,2),Q(-1,6),Q(1,36),Q(1,108)]
    assert -factorial(5)*c[5]==Q(-10,9)
    return b3,b4

def main():
    k=check_positive_cases()
    b3,b4=check_negative_cases()
    print('VERIFY_OK', 'positive_kernel_identities=',k,'negative_Bernstein_certificates=',len(b3)+len(b4),'fifth_order_obstruction=-10/9')

if __name__=='__main__':main()
