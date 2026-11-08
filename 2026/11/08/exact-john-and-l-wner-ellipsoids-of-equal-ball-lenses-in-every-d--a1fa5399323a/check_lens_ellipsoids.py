"""Supplementary numerical checks for the exact ellipsoids of an equal-ball lens.
Uses only the Python standard library. No numerical test certifies an infinite theorem.
"""
import math

def parameters(n,c):
    # Cancellation-free expression for the positive root when c is small.
    disc=math.hypot((n-1)*c*c, 2*math.sqrt(n)*c)
    x=((n-1)*c*c+disc)/(2*n)
    B=1-x
    A=B*(x-c*c)/x
    return math.sqrt(A),math.sqrt(B),x

def verify():
    checks=0
    for n in (2,3,4,5,9,20,50):
      for c in (0.0001,0.01,0.1,0.3,0.5,0.8,0.95,0.999):
        a,b,x=parameters(n,c)
        assert 0<a<1-c and 0<b<math.sqrt(1-c*c)
        assert abs((b*b-a*a)-a*c*math.sqrt(n))<2e-10
        assert abs((c+a/math.sqrt(n))**2+b*b*(1-1/n)-1)<2e-10
        for i in range(1001):
            t=i/1000
            inner=(c+a*t)**2+b*b*(1-t*t)
            outer=1-(2*c/(1+c))*t*(1-t)
            assert inner<=1+2e-12
            assert outer<=1+2e-12
            checks+=2
    print('PASS', checks, 'sampled inequalities; exact proof separate')
if __name__=='__main__':verify()
