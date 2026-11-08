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

Run `python verify.py` using a standard Python 3 interpreter. It uses no external libraries.

Checks completed successfully: 196 exact-rational comparisons between the first-threshold clock recursion and its independent exponential-density integral expansion for all camp sizes from 1 through 7 and four rational rate pairs; 49 comparisons against the combinatorial first-arrival permutation expression; tested exact mixed-parity inequalities and odd–odd equalities; 72 completely separate, labeled-vertex Markov checks on all camp sizes from 1 through 4 for three rate pairs; exact worked examples for \((m,n)=(2,4),(2,3),(3,2)\).

The labeled-vertex verifier explicitly updates each vertex to the other camp's strict majority, retaining opinion on a tie, and uses a separate state cache. It does not import the closed-form code. It checks all sample calculations from the packaged source script itself.

The general theorem is proved in `RESULT.md`; finite enumeration is not treated as exhaustive over arbitrarily large populations or continuous rate values. Exact rate calculations apply only to positive rate parameters; the limits as their ratio tends to zero or infinity follow from the proof's order-statistic comparison. No outside audit or publication is implied.
