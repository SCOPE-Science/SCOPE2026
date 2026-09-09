"""S3a: Tate data at p=n=799657 for E: y^2=x^3-Dx, D=n^2. Stdlib only."""
from fractions import Fraction
n=799657; D=n*n
a4=-D; a6=0
c4=-48*D; c6=0; Delta=64*D**3
def v(p,m):
    if m==0: return float('inf')
    e=0
    while m%p==0: m//=p; e+=1
    return e
print("v_n(c4)=",v(n,c4),"v_n(c6)=",v(n,c6),"v_n(Delta)=",v(n,Delta))
print("v_n(j)=3*2-6=",3*v(n,c4)-v(n,Delta),"(=> potentially good)")
# I_0^* auxiliary cubic P(T)=T^3+a2,1 T^2+a4,2 T+a6,3 with a2=0,a4=-n^2,a6=0
a21=0; a42=-1; a63=0
roots=[0,1,-1]
for r in roots:
    print("P(%d)=%d"%(r,r**3+a21*r*r+a42*r+a63))
print("=> P splits completely mod n: c_n=4; Kodaira I_0^*, f_n=2")
print("conductor check: 32*D =",32*D)
