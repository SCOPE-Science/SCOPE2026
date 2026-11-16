"""Exact rational/π consistency identities in two sample dimensions.
This does not replace the all-dimensional proof; it checks algebraic block entries.
Requires SymPy.
"""
import sympy as s

def E(d, alpha):
    z = s.gamma(s.Integer(d)/2+1)/s.gamma(s.Integer(d+sum(alpha))/2+1)
    for a in alpha:
        z *= s.gamma(s.Rational(a+1,2))/s.sqrt(s.pi)
    return s.simplify(z)

def Q(d, alpha):
    if any(a%2 for a in alpha[2:]):return s.S.Zero
    return E(d,alpha)/4

def G(d, alpha):
    if any(a%2 for a in alpha):return s.S.Zero
    return E(d,alpha)

def prodmom(d,P,R,restricted):
    fn=Q if restricted else G
    z=s.S.Zero
    for a,u in P.items():
        for b,v in R.items():
            z+=u*v*fn(d, tuple(x+y for x,y in zip(a,b)))
    return s.simplify(z)

def term(d,terms):
    P={}
    for c,ss in terms:
        a=[0]*d
        for i,ex in ss:a[i]+=ex
        a=tuple(a)
        P[a]=P.get(a,0)+c
    return P

for d in (3,4,5,8):
    X=term(d,[(1,[(0,1)]),(-1,[(1,1)])])
    Y=term(d,[(1,[(0,2)]),(-1,[(1,2)])])
    Z=term(d,[(1,[(2,1)])])
    W=term(d,[(1,[(0,1),(2,1)]),(1,[(1,1),(2,1)])])
    U=term(d,[(1,[(0,1),(2,1)]),(-1,[(1,1),(2,1)])])
    c=(d+2)*s.sqrt(d+4)*s.gamma(s.Integer(d)/2+1)/(8*s.sqrt(2*s.pi)*s.gamma(s.Rational(d+5,2)))
    for P,R,target in [
      (X,X,(1-2/s.pi)/4),
      (Y,Y,s.Rational(1,4)),
      (X,Y,c),
      (Z,Z,s.Rational(1,4)),
      (W,W,(1+2/s.pi)/4),
      (Z,W,2*c),
      (U,U,(1-2/s.pi)/4)]:
        numerator=prodmom(d,P,R,True)
        denom=s.sqrt(prodmom(d,P,P,False)*prodmom(d,R,R,False))
        assert s.simplify(numerator/denom-target)==0,(d,target)
    print(f'd={d}: all seven normalized block entries symbolic PASS')
print('ALL EXACT CHECKS PASSED')
