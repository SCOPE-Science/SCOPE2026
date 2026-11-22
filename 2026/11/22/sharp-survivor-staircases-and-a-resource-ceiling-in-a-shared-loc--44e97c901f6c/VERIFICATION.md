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

# Reproduction and verification

Run `python3 checker.py` with Python 3. No nonstandard Python packages, downloaded data, or external service is required.

The exact rational test verifies a three-species stationary state with \(q=(1,6/5,7/5)\), \(\theta=1/2\), \(\beta=\gamma=\alpha_i=1\), global concentration \(R=3/2\), input \(R_0=979/130\), populations \((4,4/3,4/13)\), and local nutrients \((1/2,9/10,13/10)\). All equations are checked as exact zero identities. It also checks the exact entry supplies \(C_2=11/5\), \(C_3=377/75\), the contrasting incomplete-isolation threshold \(C_2=46/5\) at \(\theta=1/4\), and the inability of species 3 to cross the ceiling at that isolation level.

The same checker evaluates exact closure and stationarity identities and the positive principal determinants of the transfer blocks for 800 additional independently generated exact rational configurations, with two through seven consumers. It checks that the scalar closure derivative is positive and that finite entry supplies are strictly ordered.

These are finite algebraic reproductions. The infinite parameter and arbitrary finite-species conclusions derive from the analytic proof in `RESULT.md`, especially the mass balance, scalar monotonicity and dissipative linearization. No exhaustive computational enumeration or external mathematical certification is claimed. Threshold equalities, global attraction, adaptive separation, extra nutrient types, demographic stochasticity and priority beyond the examined sources remain outside verification.
