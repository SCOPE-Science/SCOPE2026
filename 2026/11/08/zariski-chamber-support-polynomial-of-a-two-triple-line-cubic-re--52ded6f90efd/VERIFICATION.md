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

The file `verify_chambers.py` uses only the Python standard library. Run `python3 verify_chambers.py` in the same directory; the output should match `verification_output.txt` and conclude with `ALL_CHECKS_PASSED`.

The program constructs the full \(17\times17\) negative-curve intersection matrix directly from the Picard classes, checks the distinguished diagonal and zero-intersection entries, and iterates over all \(131072\) possible subsets. Pairwise intersecting \((-1)\)-curves are excluded because their \(2\times2\) principal submatrix is not negative definite. Every surviving submatrix is tested using exact fractions in a Schur-complement elimination. A separate combinatorial binomial evaluation produces the same seven support counts. The observed counts are \((1,17,100,281,401,255,37)\), summing to \(1092\).

The proof that the listed \(17\) curves are all the negative irreducible curves is geometric (Bezout plus adjunction), not a consequence of the finite enumeration. The cited chamber-count correspondence then turns the enumeration into the stated infinite-geometric conclusion. No independent external audit or peer review has been performed.
