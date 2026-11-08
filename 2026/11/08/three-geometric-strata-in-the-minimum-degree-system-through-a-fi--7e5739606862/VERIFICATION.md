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

Run `python verify.py` with Python 3 and no third-party dependencies. The script uses exact arithmetic in finite fields with 8 and 27 elements, built as cubic quotients of \(\mathbb F_2\) and \(\mathbb F_3\). It checks all projective parameter points in each field and calculates the rank-stratum census. For one representative from each of the three ranks, it counts all curve points in the projective plane, finds all gradient-critical projective points, and tests *every* projective line for being a component; expected factors are exactly the rational lines containing the coefficient point.

The output saved as `verify_output.txt` gives 7, 42, 24 parameter points of ranks 1, 2, 3 over \(\mathbb F_8\) and 13, 312, 432 over \(\mathbb F_{27}\). The corresponding three representative curve-point counts are 25, 17, 9 and 109, 55, 28. Every check passes and the final line is `ALL_CHECKS_PASSED`.

These are exact finite checks, not proof of the theorem for arbitrary prime powers or coefficient extensions. The geometric proof in `RESULT.md` provides the general argument; the script does not certify historical originality. Independent scientific validation has not been performed.
