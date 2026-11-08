---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python verify.py` with SymPy installed. The program specializes endpoint observations to a deterministic sum of distinct exponentials, forms all maximal Hankel minors, computes their reduced zero-dimensional ideals with Groebner bases over the rationals, and counts standard monomials. It also checks the ranks of excluded endpoint unit matrices for the same tested pairs.

Expected output ends with `ENDPOINT_SEVEN_EXACT_SPECIALIZATIONS_OK`. The verified pairs \((r,n)\) are \((2,5),(2,6),(2,7),(3,7),(3,8),(3,9),(4,9)\); their respective lengths are \(3,6,10,4,10,20,5\). These finite calculations are neither a proof that all specializations are generic nor proof of the infinite-dimensional parameter-range theorem.

The general proof uses a standard degeneracy-locus degree calculation, a direct anti-triangular minor argument, projective finiteness from ampleness, and the projection-from-a-point degree formula with positive local multiplicity and the nonincrease of projective degree under any remaining linear projection. Generic finite completeness of all minimal observation sets is from Reed–Tsakiris's uniformity theorem (arXiv:2610.27554).

Self-review is reported in REVIEW.md; independent audit has not been performed.
