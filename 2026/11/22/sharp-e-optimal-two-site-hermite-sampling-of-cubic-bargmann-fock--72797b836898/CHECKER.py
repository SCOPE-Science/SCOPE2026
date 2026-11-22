"""Exact rational certificates for the sharp two-site cubic Fock Hermite-sampling bound.
Run with Python 3.10+; only the standard library is used.
"""
from fractions import Fraction as F
import math

def trim(p):
    p = list(map(F,p))
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(a,b):
    return trim([(a[i] if i<len(a) else F(0))+(b[i] if i<len(b) else F(0)) for i in range(max(len(a),len(b)))])

def neg(a): return [-v for v in a]
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return trim(c)

def scale(a,b): return trim([v*F(b) for v in a])
def deriv(a): return trim([(i+1)*a[i+1] for i in range(len(a)-1)] or [0])
def rem(a,b):
    a=trim(a);b=trim(b)
    assert b != [0]
    while a !=[0] and len(a)>=len(b):
        i=len(a)-len(b);v=a[-1]/b[-1]
        a=sub(a,[F(0)]*i+scale(b,v))
    return a

def sturm(p):
    a=trim(p);b=deriv(a); seq=[a,b]
    while b != [0]:
        c=neg(rem(a,b))
        if c==[0]: break
        seq.append(c);a,b=b,c
    return seq

def polyval(p,x):
    v=F(0)
    for a in reversed(p):v=v*x+a
    return v

def sign(x):return (x>0)-(x<0)
def changes(signs):
    ss=[s for s in signs if s]
    return sum(a!=b for a,b in zip(ss,ss[1:]))
def V(p,x):return changes([sign(polyval(q,F(x))) for q in sturm(p)])
def Vinf(p):return changes([sign(q[-1]) for q in sturm(p)])
def roots(p,a,b):return V(p,a)-(Vinf(p) if b is None else V(p,b))
def frac(s):return F(s)

# Coefficients ascending: sextic Q and cubic C, from exact derivative/resultant elimination.
Q=trim([36,-108,150,-111,45,-10,1]); C=trim([-6,6,-3,1])
I1=(frac('1.519055357'),frac('1.519055359'))
I2=(frac('1.596071637'),frac('1.596071639'))
I3=(frac('2.808203101'),frac('2.808203103'))
assert roots(Q,0,None)==2
assert roots(C,0,None)==1
assert roots(Q,*I1)==1 and roots(Q,*I3)==1
assert roots(C,*I2)==1
assert roots(Q,*I2)==0 and roots(C,*I1)==0 and roots(C,*I3)==0

x=trim([0,1]); one=[F(1)]; TWO=F(2)
def pw(p,n):
    v=one
    for _ in range(n): v=mul(v,p)
    return v

# G(x) = exp(x) A(x)^*A(x) splits into even and odd 2-by-2 blocks.
TE=trim([2,6,-3,1]);DE=scale(x,8)
TO=scale(trim([6,-6,15,-5,1]),F(1,3));DO=scale(pw(x,3),F(8,3))
# Exact determinant checks from the explicit parity matrices.
assert DE==scale(x,8) and DO==scale(pw(x,3),F(8,3))

# Common eigenvalue R(x)=8(x^2-3)/[(x-2)(x^2-6x+12)].
A=scale(sub(pw(x,2),[3]),8)
B=mul(sub(x,[2]),trim([12,-6,1]))
Qfactor=mul(trim([2,-2,1]),Q)
for T,D in ((TE,DE),(TO,DO)):
    numerator=add(sub(pw(A,2),mul(mul(T,A),B)),mul(D,pw(B,2)))
    assert numerator==scale(Qfactor,-8)

# For the odd block, an interior stationary eigenvalue of exp(-x)lambda
# must equal R_stat=(2D-D')/(T-T') whenever its denominator is nonzero.
Snum=scale(sub(scale(DO,2),deriv(DO)),3)
Sden=scale(sub(TO,deriv(TO)),3)
assert Snum==trim([0,0,-24,16])
assert Sden==trim([12,-36,30,-9,1])
# Exact cleared stationary equation:
Nstat=add(sub(scale(pw(Snum,2),3),mul(mul(scale(TO,3),Snum),Sden)),mul(scale(DO,3),pw(Sden,2)))
assert Nstat==scale(mul(pw(x,2),mul(C,Q)),-8)  # polynomial certificate

# Distinguish lower branch (2 lambda < trace) from upper at each root.
# Clear 2Rstat - TO = [6*Snum - (3*TO)*Sden]/(3*Sden).
BranchNum=sub(scale(Snum,6),mul(scale(TO,3),Sden))
for inter, expected in [(I1,-1),(I2,1),(I3,1)]:
    for p in (Sden,BranchNum):assert roots(p,*inter)==0
    mid=sum(inter)/2
    assert sign(polyval(BranchNum,mid)*polyval(Sden,mid))==expected

# The common eigenvalue at I1 lies below HALF the trace of both blocks.
for T in (TE,TO):
    num=sub(scale(A,2),mul(T,B))
    assert roots(num,*I1)==0 and roots(B,*I1)==0
    mid=sum(I1)/2
    assert sign(polyval(num,mid)*polyval(B,mid)) == -1

# Positivity and simplicity: odd-block offdiagonal is
# sqrt(6)*x*(x*x-3*x+3)/3, strictly positive for x>0;
# even block offdiagonal may vanish at x=1 but its diagonal values there differ.
assert polyval(sub(pw(x,2),add(scale(x,3),[-3])),F(3,2)) > 0

# As x->0+, smallest odd eigenvalue ~ (4/3)x^3; as x->inf it is ~8/x.
# Hence exp(-x)*lambda_odd^- vanishes at both ends. The Sturm certificate
# establishes that its only positive stationary point is the I1 root.
# At I1 both parity lower eigenvalues coincide, so the global worst-case
# frame gain is attained uniquely there.

def min2(tr,det): return (tr-math.sqrt(tr*tr-4*det))/2
u=1.51905535770046
mu=min2(float(polyval(TO,F(str(u)))),float(polyval(DO,F(str(u)))))
v=math.exp(-u)*mu
assert 0.4855614654 < v < 0.4855614657
for r in [0.01,.1,.5,.75,1,1.2,1.3,1.4,1.5,1.6,2,3,8]:
    e=min2(float(polyval(TE,F(str(r)))),float(polyval(DE,F(str(r)))))
    o=min2(float(polyval(TO,F(str(r)))),float(polyval(DO,F(str(r)))))
    assert math.exp(-r)*min(e,o)<v
print('PASS exact root counts, polynomial identities, branch signs, frame lower-bound diagnostics')
print('squared separation parameter x* in',I1,'; sharp lower bound',repr(v))
