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

# Reproducible verification
Run `python3 VERIFY.py` with Python 3 and its standard library. Inputs are 21 integer triples copied explicitly from the first public polytope construction. No external files, network access, symbolic packages, or convex-hull solvers are required.

1. Enumerate all \(\binom{21}{3}=1330\) triples and retain exactly the supporting planes. Verify that the 37 primitive facet inequalities have offsets 1, 3, or 6, and form the full side-facet generator set.
2. Check that the four named integer vectors occur and the positive weights \(14,\frac32,\frac32,1,1,9,9,111,74\) cancel every center coordinate in the inball inequality, with objective coefficient \(257+14\sqrt{15}+3\sqrt{23}+2\sqrt{770}\).
3. Verify algebraic equality of the seven active side conditions using the four identities in the proof, and equality of both base conditions.
4. For each of the 1,362 other side facets, enclose its signed inequality slack with exact rational intervals. The bound for each square root uses \(\lfloor10^{23}\sqrt{k}\rfloor\), computed as `isqrt(k*10**46)`, yielding mathematically rigorous enclosures. Every lower-bound slack is strictly above \(1/500\).
5. Verify that the difference-vector determinant is 148, proving the active constraints single out a unique center, and verify that the maximum squared facet-normal norm is 1525.

The entire finite enumeration is exhaustive for the stated 21-point configuration. The verifier does not independently establish originality, and it makes no infinite-family claim. The arithmetic proof is readable in `RESULT.md`.
