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

# Verification

Run `python verify_critical_dispersal.py` with Python 3, SymPy and mpmath from the extracted package. This uses symbolic algebra for the polynomial identity \(f_r^2(1/2+u)-1/2=-\Delta+u^2(C-r^3u^2)\), exact factorization of the second iterate, the critical contacts and derivative, the uniform coefficient bounds, and exact-rational individual iterates. Seven arbitrary-precision parameter probes check the expected trend but are expressly **not** the proof of infinitely many real parameter cases.

The main proof proves for all \(r\in(r_*,13/4]\): \(0<\Delta\le5/1024\), \(6\le C-r^3u^2\le7\) for \(0\le u\le1/10\), strictly positive odd iterates prior to even exit, and finite first crossing. It compares positive returns to two exact doubly-exponentially shrinking sequences, giving \(K=\log_2\log(1/\Delta)+O(1)\) and the first exit index \(\tau=2K\). Critical dynamics and precritical attraction follow from the explicit factorization and increasing second iterate.

No independent mathematical audit has been performed. The uninspected full 1993 sectional-discontinuity paper and possible unindexed equivalences remain scientific-priority limitations.
