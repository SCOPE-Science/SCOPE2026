# Smallest-norm triple: pi1,pi2 = 19-pair; pi3 = 487 (-23-21w), value 2.
# Verify: norms, primariness, lam3-clean, pairwise symbols, theta certificate, central value detail.
from eisen import *
from u3lib import *
pi1=(-5,-3); pi2=(-2,3); pi3=(-23,-21)
for p in (pi1,pi2,pi3):
    print(e2str(p),"N=",enorm(p),"primary?",is_primary(p),"clean?",edivides((-3,-6),esub(p,ONE)))
print("s12=",cubic_symbol(pi1,pi2),"s21=",cubic_symbol(pi2,pi1))
print("s13=",cubic_symbol(pi1,pi3),"s31=",cubic_symbol(pi3,pi1))
print("s23=",cubic_symbol(pi2,pi3),"s32=",cubic_symbol(pi3,pi2))
Th=((-4,-4),(-4,-4),(4,0))
N=knormXYZ(*Th,pi1)
print("N(Th)=",e2str(N))
q,r=edivmod(N,pi2); print("N/pi2: q=",e2str(q),"r=",e2str(r))
print("N(pi2)=",enorm(pi2),"N(q)=",enorm(q))
et=cube_root_Zw(emul(q,(1,0)))
print("cuberoot(q)=",None if et is None else e2str(et), "check:", None if et is None else eeq(emul(emul(et,et),et),q))
for u in UNITS:
    et=cube_root_Zw(emul(q,u))
    if et is not None:
        print("  unit",e2str(u),"cuberoot",e2str(et)); break
print("central value:",central_value(Th,pi1,pi3))
# full per-root detail
STh=ksigma(Th)
for r in cube_roots_mod(pi1,pi3):
    a=evalK1(Th,r,pi3); b=evalK1(STh,r,pi3)
    print(" r=",e2str(r),"Th(r)=",e2str(emod(a,pi3)),"a=",charval(a,pi3),"b=",charval(b,pi3))
# factor N(Th)/pi2 as cube: give W with N = pi2*W^3? q = u*eta^3 => N = pi2*u*eta^3. Absorb u: u must be a cube?
print("units that are cubes:",[e2str(u) for u in UNITS if cube_root_Zw(u) is not None])
