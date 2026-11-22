"""Independent finite signed-permutation enumeration and generating-function checks.

Run with Python 3 and SymPy: python verify.py.
This checks small degrees; the general formulas require the mathematical proof.
"""
from itertools import permutations, product
from math import factorial
import sympy as s

def comp(g,h):
    return tuple((1 if z>0 else -1)*h[abs(z)-1] for z in g)

def inverse(g):
    a=[0]*len(g)
    for i,x in enumerate(g):
        a[abs(x)-1]=(i+1)*(1 if x>0 else -1)
    return tuple(a)

def brute(n):
    els=[tuple(sign[i]*(p[i]+1) for i in range(n))
         for p in permutations(range(n))
         for sign in product((1,-1), repeat=n)]
    identity=tuple(range(1,n+1))
    involutions=[g for g in els if comp(g,g)==identity]
    subgroups=set()
    for i,x in enumerate(involutions):
        if x==identity:continue
        for y in involutions[i+1:]:
            if y==identity or comp(x,y)!=comp(y,x):continue
            z=comp(x,y)
            subgroups.add(frozenset((identity,x,y,z)))
    waiting=set(subgroups)
    classes=0
    while waiting:
        H=next(iter(waiting))
        classes+=1
        for g in els:
            gi=inverse(g)
            conj=frozenset(comp(comp(g,h),gi) for h in H)
            waiting.discard(conj)
    return len(subgroups),classes

def formulas(degree):
    z=s.Symbol('z')
    P=1/((1-z)**4*(1-z**2)**6*(1-z**4))
    T=1/((1-z)**2*(1-z**2)**3*(1-z**4)**3)
    C=1/((1-z)*(1-z**3)*(1-z**4)*(1-z**6)**2)
    I=1/((1-z)**2*(1-z**2))
    F=(P+3*T+2*C)/6-I
    E=(s.exp(4*z+6*z**2+2*z**4)-3*s.exp(2*z+z**2)+2*s.exp(z))/6
    class_numbers=[int(s.expand(s.series(F,z,0,degree+1).removeO()).coeff(z,n)) for n in range(degree+1)]
    total_numbers=[int(s.expand(s.series(E,z,0,degree+1).removeO()).coeff(z,n)*factorial(n)) for n in range(degree+1)]
    return total_numbers,class_numbers

if __name__=='__main__':
    total,classes=formulas(10)
    assert classes[:11]==[0,0,2,7,23,51,116,223,431,762,1341]
    assert total[:8]==[0,0,2,25,277,2895,32631,382963]
    for n in range(1,5):
        actual=brute(n)
        assert actual==(total[n],classes[n]), (n,actual,total[n],classes[n])
    print('KLEIN_FOUR_SIGNED_PERMUTATION_CENSUS_VERIFIED n<=4; generating functions n<=10')
