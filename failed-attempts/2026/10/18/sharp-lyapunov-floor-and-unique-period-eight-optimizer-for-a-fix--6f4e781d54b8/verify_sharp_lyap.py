"""Exact tests for a sharp Lyapunov floor in a four-branch affine interval map.

These finite computations check the algebraic witness and finite itinerary
consequences. The universal result follows from the accompanying proof.
"""
from fractions import Fraction as Q

s, t, a = Q(4, 5), Q(5), Q(5)
rho = s**3*t - s - s**2 - s**3
q = rho / (1 + s**3*t)
assert Q(0) < rho < Q(1) and t*s**3 > 1
assert q == Q(76,445)

def f(x):
    assert -a*t <= x <= a*t
    if x <= -a:
        return s*(x+a)
    if x < 0:
        return t*(x+a)
    if x < a:
        return t*(x-a)
    return s*(x-a)

def branch(x):
    if x in (Q(0), -a, a):
        raise ValueError('boundary')
    return 'I' if abs(x) < a else 'O'

x = a*q
orbit = []
for _ in range(8):
    orbit.append(x)
    x = f(x)
assert x == a*q
assert orbit == [Q(76,89), -Q(1845,89), -Q(1120,89), -Q(540,89),
                 -Q(76,89), Q(1845,89), Q(1120,89), Q(540,89)]
assert [branch(v) for v in orbit] == list('IOOOIOOO')
assert (s**3*t)**2 == Q(4096,625)
assert all(f(orbit[i]) == orbit[(i+1)%8] for i in range(8))

# Every derivative-defined orbit of four consecutive steps has an inner visit.
for numer in range(-25000, 25001, 31):
    x = Q(numer, 1000)
    seq=[]
    for i in range(48):
        if x in (Q(0), -a, a):
            break
        seq.append(branch(x))
        x = f(x)
    assert 'OOOO' not in ''.join(seq)
    for k in range(len(seq)//4):
        word=seq[4*k:4*k+4]
        assert word.count('I') >= 1
        assert s**word.count('O')*t**word.count('I') >= s**3*t
# Four additional exact rational parameter cases within the claimed open region.
for sr,tr,ar in [(Q(2,3),Q(5),Q(2)),(Q(3,4),Q(5),Q(7)),
                 (Q(5,6),Q(5),Q(3)),(Q(4,5),Q(4),Q(5))]:
    rr = sr**3*tr - sr - sr**2 - sr**3
    assert 0 < rr < 1 and tr*sr**3 > 1
    uu = rr/(1 + tr*sr**3)
    abs_orbit=[uu, tr*(1-uu)]
    abs_orbit += [sr*(abs_orbit[-1]-1)]
    abs_orbit += [sr*(abs_orbit[-1]-1)]
    assert 0 < abs_orbit[0] < 1
    assert all(1 < abs_orbit[i] < tr for i in range(1,4))
    assert sr*(abs_orbit[3]-1)==uu
    z=ar*uu
    def ff(x):
        if x<=-ar:return sr*(x+ar)
        if x<0:return tr*(x+ar)
        if x<ar:return tr*(x-ar)
        return sr*(x-ar)
    vals=[]
    for _ in range(8):
        vals.append(z);z=ff(z)
    assert z==ar*uu and vals[4]==-vals[0]
print('EXACT_PERIOD8_AND_FINITE_ITINERARY_CHECKS_OK')
print('period8=',[str(z) for z in orbit])
print('rho=',rho,'minimum_four_step_multiplier=',t*s**3)
