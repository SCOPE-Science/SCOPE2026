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

The argument is analytic. The starting physical assumption is a two-level Hermitian Hamiltonian with nonzero off-diagonal coupling. Direct spectral reduction gives transition probability \(p(t)=a\sin^2(\omega t/2)\). The first-detection renewal identities, convolution inverse, sharp sinc minimum, and weak-rate expansion are developed explicitly in `RESULT.md`.

Reproduce the diagnostic check by executing `python checker.py` in a Python environment with NumPy and SciPy. The source computes the transition amplitude by independently exponentiating several Hermitian matrices; compares an exact rational Laplace transform with numerical integration of the renewal kernels; computes the unique critical sinc minimum; samples the nonnegative convolution kernel at subcritical visibilities; and independently inverts the rational transform to exhibit subcritical ordering and supercritical survival crossings. In the included run it passed 3278 deterministic assertions and returned a threshold of approximately \(0.82153497637881\).

Finite sampled checks do not prove universal positivity, lack of alternative zeros, or novelty. Those properties are addressed, respectively, by the displayed convolution representation and global minimum proof, by the interval monotonicity of the sinc function, and by explicit comparison with cited published results. The result has not undergone independent audit.
