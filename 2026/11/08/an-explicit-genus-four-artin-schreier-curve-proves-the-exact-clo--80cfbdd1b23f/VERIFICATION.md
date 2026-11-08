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

# Reproducible mathematical checks

Run `python3 verify_fields.py` and `python3 verify_closed_points.py` with Python 3; no third-party packages are required.

The direct finite-field script constructs fields of sizes 4, 16, and 64 from irreducible binary polynomials, checks \(\omega^2+\omega+1=0\), enumerates the Artin–Schreier solutions, and verifies \((N_1,N_2,N_3)=(1,9,1)\). Every \(x\in\mathbb F_{64}\) is checked to satisfy \(x^9\in\mathbb F_8\) and absolute trace zero. Successful execution ends with `TRACE_VERIFICATION_OK`.

The independent arithmetic script calculates the zeta numerator \(P(T)=(1-2T)^4(1+2T+4T^2)^2\), derives \((N_1,N_2,N_3,N_4)=(1,9,1,225)\) and \((B_1,B_2,B_3,B_4)=(1,4,0,54)\), and checks the strict lower-bound inequality for a finite sample of \(r\). Successful execution ends with `WEIL_CLOSED_POINT_VERIFICATION_OK`.

These executions are finite certificates of the displayed arithmetic computations, not proofs of existence for arbitrarily large degrees. The universal part is independently established in the theorem through the Weil bounds and an explicit induction valid for all integers \(r\ge4\). No independent mathematical audit has been performed.
