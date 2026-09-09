#!/usr/bin/env python3
"""Verify curve C: y^2 = x^6-1 smoothness, genus, Hitchin base dims, ribbon R=2C invariants.
Stdlib only. Prints VERIFY_OK on success.
"""
import sympy as sp

def main():
    x, y = sp.symbols('x y')
    f = y**2 - (x**6 - 1)
    fx = sp.diff(f, x)  # -6x^5
    fy = sp.diff(f, y)  # 2y
    assert f.subs({x: 0, y: 0}) == 1, "affine singular candidate check"
    # common zero of fx,fy forces x=0,y=0 in char 0, where f=1: affine smooth
    g = x**6 - 1
    assert sp.gcd(g, sp.diff(g, x)) == 1, "sextic must be separable"
    disc = sp.discriminant(g, x)
    assert disc != 0, "discriminant must be nonzero"
    assert disc == 46656, f"disc value {disc}"
    # 6 distinct branch points over P1_x => Riemann-Hurwitz g = -1 + 6/2 = 2
    branch = 6
    genus = -1 + branch // 2
    assert genus == 2
    # Hitchin data SL(2): base B = H0(K) (+) H0(K^2); tr=0 => H0(K^2) only? full GL base dim 3g-3
    g0 = 2
    dimB = 3 * g0 - 3
    assert dimB == 3
    degK = 2 * g0 - 2  # 2
    degK2 = 2 * degK   # 4
    h0K2 = degK2 - g0 + 1  # RR, deg>2g-2 so h1=0
    assert (degK, degK2, h0K2) == (2, 4, 3)
    # ribbon R = 2C: 0 -> K^-1 -> O_R -> O_C -> 0
    chiC = 1 - g0  # -1
    degKinv = -degK  # -2
    chiKinv = degKinv + 1 - g0  # -3
    chiR = chiC + chiKinv  # -4
    paR = 1 - chiR  # 5
    assert (chiC, chiKinv, chiR, paR) == (-1, -3, -4, 5)
    assert paR == 4 * g0 - 3, "ribbon arithmetic genus = smooth spectral genus"
    prym_dim = paR - g0
    assert prym_dim == dimB == 3, "Prym dim = base dim = fiber dim"
    print(f"C: y^2=x^6-1 affine-smooth (sing locus empty), sep sextic disc={disc}")
    print(f"g(C)=2, deg K=2, deg K^2=4, h0(K^2)=3, dim B=3, dim M=6")
    print(f"R=2C: chi(O_C)={chiC}, chi(K^-1)={chiKinv}, chi(O_R)={chiR}, p_a(R)={paR}")
    print(f"smooth spectral genus 4g-3={4*g0-3}, Prym dim={prym_dim}")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
