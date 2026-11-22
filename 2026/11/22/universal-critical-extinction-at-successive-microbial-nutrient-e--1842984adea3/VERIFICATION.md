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

# Verification of exact critical extinction law

The proof is self-contained in `RESULT.md`, including its exact entropy dissipation identity, positivity assumptions, coercive level-set argument, characterization of the invariant zero-dissipation set, simple marginal eigenvector, stable complementary spectrum, and nonzero quadratic center coefficient.

The independently executable `check.py` performs exact SymPy simplification of the transfer identity and center coefficient, rational equilibrium checks for five exchange rates, and SciPy integrations on both critical boundaries and three noncritical regimes. Its prescribed parameter family has \(\beta_3=2/3\), \(\beta_2=3\), and the exact critical biomass amplitudes \(7/81\) and \(3/7\). The script passed all assertions when executed from the package. The finite-time integrations do not prove convergence at infinity: equations (7)–(11) and the cited invariant-manifold argument supply that step.

Only self-review has been performed. Historical-priority comparisons remain bounded by accessible full text and abstracts, and an independent scientific audit has not been performed.
