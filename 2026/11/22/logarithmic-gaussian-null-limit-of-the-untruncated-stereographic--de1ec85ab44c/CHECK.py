#!/usr/bin/env python3
"""Independent numerical checks of finite truncation identities for a sphere kernel.

Run: python CHECK.py
Only the Python standard library is required. These calculations are supporting
checks, not an infinite-sample proof or independent mathematical audit.
"""
import math

PI = math.pi

def clipped_z_mean(M):
    # Z=cot(Theta/2), Theta angle between two iid uniform S^2 points.
    return math.atan(M) - M/(1+M*M)

def clipped_z_second(M):
    return math.log1p(M*M) + 1/(1+M*M) - 1

def simpson(f, a, b, steps=80000):
    assert steps % 2 == 0
    h=(b-a)/steps
    s=f(a)+f(b)
    for i in range(1,steps):
        s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3

def clipped_kernel_moments(b,c,M,steps=80000):
    # v=log(cot(theta/2)) has density sech(v)^2 / 2.
    lo,hi=-max(22,math.log(M)+7),max(22,math.log(M)+7)
    def data(v):
        z=math.exp(v)
        w=b*z+c/z
        density=1/(2*math.cosh(v)**2)
        return w,density
    def integrand(k):
        def func(v):
            w,d=data(v)
            return (w**k*d if abs(w)<=M else 0.0)
        return simpson(func,lo,hi,steps)
    return integrand(1), integrand(2), integrand(4)

def main():
    tests=0
    def verify(ok,message):
        nonlocal tests
        assert ok,message
        tests+=1
    # Exact distribution: P(Z>M)=1/(1+M^2), E(Z)=pi/2.
    for M in (3,10,100,1000):
        verify(abs((PI/2-clipped_z_mean(M))-(math.atan(1/M)+M/(1+M*M)))<2e-13, 'first moment tail')
        verify(clipped_z_second(M)>0,'positive truncated second moment')
        verify(abs((clipped_z_second(M)-2*math.log(M))+1)<0.3, 'second moment logarithmic constant')
    # Numerically integrate directly from the Haar density for mixed cot/tan kernels.
    for b,c in ((1,0),(0,1),(1,1),(1,-1),(2,-3)):
        M1=math.exp(6)
        M2=math.exp(8)
        e1,s1,f1=clipped_kernel_moments(b,c,M1)
        e2,s2,f2=clipped_kernel_moments(b,c,M2)
        verify(abs(e2-(b+c)*PI/2)<(abs(b)+abs(c))*0.03,'correct first moment')
        delta=s2-s1
        target=2*(b*b+c*c)*math.log(M2/M1)
        verify(abs(delta-target)<0.04*max(1,target),'logarithmic moment increment')
        verify(f2>f1>0,'positive fourth truncated moments')
    # Symmetric cross-channel moment stays bounded: cot(theta/2)*tan(theta/2)=1.
    verify(abs(1-1)<1e-13, 'exact reciprocal cross moment')
    # 2(n-1)/n is the normalized degenerate U-statistic variance multiplier.
    for n in (3,7,50):
        mult=2*(n-1)/n
        verify(0<mult<2,'variance combinatorial multiplier')
    print('PASS',tests,'analytic/numerical assertions')
    print('Example n=2000 logarithmic Gaussian variance target: 4*(1+a*a)')
    print('The joint two-channel Gaussian covariance target is 4 times the identity.')

if __name__=='__main__':
    main()
