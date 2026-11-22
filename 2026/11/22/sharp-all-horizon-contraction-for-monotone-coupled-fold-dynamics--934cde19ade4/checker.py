"""Reproduction checks for a sharp finite-horizon collapse theorem.
Run: python3 checker.py (standard library only).
The analytic proof is in RESULT.md; sampling is not an infinite proof.
"""
import math
import random
from fractions import Fraction

def image(x, y, f):
    return (abs(x-f(y)), abs(y-f(x)))

def lin(t, a):
    return a*t

def soft(t):
    return math.log1p(math.expm1(t)/2) if t<700 else t-math.log(2)+math.log1p(math.exp(-t))

def nonlinear(t, a):
    return t-(1-a)*(1-math.exp(-t))

def boundcheck(a, f, seed):
    rng=random.Random(seed)
    cnt=0
    for k in range(900):
        x=10**rng.uniform(-5, 2.7)
        y=10**rng.uniform(-5, 2.7)
        original=max(x,y)
        for n in range(1, 15):
            x,y=image(x,y,f)
            bound=(1-a*a)**(n//2)*original
            if max(x,y)>bound+2e-9*(original+1):
                raise AssertionError((a,n,x,y,bound))
            cnt+=1
    return cnt

def exact_linear():
    tests=0
    for a in (Fraction(1,5),Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(1,1)):
        x,y=Fraction(1),Fraction(0)
        for n in range(1,15):
            x,y=image(x,y,lambda t: lin(t,a))
            target=(1-a*a)**(n//2)
            assert max(x,y)==target, (a,n,x,y,target)
            tests+=1
    return tests

def logistic_corner():
    values=[]
    for k in range(4,13):
        x=10**(-k)
        y=x*x
        u,v=image(x,y,soft)
        U,V=image(u,v,soft)
        ratio=max(U,V)/x
        assert abs(ratio-.75)<2*x+1e-9,(x,ratio)
        values.append((x,ratio))
    return values

if __name__=='__main__':
    n=0
    for a in (.2,.5,.75,.999):
        n+=boundcheck(a,lambda t,a=a:lin(t,a),100+round(100*a))
        n+=boundcheck(a,lambda t,a=a:nonlinear(t,a),200+round(100*a))
    n+=boundcheck(a,lambda t,a=a:a*t+(1-a)*min(t,1),300+round(100*a))
    n+=boundcheck(.5,soft,400)
    q=exact_linear()
    samples=logistic_corner()
    print('PASS:',n,'floating finite-step checks;',q,'exact rational extremizer checks')
    print('Logistic small-state ratios (x, exact two-step norm/x):')
    for x,v in samples: print('%.1e %.12f'%(x,v))
    print('Finite checks supplement but do not replace the analytic proof.')
