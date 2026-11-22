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

# Verification of the two-scale chord theorem

Execute `python3 artifacts/check.py` from the extracted package directory using the Python 3 standard library. The program constructs all sign orientations without consulting the coefficient formula, discards the directed four-cycle patterns, computes all distinct zonotope vertices and their Euclidean squared distances from doubled integer coordinates, and compares them coefficient-by-coefficient against a separate inclusion-exclusion convolution implementation for dimensions \(2\) through \(6\). It checks 1,085,463 unordered pairs. It also verifies coefficient totals, the minimum positive squared distance, the unique diametral pair, and a known aggregate squared-distance moment for dimensions \(2\) through \(12\).

Expected successful terminal output:

`BICLIQUE_TWO_POINT_PASS brute_force_n=2..6 checked_pairs= 1085463 transfer_n=2..12`

The program's finite tests corroborate the exact formula. They do not prove either asymptotic limit. Those limits use the proved two-branch decomposition, a bivariate central limit theorem, covariance diagonalization, a law of large numbers, and exponentially small exceptional mass as detailed in `RESULT.md`. The comparison with published literature supports provisional historical originality, not an exhaustive global priority guarantee.
