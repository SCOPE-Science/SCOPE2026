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

# Reproducibility and verified bounds

The accompanying `checks/verify_relaxation.py` uses exact symbolic algebra for the energy Lie derivative, SciPy beta values for the two quartic-orbit integrals, and high-accuracy numerical one-turn returns for \(\varepsilon\in\{1/4,1\}\) at energies \(10^{-4},10^{-6},10^{-8},10^{-10}\). It verifies that both the normalized period defect and leading-order energy-loss discrepancy shrink along each test sequence. The rerun output from that script is:

```
VERIFY_OK symbolic_energy_identity=1 small_energy_return_cases=8
BETA_INTEGRALS I0=1.31102877715 I6=0.359442070421
LIMIT_COEFFICIENTS_EPS_QUARTER energy=13.3035220819 count=0.728365620395
MAX_LAST_SCALE_RELATIVE_ERRORS period=0.00454997 loss=0.02231037
FINITE_CHECK_ONLY: asymptotic conclusions require the analytical return-map proof.
```

The infinite-time limits, all-initial-condition quantifier, and uniqueness of the next section crossing near the quartic oval are analytical arguments in `RESULT.md`, not consequences of numerical testing. The procedure requires Python 3, SymPy and SciPy; no external data files or precomputed certificates are needed.
