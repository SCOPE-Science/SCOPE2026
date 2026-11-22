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

# Verification of geometric support and marked bridge law

The included `CHECK.py` was executed under Python 3 with installed NumPy and SciPy. It prints `GAUSSIAN_BRIDGE_POLYTOPE_PASS` after checking 546 direct tree-enumeration support evaluations, the integrated order-statistic density normalization, and finite-dimensional Gumbel/exponential scaling diagnostics. The exact \(q\)-dimensional support identity and joint density are proved algebraically. The limiting joint law and width expansion are derived analytically using Gaussian tail asymptotics, conditional truncation, a triangular-array central limit theorem and uniform integrability. No finite computation verifies an infinite limit.

To rerun: `python3 CHECK.py` in the extracted directory. Independent audit and historical priority certification have not been performed.
