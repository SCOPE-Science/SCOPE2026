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

# Verification of the mathematical claim

The companion `verify.py` uses only the Python standard library. From any directory containing the file, run `python3 verify.py`. Its own graph construction builds one shared central vertex with separate vertex-disjoint cycles. An independent edge-include/edge-exclude recursion computes matching-polynomial coefficients, without using the analytic cut-vertex product formula. For all 126 combinations of one through four cycles of lengths three through nine whose total cycle-edge count is at most nineteen, every coefficient agrees with the analytic formula. All those cases also satisfy the exact root order and signed first surviving coefficient. Another 336 equal-length cases test up to twelve cycles and lengths through thirty symbolically.

Successful execution prints `FULL_POLYNOMIAL_DIRECT_MATCHING_CHECK_OK 126 mixed-cycle bouquets`, `ALL_EQUAL_LENGTH_FAMILIES_OK 336`, and `VERIFY_OK`. These finite calculations cannot certify the general all-parameter theorem. Its noncancellation argument follows from the path generating function and a strictly positive reciprocal sum, as reconstructed in `RESULT.md`.

Independent mathematical audit has not been performed.
