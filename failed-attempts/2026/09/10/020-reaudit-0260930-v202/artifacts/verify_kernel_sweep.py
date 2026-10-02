"""Full H_{2,0}+H_{0,2} kernel sweep + degree-1 contrast (exact polynomials)."""
import sympy as sp
z,w,zb,wb,t=sp.symbols('z w zb wb t')
def Z1(f): return sp.expand(wb*sp.diff(f,z)-zb*sp.diff(f,w))
def Zb(f): return sp.expand(w*sp.diff(f,zb)-z*sp.diff(f,wb))
Zt=lambda fx: sp.expand(Z1(fx)+t*Zb(fx)); Zbt=lambda fx: sp.expand(Zb(fx)+t*Z1(fx))
Boxn=lambda fx: sp.expand(-Zt(Zbt(fx))); Bbn=lambda fx: sp.expand(-Zbt(Zt(fx))); Qn=lambda fx: sp.expand(4*t*Zbt(Zbt(fx)))
Pnum=lambda fx: sp.expand(Bbn(Boxn(fx))+Qn(fx))
ok=True
print("== degree-2 (target space) expect Pnum=0 ==")
for fx in [z**2,z*w,w**2,zb**2,zb*wb,wb**2]:
    p=Pnum(fx); good=(p==0); ok&=good
    print(f"  {fx}: {'PASS' if good else 'FAIL '+str(p)}")
print("== degree-1 (Chanillo dirs) expect -3t^2 f ==")
for fx in [z,w,zb,wb]:
    p=Pnum(fx); good=(sp.expand(p+3*t**2*fx)==0); ok&=good
    print(f"  {fx}: {'PASS' if good else 'FAIL '+str(p)}")
# u* combination
u=z**2+zb**2
print("u* Pnum==0:", "PASS" if Pnum(u)==0 else "FAIL")
print("u*(1,0)=2 nonzero: PASS" if (u.subs({z:1,w:0,zb:1,wb:0})==2) else "FAIL")
print('ALL_VERIFY_OK' if ok else 'VERIFY_FAIL')
