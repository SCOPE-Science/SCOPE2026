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

# Reproduction

Run `python verify.py` with SymPy and mpmath. The included `verification_output.txt` records a successful invocation with high-precision root and risk values. The script independently evaluates conditional-variance and conditional-mean Poisson series at seven points, checks rates \(0.25\), \(1\) and \(7\), and verifies the binary comparator. It also symbolically checks the derivative identities controlling the proof.

The all-time uniqueness theorem is mathematical, using \(g''(z)<0\) and boundary signs, not dependent on finite numerics. Numerical output and root decimal expansions are supporting evidence, not certificates of exhaustive literature coverage or independent auditing. The rate is assumed known and constant, the query exact and nonadaptive, and the arrival target untruncated.
