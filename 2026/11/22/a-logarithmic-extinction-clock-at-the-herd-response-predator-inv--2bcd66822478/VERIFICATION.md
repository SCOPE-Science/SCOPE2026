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

# Verification of the mathematical claim

The proof defines the map and the forward-invariant wedge, proves all its positive orbits tend to the boundary equilibrium, derives a slaving remainder of order \(O(y_n^3)\), and converts a cubic scalar recurrence into a summable error in reciprocal extinction time. The derivation proves a finite orbit-dependent limit; it does not infer an infinite-time result from simulations.

Running `python check.py` with SymPy installed returned `exact symbolic checks: PASS` and `finite trajectory diagnostics: PASS`. Exact coefficients checked were the quadratic slaving coefficient \(a^2(d+1)/2\), the cubic scalar term \(-a^2d(d+3)/8\), and the logarithmic time-shift coefficient \(3a(d+1)/4\). Numerical examples \((a,d)=(1,2)\) and \((0.7,0.9)\), both within the small positive wedge, showed convergence of the corrected reciprocal clock and of the scaled prey-deficit coefficient. All finite computations are illustrative checks only.

A full mathematical manuscript and checker are embedded together in the research record. No independently performed audit or formal proof certification is claimed. The result applies only for the stated neutral parameter and local positive-data wedge.
