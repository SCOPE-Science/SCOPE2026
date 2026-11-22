"""Reproduce deterministic arithmetic diagnostics for a two-class Langmuir mixture.

Run with Python 3 standard library: python CHECK.py
Finite diagnostics supplement, and do not replace, the analytic proof.
"""
import math
import random


def forward(a, b, w):
    assert 0 < a < b and 0 < w < 1
    c = w*b + (1-w)*a
    d = w*a + (1-w)*b
    p = a*b
    m = math.sqrt(p*c/d)
    h = 2*math.sqrt(p)/(math.sqrt(p)+math.sqrt(c*d))
    z = 2*p/(math.sqrt((c-d)**2+4*p)+(c-d))
    return m,h,z


def inverse(m, h, z):
    assert m>0 and 0<h<1 and z>0
    r = 2/h-1
    c = r*m
    p = z*m*(z+r*m)/(m+r*z)
    d = r*p/m
    disc = (c+d)**2-4*p
    b = (c+d+math.sqrt(disc))/2
    a = p/b
    w = (c-a)/(b-a)
    return a,b,w


def slope(x, a, b, w):
    c = w*b+(1-w)*a
    d = w*a+(1-w)*b
    p = a*b
    return 1-(c*d-p)*x/((x+c)*(p+d*x))


def half_occupancy(x,a,b,w):
    return w*x/(a+x)+(1-w)*x/(b+x)


def close(x,y,tol=3e-9):
    assert math.isclose(x,y,rel_tol=tol,abs_tol=tol*min(1,abs(y))) , (x,y)


def run():
    rng = random.Random(20261115)
    count=0
    for j in range(1500):
        a=10**rng.uniform(-2,2)
        b=a*(1+10**rng.uniform(-1,2))
        w=rng.uniform(0.01,0.99)
        m,h,z=forward(a,b,w)
        a2,b2,w2=inverse(m,h,z)
        for x,y in zip((a,b,w),(a2,b2,w2)):
            close(x,y);count+=1
        close(half_occupancy(z,a,b,w),0.5);count+=1
        close(slope(m,a,b,w),h);count+=1
        for fac in (0.001,0.2,0.8,1.2,3.0,100.0):
            assert slope(m*fac,a,b,w)>h-1e-12
            count+=1
    # Arbitrary realizable diagnostic triples, rather than forward-generated ones.
    for j in range(1500):
        m=10**rng.uniform(-2,2)
        z=10**rng.uniform(-2,2)
        h=rng.uniform(0.02,0.98)
        a,b,w=inverse(m,h,z)
        assert 0<a<b and 0<w<1;count+=1
        got=forward(a,b,w)
        for x,y in zip(got,(m,h,z)):
            close(x,y);count+=1
    a,b,w=1.,9.,.25
    m,h,z=forward(a,b,w)
    close(m,math.sqrt(27/7));count+=1
    close(h,6/(3+math.sqrt(21)));count+=1
    close(z,2+math.sqrt(13));count+=1
    print(f"PASS: {count} arithmetic and qualitative assertions")


if __name__ == '__main__':
    run()
