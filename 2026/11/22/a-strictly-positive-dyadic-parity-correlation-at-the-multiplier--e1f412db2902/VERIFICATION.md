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

# Verification details

Run `python3 verify_correlation.py` with Python 3.8 or later. No third-party libraries, external data, networks, or files are required. The program reconstructs the seven-state transition matrix from the exact digit/carry operation, independently computes the signs of the terminal carry, and checks the exact seven-component identity
\[
(M^4-M-2I)v=(0,0,4,0,-4,0,0)^{\mathsf T}.
\]
It then checks the invariant row coordinates and the claimed recurrence through 41 levels, and independently enumerates the complete summand range for every \(0\leq L\leq15\).

Expected opening output: `PASS: carry transitions, tail, exact matrix-vector identity` followed by two further `PASS` lines. The recurrence is proved for all \(L\) by the explicit invariant in `RESULT.md`; no finite bound is being promoted to a universal computational proof. The checks do not establish publication priority or independent scientific validation.
