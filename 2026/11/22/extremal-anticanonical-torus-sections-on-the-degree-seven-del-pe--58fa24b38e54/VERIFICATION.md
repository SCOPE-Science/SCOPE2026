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

# Verification

The standard-library `check.py` uses exact integer inclusion–exclusion to enumerate all 255 nonempty exponent subsets of the eight-monomial polygon. It compares shadow polynomial coefficients with each proposed lower bound after the substitution `t=s+4` and checks coefficientwise nonnegativity. Each cardinality has a matching subset. The footprint theorem and falling-factorial witnesses convert this finite certificate into a proof for all finite fields q>=5.

The program independently enumerates all rank-three and rank-four flats of torus evaluation rows over the prime fields of five and seven elements, using exact modular elimination. It finds 8 and 96 optimizing flats in characteristic five and 12 and 360 in characteristic seven. Their configurations are checked against coordinate-fibre geometry. Output is in `check_output.txt`. The program is finite corroboration and does not substitute for the interpolation proof of all equality cases.

The interpolation proof establishes that no non-coordinate line can contain an optimal point set and two distinct points outside any coordinate fibre impose independent evaluations on the residual sections. Together these show exactly one full coordinate fibre for each optimal rank-three flat and exactly that fibre plus one off-fibre point for each optimal rank-four flat. Source comparisons, limitations, and review status are separately recorded. No independent audit or external mathematical certification has been performed.
