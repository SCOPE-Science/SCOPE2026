"""Final verifier: VdP mu=1 annular trapping region (stdlib only, exact Fractions).
Certifies: (O) outer transverse-inward, (I) inner transverse-outward,
(N) nesting, (S) min speed + transit-time bound. Exit 0 iff all pass."""
from fractions import Fraction as F
import math, sys

outer=[(F(287,100),F(20,100)),(F(286,100),F(347,100)),(F(-18,100),F(309,100)),(F(-125,100),F(217,100)),(F(-287,100),F(-20,100)),(F(-286,100),F(-347,100)),(F(18,100),F(-309,100)),(F(125,100),F(-217,100))]
inner=[(F(45,100),F(-2,100)),(F(1,4),F(1,4)),(F(-2,100),F(41,100)),(F(-2,5),F(2,5)),(F(-45,100),F(2,100)),(F(-1,4),F(-1,4)),(F(2,100),F(-41,100)),(F(2,5),F(-2,5))]
fails=[]
def check(name,cond,detail=""):
    print(("PASS " if cond else "FAIL ")+name+" "+str(detail))
    if not cond: fails.append(name)

# (O) outer: CCW, convex, F.n_out sup<0 via Lipschitz grid N=40
S=sum(outer[i][0]*outer[(i+1)%8][1]-outer[(i+1)%8][0]*outer[i][1] for i in range(8))
check("O_ccw",S>0,"area2=%s"%float(S))
cs=[(outer[(i+1)%8][0]-outer[i][0])*(outer[(i+2)%8][1]-outer[(i+1)%8][1])-(outer[(i+1)%8][1]-outer[i][1])*(outer[(i+2)%8][0]-outer[(i+1)%8][0]) for i in range(8)]
check("O_convex",all(c>0 for c in cs))
def edge_sup(p1,p2,N):
    (x1,y1),(x2,y2)=p1,p2; dx,dy=x2-x1,y2-y1; nx,ny=dy,-dx; a,b=x1,dx
    c3=-b**3/3; c2=-a*b**2; c1=dy-a**2*b+b; c0=y1-a**3/3+a
    h3=c3*nx; h2=c2*nx; h1=c1*nx-b*ny; h0=c0*nx-a*ny
    L=3*abs(h3)+2*abs(h2)+abs(h1)
    mx=max(h3*F(k)**3+h2*F(k)**2*N+h1*F(k)*N**2+h0*N**3 for k in range(N+1))
    return mx/F(N**3)+L/F(2*N)
ob=[edge_sup(outer[i],outer[(i+1)%8],40) for i in range(8)]
check("O_inward",all(v<0 for v in ob),["%.4f"%float(v) for v in ob])
# (I) inner: CCW, F.n_out(=right normal) inf>0 via grid N=60
S2=sum(inner[i][0]*inner[(i+1)%8][1]-inner[(i+1)%8][0]*inner[i][1] for i in range(8))
check("I_ccw",S2>0,"area2=%s"%float(S2))
def edge_inf(p1,p2,N):
    (x1,y1),(x2,y2)=p1,p2; dx,dy=x2-x1,y2-y1; nx,ny=dy,-dx; a,b=x1,dx
    c3=-b**3/3; c2=-a*b**2; c1=dy-a**2*b+b; c0=y1-a**3/3+a
    h3=c3*nx; h2=c2*nx; h1=c1*nx-b*ny; h0=c0*nx-a*ny
    L=3*abs(h3)+2*abs(h2)+abs(h1)
    mn=min(h3*F(k)**3+h2*F(k)**2*N+h1*F(k)*N**2+h0*N**3 for k in range(N+1))
    return mn/F(N**3)-L/F(2*N)
ib=[edge_inf(inner[i],inner[(i+1)%8],60) for i in range(8)]
check("I_outward",all(v>0 for v in ib),["%.5f"%float(v) for v in ib])
# (N) origin strictly in hole; hole verts strictly in outer
def leftval(poly,i,pt):
    x1,y1=poly[i]; x2,y2=poly[(i+1)%len(poly)]
    return (x2-x1)*(pt[1]-y1)-(y2-y1)*(pt[0]-x1)
check("N_origin_in_hole",all(leftval(inner,i,(F(0),F(0)))>0 for i in range(8)))
check("N_hole_in_outer",all(all(leftval(outer,j,p)>0 for j in range(8)) for p in inner))
# (S) speed: P_outer upper bound via exact sqrt majorants
P=F(0)
for i in range(8):
    dx=outer[(i+1)%8][0]-outer[i][0]; dy=outer[(i+1)%8][1]-outer[i][1]
    q=dx*dx+dy*dy; M=math.ceil(math.sqrt(float(q))*10**6)+1
    assert F(M*M,10**12)>=q; P+=F(M,10**6)
check("S_perim",True,"P_outer<=%s=%.5f"%(P,float(P)))
# hole x-range + edge slopes
xs=[p[0] for p in inner]
Xmax=max(abs(x) for x in xs)
slopes=[]
for i in range(8):
    dx=inner[(i+1)%8][0]-inner[i][0]; dy=inner[(i+1)%8][1]-inner[i][1]
    if dx!=0: slopes.append(abs(dy/dx))
Sm=max(slopes)
print("INFO Xmax=%s Sm=%s=%.4f"%(Xmax,Sm,float(Sm)))
def yrange(poly,x):
    ys=[]
    for i in range(len(poly)):
        x1,y1=poly[i]; x2,y2=poly[(i+1)%len(poly)]
        if (x1-x)*(x2-x)<=0 and x1!=x2:
            t=(x-x1)/(x2-x1); ys.append(y1+t*(y2-y1))
    return (min(ys),max(ys))
assert Xmax<=F(45,100)
D=F(1,10000); mn=None
for k in range(-4500,4501):
    x=F(k,10000)
    if abs(x)>F(45,100): continue
    r=yrange(inner,x); h=x**3/3-x
    gap=min(abs(r[0]-h),abs(r[1]-h))
    q=max(x*x,gap*gap)
    mn=q if mn is None else min(mn,q)
# Lipschitz: x^2 Lf<=2*Xmax; gap Lip<=Sm+1 (hole edge slope + |h'|<=1); gap<=1 so gap^2 Lip<=2(Sm+1)
Lf=2*Xmax; Lg=2*(Sm+1); Lmax=max(Lf,Lg)
slack=Lmax*D/2
print("INFO gridmin=%s=%.6f slack=%.6f"%(mn,float(mn),float(slack)))
check("S_gap",mn-slack>=F(1,25),"min-slack=%.6f>=0.04"%float(mn-slack))
# global: |x|>=Xmax -> q>=Xmax^2=0.2025; strip -> q>=1/25. So |v|>=1/5.
m=F(1,5)
Tbound=P/m
check("S_transit",True,"|v|>=%s, T<=%s=%.3f"%(m,Tbound,float(Tbound)))
print("RESULT:", "ALL PASS" if not fails else "FAILURES: %s"%fails)
sys.exit(0 if not fails else 1)
