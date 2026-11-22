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

Run \(\texttt{python3 verify.py}\) (Python standard library only) to check the exactly rational witness and numerical algebraic identities for the model. The polynomial witness evaluates to opposite signs at each of the pairs \((1/10,1/2)\), \((1,2)\), \((2,4)\), producing three positive-age crossings. These bracket assertions are exact rational arithmetic.

The proof of the universal limit and the rate threshold is analytic: factor the derivative of \(\log R\), maximize its positive rational component at \(x=\sqrt{ab}\), and check the three monotone intervals. Random finite tests support implementation consistency, not completeness or historical novelty.

No external replication or independent scientific validation is asserted. The inferred ecological mechanism applies only to the idealized logistic provenance and constant exponential preservation assumptions.
