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

Execute `python3 verify.py` with Python 3 and the standard library. It calculates the integer-coefficient exponential generating functions and their \(q\)-refined versions from the four formal-series equations; all output coefficients are exact integers.

It independently enumerates trees using Prüfer sequences, so every labelled tree and every orientation is covered through order seven. At orders at most six it additionally checks all Boolean valuations directly against the semantics of \(\Delta p\to\Delta\Delta p\). For order seven it checks only the independently reconstructed adjacency criterion, not all valuations. A separate exact bivariate computation agrees with the direct branching-count distribution through order seven. The expected output ends with `VERIFY_OK` and `BIVARIATE_VERIFY_OK`.

The first totals are \(1,2,12,128,1940,38292,937048,27442816,937015920\) through order nine. No experimental bound is extrapolated into an all-order assertion: the all-order claim is established by the proof in `RESULT.md`.

Historical priority has not been independently established. No proof assistant or external certification is claimed.
