"""Independent finite-precision spot checks for a covering-radius asymptotic.
The theorem's infinite and optimality claims depend on the written analytic proof.
"""
import math

def H(t):
    return -t*math.log(t)-(1-t)*math.log1p(-t) if 0<t<1 else 0.

def kappa(n):
    u=H(0.5+1/n)
    return 0.5*u if n%2==0 else 0.25*(math.log(2)+u)

def circle(x,y):
    delta=(x-y)%1.0
    return min(delta,1-delta)

def radius_at(n,p,x,y):
    return min((circle(x,j/n)**p+circle(y,j/n)**p)**(1/p) for j in range(n))

def candidate(n,p):
    eps=p-1
    if n%2==0:
        x=-0.25+0.5/n
        z=0.
    else:
        x=-0.25
        plus=0.5*math.log(2)
        minus=0.5*H(0.5+1/n)
        z=(plus-minus)/2
    return radius_at(n,p,x,x+0.5+eps*z)

def main():
    # Exact numerical equivalence of the n=3 coefficient with its earlier form.
    expected=math.log(12)/4-5*math.log(5)/24
    assert abs(kappa(3)-expected)<1e-14
    for n in range(3,17):
        for eps in (1e-3,1e-4,1e-5):
            observed=(0.5-candidate(n,1+eps))/eps
            assert abs(observed-kappa(n))<0.003, (n,eps,observed,kappa(n))
        # Sample 512 unoptimized positions; every sample must stay below 1/2
        for k in range(512):
            x=((37*k)%512)/512
            y=((191*k)%512)/512
            assert radius_at(n,1.2,x,y)<0.5
    for p in (1,1.001,1.1,2,8):
        assert abs(radius_at(2,p,0.,0.5)-0.5)<1e-12
    print('PASS: n=3..16, 42 directional finite-difference tests, 7168 sampled points, n=2 endpoint checks.')
if __name__=='__main__':main()
