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

# Verification scope

Run `python verify.py` with Python 3.9 or newer; only the standard library is used. The exact-rational verifier examines every two-coordinate support state and each of the \(2m\) equally weighted midpoint noise cells for \(1\le m\le11\). For \(1\le m\le6\), it also checks every transition of each distinct three-coordinate parity-class configuration, verifying the proposed invariant law and averaged-coordinate variance.

Executed command: `python verify.py`

Observed outcome: `PASS 11056 exact-rational assertions; pair M=1..11 and three-coordinate M=1..6`

These are finite checks only. The proof in `RESULT.md` supplies the all-dimension statements, the exact geometric holding-time decomposition and the invariant-law detailed-balance arguments. No computer enumeration establishes all parameter values. Ordinary-time convergence to stationarity is specifically not claimed because the chain has period two. Historical originality has not undergone independent confirmation.
