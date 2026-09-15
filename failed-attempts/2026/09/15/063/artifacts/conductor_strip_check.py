"""Bounded recovery test: standard effective strip vs claimed power strip.
Compares 1/log(C(D)) (standard effective, Hoffstein-Ramakrishnan style)
against c*C_target^{-eps} for the GHL auxiliary D(s)=L(s,Pi x Pi~).
Also quantifies chi-uniformity cost: number of chi ~ Q^{O(A)} vs fixed eta saving.
"""
import math

def main():
    n, np_ = 3, 1
    B = 2*(1+n+np_)  # conductor exponent blow-up, crude
    print(f"n={n} n'={np_} B~{B}")
    for logC in [math.log(1e6), math.log(1e12), math.log(1e24)]:
        C = math.exp(logC)
        std = 1.0/(B*logC)
        for eps in [0.05, 0.1]:
            claimed = C**(-eps)
            print(f"C_target=1e{logC/math.log(10):.0f} eps={eps}: std~{std:.3e} claimed~{claimed:.3e} ratio_claimed/std={claimed/std:.3e}")
    # chi-uniformity: family sizes
    for Qexp in [6, 12]:
        Q = 10.0**Qexp
        for A in [1, 2]:
            nchi = Q**(2*A)  # rough #chi with C(chi)<=Q^A over number field
            print(f"Q=1e{Qexp} A={A}: #chi~1e{2*A*Qexp}, fixed-eta saving on |F_n|~Q^5-scale cannot absorb unless gain>>#chi")

if __name__ == "__main__":
    main()
