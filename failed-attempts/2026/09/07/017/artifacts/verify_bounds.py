"""Rerunnable verification for lane-20 L-membrane bounds.
Loads output/artifacts/mesh_N256.npz + P1_N256_rayleigh.npz, recomputes P1 assembly,
re-evaluates Rayleigh quotient + Higham rounding bound -> rigorous upper U,
re-runs exact-rational Faber-Krahn lower L0, checks MPS containment and widths.
Runs in <60s (no eigensolve). Python3 + numpy only.
"""
import numpy as np, sys, time, os
from fractions import Fraction
t0=time.time()
HERE=os.path.dirname(os.path.abspath(__file__))
d = np.load(os.path.join(HERE,"mesh_N256.npz"))
coords, tris = d["coords"], d["tris"]
r = np.load(os.path.join(HERE,"P1_N256_rayleigh.npz"))
x = r["x"]
print(f"mesh: nodes={len(coords)} tris={len(tris)} free={len(x)}")

# boundary mask (same as generation)
tol=1e-9
bx=np.zeros(len(coords),dtype=bool)
Xc=coords[:,0]; Yc=coords[:,1]
bx|=(np.abs(Xc)<tol)|(np.abs(Yc)<tol)
bx|=(np.abs(Xc-2)<tol)&(Yc<=1+tol)
bx|=(np.abs(Yc-2)<tol)&(Xc<=1+tol)
bx|=(np.abs(Xc-1)<tol)&(Yc>=1-tol)
bx|=(np.abs(Yc-1)<tol)&(Xc>=1-tol)
free=np.where(~bx)[0]
assert len(free)==len(x) and np.array_equal(free, r["free"]), "free mismatch"
fmap=-np.ones(len(coords),dtype=int); fmap[free]=np.arange(len(free))

# assemble P1 COO (exact-domain, N even => no variational crime)
nt=len(tris); n=len(coords)
rows=np.empty(9*nt,dtype=np.int64); cols=np.empty(9*nt,dtype=np.int64)
Aval=np.empty(9*nt); Mval=np.empty(9*nt)
for t in range(nt):
    i,j,k=tris[t]
    x1,y1=coords[i]; x2,y2=coords[j]; x3,y3=coords[k]
    det=(x2-x1)*(y3-y1)-(x3-x1)*(y2-y1); Ar=abs(det)/2
    b0=y2-y3; b1=y3-y1; b2=y1-y2; c0=x3-x2; c1=x1-x3; c2=x2-x1
    bb=(b0*b0,b0*b1,b0*b2,b1*b0,b1*b1,b1*b2,b2*b0,b2*b1,b2*b2)
    cc=(c0*c0,c0*c1,c0*c2,c1*c0,c1*c1,c1*c2,c2*c0,c2*c1,c2*c2)
    ids=(i,j,k)
    for a in range(3):
        for qq in range(3):
            o=9*t+a*3+qq
            rows[o]=ids[a]; cols[o]=ids[qq]
            Aval[o]=(bb[a*3+qq]+cc[a*3+qq])/(4*Ar)
    m2=Ar/12*2; m1=Ar/12
    mv=(m2,m1,m1,m1,m2,m1,m1,m1,m2)
    for qq in range(9): Mval[9*t+qq]=mv[qq]
rf=fmap[rows]; cf=fmap[cols]; m=(rf>=0)&(cf>=0)
rA,ccA,Av=rf[m],cf[m],Aval[m]; rM,ccM,Mv=rf[m],cf[m],Mval[m]
nf=len(x)
def mv(rows,cols,V,z):
    y=np.zeros(nf); np.add.at(y,rows,V*z[cols]); return y
Ax=mv(rA,ccA,Av,x); Mx=mv(rM,ccM,Mv,x)
Nhat=float(x@Ax); Dhat=float(x@Mx); mu=Nhat/Dhat
ax=np.abs(x)
SA=float(ax@mv(rA,ccA,np.abs(Av),ax)); SM=float(ax@mv(rM,ccM,np.abs(Mv),ax))
eps=2.0**-52; g7=7*eps/(1-7*eps); gn=48641*eps/(1-48641*eps)
dN=(g7+gn+g7*gn)*SA; dD=(eps/2)*SM+(g7+gn+g7*gn)*SM
U=(Nhat+dN)/(Dhat-dD)
print(f"muhat={mu:.10f} dN={dN:.2e} dD={dD:.2e} U={U:.10f}")

# exact-rational FK lower
x0=Fraction(120241,50000); q=x0*x0/Fraction(4,1)
a=[Fraction(1)]
for k in range(1,16): a.append(a[-1]*q/Fraction(k*k))
K=12; s=sum(((-1)**k)*a[k] for k in range(K+1)); rem=a[K+1]
assert s-rem>0 and q<Fraction(146,100)
def ab(n_,d_,K_):
    xx=Fraction(n_,d_); ss=sum(((-1)**k)*Fraction(xx**(2*k+1),2*k+1) for k in range(K_))
    rr=Fraction(xx**(2*K_+1),2*K_+1)
    return (ss,ss+rr) if K_%2==0 else (ss-rr,ss)
lo1,hi1=ab(1,5,12); lo2,hi2=ab(1,239,4)
pi_lo=16*lo1-4*hi2
assert pi_lo>Fraction(314159,100000)
L0=Fraction(314159,100000)*x0*x0/Fraction(3,1)
L0f=float(L0)
print(f"L0={L0f:.8f} (exact {L0})")
MPS=9.63972384402
print(f"MPS={MPS} in [{L0f},{U}]? {L0f<=MPS<=U}")
print(f"width={float(U)-L0f:.6f}; target 5e-04 met? {float(U)-L0f<=5e-04}; fallback 5e-03 met? {float(U)-L0f<=5e-03}")
print(f"numpy {np.__version__} python {sys.version.split()[0]} elapsed {time.time()-t0:.1f}s")
