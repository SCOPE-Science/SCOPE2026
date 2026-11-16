"""Exact and numerical checks for the square-cycle domination Fourier theorem.
Run with Python >=3.9; only Python standard library needed.
"""
from fractions import Fraction as F
from math import comb, cos, pi
from itertools import product

# All calculations through the root/peak certification use exact rationals.
class I:
    def __init__(self,a,b=None):
        if isinstance(a,I):self.a,self.b=a.a,a.b;return
        self.a=F(a);self.b=F(a if b is None else b)
        assert self.a<=self.b
    def __add__(self,o):
        o=I(o);return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,o):return self+-I(o)
    def __rsub__(self,o):return I(o)+-self
    def __mul__(self,o):
        o=I(o); p=(self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b);return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=I(o);assert o.a*o.b>0;return self*I(1/o.b,1/o.a)
    def __pow__(self,n):
        out=I(1)
        for _ in range(n):out=out*self
        return out
    def sign(self):
        assert self.a>0 or self.b<0, (float(self.a),float(self.b))
        return 1 if self.a>0 else -1
    def bounds(self):return float(self.a),float(self.b)

def poly(coeff,x):
    ans=I(0)
    for a in reversed(coeff):ans=ans*x+a
    return ans

def h(t):return sum(t**j for j in range(1,6))-1

def pq(t):
    p=[4*t**3*(t+1),-4*(t**2-t+1)*(t**2+t-1),-8*(t-1)*(t**3+2*t**2+t-1),16*(2*t-1)]
    q=[-2*(3*t**4+2*t**3-t**2-1),4*(3*t**4+4*t**3+2*t**2+4*t-3),8*t*(4*t**3+3*t**2-1),-16*(t**4+2*t**3+2*t**2+4*t-3),-32*(t**4+t**3+t**2+t-1)]
    return p,q

def rcoeff(t):
    return [8*(7*t**4+4*t**3-11*t**2-14*t+9),64*t*(t+1)*(2*t-1)**2,-32*(15*t**4+13*t**3+7*t**2+9*t-9),-128*(3*t**4+6*t**3+4*t**2+2*t-3),128*(9*t**4-2*t**3-13*t**2+3),512*(t**4-4*t**2-4*t+3),-512*(t**4+t**3+t**2+5*t-3)]

def spectral(t,x):
    p,q=pq(t); return poly(p,x)/poly(q,x)

def check_certificate():
    lo=F(508660391641,10**12);hi=F(508660391643,10**12)
    assert h(lo)<0<h(hi)
    t=I(lo,hi); R=rcoeff(t)
    # Descartes transform H(y)=(1+y)^6 R((y-1)/(y+1)).
    H=[]
    for k in range(7):
        v=I(0)
        for j in range(7):
            for a in range(j+1):
                b=k-a
                if 0<=b<=6-j:
                    v+=R[j]*((-1)**(j-a)*comb(j,a)*comb(6-j,b))
        H.append(v)
    signs=[z.sign() for z in H]
    assert signs==[1,-1,-1,1,1,1,-1],signs
    # Therefore the number of roots in (-1,1), counting multiplicity, is at most 3.
    # These three disjoint intervals certify at least three via alternating signs.
    ints=[(F(-829815,10**6),F(-829814,10**6)),(F(-353447,10**6),F(-353446,10**6)),(F(218869,10**6),F(218871,10**6))]
    for a,b in ints:
        assert poly(R,I(a)).sign()!=poly(R,I(b)).sign(),(float(a),float(b),poly(R,I(a)).bounds(),poly(R,I(b)).bounds())
    # Monotonicity intervals are then exact, and the global extrema are at the roots or endpoints.
    p,q=pq(t)
    candidates=[spectral(t,I(-1)),spectral(t,I(1))]+[spectral(t,I(a,b)) for a,b in ints]
    # In x order: left endpoint, right endpoint, local high at first, low at second, global high at third.
    assert candidates[4].a>max(z.b for i,z in enumerate(candidates) if i!=4)
    assert candidates[1].b<min(z.a for i,z in enumerate(candidates) if i!=1)
    mu=sum(j*t**j for j in range(1,6))
    rate=I(1)/mu
    rat=candidates[4]/candidates[1]
    assert F(1479,1000)<rat.a and rat.b<F(1481,1000)
    print('Exact peak certification: PASS; 3 interior critical points; unique maxima/minima; ratio interval',rat.bounds())
    for n,v in zip(['S(-1)/rate','S(1)/rate','local-max-1/rate','local-min/rate','global-max/rate'],candidates):
        print(n,v.bounds())

def matmul(A,B):
    n=len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def matpowers(M,n):
    powers=[[[int(i==j) for j in range(len(M))] for i in range(len(M))]]
    for i in range(n):powers.append(matmul(powers[-1],M))
    return powers
def trace(A):return sum(A[i][i] for i in range(len(A)))

def moments_transfer(n):
    M=[[0]*5 for _ in range(5)]
    for r in range(5):
        M[r][0]=1
        if r<4:M[r][r+1]=1
    pows=matpowers(M,n)
    z=trace(pows[n]);a=pows[n][0][0]
    pairs=[]
    for j in range(n):
        # Tr(D M^j D M^(n-j)) = M^j[0,0] M^(n-j)[0,0]
        pairs.append(pows[j][0][0]*pows[n-j][0][0])
    return z,a,pairs

def moments_enum(n):
    z=a=0;pairs=[0]*n
    for xs in product((0,1),repeat=n):
        if any(sum(xs[(i+j)%n] for j in range(5))==0 for i in range(n)):continue
        z+=1;a+=xs[0]
        for j in range(n):pairs[j]+=xs[0]*xs[j]
    return z,a,pairs

def numerical(n):
    z,a,pair=moments_transfer(n);base=F(a,z);cov=[F(q,z)-base*base for q in pair]
    ev=[sum(float(c)*cos(2*pi*k*j/n) for j,c in enumerate(cov)) for k in range(n)]
    return ev

def check_finite():
    for n in range(3,15):
        m=moments_transfer(n); e=moments_enum(n)
        assert m==e,(n,m,e)
        ev=numerical(n)
        assert min(ev)>1e-9,(n,min(ev))
    print('Exact brute-force matching of transfer formulas for n=3..14: PASS')

    t=.5086603916420042
    mu=sum(j*t**j for j in range(1,6));rate=1/mu
    for n in [16,24,32,48,64]:
        ev=numerical(n)
        ph=[]
        for k in range(n):
            angle=2*pi*k/n
            if k==0:
                s0=sum(j*j*t**j for j in range(1,6));var=s0-mu*mu; y=rate*var/(mu*mu)
            else:
                z=sum(t**j*complex(cos(j*angle),__import__('math').sin(j*angle)) for j in range(1,6))
                y=rate*(1-abs(z)**2)/abs(1-z)**2
            ph.append(y)
        diff=max(abs(a-b) for a,b in zip(ev,ph))
        print('n',n,'uniform spectral difference',diff)
        if n>=48:assert diff<1e-5
    print('Numerical convergence checks: PASS')

if __name__=='__main__':
    check_certificate();check_finite()
