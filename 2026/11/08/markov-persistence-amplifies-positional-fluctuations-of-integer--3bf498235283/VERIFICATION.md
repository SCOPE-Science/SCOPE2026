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

The standalone `checks/verify.py` uses the Python standard library only. Execute `python3 checks/verify.py` in the directory containing the package files. The run returned `PASS: 159 exact rational finite checks`.

The finite checks integrate the linear observable against a deterministic integer multiplication map by exact branch decomposition (multipliers 2 through 69), compare short two-state Markov environment path enumeration with matrix-power covariances (six parameter triples, seven lags each), verify the derivative numerator identity, verify the independent and frozen endpoints, test explicit slope pair (2,3), and compare finite-block variance to its Green–Kubo limit.

The proof in `RESULT.md` separately establishes stationarity, mixing, the exact covariance and determinant identities, and the annealed functional central limit theorem by bounded reversed martingale approximation. Finite calculations cannot prove these infinite-dimensional or limit claims. The functional limit is not a quenched statement. At perfect persistence the environment is nonergodic and the limiting one-time distribution is a non-Gaussian two-normal mixture for distinct slopes. No independent audit has been performed.
