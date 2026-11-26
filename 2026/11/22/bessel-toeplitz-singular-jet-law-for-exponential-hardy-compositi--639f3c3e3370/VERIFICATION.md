---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Exponential conjugacy gives the simple eigenvalues q^k and the exact iterate M_{exp(A(1−q)z)}D_q, q=r^n. On the j-fold exterior space, q^{−j(j−1)/2} times the exterior power of D_q differs from the projection onto the first j monomials wedged together by an operator of norm q: all other index sums increase by at least one. The multipliers converge in operator norm as q→0, giving the stated rank-one limit; the exterior norm is the singular-value product. The limiting squared norm is the positive Gram determinant of z^k exp(Az), with entries I_{k−ℓ}(2A). Division for consecutive j gives the asserted fixed-rank law. For the strict bound, reverse the minimizing monic polynomial to p*, with p*(0)=1 and identical boundary modulus. The trial integral is the squared Hardy norm of exp(Az)p*, which is at least 1 from its constant coefficient and equals 1 only if p*=exp(−Az), impossible for A>0. Multiplying the monic trial by z gives monotonicity, and reversed exponential Taylor polynomials give the limiting upper bound 1. At A=0 the operator is diagonal. RESULT.md, VERIFICATION.md and checker.py were inspected; finite truncations are corroboration, not the proof.

## originality

PASS

Pass for the explicit fixed-rank iterate coefficients in the exponential Hardy model and their comparison to its eigenvalue coefficients. The graded exterior-power method has been used for other families, and the Toeplitz prediction-error interpretation and rank limit are classical in substance. No inspected distinct result supplies this operator's Bessel Gram ratios as its fixed-index iterate asymptotics.

## value

PASS

Optimal fixed-rank approximation errors for these iterates are not determined by the exactly geometric spectrum. The constants measure that discrepancy at every fixed rank and prove that it disappears as the rank of the coefficient increases, a useful quantitative refinement of convergence to rank one. No simultaneous rank/iterate limit is required for that interpretation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
