"""Independent numerical checks for the half-wave shared-cap phase theorem.
Run: python CHECKER.py (standard library only).
Numerical integration supplements, and does not replace, the analytic proof.
"""
import math

PI = math.pi

def theta(a):
    return math.acos(1.0 / (2.0 * math.cos(a)))

def bracket(a, eta):
    t = theta(a)
    return 2.0 * math.sin(t) + eta * (t + math.sin(t) * math.cos(t) - (PI-a)/2.0)

def objective_closed(a, eta):
    c = math.cos(a)
    v = 2.0 / PI + eta*((PI-a)*c + math.sin(a))/(2.0*PI)
    if a >= PI/3:
        return v
    t = theta(a)
    lost = (2.0*c*math.sin(t) - t + eta*(c*(t + math.sin(t)*math.cos(t)) - math.sin(t))) / PI
    return v-lost

def optimum(eta):
    assert 0.0 < eta <= 1.0
    lo, hi = PI/4.0, PI/3.0
    for _ in range(95):
        mid = (lo+hi)/2.0
        if bracket(mid, eta)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2.0

def direct_integral(a, eta, n=100000):
    h=2.0*PI/n
    s=0.0
    for j in range(n):
        t=-PI+(j+0.5)*h
        p=max(0.0, math.cos(t-a))+max(0.0, math.cos(t+a))
        s += (1.0+eta*max(0.0, math.cos(t)))*min(1.0,p)
    return s/n

def run():
    checks=0
    for eta in (0.01,0.1,0.5,1.0):
        a=optimum(eta)
        assert PI/4<a<PI/3;checks+=1
        assert abs(bracket(a,eta))<2e-12;checks+=1
        assert objective_closed(a,eta)>objective_closed(0.0,eta);checks+=1
        for test_a in (0.0,0.2,0.5,PI/4,a,1.04,PI/3,1.2,PI/2):
            analytic=objective_closed(test_a,eta)
            integ=direct_integral(test_a,eta)
            assert abs(analytic-integ)<3e-8,(eta,test_a,analytic,integ)
            checks+=1
        for i in range(1,199):
            v=(PI/2)*i/199
            assert objective_closed(a,eta)>=objective_closed(v,eta)-2e-13
            checks+=1
    for eta in (0.00001,0.0001,0.001):
        a=optimum(eta)
        ratio=(PI/3-a)/(eta*eta)
        target=PI*PI/(72*math.sqrt(3))
        assert abs(ratio-target) < 0.0002, (eta,ratio,target)
        checks+=1
    prev=optimum(0.0001)
    for eta in (0.001,0.01,0.1,0.5,1.0):
        val=optimum(eta)
        assert val<prev
        prev=val;checks+=1
    print('PASS',checks,'diagnostics; optimum at eta=1:',repr(optimum(1.0)), 'radians, separation degrees:',repr(360*optimum(1.0)/PI))

if __name__=='__main__':run()
