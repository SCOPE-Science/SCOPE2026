"""Finite-state and large-graph checks for block-excluded dimer adsorption.
Run: python verify_block.py
No numerical check substitutes for the convergence proof.
"""
from fractions import Fraction
from functools import lru_cache
from math import exp, log, isclose
import random

@lru_cache(None)
def terminal_law(x, u, y, v):
    assert x+u == y+v
    total = x*v+u*y+u*v
    if total == 0:
        return {x+u: Fraction(1)}
    terms=((x*v,(x-1,u,y,v-1)),(u*y,(x,u-1,y-1,v)),(u*v,(x,u-1,y,v-1)))
    out={}
    for weight,state in terms:
        if not weight:continue
        for k,prob in terminal_law(*state).items():
            out[k]=out.get(k,Fraction(0))+Fraction(weight,total)*prob
    assert sum(out.values())==1
    return out

def limit(alpha,beta):
    if abs(alpha-beta)<1e-14:
        return alpha*exp(1-1/alpha)
    return exp(((1-alpha)*log(alpha)-(1-beta)*log(beta))/(beta-alpha))

def simulate(n,a,b,rng):
    x,u,y,v=a,n-a,b,n-b
    while True:
        w1,w2,w3=x*v,u*y,u*v
        t=w1+w2+w3
        if t==0:return x+u
        j=rng.randrange(t)
        if j<w1:x-=1;v-=1
        elif j<w1+w2:u-=1;y-=1
        else:u-=1;v-=1

def main():
    count=0
    for n in range(2,9):
        for a in range(0,n+1):
            for b in range(0,n+1):
                law=terminal_law(a,n-a,b,n-b)
                assert sum(law.values())==1
                assert min(law)>=max(0,a+b-n)  # maximum-matching obstruction
                assert max(law)<=min(a,b) if a>0 and b>0 else max(law)==0
                count+=1
    # Check all finite transition laws against direct enumeration for selected cases.
    assert terminal_law(1,1,1,1)=={1:Fraction(1,3),0:Fraction(2,3)}
    assert terminal_law(2,0,2,0)=={2:Fraction(1)}
    assert terminal_law(0,3,0,3)=={0:Fraction(1)}
    for a,b in ((.1,.5),(.25,.25),(.4,.6),(.2,.4),(.49,.49),(.8,.4)):
        x=limit(a,b)
        assert x>0 and x<=min(a,b)
        m=(a+b)/2
        assert x<=m*exp(1-1/m)+1e-12
        if a+b<=1:assert x<=1/(2*exp(1))+1e-12
    rng=random.Random(20261105)
    cases=((1000,250,250),(1000,250,400),(1000,500,500),(2000,400,600))
    for n,a,b in cases:
        samples=[simulate(n,a,b,rng)/n for _ in range(160)]
        mean=sum(samples)/len(samples)
        theory=limit(a/n,b/n)
        assert abs(mean-theory)<0.03,(n,a,b,mean,theory)
        print('finite-density:',n,a,b,'mean',round(mean,5),'limit',round(theory,5))
    print('PASS:',count,'exact rational terminal-law states; boundary and Jensen checks; seeded large-size trials')

if __name__=='__main__':main()
