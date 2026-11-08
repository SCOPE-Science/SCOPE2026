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

# Reproducibility and limits

Run `python verify.py` using the Python standard library. It should print `VERIFY_OK 367 exact/reproducible assertions` and exit successfully.

The verifier derives the exact distribution from factorial moments; independently enumerates all \((2n-1)!!\) perfect matchings for \(2\le n\le6\); checks the cyclic matching formula and rational moment identities; and checks normalization, nonnegativity, exact first two moments, and recurrence identities through \(n=40\). Additional numerical comparisons at \(n=40,80,120\) test the proposed scaling without claiming infinite verification.

The critical proof dependencies are the exact cycle-matching count, the uniform moment remainder and Cauchy's coefficient inequality. The first is checked exactly on finite cases and proved algebraically in `RESULT.md`; the second and third require the written analytic proof and cannot be certified by the executable tests alone. Scientific historical priority and independent external validation remain unverified.
