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

The included `verify_hopf.py` is executable with Python 3 and SymPy and checks the exact payoff reduction, equilibrium, characteristic polynomial, transversal eigenvalue crossing, normalized eigenvectors, derivative tensors and first Lyapunov coefficient. Its successful execution is an internal symbolic reproducibility check only; the analytic Hopf theorem supplies the passage from the checked local jet to small attracting periodic orbits. The calculation does not establish global uniqueness of cycles, their basins, or historical priority. Independent audit has not been performed.
