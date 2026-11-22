"""Reproduce numerical checks for the three-target seasonal Poisson theorem.

Only finite numerical checks; the universal statement is justified in RESULT.md.
Run: python verify.py
"""
import math
import random


def probs(a, b, effort, theta):
    q = [math.exp(-effort*(a+b*math.cos(theta+2*math.pi*j/3))) for j in range(3)]
    p0 = math.prod(q)
    p1 = sum((1-q[i])*math.prod(q[j] for j in range(3) if j != i) for i in range(3))
    p3 = math.prod(1-x for x in q)
    p2 = 1-p0-p1-p3
    return [p0, p1, p2, p3]


def check():
    rng = random.Random(17032024)
    tests=0
    for _ in range(200):
        a = rng.uniform(0.2, 6.0)
        b = a*rng.uniform(0.01, 0.98)
        effort = rng.uniform(0.02, 7.0)
        plus=probs(a,b,effort,0)
        minus=probs(a,b,effort,math.pi/3)
        assert abs(sum(plus)-1)<1e-12
        assert abs(sum(minus)-1)<1e-12
        assert abs(plus[0]-minus[0])<1e-12
        assert plus[1]>minus[1]-1e-13, (a,b,effort,plus,minus)
        assert plus[2]<minus[2]+1e-13
        assert plus[3]>minus[3]-1e-13
        assert sum(i*plus[i] for i in range(4))>sum(i*minus[i] for i in range(4))-1e-13
        d=4*math.exp(-2*a*effort)*math.sinh(b*effort/2)*(math.cosh(b*effort/2)-1)
        assert abs((plus[1]-minus[1])-d)<1e-11
        assert abs((minus[2]+minus[3]-plus[2]-plus[3])-d)<1e-11
        tests+=9
        # Grid verifies the prescribed extrema for diverse positive parameters.
        for j in range(41):
            theta=2*math.pi*j/123
            p=probs(a,b,effort,theta)
            eps=2e-12
            assert minus[1]-eps <= p[1] <= plus[1]+eps
            assert plus[2]-eps <= p[2] <= minus[2]+eps
            assert minus[3]-eps <= p[3] <= plus[3]+eps
            assert plus[2]+plus[3]-eps <= p[2]+p[3] <= minus[2]+minus[3]+eps
            tests+=4
    # Positive mixture of two shared-effort states inherits each strict comparison.
    a,b=2,1
    w=.36
    plus=[w*x+(1-w)*y for x,y in zip(probs(a,b,.7,0),probs(a,b,3,0))]
    minus=[w*x+(1-w)*y for x,y in zip(probs(a,b,.7,math.pi/3),probs(a,b,3,math.pi/3))]
    assert plus[1]>minus[1] and plus[2]<minus[2] and plus[3]>minus[3]
    tests+=1
    # Locate unique effort contrast maximum via the strictly decreasing coth sum.
    a,b=2,1
    def resid(e):
        x=b*e/2
        return 1/math.tanh(x)+1/math.tanh(x/2)-4*a/b
    lo,hi=.001,10.
    for _ in range(100):
        mid=(lo+hi)/2
        if resid(mid)>0:lo=mid
        else:hi=mid
    optimum=(lo+hi)/2
    assert abs(resid(optimum))<1e-12
    assert abs(optimum-.7683126207519425)<1e-12
    tests+=2
    print('PASS',tests,'finite numerical assertions')
    print('example at effort 1')
    for label,theta in [('one-peak season',0),('two-peak season',math.pi/3)]:
        p=probs(2,1,1,theta)
        print(label, 'P0,P1,P2,P3:', ', '.join(f'{x:.12f}' for x in p))
    print('contrast-maximizing effort example:',f'{optimum:.12f}')

if __name__=='__main__':
    check()
