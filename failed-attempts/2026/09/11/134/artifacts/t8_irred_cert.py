import sympy as sp
T=sp.symbols('T')
hT=sp.Poly(T**8+T**6-3*T**4+3*T**2-1, T, domain=sp.GF(3))
print("hT mod3:", hT.as_expr())
base=sp.Poly(T, T, domain=sp.GF(3))
def poly_mod_pow(base_poly, e, mod_poly):
    # compute base^(3^e) mod mod_poly via repeated cubing
    r=base_poly
    for _ in range(e):
        r=(r**3) % mod_poly
    return r
for d in [1,2,4]:
    r=poly_mod_pow(base,d,hT)
    g=sp.gcd(r-base, hT)
    print(f"d={d}: deg gcd(T^{3**d}-T,hT)={g.degree() if g else 0} monic={g}")
# order check: hT divides T^{3^8}-T ?
r8=poly_mod_pow(base,8,hT)
print("T^{3^8}-T mod hT == 0 ?", (r8-base).is_zero)
# degree check
print("deg hT =", hT.degree())
# six candidate cyclotomic trace polys, phi(N)=16
from sympy import cyclotomic_poly, resultant, expand
y=sp.symbols('y')
hQ=T**8+T**6-3*T**4+3*T**2-1
print("hT over QQ factor:", sp.factor(hQ))
for N in [17,32,34,40,48,60]:
    Phi=cyclotomic_poly(N,y)
    R=expand(resultant(Phi, y**2-T*y+1, y))
    # R should be square of degree-8 minpoly; take sqrt via factor
    fl=sp.factor_list(R)
    print(f"N={N}: factor_list={fl}")
    # extract square root
    from collections import Counter
    sq=1
    for fac,mult in fl[1]:
        sq*=fac**(mult//2)
    print(f"   sqrt poly = {expand(sq)}; equals hT? {expand(sq-hQ)==0 or expand(sq+hQ)==0}")
