import math, random

C1 = 6.0 * math.sqrt(3.0) - 8.0
C2 = 3.0 * math.sqrt(6.0) - 4.0 * math.sqrt(2.0)

def phi(t):
    s = math.sqrt(4.0 + 4.0*t + 3.0*t*t)
    return 2.0*(4.0 + 3.0*t)/(s + 2.0)

def deriv_numerator(t):
    s = math.sqrt(4.0 + 4.0*t + 3.0*t*t)
    return 8.0 - 12.0*t + 12.0*s

for i in range(1, 200002):
    t = 0.5*i/200001.0
    assert deriv_numerator(t) > 0.0
    assert phi(t) <= C1 + 2e-14
assert abs(phi(0.5) - C1) < 2e-14
assert abs(C1*math.sqrt(2.0)/2.0 - C2) < 2e-14
assert C2 < 2.0

def invariants(A,B,C):
    ax,ay=A; bx,by=B; cx,cy=C
    a=math.hypot(bx-cx,by-cy)
    b=math.hypot(cx-ax,cy-ay)
    c=math.hypot(ax-bx,ay-by)
    area2=abs((bx-ax)*(cy-ay)-(by-ay)*(cx-ax))
    if area2 < 1e-10:
        return None
    area=area2/2.0
    p=a+b+c
    s=p/2.0
    r=area/s
    R=a*b*c/(4.0*area)
    return p,r,R

rng=random.Random(20261002)
generic=0
lattice=0
worst_generic=-1e99
worst_lattice=-1e99
for _ in range(30000):
    pts=[(rng.uniform(-3,3),rng.uniform(-3,3)) for _ in range(3)]
    inv=invariants(*pts)
    if inv:
        p,r,R=inv
        gap=(p-4.0*R)-C1*r
        worst_generic=max(worst_generic,gap)
        assert gap <= 2e-10
        generic += 1
for _ in range(30000):
    pts=[(rng.random(),rng.random()) for _ in range(3)]
    inv=invariants(*pts)
    if inv:
        p,r,R=inv
        gap=(p-4.0*R)-C2
        worst_lattice=max(worst_lattice,gap)
        assert gap <= 2e-10
        lattice += 1
print('VERIFY_OK', 'generic', generic, 'unit_square_lattice_free', lattice,
      'worst_generic_gap', format(worst_generic,'.3e'),
      'worst_lattice_gap', format(worst_lattice,'.3e'),
      'C2', format(C2,'.15f'))
