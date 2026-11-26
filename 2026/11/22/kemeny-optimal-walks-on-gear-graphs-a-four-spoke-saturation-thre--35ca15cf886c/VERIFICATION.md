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

For L=I−P the regularized inverse trace is strictly convex in the unrestricted edge variables: its second derivative in a nonzero direction H is twice the squared Frobenius norm of A^{-1} H A^{-1/2}. Compactness and divergence at disconnected limits give a unique optimum. Dihedral invariance leaves two weights, and increasing y at fixed x lowers the trace strictly, so y=(1−x)/2. The constant Fourier block has two positive eigenvalues with sum (n+1)x+4y and product 2(2n+1)xy. The nonconstant two-by-two blocks have determinant 2xy+4y² sin²(π j/n) and trace x+4y, giving the scalar objective. At x=1/n the nonconstant derivative contribution has sign given by (3−x)S1−(2−x)S2, where S_k=sum d_j^{-k}. The mean of d_j is (n+2)/(2n); Jensen and Cauchy–Schwarz give the strictly negative sign for n≥7 since n²−7n+2>0. The constant-block contribution is negative there as well. Exact differentiation of full rational inverse matrices confirms all four endpoint derivatives for n=3–6; the n=3 objective is also exactly recovered. Strict convexity implies saturation precisely for n≥4 and the unique interior quartic root at n=3. The cyclic resolvent sums a geometric progression of surviving Fourier coefficients; after removal of the zero grid point it gives the stated coth formula. Its prefactor is 2n+1+1/(n−1), the constant block tends to 3/2, and the coth correction is exponentially small. For the benchmark, the Riemann integral of 1/(2+4 sin²(π u)) is 1/(2√3).

## originality

PASS

The identical catalogue entry is the bound finding, not an independent antecedent. The strongest distinct inspected analogues are exact saturated-hub and Kemeny results on wheels and helms; neither has the alternating subdivided rim or the relevant Fourier denominators. The general reversible optimization framework and fixed-conductance index do not give the exceptional size or asymptotic constants. This is a bounded, best-of-knowledge judgment.

## value

PASS

This is a complete allocation and holding classification for a standard graph family, with an actual change of active constraint at n=4. The exact threshold and the change from n² to n^{3/2} show why a natural degree-based symmetric walk is not order-optimal. Neither a fixed-weight index nor a generic solver would supply that structural conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
