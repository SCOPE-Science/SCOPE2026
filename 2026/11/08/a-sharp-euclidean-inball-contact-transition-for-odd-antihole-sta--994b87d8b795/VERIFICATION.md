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

The standalone `checker.py` was executed with Python 3, NumPy 2.3.5, and SciPy 1.17.0. It printed `ODD_ANTIHOL_EUCLIDEAN_INBALL_FINITE_CHECKS_PASSED` after testing \(a=2,3,4,5,6,7\). For each instance, the code generates all \(2n+1\) actual stable-set vertices and every proposed facet; checks vertex feasibility and facet affine ranks; solves the Euclidean inball LP independently; compares 40 deterministic random-direction LP support values with the exact vertex support function; and verifies clique-shell multiplicities and tangent counts. The infinite facet completeness, uniqueness, and threshold results are proved analytically in `RESULT.md` rather than inferred from finite experiments.

Run from the directory containing the two files with `python checker.py`, after installing `requirements.txt`. Numerical LP comparisons use tolerances stated in the source; these are finite numerical checks, not an exact general certificate. Full primary texts were not available for every older source cited in the literature comparison. No external or independent mathematical audit has been performed.
