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

# Reproduction and limits

Run `python3 verify.py` from a directory containing the supplied `verify.py`. It requires the Python standard library only.

The checker compares the closed all-field weak and strict count formulas against independently enumerated part magnetizations for each integer \(1\le n\le17\), at all half-integer field values in a symmetric interval containing the critical fields. It separately enumerates all labeled spins for sizes \(1\le n\le4\) across those half-integer grids and for \(n=5\) at eight fields, checking each one-spin energy change and, for every nonground weak minimum, a zero-cost then downhill two-flip sequence.

Observed replay result: `PASS: 2902 independent group and full-spin assertions; n<=17 group, n<=5 brute.`

The infinite all-field classification follows from the analytical magnetization-case proof in `RESULT.md`, not from finite checks. The checker does not establish novelty, physically realizable kinetic trapping, a positive-temperature phase transition, or independent validation.
