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

## Checks actually performed

The proof derives the closed, all-size complex two-point recurrence from the generator, including the exceptional neighbouring-site boundary cases, and uniquely solves it with the two exact ring boundaries. The limit follows analytically from the arcosh expansion and the winding residue of the cycle.

The separate `verify.py` builds a sparse transition-rate generator for each complete finite configuration space, solves its stationary distribution, then recomputes correlations directly. It compares all distances for ring/colour sizes \((3,3),(4,3),(5,3),(4,4),(5,4)\) at refresh rate \(1/2\), and checks the small-refresh scaling for multiple winding residues. The standalone program needs Python 3, NumPy and SciPy. A numerical tolerance applies only to these independent finite comparisons; the analytic theorem does not use floating-point proof.

## Boundaries

Positive refresh gives irreducibility; at zero refresh the theorem only asserts the specified limiting correlation profile. Two-point functions do not determine the full stationary law. Historical priority is reviewed only against identified literature, not independently certified.
