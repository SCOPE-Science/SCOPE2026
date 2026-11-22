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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.9 or later. The script uses only the Python standard library. It enumerates all acyclic edge subsets for six generalized theta graphs, computes unnormalized Walsh transforms exactly, checks every coefficient against formula (2), checks the modulo-four congruence (4), and verifies predicted nullities for the five- and nine-arm examples. On completion it prints `PASS: 284032 individual exact Fourier comparisons and congruence checks`.

The largest test has 18 edges, giving 262144 Fourier frequencies. The tested integer computations contain no tolerances or randomized steps. The general theorem is proved by the path decomposition and congruence argument in RESULT.md; the finite tests cannot establish the infinite claim by themselves. No independent audit is represented or performed.
