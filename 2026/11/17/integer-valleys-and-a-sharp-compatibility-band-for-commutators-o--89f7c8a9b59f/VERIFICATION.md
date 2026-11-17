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

Analytical verification: trace/Frobenius and commutator singular-value formulas were reconstructed directly from real two-by-two orthogonal projection blocks. The sublevel constraint is exactly a union of two scalar intervals. The rank-count lower bound, upper feasible-coordinate bound, equality saturation, continuous image argument and unique crossover are all proved in `RESULT.md`.

Reproducible computation: execute `python check_projection_envelopes.py` from this package. The script checks 110,065 scalar constructions, random samples and cell-peak cases plus 1,800 direct finite matrix identities and norm inequalities when NumPy is installed. Both test groups passed in the preparation environment. Calculations sample parameter values; analytic proof is required for the universal theorem.

Scope: real or complex finite-dimensional Hilbert space with dimension at least twice the common rank. No external validation or independent audit was performed. Prior-literature coverage remains limited by inaccessible full text and possible older equivalent formulations.
