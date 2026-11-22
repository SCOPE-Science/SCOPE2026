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

# Reproducibility and verification

Run `python3 verify.py` and `python3 alternate_verify.py` with `clique_cover.json` and `optima.json` in the same directory. Neither program requires nonstandard Python packages. The first verifies all \(28\) conflict cliques, the integer-weight cover and the \(98/16\) upper certificate; it also enumerates optimal ternary codebooks for lengths two through five, checks their exact counts, and reconstructs all seven length-five symmetry classes. The second constructs compatibility via longest-common-subsequence dynamic programming and independently counts the \(12\) optimal normal-form codebooks.

Expected output includes `VERIFY_OK` and `ALTERNATE_OK`. The programs were executed from the actual packaged file directory with both outcomes. The upper-bound certificate is an exact finite proof; the code enumerates all cases within the stated alphabet and lengths, not an extrapolation from samples. The census is bounded to the stated finite domain. Independent external audit has not been performed.
