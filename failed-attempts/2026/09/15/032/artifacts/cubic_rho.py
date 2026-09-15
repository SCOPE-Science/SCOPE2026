"""Resolve Eq.(18) typesetting: try Cardano from cubic in rho0 directly.
From 4(1-J/r)=J^2, J=a(1-r): 4(1 - a(1-r)/r) = a^2(1-r)^2.
=> a^2(1-r)^2 + 4a(1-r)/r - 4 = 0 => multiply r: a^2 r(1-r)^2 + 4a(1-r) - 4r = 0
=> a^2(r - 2r^2 + r^3) + 4a - 4a r - 4r = 0
=> a^2 r^3 - 2a^2 r^2 + (a^2 - 4a - 4) r + 4a = 0.  ...(B)
Depress and solve; compare physical root with J-cubic root; test printed formula variants.
Also directly test whether printed (18) might use cos(theta/3) or cos((pi-theta)/3) etc.
with theta from (19) — but (19) itself may be mis-extracted (sqrt(6)*sqrt(...)? signs?).
Brute-force: evaluate all cos((k*pi ± theta)/3) variants.
"""
import numpy as np, math

def phys_rho(a):
    c = np.poly1d([a*a, -2*a*a, a*a-4*a-4, 4*a])
    rs = np.roots(c)
    out=[]
    for r in rs:
        if abs(r.imag)<1e-8 and 0<float(r.real)<1:
            out.append(float(r.real))
    return out

def variants(a):
    th_denom = 36-18*a-a*a
    th_num = 6*math.sqrt(6*a**4+18*a**3+20*a**2+24*a+8)
    theta = math.atan2(th_num, a*th_denom)
    pre = math.sqrt(a*a+12*a+12)/a
    res={}
    for k in range(3):
        for s in [+1,-1]:
            r=(2/3)*(1-pre*math.cos((k*math.pi+s*theta)/3))
            res[f"k={k},s={s:+d}"]=r
    return theta,res

for a in [0.5,0.7,1.0]:
    print(f"a={a} physroots={phys_rho(a)}")
    th,res=variants(a)
    print(f"  theta={th:.6f}")
    for k,v in res.items():
        J=a*(1-v)
        ok = (0<v<1 and J<v)
        print(f"   {k}: rho={v:.6f} {'PHYS?' if ok else ''}")
