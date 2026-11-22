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

# Verification and boundaries

Run `python3 verify_cayley.py` in the same directory as this file. The program uses only the Python standard library and prints distinct `PASS` markers for Prüfer-enumeration/Walsh-transform checks at \(n=3,4,5,6\) and exhaustive signed-cofactor frequency-boundary checks at \(n=4,6,8\). The latter include all frequencies through the first zero degree and explicit negative star witnesses.

Exact outputs observed from the packaged program: no Walsh zero at odd orders \(3,5\); the counts at the first even-order zero degree are \(6,60,280\) for orders \(4,6,8\); the exhibited first negative star coefficients are \(-4,-192,-27648\), respectively. The program also compares independent arithmetic realizations of the same coefficients.

The infinite-order theorem is proved by the signed matrix-tree eigenvalue identity, the sharp \(k+1\) Laplacian bound with its equality case, and parity; no finite enumeration is offered as an all-order certificate. No independent mathematical audit or validation has been performed.
