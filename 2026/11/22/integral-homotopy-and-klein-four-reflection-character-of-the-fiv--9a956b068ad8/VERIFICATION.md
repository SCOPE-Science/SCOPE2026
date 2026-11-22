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

Run `python3 verify_grid45_robust.py` from a directory containing the bundled Python file. It requires only Python 3 standard-library modules and no external papers or downloads. The included `CHECK_OUTPUT.txt` is the actual expected terminal output from the supplied source.

The source tests all 1,048,576 subsets by both an exact independence-number recursion and a separate exhaustive list of independent five-subsets with Boolean propagation. It validates the exact face vector and Euler characteristic, regenerates all 36,039 matched cover incidences, confirms the 490 critical cells, and topologically sorts the complete oriented 446,610-incidence Hasse diagram. These exact finite computations, together with Forman's theorem, imply the integral wedge homotopy type.

For all four geometric symmetries it computes the full simplicial Lefschetz number with the sign of each induced oriented-simplex permutation, then uses the uniquely supported seventh homology to compute traces and rational character multiplicities.

A successful run prints `VERIFY_OK`. A failed assertion or incomplete directed sort is not a certificate of the claim. The code proves only the specified fixed finite complex, not larger grid families. Independently checking bibliographic priority and the mathematical proof remains outside these automated reproductions.
