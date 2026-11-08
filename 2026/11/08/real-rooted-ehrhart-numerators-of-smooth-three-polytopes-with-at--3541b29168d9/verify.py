"""Exact certificate for real-rooted Ehrhart numerators in the smooth five-facet threefold classification.
Usage: python verify.py certificate.json  (requires sympy)
"""
import json, sys
import sympy as sp

A,B,C,t,z=sp.symbols('A B C t z')

def numerator(L):
    v=[sp.expand(L.subs(t,j)) for j in range(4)]
    h=[sp.expand(sum((-1)**i*sp.binomial(4,i)*v[j-i] for i in range(j+1))) for j in range(4)]
    return sp.expand(sum(h[j]*z**j for j in range(4))),h

def source_forms():
    a,b=A+1,B+1
    # q=2, p=1, C=c1+c2 (only sum enters because each weak-composition coordinate has the same mean)
    L12=sp.expand((b*t+1)*(b*t+2)*(1+t*(a+b*C/3))/2)
    # q=1, p=2, C=c1
    L21=sp.expand((b*t+1)*((a*t+1)*(a*t+2)+C*(2*a*t+3)*b*t/2+C*C*b*t*(2*b*t+1)/6)/2)
    return {'p1q2':L12,'p2q1':L21}

def decode_coeffs(poly):
    terms=sp.Poly(sp.expand(poly),A,B,C).terms()
    return [[*list(monom),str(sp.Rational(coeff))] for monom,coeff in terms]

def compute():
    result={}
    for key,L in source_forms().items():
        hstar,h=numerator(L)
        discriminant=sp.expand(sp.discriminant(hstar,z))
        terms=decode_coeffs(discriminant)
        assert terms and all(sp.Rational(row[3])>0 for row in terms)
        # Check independently against direct cubic discriminant formula
        h0,h1,h2,h3=h
        assert h0==1
        direct=sp.expand(h1*h1*h2*h2-4*h2**3-4*h3*h1**3-27*h3**2+18*h3*h2*h1)
        assert sp.expand(discriminant-direct)==0
        result[key]={'term_count':len(terms),'terms':terms,'h_star':[str(sp.expand(hi)) for hi in h]}
    return result

if __name__=='__main__':
    got=compute()
    fname=sys.argv[1] if len(sys.argv)>1 else 'certificate.json'
    with open(fname,encoding='utf-8') as f: expected=json.load(f)
    assert got==expected['cases']
    # 4-facet simplex: for a >=2, writing u=a-2 >=0,
    # cubic discriminant is (u+1)^2(u+2)^6/108 times the following positive polynomial.
    u=sp.symbols('u')
    disc_simplex=(u+1)**2*(u+2)**6*(u**4+22*u**3+183*u**2+540*u+54)/108
    a=u+2
    L=sp.prod(a*t+j for j in (1,2,3))/6
    hstar,_=numerator(L)
    assert sp.simplify(sp.discriminant(hstar,z)-disc_simplex)==0
    assert expected['simplex_discriminant_in_u']==str(sp.factor(disc_simplex))
    # Independent direct-sum tests of the lattice enumeration, not used as proof.
    for aa in (1,2,4):
      for bb in (1,2,3):
       for cc in (0,1,3):
        form=source_forms()['p2q1'].subs({A:aa-1,B:bb-1,C:cc})
        for k in (0,1,2,3):
         direct=sum(sp.binomial(aa*k+cc*j+2,2) for j in range(bb*k+1))
         assert sp.simplify(form.subs(t,k)-direct)==0
    for aa in (1,2):
      for bb in (1,2):
       for c1,c2 in ((0,0),(1,0),(1,2)):
        form=source_forms()['p1q2'].subs({A:aa-1,B:bb-1,C:c1+c2})
        for k in (0,1,2):
         direct=sum(aa*k+c1*y+c2*j+1 for y in range(bb*k+1) for j in range(bb*k+1-y))
         assert sp.simplify(form.subs(t,k)-direct)==0
    print('CERTIFIED exact polynomial identities; monomial coefficients strictly positive:',
          {k:v['term_count'] for k,v in got.items()},'; simplex checked; enumeration tested')
