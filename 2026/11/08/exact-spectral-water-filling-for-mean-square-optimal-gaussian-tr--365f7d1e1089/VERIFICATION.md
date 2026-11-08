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

# Reproducibility and limits

For a real symmetric positive semidefinite matrix, eigenvalues sorted in descending order, integers \(1\le r<n\) and \(m\ge1\), the complete proof and exact target risk are in `RESULT.md`. The test script `check.py` uses Python 3, NumPy and SciPy. Execute `python3 check.py` from the extracted package directory.

The script evaluates the clipped scalar equation over 5,040 synthetic spectra/ranks/probe counts, checks feasibility, spectral ordering and stationarity, and compares with a separate constrained numerical minimizer. It then checks the exact three-dimensional rotated compression, exact rational mean-square errors and 20 rank-one cases, for 5,060 reported checks. It does not rely on Monte Carlo samples.

The nonstandard bridge between eigenvalue intervals and an *attainable real orthogonal compression* is the classical Fan–Pall converse (references in `RESULT.md`). Finite calculations are consistency checks, not certification of its general theorem, and cannot establish historical priority. The result covers no stochastic adaptivity, no optimization over subspace-learning cost, and no noise distributions other than standard real Gaussian probes.
