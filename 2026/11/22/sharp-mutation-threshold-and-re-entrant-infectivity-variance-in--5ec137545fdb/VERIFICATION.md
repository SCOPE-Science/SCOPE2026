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

# Reproducibility and mathematical verification

The proof is analytical and covers every positive time for the stated global continuum model. The finite checks reproduce critical nonstandard algebraic identities and the finite-time rational witness, but are not substituted for the global argument.

Run `python verify.py` with Python 3 and the SymPy, NumPy and SciPy packages. The program checks by symbolic simplification that an evolving Gaussian component solves the linear-potential diffusion equation exactly; that logistic mixture masses give the displayed variance derivative; and that \(g(p)=p(1-p)(2p-1)\) attains maximum \(1/(6\sqrt3)\). It then verifies the strict rational signs for the re-entrant example and independently tests finite-time Gaussian mixture moments by numerical quadrature.

Infinite-time susceptible exhaustion is established by the analytical contradiction in RESULT.md: any positive limiting susceptible fraction forces unbounded infectivity mean and eventually an impossible exponential increase of infected fraction. The exact critical threshold follows by optimizing the skewness polynomial globally over the whole mixture interval. The script does not attempt to certify arbitrary numerical epidemic curves, uniqueness of the turning points in the re-entrant witness, or physically bounded infectivity dynamics.

Scientific status: self-review passed. Independent audit has not been performed.
