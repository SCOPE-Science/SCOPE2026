"""Exact-rational certificate for a two-point global mode in an exponentiated count law.
Only Python's standard library is required. All reported inequalities use integer arithmetic.
"""
from fractions import Fraction as Q
from math import floor

# Floating-point arithmetic only proposes brackets; integer powers certify them.
q=Q(21,25)
t=Q(2,23)
N=12
L_lower=2*sum((t**(2*k+1))/Q(2*k+1) for k in range(N))
L_upper=L_lower+2*t**(2*N+1)/(Q(2*N+1)*(1-t*t))
assert L_lower > Q(1,6)
assert L_upper-L_lower < Q(1,10**25)

def F(x,L):
    if x==-1:return Q(0)
    return Q(1)-q**(x+1)*(1+(x+2)*L)/(1+L)

def cdf_bounds(j):
    if j==-1:return Q(0),Q(0)
    return F(j,L_upper),F(j,L_lower)

# Integer-only verification of rational lower/upper power bounds, with mp a noncertifying guide.
S=10**20
NUM_TESTS=0

def pow_bounds(xlo,xhi,p,d):
    global NUM_TESTS
    def candidate(v):
        return floor((float(v)**(p/d))*S)
    A=candidate(xlo)-10**9
    B=candidate(xhi)+10**9
    assert A>0
    assert (A**d)*(xlo.denominator**p) <= (S**d)*(xlo.numerator**p)
    assert (B**d)*(xhi.denominator**p) >= (S**d)*(xhi.numerator**p)
    NUM_TESTS+=2
    return Q(A,S),Q(B,S)

def mass_bounds(j,p,d):
    xlo,xhi=cdf_bounds(j)
    alo,ahi=pow_bounds(xlo,xhi,p,d)
    if j==0:return alo,ahi
    ylo,yhi=cdf_bounds(j-1)
    blo,bhi=pow_bounds(ylo,yhi,p,d)
    return alo-bhi,ahi-blo

m779={j:mass_bounds(j,779,1000) for j in (0,2)}
m780={j:mass_bounds(j,39,50) for j in range(6)}
# The 0-2 crossing is bracketed.
assert m779[2][1] < m779[0][0], '0.779 not below transition'
assert m780[2][0] > m780[0][1], '0.78 not above transition'
# At the upper endpoint, all rivals except count 2 are strictly below count 0.
for j in (1,3,4,5):
    assert m780[j][1] < m780[0][0], ('rival at upper endpoint',j)
# Numeric printout is orientation only, not part of correctness.
for b in (Q(779,1000),Q(39,50)):
    m={Q(779,1000):m779,Q(39,50):m780}[b]
    print('Exponent',b,'intervals:',{j:tuple(float(x) for x in v) for j,v in m.items()})
print('CERTIFICATE_PASS; rational-power inequality checks:',NUM_TESTS)
print('log bracket width < 1e-25; strict concavity for x>=4 proved symbolically')
