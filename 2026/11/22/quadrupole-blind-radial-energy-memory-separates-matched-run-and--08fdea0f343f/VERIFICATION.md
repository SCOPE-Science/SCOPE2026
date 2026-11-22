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

# Verification scope
The analytic proof in RESULT.md identifies the bounded stationary convolution and closes five exact generator moment equations. In particular, it does not infer all-time covariance from finitely many measured lags: the full time dependence follows from solving a two-equation backward-generator system. The result holds for every positive physical rate in the two named models and for angular Markov processes meeting the stated eigenfunction hypotheses.

Run `python check.py` with Python 3, NumPy and SymPy installed. The code independently checks the defining exact generator balance identities and the covariance ODE, evaluates positive rational test parameters, and simulates 11,500 independent three-dimensional particle paths under each of two orientation dynamics. The completed run reported 38 assertions passed; its fixed-seed numerical output is included below.

RTP: mean 0.498169, squared-radius variance 0.067504, normalized covariance at 0.96 approximately 0.424642.
ABP: mean 0.501599, squared-radius variance 0.024448, normalized covariance at 0.96 approximately 0.438807.
The exact corresponding means, variances and normalized covariance are 0.5, 0.0694444 / 0.025 and approximately 0.428092. The simulator's finite-time step and finite sample size limit its precision; it supports, but cannot establish, an infinite-time or all-rate theorem.

The publication-priority assessment was confined to searched accessible sources; independent scientific review and exhaustive literature priority verification are not claimed. No numerical test substitutes for the stationary-generator proof.
