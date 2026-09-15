import numpy as np
def residual(d,b,r):
    s=2-b; beta=(d-2)/s; alpha=(4-2*b)/(d-2)
    C=((d-b)*(d-2))**(1/alpha)
    u=1+r**s
    W=C*u**(-beta)
    Wp=C*(-beta)*s*r**(s-1)*u**(-beta-1)
    Wpp=C*(-beta)*s*((s-1)*r**(s-2)*u**(-beta-1)+r**(s-1)*(-beta-1)*s*r**(s-1)*u**(-beta-2))
    return Wpp+(d-1)/r*Wp + r**(-b)*W**(alpha+1), W
for d,b in [(6,0.3),(6,1.0),(7,1.5),(10,0.7),(12,1.9)]:
    for r in [0.05,0.5,2.0,20.0]:
        res,W=residual(d,b,r)
        print(f"d={d} b={b} r={r}: W={W:.6e} resid={res:.3e}")
    s=2-b; beta=(d-2)/s
    print(f"  tail check: W*r^(d-2) -> {residual(d,b,1e4)[1]*1e4**(d-2):.6f} (expect C={( ((d-b)*(d-2))**((d-2)/(4-2*b)) ):.6f})")
