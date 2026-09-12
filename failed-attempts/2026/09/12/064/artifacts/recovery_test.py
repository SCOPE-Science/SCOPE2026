# Bounded recovery tests (exact integer arithmetic unless noted):
# T1: ideal of norm 15 in O_K, K=Q(sqrt(-23)): needs a^2+23 b^2 (or norm form) representations.
# O_K = Z[(1+sqrt(-23))/2]; Norm((u+v*sqrt(-23))/2) = (u^2+23 v^2)/4, u%v same parity.
# An ideal of norm 15 exists iff ...; necessary: 5 represented. Test representations of 3,5,15.
def reps(N, B=200):
    out=[]
    for u in range(-B,B+1):
        for v in range(-B,B+1):
            if (u-v)%2!=0: continue
            if u==0 and v==0: continue
            if (u*u+23*v*v)==4*N: out.append((u,v))
    return out
for N in [3,5,15]:
    print(f"N={N} element-reps: {reps(N)}")
# T2: Kronecker witnesses (exact)
for p in [3,5,13]:
    print(p, (-23)%p, pow((-23)%p,(p-1)//2,p))
# T3: small K-point search for conductor-1 Heegner candidates: x,y in (1/2)O_K grid, |coords|<=6
from fractions import Fraction as F
a1,a2,a3,a4,a6=F(1),F(1),F(1),F(-10),F(-10)
def Fval(xr,xi,yr,yi):
    # represent x=(xr+xi*s)/2? Use basis {1,w}, w=(1+s)/2, s^2=-23. x = p+q*w.
    # brute over (p,q) integer pairs via half-integers: work in Q(s): x=(X0+X1 s)/2 etc.
    return None
sols=[]
R=6
def to_half(p,q): return (F(p*2+q,2), F(q,2))  # (const, s-coeff) for p+q*w
pts=[(p,q) for p in range(-R,R+1) for q in range(-R,R+1)]
def addM(a,b): return (a[0]+b[0],a[1]+b[1])
def mulM(a,b): return (a[0]*b[0]-23*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def eqM(a,b): return a[0]==b[0] and a[1]==b[1]
def Eres(X,Y):
    # Y^2 + X Y + Y - X^3 - X^2 +10 X +10
    Y2=mulM(Y,Y); XY=mulM(X,Y); X2=mulM(X,X); X3=mulM(X2,X)
    r=addM(addM(Y2,XY),Y)
    r=(r[0]-X3[0]-X2[0]+10*X[0]+10, r[1]-X3[1]-X2[1]+10*X[1])
    return r
found=[]
for px,qx in pts:
    X=to_half(px,qx)
    for py,qy in pts:
        Y=to_half(py,qy)
        r=Eres(X,Y)
        if eqM(r,(F(0),F(0))): found.append(((px,qx),(py,qy)))
print("K-grid points |p|,|q|<=6 on E:", found)
