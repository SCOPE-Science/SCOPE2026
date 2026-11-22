"""Exact-rational checks accompanying the three-shock tail-concordance theorem.

Run with Python 3.9+ as `python checks.py`. The symbolic proof and analytic
continuity argument are supplied separately; finite checks are corroborative.
"""
from fractions import Fraction as F

checks = 0

def check(statement):
    global checks
    assert statement
    checks += 1

def directional(p, q):
    assert sum(p) == sum(q) == 1 and all(x > 0 for x in p + q)
    r = [q[i] / p[i] for i in range(len(p))]
    k = lambda i, j: min(r[i] / r[j], r[j] / r[i])
    x = sum(p[i] * p[j] * k(i, j)
            for i in range(len(p)) for j in range(len(p)))
    y = sum(q[i] * q[j] * k(i, j)
            for i in range(len(p)) for j in range(len(p)))
    return x, y

def exponent(p, q, s, u):
    return sum(max(s * a, u * b) for a, b in zip(p, q))

def family(t):
    p = [F(2, 3) - F(8, 9) * t, t, F(1, 3) - t / 9]
    q = [p[0] / 2, F(2, 3) * p[1], 2 * p[2]]
    return p, q

p = [F(2,5), F(3,10), F(3,10)]
q = [F(1,5), F(1,5), F(3,5)]
check(sum(p) == sum(q) == 1)
check(directional(p, q) == (F(16,25), F(16,25)))
check(sum(min(x,y) for x,y in zip(p,q)) == F(7,10))
check(exponent(p,q,2,3) == F(16,5))
check(exponent(p,q,3,2) == F(33,10))
for numer in range(250, 351):
    t = F(numer,1000)
    a,b = family(t)
    check(all(z > 0 for z in a+b))
    check(sum(a)==sum(b)==1)
    check(directional(a,b)[0] - directional(a,b)[1] ==
          2*t*(10*t-3)/81)
    check(exponent(a,b,3,2)-exponent(a,b,2,3) == t/3)
check(directional(*family(F(1,4)))[0] - directional(*family(F(1,4)))[1] == -F(1,324))
check(directional(*family(F(7,20)))[0] - directional(*family(F(7,20)))[1] == F(7,1620))
for i in range(1,80):
    for j in range(1,80):
        x=F(i,81)
        y=F(j,81)
        a,b=directional([x,1-x],[y,1-y])
        check((a==b) == ((x==y) or (x+y==1)))
print(f"PASS {checks} exact rational assertions")
