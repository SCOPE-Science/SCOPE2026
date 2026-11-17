---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: For N=2^k and C={(x,x³)}, write s=x+y. The exact identity x³+(s−x)³=s³−3s x(s−x) gives two Hensel-lift solutions for each odd t when s odd; s=0 contributes r(0,0)=N. For nonzero even s=2^v u, choosing 2h=s reduces to t−2h³=3s(x−h)², so each target fiber equals 2^v times square-root count rho_{k−v}. The standard unit-square classification yields B_m=∑rho_m²=m·2^m by the recurrence B_m=2^(m+1)+4B_{m−2}; square-image counts Q_m yield the two parity cases for support. Summation gives E=N²(k²−k+8)/4 and |C+C|=(5N²+13N−10)/18 for odd k, or (5N²+14N−10)/18 for even k. Character orthogonality proves normalized fourth moment. Independently exhaustively enumerated all pairs k=1..8 with exact matches; no inference from finite range.

## originality

PASS

PASS best-of-knowledge: General mod-2^k quadratic-congruence root solvers are prior standard arithmetic and cover pointwise root counts, not their valuation-weighted aggregate energy and support laws for this graph. Hickman–Wright finite-ring Fourier restriction and Wooley cubic Weyl literature provide bounds/general frameworks, not both exact dyadic aggregate formulas. Closely named published Resultary theorems for (x,x²,x³) have a THIRD coordinate and energy kN², not this two-coordinate (x,x³) curve with energy N²(k²−k+8)/4. The known 3D case does not imply the 2D energy; the 2D graph has fewer equality constraints and a different support constant.

## value

PASS

PASS: Exact additive energy, support density 5/18 and complete convolution fibers for a natural cubic Fourier graph over all dyadic rings measure 2-adic ramification in a nonquadratic restriction model. The quadratic-in-k normalized fourth moment is a substantial infinite family invariant, not a routine root-solver relabeling; no sharp arbitrary-weight extension claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
