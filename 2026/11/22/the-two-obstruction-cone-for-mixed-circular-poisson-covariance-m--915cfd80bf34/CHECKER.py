"""Exact arithmetic checks for a two-modulation circular Poisson covariance theorem.

Run: python3 CHECKER.py.  Uses Python standard library only.  These checks
corroborate finite identities and explicit witnesses; the infinite-dimensional
positivity classification is proved analytically in RESULT.md.
"""
from fractions import Fraction as F

class Q2:
    """An element a+b*sqrt(2) with rational a,b."""
    def __init__(self, a=0, b=0):
        self.a = F(a); self.b = F(b)
    @staticmethod
    def cv(x): return x if isinstance(x, Q2) else Q2(x)
    def __add__(self, x):
        x=self.cv(x); return Q2(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return Q2(-self.a,-self.b)
    def __sub__(self,x): return self+-self.cv(x)
    def __rsub__(self,x): return self.cv(x)+-self
    def __mul__(self,x):
        x=self.cv(x); return Q2(self.a*x.a+2*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.cv(x); den=x.a*x.a-2*x.b*x.b
        if den==0: raise ZeroDivisionError()
        return Q2((self.a*x.a-2*self.b*x.b)/den,(self.b*x.a-self.a*x.b)/den)
    def __eq__(self,x):
        x=self.cv(x);return (self.a,self.b)==(x.a,x.b)
    def __repr__(self): return f'Q2({self.a},{self.b})'

# cos(k*pi/4), as elements of Q(sqrt(2)).
COS = [Q2(1),Q2(0,F(1,2)),Q2(0),Q2(0,-F(1,2)),
       Q2(-1),Q2(0,-F(1,2)),Q2(0),Q2(0,F(1,2))]
def kernel8(i,j,r,a,b,c):
    d=COS[(i-j)%8]; s=COS[(i+j)%8]
    return (1-r*r)/(1-2*r*d+r*r)*(a+b*s+c*d)

def quadratic8(weights,r,a,b,c):
    return sum((weights[i]*weights[j]*kernel8(i,j,r,a,b,c)
                for i in range(8) for j in range(8)),Q2())

def test():
    cnt=0
    # The first Fourier-neighbor coefficient is exactly r at zero
    # and (r+1/r)/2 away from zero.
    for r in [F(1,5),F(1,2),F(3,4)]:
        mu=(r+1/r)/2
        for n in range(-12,13):
            ratio=(r**abs(n-1)+r**abs(n+1))/(2*r**abs(n))
            assert ratio==(r if n==0 else mu)
            cnt+=1
        for n in range(-12,13):
            w=r**abs(n)
            # Cross-coupling normalized weight squared.
            coupling=w*w/(r**(abs(n-1)+abs(n+1)))
            assert coupling==(r**-2 if n==0 else 1)
            cnt+=1
    # Verify the exact even-sector determinant factorization.
    for r in [F(1,5),F(1,2),F(3,4)]:
        mu=(r+1/r)/2; delta=(1/r-r)/2
        for a in [F(-1,3),F(0),F(1,5),F(2)]:
            for c in [F(-2),F(0),F(3,5),F(2)]:
                h=a+c*mu
                assert h*h-c*c*delta*delta==(a+c*r)*(a+c/r)
                cnt+=1
    # All eight nodes; exact negative Gram witness despite positive diagonal.
    weights=[0,-1,-7,-1,0,-1,-7,-1]
    r=Q2(F(1,2));a=Q2(F(-1,4));b=Q2(F(67,100));c=Q2(1)
    q=quadratic8(weights,r,a,b,c)
    assert q==Q2(F(-1217,1275)),q
    cnt+=1
    for i in range(8):
        assert kernel8(i,i,r,a,b,c).a>0
        cnt+=1
    # At an even-sector spectral boundary, a=-1/4, c=1, r=1/2,
    # b^2=7/16; the odd-sector threshold is |b|<=4/5.
    rr=F(1,2); aa=-F(1,4); cc=F(1); mu=(rr+1/rr)/2
    delta=(1/rr-rr)/2; h=aa+cc*mu
    assert h==1 and h*h-cc*cc*delta*delta==F(7,16)
    assert h*h/(mu*mu)==F(16,25)>F(7,16)
    cnt+=2
    # At a=0 and b=c>0, K=2c cos(theta)cos(phi)P_r,
    # hence zero rows at theta=pi/2 and 3pi/2.
    for j in range(8):
        assert kernel8(2,j,Q2(F(1,2)),Q2(0),Q2(1),Q2(1))==0
        assert kernel8(6,j,Q2(F(1,2)),Q2(0),Q2(1),Q2(1))==0
        cnt+=2
    # At a=-mu*c, b=0, c=-1, the kernel is the constant delta.
    rr=F(1,2); mu=F(5,4); delta=F(3,4)
    for i in range(8):
        for j in range(8):
            assert kernel8(i,j,Q2(rr),Q2(mu),Q2(0),Q2(-1))==Q2(delta)
            cnt+=1
    print(f'PASS: {cnt} exact rational/quadratic-field assertions')

if __name__=='__main__': test()
