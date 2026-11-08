"""Exact-arithmetic checks of period constraints and period-four existence."""
from fractions import Fraction as Q
from math import sqrt

class I:
    def __init__(self, lo, hi=None):
        self.lo=Q(lo);self.hi=Q(lo) if hi is None else Q(hi)
        assert self.lo<=self.hi
    def __add__(self,o):
        o=co(o);return I(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,o):return self+-co(o)
    def __rsub__(self,o):return co(o)+-self
    def __mul__(self,o):
        o=co(o); cs=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return I(min(cs),max(cs))
    __rmul__=__mul__
    def absmax(self):return max(abs(self.lo),abs(self.hi))
    def contains(self,x):return self.lo<=x<=self.hi
    def __repr__(self):return '['+str(float(self.lo))+','+str(float(self.hi))+']'

def co(o):return o if isinstance(o,I) else I(o)

def mapN(x,y,a,steps=4,interval=False):
    one=I(1) if interval else Q(1)
    half=I(Q(1,2)) if interval else Q(1,2)
    three=I(3) if interval else Q(3)
    aa=I(a) if interval else a
    xs=[]
    for i in range(steps):
        xs.append(x)
        x,y=(three+y)*x*(one-x),y+(aa if i%2==0 else -aa)*(xs[-1]-half)
    return x,y,xs

def jacobian4(x,y,a,interval):
    one=I(1) if interval else Q(1)
    two=I(2) if interval else Q(2)
    aa=I(a) if interval else a
    three=I(3) if interval else Q(3)
    half=I(Q(1,2)) if interval else Q(1,2)
    p00,p01,p10,p11=one,co(0) if interval else Q(0),co(0) if interval else Q(0),one
    for i in range(4):
        s=aa if i%2==0 else -aa
        d00=(three+y)*(one-two*x);d01=x*(one-x)
        n00=d00*p00+d01*p10;n01=d00*p01+d01*p11
        n10=s*p00+p10;n11=s*p01+p11
        p00,p01,p10,p11=n00,n01,n10,n11
        x,y=(three+y)*x*(one-x),y+s*(x-half)
    return [[p00-one,p01],[p10,p11-one]]

c=[Q("0.584659370623430440690721939042858948322863116678"),
   Q("-1.41236581213595531877756480186345406366138289085")]
a=Q(6)
J=jacobian4(c[0],c[1],a,False)
det=J[0][0]*J[1][1]-J[0][1]*J[1][0]
assert det!=0
C=[[J[1][1]/det,-J[0][1]/det],[-J[1][0]/det,J[0][0]/det]]
# Exact rational inverse at the chosen center, no numerical ambiguity.
rad=Q(1,10**8)
box=[I(t-rad,t+rad) for t in c]
P=jacobian4(box[0],box[1],a,True)
M=[[I(int(i==j))-sum((I(C[i][k])*P[k][j] for k in range(2)),I(0)) for j in range(2)] for i in range(2)]
fn=mapN(c[0],c[1],a,interval=False)
fc=[fn[i]-c[i] for i in range(2)]
shift=[-sum((C[i][k]*fc[k] for k in range(2)),Q(0)) for i in range(2)]
# T(z)-c = -C F(c)+(I-C DF(box))(z-c)
image=[I(shift[i])+sum((M[i][j]*I(-rad,rad) for j in range(2)),I(0)) for i in range(2)]
row_bounds=[sum((M[i][j].absmax() for j in range(2)),Q(0)) for i in range(2)]
assert max(row_bounds)<1
assert all(-rad < d.lo and d.hi < rad for d in image)
# Interval orbit is strictly inside physical unit interval and has four different values.
X,Y=box
positions=[]
ranges=[]
for i in range(4):
    ranges.append(I(3)+Y)
    positions.append(X)
    X,Y=(I(3)+Y)*X*(I(1)-X),Y+(I(6) if i%2==0 else I(-6))*(positions[-1]-I(Q(1,2)))
assert all(0<d.lo<=d.hi<1 for d in positions)
assert all(0<d.lo<=d.hi<4 for d in ranges)
assert all(positions[i].hi<positions[j].lo or positions[j].hi<positions[i].lo for i in range(4) for j in range(i+1,4))
print('CERTIFIED_PERIOD_FOUR', 'center',*[str(float(v)) for v in c], 'max_newton_contraction',float(max(row_bounds)), 'max_box_fraction',float(max(max(d.absmax() for d in image)/rad,0)), 'x',*[str(k) for k in positions], 'effective_parameters',*[str(k) for k in ranges])

# Exact matrix identity, eigenvalues and stability cutoff
for a in [Q(1,100),Q(1,10),Q(1),Q(2),Q(4),Q(5),Q(6),Q(8),Q(12)]:
    # at x=1/2, y=-1 (base r=3)
    jp=[[Q(0),Q(1,4)],[a,Q(1)]]
    jm=[[Q(0),Q(1,4)],[-a,Q(1)]]
    M2=[[sum(jm[i][k]*jp[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    tr=M2[0][0]+M2[1][1];det2=M2[0][0]*M2[1][1]-M2[0][1]*M2[1][0]
    assert tr==1 and det2==-a*a/16
    lp=(1+sqrt(1+float(a*a)/4))/2
    lm=1-lp
    assert lp>1
    assert (lm>-1)==(a*a<Q(32))
print('VERIFY_OK rational_interval_existence=1 analytic_floquet_cases=9')
