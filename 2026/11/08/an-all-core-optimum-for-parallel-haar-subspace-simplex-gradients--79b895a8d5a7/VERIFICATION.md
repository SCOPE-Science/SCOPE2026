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

# Verification of the claimed mathematical result

The exact expected-decrease formula is stated in Theorem 4.2 of the cited primary paper, and its Section 4.2 states the two-stage parallel cost. The new proof uses the analytic Gamma recurrence and a strict digamma integral bound, rather than assuming numerical scans are exhaustive.

Reproducible supplementary command from this file's directory:

```sh
python3 verify_parallel_haar.py
```

Observed result: `PASS; supplementary comparisons: 460267`.

The checker uses only the Python standard library. It compares all ambient dimensions 2 through 119 against all core counts 1 through 64, checks the theoretical two-core tie, and checks many Gamma recurrence and batch inequalities. These finite tests verify implementation consistency, but do not prove the infinite family. The paper-specific source comparison covers the 2023 full preprint; publisher final full text was not accessible, and no independent audit has occurred.
