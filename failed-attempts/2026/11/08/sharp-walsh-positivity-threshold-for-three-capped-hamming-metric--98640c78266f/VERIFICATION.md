---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A nontrivial Walsh character of weight s has shell sums z=n−2s and (z²−n)/2 on shells 1 and 2, and sum −1 over all nonzero vectors. The resulting distance eigenvalue is −3^p+(1−3^p)z+(2^p−3^p)(z²−n)/2. It is concave in z with vertex at −(3^p−1)/(3^p−2^p). For 0<p<1 this ratio lies strictly between 2 and 3: strict concavity gives the first inequality, while 2·3^p−3·2^p+1 grows strictly from zero. The unique nearest admissible z is −2 for even n and −3 for odd n, including n=4 and 5. Twice the maximizing eigenvalue is the stated threshold polynomial in each parity. At p=0 each equals −2; at p=1 they are n−2 and n−3. Both strictly increase for p≥0: in the even case the positive base-3 term dominates the base-2 term after differentiation; in the odd case n=5,7,9 have nonnegative coefficients and n≥11 has the same derivative dominance as the even case. Thus the unique critical level stays positive above the root even for p≥1. The small-time kernel Fourier coefficient has derivative −λ_s(p) on its nonconstant layer; Schoenberg supplies the converse and the rank of the centered Gram matrix gives the minimal dimensions. For the asymptotic write the threshold expression as n(3^p−2^p)−u3^p+v2^p−h, with (u,v,h)=(2,4,4) or (5,9,6). Matching the constant and n⁻¹ terms gives p=2/(nL)+c/n² with c=2[(u−1)log3−(v+1)log2]/L²; the residual O(n⁻²) and derivative nL+O(1) give an O(n⁻³) root error. The critical multiplicity is a binomial coefficient a bounded offset from the center, so Stirling gives its stated asymptotic.

## originality

FAIL

Two distinct same-day Resultary records explicitly restrict to q≥3, so their theorem statements alone do not include the binary case and their dates do not order priority. However, the complete nearest-lattice and strictness proof in a7286fd067ef is valid at q=2 without its stated restriction and gives the exact binary threshold and nullity. The second-order and multiplicity expansions in 620a1519c809 also transfer once this crossing is known. The remaining parity expressions are literal substitutions. This is verified substantive proof coverage, not an inference from titles, dates or an unavailable source.

## value

FAIL

The exact negative-type threshold and rank jump are natural mathematical invariants. Here, however, the distinct binary record offers a parameter evaluation of the identical Fourier-layer mechanism that already covers the binary case at proof level. The parity split and coefficients follow by arithmetic from the matching general formulas and do not close an additional substantive gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
