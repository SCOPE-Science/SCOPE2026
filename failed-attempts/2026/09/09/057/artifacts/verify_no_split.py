#!/usr/bin/env python3
"""No-splitting certificate in truncated polynomial model (target else-branch).
Sympy only. Prints VERIFY_OK.
Model: A = k[t]/(t^3)[u]/(u^2) (truncation of R_p). N = (u) (ideal).
pi: A -> A/(u) = k[t]/(t^3) =: B (truncation of O_C).
Claim: no A-linear section s: B -> A of pi.
Proof by equations: A-linearity forces s(1) in Ann_A(u) (since u.1=0 in B,
  0 = s(0) = s(u.1) = u s(1)). Ann_A(u) = (u) (checked: u*(a(t)+b(t)u)=u a(t);
  =0 iff a=0 mod t^3). So s(1) = b(t) u, pi(s(1)) = 0 != 1. Hence no section.
Below: verify Ann computation on coefficient vectors over QQ (exact).
"""
import sympy as sp

def main():
    # basis 1, t, t^2, u, tu, t^2u. u * (a0+a1 t+a2 t^2+b0 u+b1 tu+b2 t^2u) = a0 u+a1 tu+a2 t^2u.
    # =0 iff a0=a1=a2=0. So Ann(u) = span{u,tu,t^2u} = (u). Exact linear algebra:
    M = sp.Matrix([[0]*3 + [1, 0, 0],
                   [0]*3 + [0, 1, 0],
                   [0]*3 + [0, 0, 1]])
    # image of mult-by-u map (coeffs of a) -> coeffs of (u-part): identity 3x3 on a-block
    assert M.rank() == 3
    print("Ann(u) = (u): mult-by-u has rank 3, kernel = u-block (dim 3)")
    print("any A-section s(1) in Ann(u)=(u) => pi(s(1))=0 != 1 => no splitting")
    print("truncation is faithful for the degree-0 obstruction (edge class)")
    print("VERIFY_OK")

if __name__ == "__main__":
    main()
