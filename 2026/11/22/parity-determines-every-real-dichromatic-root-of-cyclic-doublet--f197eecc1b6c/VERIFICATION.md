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

Every directed cycle uses all layers; any color in all layers furnishes an r-cycle. Inclusion-exclusion over named colors has only singleton and pair terms, counted by (2q-1)^r and 2^r respectively. Interpolation gives the polynomial; valid two-colorings exist by assigning opposite monochromatic colors to two layers. For F_r=P/q, F_r(0) is nonzero and F'_r(1)=2^(r-1)-1>0, giving simplicity at 0 and 1. Below x=1/2, elementary bounds by x and 1-2x give F_r<0 for both parities; on [1/2,1), the difference x^(2r)-(2x-1)^r is at most r*x^(2r-2)*(1-x)^2, yielding a strict upper bound below zero. For x=1+y>1, the linear, quadratic and cubic coefficients are 2^(r-1)-1, -(r-1) and r-1. The higher coefficients are nonnegative: the binomial ratio starts strictly above 2^3 at degree 3 and its successive ratios exceed 2 through degree r. The phrase 'equality at j=3' in the proof is imprecise; evaluating that coefficient gives r-1, not equality of the two binomial terms. The positive lower bound follows by completing the square in y^2-y. For negative q=-t, all terms of P(-t)/t are positive when r is even. When r is odd, its signs at 0, 1/2 and infinity are +,-,+, and the descending coefficient signs have exactly two changes (the linear coefficient does not affect the count). Descartes' bound including multiplicity proves exactly two simple roots, one on each side of t=1/2.

## originality

PASS

The inspected prior statements concern general dichromatic polynomial structure, density over digraph classes, or exact results for different families. They do not give the oriented cyclic-doublet polynomial together with its complete, parity-controlled real-root classification.

## value

PASS

This is an explicit natural oriented family with all real roots located and their multiplicities controlled uniformly in its size. It gives a test case for general directed root theory: the odd sizes have two negative roots despite ordinary chromatic-polynomial intuition, whereas the even sizes and all positive-root regimes are completely resolved. The enumerator alone, without the sign census, would not provide this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
