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

The theorem is proved in `RESULT.md`. For a finite check run `python3 checks/verify.py` and `python3 checks/verify_orbits.py` using only the Python standard library, and compare with `checks/expected_output.txt`. The first script tests all \(2^{14}\) generator-image assignments for \(m=2\) over \(\mathbb F_2\), including assignments with constant terms. It checks the full Leibniz law and idempotence; it also computes projection fibers by independent finite-field linear algebra over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\). The second script explicitly constructs every automorphism of the \(m=2\) algebra over \(\mathbb F_2\) and tests conjugacy orbit sizes. Larger dimensions and arbitrary characteristics are proved algebraically; these finite computations do not establish completeness for all \(m\). No independent human mathematical audit has been performed.
