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

Run `python3 checker.py` using the Python standard library. The program enumerates precisely \(16\times81=1296\) combinations of fixed ex ante tie-breaking vectors and four-agent weak-order profiles. It separately enumerates the two possible complete matching assignments, checks stability, checks worker-optimality among strictly stable matchings, and tests two-sided Pareto dominance under the **unrefined** preferences. It verifies the full \((1,2),(2,3),(3,4)\) failure coefficient table and its \(10,4,2\) multiplicities, plus the pointwise optimality and independent-policy expectation at six rational parameter values.

The exhaustive finite enumeration is the proof of the coefficient table; weighting it by \(t^k((1-t)/2)^{4-k}\) is an exact symbolic derivation for every real \(t\in[0,1]\). The parameter substitutions are additional arithmetic checks, not a claim of exhaustive testing over the continuum. The proof also establishes independently why profiles with zero, one, or four ties cannot cause this Pareto failure.

No independent review or external validation is asserted. Uninspected or unindexed equivalent literature may affect novelty; results do not extend beyond the stated model without further proof.
