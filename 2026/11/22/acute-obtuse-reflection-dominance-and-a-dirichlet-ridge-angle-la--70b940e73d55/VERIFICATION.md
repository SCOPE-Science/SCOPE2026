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

Run `python3 verify.py` in a directory containing the extracted `verify.py` and this document. Python 3.9 or newer is sufficient; no nonstandard packages or downloaded data are needed.

The checker enumerates all tubes and compatible pairs of cycles of lengths 3 through 12, compares squared exterior-normal cosines exactly as rational numbers, and verifies all angle multiplicity formulas. For lengths 3 through 6 it independently constructs the complete vertex set of the Minkowski sum by taking coordinate maxima of every connected-subset simplex over all strict coordinate orders. It checks ranks of every proposed facet and every pair-face; ranks are calculated exactly modulo the prime 1,000,000,007. The modular-rank check establishes a full rational-rank lower bound whenever full rank is found. For these small integer matrices, the asserted lower and upper dimensions coincide, giving the tested face incidences. The script also checks finite reflected-angle dominance for orders 4 through 25 by rational squared-cosine keys.

Expected terminal result: `CYCLO_RIDGE_AND_REFLECTION_PASS`.

# Limits of checks

The finite enumerations are not an exhaustive proof over unbounded dimensions. The general counting and the Dirichlet weak limit are proved in `RESULT.md` by exact facet-combinatorics and composition/Riemann-sum arguments. No independently performed mathematical audit is claimed.
