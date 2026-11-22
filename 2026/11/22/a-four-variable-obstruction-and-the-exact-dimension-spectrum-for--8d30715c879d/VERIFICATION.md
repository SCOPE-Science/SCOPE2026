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

Run `python3 verify.py` using standard-library Python 3. No third-party dependencies or external data files are required.

The program enumerates all 15 nonzero cubic coefficient vectors and all 64 quadratic coefficient vectors on four Boolean coordinates, for 960 distinct nonlinear polynomials. Every linear summand leaves the second polar unchanged and therefore does not need separate enumeration. For every case it explicitly forms all 16 rows and checks the 210 ordered pairs of distinct nonzero vectors. No case satisfies ordered separation.

It additionally checks all eight canonical nested-row witnesses (both possible strict inclusion patterns), then checks separating examples in dimensions 3, 5, 6, 7, and 8, and verifies that a dimension-four quadratic with nondegenerate second polar *does* separate. The expected actual output, reproduced from the packaged file, is:

```text
VERIFY_OK 960 [3, 5, 6, 7, 8] WITNESS_OK
```

The finite test is a cross-check, not a proof of the all-dimensional existence direction. That direction uses the structural proof and the cited published direct-sum theorem. The proof of nonexistence in dimension four is fully analytical and requires no executable artifact.
