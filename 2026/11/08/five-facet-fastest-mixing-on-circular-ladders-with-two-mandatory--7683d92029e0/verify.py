"""Exact small-case checks for the two-floor prism-chain formula.

Uses only the Python standard library. Fractions and the quadratic field
Q(sqrt(5)) eliminate floating-point comparisons in the tested instances.
"""
from fractions import Fraction as F

class Q5:
    """Exact value a+b*sqrt(5), a,b rational."""
    __slots__ = ('a','b')
    def __init__(self,a=0,b=0):
        if isinstance(a,Q5): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,x):
        x=Q5(x);return Q5(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self): return Q5(-self.a,-self.b)
    def __sub__(self,x): return self+(-Q5(x))
    def __rsub__(self,x): return Q5(x)-self
    def __mul__(self,x):
        x=Q5(x);return Q5(self.a*x.a+5*self.b*x.b,self.a*x.b+self.b*x.a)
    __rmul__=__mul__
    def __truediv__(self,x):
        x=Q5(x);d=x.a*x.a-5*x.b*x.b
        assert d!=0
        return Q5((self.a*x.a-5*self.b*x.b)/d,(self.b*x.a-self.a*x.b)/d)
    def __eq__(self,x):
        x=Q5(x);return self.a==x.a and self.b==x.b
    def sign(self):
        a,b=self.a,self.b
        if a==0:return (b>0)-(b<0)
        if b==0:return (a>0)-(a<0)
        if a>0 and b>0:return 1
        if a<0 and b<0:return -1
        diff=a*a-5*b*b
        if a>0:return (diff>0)-(diff<0)
        return (diff<0)-(diff>0)
    def __lt__(self,x):return (self-Q5(x)).sign()<0
    def __le__(self,x):return (self-Q5(x)).sign()<=0
    def __gt__(self,x):return (self-Q5(x)).sign()>0
    def __ge__(self,x):return (self-Q5(x)).sign()>=0
    def __repr__(self):return f'({self.a})+({self.b})sqrt5'

ONE=Q5(1); TWO=Q5(2); FOUR=Q5(4)

def setup(m):
    if m==4:
        return Q5(2),Q5(4),[Q5(x) for x in (1,0,-1,0)]
    if m==5:
        a=Q5(F(5,2),F(-1,2));b=Q5(F(5,2),F(1,2))
        c1=Q5(F(-1,4),F(1,4));c2=Q5(F(-1,4),F(-1,4))
        return a,b,[ONE,c1,c2,c2,c1]
    if m==6:
        return ONE,FOUR,[Q5(x) for x in (1,F(1,2),F(-1,2),-1,F(-1,2),F(1,2))]
    raise ValueError('Only m=4,5,6 are tested with exact arithmetic')

def facets(a,b,tau,eta):
    return [b/(b+TWO*a),b*tau/TWO,
            (b-a+TWO*a*eta)/(a+b),FOUR*tau-ONE,
            b*tau+TWO*eta-ONE]

def validate(m,tau,eta,do_matrix=False):
    a,b,cos=setup(m)
    assert TWO*tau+eta<=ONE and tau>=0 and eta>=0
    vals=facets(a,b,tau,eta)
    mu=max(vals)
    r=max(tau,(ONE-mu)/a)
    v=max(eta,(ONE-mu)/TWO)
    assert r>=tau and v>=eta and TWO*r+v<=ONE
    assert mu>=0 and mu<=ONE
    expected=max(ONE-a*r,ONE-TWO*v,b*r+TWO*v-ONE)
    assert mu==expected
    # Independent endpoint evaluation for every Fourier wave number and both layers.
    vals_all=[]
    for k in range(m):
        ak=TWO-TWO*cos[k]
        for parity in (0,1):
            ev=ONE-r*ak-TWO*v*parity
            if k or parity: vals_all.append(ev if ev>=0 else -ev)
    assert mu==max(vals_all)
    if do_matrix:
        P=[[Q5(0) for _ in range(2*m)] for _ in range(2*m)]
        for j in range(m):
            for layer in (0,1):
                i=2*j+layer
                P[i][i]=ONE-TWO*r-v
                P[i][2*((j-1)%m)+layer]=r
                P[i][2*((j+1)%m)+layer]=r
                P[i][2*j+(1-layer)]=v
        for row in P:
            assert all(entry>=0 for entry in row)
            assert sum(row,Q5(0))==ONE
        for k in range(m):
            ak=TWO-TWO*cos[k]
            for parity in (0,1):
                lam=ONE-r*ak-TWO*v*parity
                vec=[cos[(k*j)%m]*(1 if layer==0 or parity==0 else -1)
                     for j in range(m) for layer in (0,1)]
                for i in range(2*m):
                    lhs=sum((P[i][h]*vec[h] for h in range(2*m)),Q5(0))
                    assert lhs==lam*vec[i]
    return vals

def test_nonredundancy(m,witnesses):
    a,b,_=setup(m)
    for index,(t,e) in witnesses.items():
        v=facets(a,b,Q5(t),Q5(e))
        assert all(v[index]>v[j] for j in range(5) if j!=index),(m,index,v)

cases=0
for m in (4,5,6):
    a,b,_=setup(m)
    assert a+b>FOUR
    for p in range(21):
        for q in range(41-2*p):
            validate(m,Q5(F(p,40)),Q5(F(q,40)))
            cases+=1
    for t,e in ((0,0),(F(7,20),0),(0,F(3,5)),(F(17,50),F(1,4)),(F(1,2),0)):
        if 2*t+e<=1:validate(m,Q5(t),Q5(e),True)

# Five genuinely different active affine bounds on the odd prism.
test_nonredundancy(5,{
    0:(0,0),1:(F(7,20),0),2:(0,F(3,5)),
    3:(F(1,2),0),4:(F(17,50),F(1,4))
})
# For even cycles, the fourth bound is always below the rim-floor bound.
for m in (4,6):
    a,b,_=setup(m)
    assert b==FOUR
    for p in range(21):
        t=Q5(F(p,40))
        assert FOUR*t-ONE<=b*t/TWO

test_nonredundancy(4,{0:(0,0),1:(F(7,20),0),2:(0,F(3,5)),4:(F(3,10),F(3,10))})
test_nonredundancy(6,{0:(0,0),1:(F(2,5),0),2:(0,F(3,5)),4:(F(9,25),F(1,5))})
print('VERIFY_OK',cases,'exact feasible floor-pair instances; 150 matrix-mode eigenvector checks; facet witnesses passed')
