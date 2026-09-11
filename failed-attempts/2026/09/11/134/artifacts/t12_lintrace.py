import sympy as sp
T,T2,y=sp.symbols('T T2 y')
fT=T**4+9*T**3+27*T**2+35*T+17
print("fT(0)=17, fT(-1)=1, fT(-2)=3, fT(-4)=161, fT(-5)= 625-1125+675-175+17=17? ", sp.expand(fT).subs(T,-5))
from sympy import factor_list
for p in [2,3,5,7]:
    try:
        print(f"mod{p}:", factor_list(fT, domain=sp.GF(p)))
    except Exception as e: print("err",e)
# Rabin test mod3 if promising
from sympy import Poly
hT=Poly(T**4+2*T+2, T, domain=sp.GF(3))  # fT mod3
base=Poly(T,T,domain=sp.GF(3))
def ppow(e):
    r=base
    for _ in range(e):
        r=(r**3)%hT
    return r
for d in [1,2]:
    print(f"mod3 d={d} gcd deg:", sp.gcd(ppow(d)-base,hT).degree())
print("T^(3^4)-T mod hT ==0 ?", (ppow(4)-base).is_zero)
# candidate degree-4 trace polys (phi=8): compare
cands={"15":T**4-T**3-4*T**2+4*T+1,"16":T**4-4*T**2+2,"20":T**4-5*T**2+5,"24":T**4-4*T**2+1,"30":T**4+T**3-4*T**2-4*T+1}
for k,v in cands.items():
    print(k, "equal fT?", sp.expand(v-fT)==0)
