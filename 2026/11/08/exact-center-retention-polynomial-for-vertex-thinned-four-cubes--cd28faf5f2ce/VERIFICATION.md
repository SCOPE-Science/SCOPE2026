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

Run `python3 verify_cube_center.py` using Python 3 and no third-party packages. The script performs two fully separate finite calculations with rational and integer arithmetic. Method one checks exact circuits of eight antipodal-pair representatives, characterizes all possible strict sign patterns, constructs integer normal witnesses for all 104 feasible patterns, and counts the down-closures of their 16-bit vertex masks. Method two enumerates inclusion-minimal positive dependencies among all sixteen vertices, classifies their sizes as eight pairs, twenty-four quadruples and sixteen quintuples, and directly counts masks containing any such support. Both methods return the identical complete cardinality distribution and certify the exact polynomial.

Execution on the embedded source returned `CUBE4_EXACT_RELIABILITY_TWO_CERTIFICATES_PASSED`. These computations are genuinely exhaustive for the stated finite cube, by strict hyperplane separation and the five-vertex support bound from Carathéodory's theorem. No finite calculation is used as a substitute for an infinite-dimensional statement. No independent audit has been performed; historical novelty remains provisional.
