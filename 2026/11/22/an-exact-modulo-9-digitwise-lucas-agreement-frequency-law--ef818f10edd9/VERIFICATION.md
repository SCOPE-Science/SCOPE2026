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

# Verification record

The accompanying `verify.py` is standalone Python 3 with no external dependencies. It reconstructs the eighteen-state exact digit transfer, computes \(W_L\), checks the twenty recurrence residuals (all zero), and checks the specified initial data. The Cayley–Hamilton proof uses the explicit nineteen-dimensional block matrix, making nineteen consecutive exact residual checks sufficient for every remaining index.

An independent Pascal-triangle calculation modulo \(9\) compares the binomial entries, the digitwise product, and the two claimed counts for every triangular position for \(L=1,2,3,4,5,6\). There are \(299{,}481\) tested positions, and all agree. This finite test is a separate check; the proof of all lengths uses the preceding transfer and finite algebraic certificate, not experimental extrapolation.

No independent audit has been performed. No claim is made about modulus \(27\), arbitrary prime powers, or an independently validated bibliographic priority.
