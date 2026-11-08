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

# Reproducibility and scope of checks

The bundled standalone Python 3 script `check_biclique_root.py` requires `numpy` and `scipy`. Execute `python check_biclique_root.py` to enumerate integer instances \(2\le p,q\le7\) with proper nonempty block sizes and independently optimize convex combinations of the graph-root vertices. It compares the optimizer's center and squared radius to the analytic formulas, and checks each predicted contact orbit and the positive squared-distance clearance where appropriate.

The check succeeded for 441 parameter quadruples, including 205 strict-screening cases, with the marker:

`BICLIQUE_ROOT_MINIMUM_SPHERE_CHECKS_PASSED 441 screened_cases 205`

The analytical proof, not these finite floating-point experiments, establishes the result for arbitrarily large integer parameters. Floating-point optimization may have numerical tolerances; the symbolic algebraic deductions in `RESULT.md` are the primary evidence. No external independent audit has been performed.
