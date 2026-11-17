---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the fixed right-acting row-Markov reverse chronological pulse convention, the two-term Magnus logarithm is hΣG_i+(h²/2)Σ[G_{i+1},G_i]. Its 4x4 upper-triangular matrix has diag (−h,−h,−h,0), first superdiagonal h+h²/2,h+h²/2,h and second superdiagonal −h²/2 twice. The first three exponential columns follow from a nilpotent 3x3 block and row conservation fixes the fourth column. The sole possibly negative entry is P14=1−e^(−h)(1+h+h²/2+h³/2+h⁴/8), whose derivative is e^(−h)h²(h²−8)/8: decreases below sqrt8, increases above, has exactly one positive zero ~5.2022837279. For arbitrary positive rates and n>=4, direct order-h³ coefficient of exp(hA+h²B) at (1,4) is −a1a2a3/3. Independently checked the commutator signs, matrix formula, derivative and cubic coefficient in exact SymPy. n=2,3 positivity follows explicit entries. This proves only endpoint positivity of Magnus exponential, not approximation accuracy.

## originality

PASS

The Markov Magnus literature already establishes that commutators need not preserve positivity; that qualitative phenomenon is credited as prior. The precise four-state iff recovery threshold, complete single-negative-entry classification, least equal-rate reverse-cascade dimension and universal weighted cubic coefficient are a narrower concrete classification. Resultary returned other Padé/RK4/Radau/Stiff integrator positivity horizons, each a different one-step map, and no prior same Magnus two-term reverse-pulse formula. Best of knowledge PASS subject to inaccessible full primary article text.

## value

PASS

Nonnegativity of numerical Markov propagators is essential and not guaranteed by mass conservation. The four-state reverse-cascade is a natural smallest exact counterexample, and the unexpected reentrant interval identifies precisely where a fixed two-term Magnus exponential regains the Markov property despite gross inaccuracy in the true transition. It supplies a concrete analysis tool for positivity-preserving methods and shows why small step does not guarantee positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
