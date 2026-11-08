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

Run `python3 verify.py` in the same directory as the embedded sources. The script independently computes \(\binom n3\) using exact integer arithmetic over the full proposed periods for levels \(1\le k\le13\) and checks each fiber, including the special base case. It verifies the least period by a specific counterexample to a half-period, checks the four chart identities and their finite-level isometry property, and checks that lower-index columns one and two are uniformly distributed.

For unrestricted exponents, the proof requires no computational certificate. The decisive nonstandard step is the odd divided-difference quotient for each \(g_r\), which establishes bijectivity on every \(\mathbb Z/2^m\mathbb Z\). Exact experimentation up to a finite level is not used to infer an infinite assertion. The result has not undergone independent audit.
