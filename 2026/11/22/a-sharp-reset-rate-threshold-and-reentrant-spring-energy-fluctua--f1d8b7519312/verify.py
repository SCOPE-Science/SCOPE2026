"""Exact rational and polynomial certificate for a selectively reset Brownian spring pair.

Requires Python 3 and SymPy; run with `python verify.py`.
"""
import sympy as S

r, g, z = S.symbols('r g z', positive=True)

# Stationary generator identities in homogeneous degrees 2 and 4.
def stationary_moments(degree, lower):
    U = {(i, degree-i): S.Symbol(f'M{i}_{degree-i}') for i in range(degree+1)}
    def m(i,j):
        if i<0 or j<0: return S.Integer(0)
        if i+j==degree: return U[(i,j)]
        if i+j==0: return S.Integer(1)
        return lower[(i,j)]
    eqs = []
    for i,j in U:
        eqs.append(-(i+j/g+(r if i>0 else 0))*m(i,j)
                   + i*m(i-1,j+1) + j/g*m(i+1,j-1)
                   + i*(i-1)*m(i-2,j) + j*(j-1)/g*m(i,j-2))
    answers=S.solve(eqs,list(U.values()),simplify=False)
    assert len(answers)==degree+1
    return {ij:S.factor(answers[v]) for ij,v in U.items()}

m2=stationary_moments(2,{})
m4=stationary_moments(4,m2)
mean=S.factor(m2[(1,1)]-m2[(2,0)]/2)
raw2=S.factor(m4[(2,2)]-m4[(3,1)]+m4[(4,0)]/4)
noise=S.factor((raw2-mean**2)/mean**2)
assert S.cancel(mean-(g+1)/(r*(g*r+2*g+1)))==0
assert S.limit(noise,g,0)==2*r+5
Cinf=(2*r**4+14*r**3+28*r**2+21*r+8)/(r+4)
assert S.cancel(S.limit(noise,g,S.oo)-Cinf)==0
P=r**4+7*r**3+13*r**2+4*r-6
assert S.cancel(Cinf-(2*r+5)-2*P/(r+4))==0
assert P.subs(r,S.Rational(49168,100000))<0
assert P.subs(r,S.Rational(49169,100000))>0
assert all(c>0 for c in S.Poly(S.diff(P,r),r).all_coeffs())

# The derivative numerator N is a degree-seven polynomial in g.
# All signs on r in [1/2,3/5] are certified using exact Bernstein coefficients.
N=S.Poly(S.together(S.diff(noise,g)).as_numer_denom()[0],g)
assert N.degree()==7

def bernstein_coefficients(poly):
    t=S.symbols('t')
    p=S.Poly(S.expand(poly.subs(r,S.Rational(1,2)+t/10)),t)
    n=p.degree()
    return [S.factor(sum(p.nth(k)*S.binomial(i,k)/S.binomial(n,k)
                         for k in range(i+1))) for i in range(n+1)]

for j in [7,5,4,3,2,1,0]:
    sign = +1 if j in [7,2,1,0] else -1
    values=bernstein_coefficients(sign*N.nth(j))
    assert all(v>0 for v in values), (j, values)
# The g^6 coefficient needs no fixed sign; either sign has two variations.
assert all(v>0 for v in bernstein_coefficients(-N.eval(1)))
assert S.factor(N.eval(0))>0
# Hence by Descartes, N has at most 2 positive roots. N(0)>0,
# N(1)<0, and its leading coefficient is positive, forcing exactly 2.
# The derivative denominator is strictly positive for all r,g>0.
den=S.factor(S.together(S.diff(noise,g)).as_numer_denom()[1])
assert all(c>0 for c in S.Poly(den,g).all_coeffs())

# Direct unreduced rational generator check at two positive rate pairs.
for rv,gv in [(S.Rational(1,2),S.Rational(1,2)),(S.Rational(3,5),S.Integer(2))]:
    sample={r:rv,g:gv}
    vals={ij:S.cancel(m.subs(sample)) for ij,m in {**m2,**m4}.items()}
    for degree in (2,4):
        for i in range(degree+1):
            j=degree-i
            def a(i,j):
                if i<0 or j<0:return S.Integer(0)
                if i+j==0:return S.Integer(1)
                return vals[i,j]
            res=-(i+j/g+(r if i else 0))*a(i,j)+i*a(i-1,j+1)+j/g*a(i+1,j-1)+i*(i-1)*a(i-2,j)+j*(j-1)/g*a(i,j-2)
            assert S.cancel(res.subs(sample))==0
print('PASS exact generator recurrences; stationary moment ratios; sharp endpoint threshold; two memory extrema throughout 1/2 <= r <= 3/5')
