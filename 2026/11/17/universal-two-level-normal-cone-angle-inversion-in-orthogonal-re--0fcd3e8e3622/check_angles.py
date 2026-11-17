"""Self-contained numerical checks for normal-fan angular weights of orthogonal polygon joins.
This script is supplemental evidence, not a substitute for the analytical theorem.
"""
import math
import random


def simpson(f, lo, hi, n=1200):
    if n % 2: raise ValueError('n must be even')
    h = (hi-lo)/n
    acc = f(lo)+f(hi)
    for k in range(1,n):
        acc += (4 if k%2 else 2)*f(lo+k*h)
    return acc*h/3


def winner_integral(p, q, n=1200):
    a = math.pi/p
    b = math.pi/q
    def inner(alpha):
        c = math.cos(alpha)
        z = c/math.sqrt(1+c*c)
        return z*math.atan(z*math.tan(b))
    return p*q/(math.pi**2)*simpson(inner,0,a,n)


def winner_double(p, q, n=200):
    a,b=math.pi/p, math.pi/q
    def outer(x):
        ca=math.cos(x)**2
        return simpson(lambda y:ca/(ca+math.cos(y)**2),0,b,n)
    return p*q/(math.pi**2)*simpson(outer,0,a,n)


def winner_limit(p):
    return 1-(p/(math.pi*math.sqrt(2)))*math.atan(math.tan(math.pi/p)/math.sqrt(2))


def monte_carlo(p, q, seed=987654, n=150_000):
    rng=random.Random(seed)
    w=0
    # Angular reduction is independent from the square radius beta(1,1).
    for _ in range(n):
        d1=rng.random()*math.pi/p
        d2=rng.random()*math.pi/q
        u=rng.random()
        if u*math.cos(d1)**2 > (1-u)*math.cos(d2)**2:
            w+=1
    return w/n


def direct_gaussian_check(p=4, q=5, seed=87654, n=100_000):
    rng = random.Random(seed)
    verts_p = [(math.cos(2*math.pi*j/p),math.sin(2*math.pi*j/p)) for j in range(p)]
    verts_q = [(math.cos(2*math.pi*j/q),math.sin(2*math.pi*j/q)) for j in range(q)]
    winner_counts = [0]*(p+q)
    for _ in range(n):
        g1,g2,g3,g4 = (rng.gauss(0,1) for z in range(4))
        scores=[g1*x+g2*y for x,y in verts_p]+[g3*x+g4*y for x,y in verts_q]
        best=max(range(p+q),key=lambda i:scores[i])
        winner_counts[best]+=1
    group_wins=sum(winner_counts[:p])/n
    predicted=winner_integral(p,q)
    assert abs(group_wins-predicted)<.006,(group_wins,predicted)
    for i,cnt in enumerate(winner_counts):
        expected=predicted/p if i<p else (1-predicted)/q
        assert abs(cnt/n-expected)<.008,(i,cnt/n,expected)
    print('independent Gaussian support check:',group_wins, 'vertex counts:',winner_counts)


def run():
    for p in range(3,17):
        assert winner_limit(p)>0.39 and winner_limit(p)<0.5
        for q in range(p+1, min(p+20, 30)):
            f=winner_integral(p,q,400)
            assert p/(p+q)<f<0.5, (p,q,f)
            assert f>winner_limit(p), (p,q,f)
            if q<12:
                assert abs(f+winner_integral(q,p,400)-1)<1e-10
    for p,q in [(3,4),(3,5),(4,5),(4,9),(5,8),(7,11),(11,13)]:
        f=winner_integral(p,q)
        g=winner_double(p,q,240)
        assert abs(f-g)<1e-11,(p,q,f,g)
        print(f'{p},{q}: 1D={f:.12f} 2D={g:.12f} p-vertex={f/p:.12f} q-vertex={(1-f)/q:.12f}')
    f=winner_integral(4,5)
    assert 0.47968<f<0.47969
    direct_gaussian_check()
    empirical=monte_carlo(4,5)
    print('square-pentagon simulation:',empirical,'analytical:',f)
    assert abs(empirical-f)<0.005
    print('All independent deterministic and sampling checks passed')

if __name__=='__main__':run()
