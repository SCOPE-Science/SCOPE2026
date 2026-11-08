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

The proof in RESULT.md treats all positive factor lengths and all positive zero-run parameters; the finite script is a cross-check, not an infinite certificate.

Run `python3 verify_triangle.py` with standard Python 3. It independently constructs a finite prefix longer than the proven cutoff, enumerates every distinct factor and every minimal absent factor at lengths 1 through 26, and compares with the two closed forms. It checks that the length-\(N(N+3)/2\) prefix contains all length-\(N\) factors and that the preceding prefix does not, for every \(N\) from 1 through 26. It also compares finite-prefix and infinite-model minimal absent factors at every shorter length.

Expected output begins `CHECK_OK exact_maw_lengths=1..26`. The script checks 1,755 distinct factor instances and 24 minimal absent words in its tested range. The proof covers the untested infinite tail.
