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
# Verification of the exact reset-neutral time optimizer

The proof covers all integer \(a\ge4\), \(0<p<1\), \(0<\gamma<1\) without relying on sampling. The core steps are exact solutions of the killed-walk recurrence, a coefficient-matching necessity argument over a continuum of reset rates, symmetric averaging and a strictly increasing hyperbolic quotient, and a standard renewal expression that counts each reset event as one time step. The neutral splitting constraints are imposed for every reset probability, not one chosen rate.

`checker.py` can be executed with Python 3 and the SymPy and NumPy packages. It computes transient Markov inverses in exact rational arithmetic for finite domains, explicitly checks absorption on either endpoint after resetting, validates mean times for each starting site and candidate paired policy, and compares the closed formula with double-precision linear solves. A successfully replayed package reports `PASS 3666 independent exact and numerical assertions`.

Finite checks do not establish the universal theorem on their own. No independent external mathematical review has been conducted. Scientific caveats: reset-independent policy and unit-time reset event counting, no reset movement cost, and fixed positive \(\gamma\).
