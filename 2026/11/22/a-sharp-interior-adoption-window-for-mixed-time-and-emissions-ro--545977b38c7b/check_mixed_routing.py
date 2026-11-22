"""Exact rational checks for a two-link two-preference traffic model."""
from fractions import Fraction as F
from random import Random


def clip(z, lo, hi):
    return min(hi, max(lo, z))


def equilibrium(theta, a, b):
    x = clip(theta, a, b)
    # eco share on road 1; all remaining road-1 share is time-routing
    eco_1 = min(theta, b)
    time_1 = x - eco_1
    return x, eco_1, time_1


def check():
    rng = Random(180234)
    tests = 0
    for _ in range(3000):
        a = F(rng.randint(1, 30), 100)
        b = F(rng.randint(50, 90), 100)
        v = F(rng.randint(1, 30), 7)
        z = F(rng.randint(1, 30), 7)
        p = F(rng.randint(1, 30), 9)
        q = F(rng.randint(1, 30), 9)
        # positive affine link costs with prescribed preference crossover roots
        t1_0 = F(20)
        t2_0 = t1_0 + p * a - q * (1-a)
        e1_0 = F(20)
        e2_0 = e1_0 + v * b - z * (1-b)
        rho = z/(v+z)
        s = (b+rho)/2
        for theta in (F(0),F(1),a,b,s, F(rng.randint(0,100),100)):
            x, eco_1, time_1 = equilibrium(theta,a,b)
            assert 0<=time_1<=1-theta
            assert 0<=eco_1<=theta
            assert x == eco_1+time_1
            dt = t1_0+p*x-(t2_0+q*(1-x))
            de = e1_0+v*x-(e2_0+z*(1-x))
            if time_1>0: assert dt<=0
            if time_1<1-theta: assert dt>=0
            if eco_1>0: assert de<=0
            if eco_1<theta: assert de>=0
            G=x*(e1_0+v*x)+(1-x)*(e2_0+z*(1-x))
            star=clip(s,a,b)
            Gstar=star*(e1_0+v*star)+(1-star)*(e2_0+z*(1-star))
            assert G-Gstar==(v+z)*((x-s)**2-(star-s)**2)
            assert G>=Gstar
            tests+=8
    # Concrete exact witness and pure strategy comparison
    a,b=F(1,5),F(4,5)
    s=F(1,2)
    assert equilibrium(F(0),a,b)[0]==a
    assert equilibrium(F(1),a,b)[0]==b
    G=lambda x: F(5)-5*x+5*x*x
    assert G(a)==G(b)==F(21,5)
    assert G(s)==F(15,4)
    assert G(a)-G(s)==G(b)-G(s)==F(9,20)
    print('PASS: 18,000 exact rational Wardrop instances; %d supplementary conditions; witness certified' % tests)
if __name__=='__main__': check()
