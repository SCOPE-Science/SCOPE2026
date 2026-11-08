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

# Reproducibility and verification

Run `python verify_exact.py` and `python verify_limit.py` from a directory containing both scripts. The latter requires SymPy and SciPy. Tested versions: Python 3.13.5, SymPy 1.14.0, SciPy 1.17.0.

`verify_exact.py` derives terminal laws from the integer-part-size recurrence in exact fractions. It independently constructs the labeled graph's edges and recursively explores their weighted choices. It compares the full distributions across the permitted small configurations at relative weights \(1/2,1,3/2,2,3\), and confirms that terminal configurations have at most one nonempty part.

`verify_limit.py` differentiates the candidate first integrals symbolically along the two-dimensional ODE, checks numerical deterministic solutions for nine parameter triples, and runs reproducible finite-state simulations in six regimes. Simulation checks use a deliberately coarse absolute tolerance \(0.035\); they are consistency tests only.

The actual replay output is in `CHECK_OUTPUT.txt`. The proof of the asymptotic theorem is analytical: an exponential-clock representation, martingale fluid limit, explicit integrals, and terminal pathwise sandwich. Neither small-state enumeration nor simulation alone proves that theorem.

The tested model assumes all available cross-part edges, weights \(1,1,\rho\), initial sizes \(\lfloor aN\rfloor,\lfloor bN\rfloor,\lfloor bN\rfloor\), and \(a,b,\rho>0\). These verifiers do not establish rates of convergence, critical-window fluctuation laws, or any claim about spatially diffusion-limited annihilation.
