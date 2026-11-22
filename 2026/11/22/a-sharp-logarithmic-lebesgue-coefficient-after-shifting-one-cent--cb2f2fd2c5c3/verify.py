"""Reproducible finite checks for one displaced Chebyshev–Lobatto node.

Finite checks are diagnostics, not a replacement for the all-degree proof.
Run: python3 verify.py
"""
import math


def maximizer(alpha):
    def g(u):
        z = math.pi*u
        return math.pi*u*u*math.cos(z)/(math.sin(z)-z*math.cos(z))
    lo, hi = 1.e-6, 0.5
    for _ in range(100):
        mid = 0.5*(lo+hi)
        if g(mid) > alpha:
            lo = mid
        else:
            hi = mid
    u = 0.5*(lo+hi)
    return u, (2/math.pi)*math.sin(math.pi*u)*(1+alpha/u)


def transformed_cardinals(n, alpha, t):
    """Evaluate the exact rank-one node replacement identities."""
    assert n >= 4 and n % 2 == 0 and 0 < alpha < 1
    j = n//2
    theta = math.pi/2 + math.pi*t/n
    x = -math.sin(math.pi*t/n)
    y = -math.sin(math.pi*alpha/n)
    # Avoid the interpolation nodes (none of the test points below coincide).
    W = -math.cos(math.pi*t/n)*((-1)**j)*math.sin(math.pi*t)
    ell_j_y = math.cos(math.pi*alpha/n)*math.sin(math.pi*alpha)/(n*math.sin(math.pi*alpha/n))
    out = []
    for i in range(n+1):
        if i == j:
            ell_j = W/(n*((-1)**j)*x)
            out.append(ell_j/ell_j_y)
        else:
            xi = math.cos(i*math.pi/n)
            Wi = n*((-1)**i)*(2 if i == 0 or i == n else 1)
            li = W/(Wi*(x-xi))
            out.append(li*(x-y)/x*xi/(xi-y))
    return out


def reference_cardinals(n, alpha, t):
    """Independent product interpolation for small n, without rank-one identity."""
    nodes = [math.cos(i*math.pi/n) for i in range(n+1)]
    nodes[n//2] = -math.sin(math.pi*alpha/n)
    x = -math.sin(math.pi*t/n)
    weights=[]
    for i, xi in enumerate(nodes):
        top=1.0
        bot=1.0
        for k, xk in enumerate(nodes):
            if k!=i:
                top *= x-xk
                bot *= xi-xk
        weights.append(top/bot)
    return weights


def local_lebesgue(n, alpha, t):
    return sum(map(abs,transformed_cardinals(n,alpha,t)))


def run():
    count=0
    for n in (4,6,10,16):
        for alpha in (0.15,0.5,0.85):
            for t in (-0.37,-0.18,0.11,0.37):
                if abs(t-alpha)<1.e-8:
                    continue
                a=transformed_cardinals(n,alpha,t)
                b=reference_cardinals(n,alpha,t)
                assert max(abs(x-y) for x,y in zip(a,b))<2.e-8
                assert abs(sum(a)-1)<2.e-8
                count+=2
    for alpha in (0.2,0.5,0.8):
        u, C = maximizer(alpha)
        assert 0<u<0.5 and C>2/math.pi
        count+=2
        vals=[]
        for n in (1024,4096,16384):
            val=local_lebesgue(n,alpha,-u)
            assert abs(val-C*math.log(n))<12.0
            vals.append(val)
            count+=1
        # A bounded correction cancels in scale-to-scale differences.
        estimate=(vals[-1]-vals[1])/math.log(4)
        assert abs(estimate-C)<0.02, (alpha,estimate,C)
        count+=1
    print('PASS:',count,'finite assertions; exact cardinal identities, unique-root estimates, and logarithmic scales')


if __name__=='__main__':
    run()
