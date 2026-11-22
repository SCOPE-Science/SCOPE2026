"""Reproducible finite diagnostics of a deterministic polynomial-flow theorem.

Run with: python3 check.py. Only the written mathematical argument proves
uniform asymptotics; this script samples finitely many parameter values.
"""
import math

P = {
    1: lambda x, y: x*x*y,
    2: lambda x, y: x*y*y,
    3: lambda x, y: -x*x*y,
    4: lambda x, y: x*x*x,
}

def polar(k, theta):
    x, y = math.cos(theta), math.sin(theta)
    q1 = -x
    q2 = -y + P[k](x, y)
    f = x*q1 + y*q2
    g = x*q2 - y*q1
    return f, g

def rhs(k, v, theta):
    f, g = polar(k, theta)
    return 2*(-f-v), g/v

def reach(k, delta, radius=1.6, step=0.02):
    angle = (0.0 if k <= 2 else math.pi/2)
    target = angle + math.pi/4
    v = radius**-2
    theta = angle + delta
    t = 0.0
    while theta < target and t < 1000:
        a1, b1 = rhs(k, v, theta)
        a2, b2 = rhs(k, v+step*a1/2, theta+step*b1/2)
        a3, b3 = rhs(k, v+step*a2/2, theta+step*b2/2)
        a4, b4 = rhs(k, v+step*a3, theta+step*b3)
        vn = v+step*(a1+2*a2+2*a3+a4)/6
        thn = theta+step*(b1+2*b2+2*b3+b4)/6
        assert vn > 0 and thn >= theta
        if thn >= target:
            return t + step*(target-theta)/(thn-theta)
        v, theta = vn, thn
        t += step
    raise AssertionError("Crossing not observed within finite diagnostic horizon")

for k in range(1,5):
    for j in range(400):
        f, g = polar(k, 2*math.pi*j/400)
        assert f < -0.6, (k,j,f)
    left = 0 if k<=2 else math.pi/2
    for d in (0.015, 0.03, 0.055):
        _, g = polar(k, left+d)
        exact = math.tan(d)**k / (1+math.tan(d)**2)**2
        assert abs(g-exact)<1e-12
    assert polar(k,left+0.1)[1] > 0

tests = ((1,0.01,1.0,0.08), (2,0.01,1.0,0.025),
         (3,0.06,0.5,0.04), (4,0.14,1/3,0.03))
for k,d,target,tolerance in tests:
    t = reach(k,d)
    scaled = t/math.log(1/d) if k==1 else t*d**(k-1)
    assert abs(scaled-target)<tolerance, (k,t,scaled,target)
print("VERIFY_OK")
