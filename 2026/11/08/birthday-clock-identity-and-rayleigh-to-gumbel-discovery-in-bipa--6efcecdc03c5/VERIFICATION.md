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

# Finite verification and limits

Run `python3 verify.py` with the unmodified standard library. In the verified execution it printed `VERIFY_OK 1516 exact assertions`. The checker derives a direct rational transition kernel between successive newly occupied vertices, computes its class-completion CDF by dynamic programming, and separately computes the inclusion-exclusion product expression. It compares every case with \(2\le a\le8\), \(1\le b\le16\), and \(0\le j\le b\), tests monotonicity and endpoints, checks the union-bound envelope, and verifies the geometric failure moment formulas. These tests are finite and are not an exhaustive proof of the theorem for arbitrary parameters.

The complete general proof is in `RESULT.md`. The exponential-clock and Poisson approximations rely on an independent geometric-block representation; the growing-class limit also invokes the classical coupon-collector Gumbel theorem. Neither an independent audit nor automated formal proof is claimed.
