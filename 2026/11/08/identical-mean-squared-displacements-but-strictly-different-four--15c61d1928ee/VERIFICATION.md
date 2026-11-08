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

# Verification and reproducibility

The continuum proof is written in `RESULT.md`. `check.py` independently constructs the Gaussian four-point law from all three Wick pairings and the telegraph four-point law from disjoint Poisson increments. The pairings are reduced to the proposed connected-kernel identities at 40 positive random parameter sets. A second one-dimensional quadrature reconstructs both fourth cumulants and their positive difference and checks their limits. A separate Nyström discretization verifies the Gaussian conditional quadratic-form identity \(\kappa_4=6\operatorname{tr}[(C_UC_Y)^2]\) in three parameter regimes. In total the executable checker reports **193 passed diagnostics**. The calculations use Python, NumPy and SciPy with version constraints in `requirements.txt`.

Run with `python check.py` in the extracted file directory after installing `requirements.txt`. The script should print `PASS checks 193 ; algebra/Wick, positivity, rates, Nyström, short-time` and return zero. The random generator uses a fixed seed. Finite-grid checks cannot prove the statements for all time or parameters; these follow from the ordered four-time cumulant identity, its positive integrals, dominated convergence and the operator Gaussian-integrability argument.

The derivation does not assume or verify a repulsive-interaction extension, a thermodynamic many-particle limit, a statistical sampling theorem, or priority over every inaccessible publication. No independent audit was performed.
