"""Exact verification for the three-habitat extinction/colonization theorem.

Requires Python 3 and SymPy. This script rebuilds the transient generator,
checks a polynomial certificate, rational root brackets and the two-site case.
All assertions use exact rational/symbolic arithmetic.
"""
import sympy as sp

c, t = sp.symbols('c t', positive=True)


def extinction_time(extinctions, graph):
    n = len(extinctions)
    states = range(1, 1 << n)
    idx = {s: i for i, s in enumerate(states)}
    m = sp.zeros(len(idx))
    for state in states:
        i = idx[state]
        for v in range(n):
            if state & (1 << v):
                rate = extinctions[v]
                dest = state ^ (1 << v)
            else:
                rate = c * sum(
                    1 for a, b in graph
                    if (a == v and state & (1 << b))
                    or (b == v and state & (1 << a))
                )
                dest = state | (1 << v)
            m[i, i] += rate
            if dest:
                m[i, idx[dest]] -= rate
    v = m.inv(method='DM') * sp.ones(len(idx), 1)
    return sp.cancel(v[-1])


p = [
    -(t-1)*(20*t**5+200*t**4+775*t**3+1240*t**2+780*t+144),
    -2*(200*t**5+1238*t**4+2071*t**3-602*t**2-2640*t-912),
    -2*(12*t**5+1502*t**4+5551*t**3+1840*t**2-8202*t-4568),
    -4*(120*t**4+2774*t**3+3943*t**2-5786*t-6016),
    -8*(359*t**3+2243*t**2-1590*t-4564),
    -32*(2*t**3+202*t**2+51*t-1006),
    -384*(t**2+9*t-40),
    -512*(t-6),
]
N = sum(p[k]*c**k for k in range(8))
H = (128*c**4 + (96*t+288)*c**3
     + (16*t**2+276*t+232)*c**2
     + (96*t**2+180*t+78)*c
     + 12*t**3+36*t**2+33*t+9)
D = 2*t*(4*c+t+2)*(8*c+t+4)*H

path = [(0,1), (1,2)]
T_leaf = extinction_time([sp.Rational(1,2),t,1], path)
T_center = extinction_time([1,t/2,1], path)
assert sp.cancel((T_center-T_leaf)*D-N) == 0
print('Exact 7-state generator and polynomial difference: PASS')

# Each p[k] has exactly one positive root: Descartes sign changes (one),
# plus the signs at zero and infinity. Isolating rational intervals prove order.
intervals = [
    (sp.Rational(1),sp.Rational(1)),
    (sp.Rational(106,100),sp.Rational(107,100)),
    (sp.Rational(116,100),sp.Rational(117,100)),
    (sp.Rational(132,100),sp.Rational(133,100)),
    (sp.Rational(158,100),sp.Rational(159,100)),
    (sp.Rational(208,100),sp.Rational(209,100)),
    (sp.Rational(326,100),sp.Rational(327,100)),
    (sp.Rational(6),sp.Rational(6)),
]
for k in range(8):
    pk = sp.Poly(p[k],t)
    signs = [sp.sign(co) for co in pk.all_coeffs() if co != 0]
    changes = sum(a != b for a,b in zip(signs,signs[1:]))
    assert changes == 1, (k, changes)
    lo,hi = intervals[k]
    if lo==hi:
        assert pk.eval(lo) == 0
    else:
        assert pk.eval(lo) > 0 and pk.eval(hi) < 0, k
    if k<7:
        assert intervals[k][1] < intervals[k+1][0]
print('Unique ordered positive coefficient roots and rational isolators: PASS')

# Degree two cannot exhibit a switch between which vertex to protect.
T_two_low = extinction_time([sp.Rational(1,2),t],[(0,1)])
T_two_high = extinction_time([1,t/2],[(0,1)])
N2 = -(t-1)*(12*c**2+12*c*t+12*c+2*t**2+7*t+2)
D2 = t*(4*c+t+2)*(4*c+2*t+1)
assert sp.cancel((T_two_high-T_two_low)*D2-N2)==0
print('Two-site sharp-minimality certificate: PASS')

# Direct exact rational evaluations across representative parameter regions.
for tv in [sp.Rational(1,2),sp.Rational(1),sp.Rational(3,2),sp.Rational(2),sp.Rational(5),sp.Rational(6),sp.Rational(8)]:
    for cv in [sp.Rational(0),sp.Rational(1,10),sp.Rational(1),sp.Rational(3),sp.Rational(10)]:
        calc = sp.sign(sp.factor((T_center-T_leaf).subs({t:tv,c:cv})))
        cert = sp.sign(sp.expand(N).subs({t:tv,c:cv}))
        assert calc == cert, (tv,cv,calc,cert)
print('35 independently substituted exact parameter tests: PASS')

# Explicit t=2 crossover witness: exactly one positive root by Descartes.
w = sp.Poly(N.subs(t,2),c)
w_sign = [sp.sign(a) for a in w.all_coeffs() if a]
assert sum(x != y for x,y in zip(w_sign,w_sign[1:])) == 1
assert w.eval(sp.Rational(2584,1000)) < 0
assert w.eval(sp.Rational(2585,1000)) > 0
print('t=2 switch isolated in (2.584, 2.585): PASS')
print('ALL EXACT CHECKS PASSED')
