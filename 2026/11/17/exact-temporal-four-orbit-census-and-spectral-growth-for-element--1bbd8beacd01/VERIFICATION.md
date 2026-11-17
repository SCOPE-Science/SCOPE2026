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

The exact transfer certificate `transfer_certificate.py` uses only Python 3 standard library modules and reconstructs all relevant cyclic components for temporal periods dividing one through four. It computes the ten-state characteristic polynomial with integer Faddeev–LeVerrier operations, checks its traces and their recurrence, and verifies the shared-root positive-walk lengths needed for the existence statement. The recorded output `transfer_output.txt` ends with an explicit `PASS` line.

The independent program `direct_enumeration.cpp` uses C++17 and checks every labelled binary cyclic word for every circumference from three through twenty, directly applying the Rule 54 bit update up to four times. The recorded output `direct_output.txt` ends with `PASS`. This independently confirms the displayed trace counts for that finite interval and checks the low-period special cases.

For all ring lengths beyond twenty, correctness rests on the finite-space-time bijection, exact strongly connected component lists, Cayley–Hamilton recurrence, and primitive nonnegative-matrix spectral argument in `RESULT.md`; finite testing is not offered as an infinite proof. No unrelated graph dynamics, asynchronous Rule 54 convention, or longer temporal periods are covered.
