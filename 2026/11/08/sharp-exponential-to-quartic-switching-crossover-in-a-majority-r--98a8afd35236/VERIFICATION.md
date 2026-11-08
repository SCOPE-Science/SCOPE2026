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

The analytic calculation reduces one-cycle majority switching to an exact odd-binomial tail integrated over a Poisson interval. The fixed-detuning case uses a uniform first-success mass ratio and a nondegenerate Laplace saddle; the critical case uses a binomial central-limit limit in the \(N^{-1/4}\) temporal window with a Hoeffding dominator. A geometric renewal transform yields the full first-switch exponential limit.

`check.py` completed 37 independent finite numerical assertions using Python 3, NumPy and SciPy. These test small-size polynomial/Fourier formulas against binomial period integrals, fixed-detuning and critical-window asymptotic ratios, the boundary gamma constant and the renewal Laplace transform. They are not a proof for arbitrary population size. Reproduce with `python check.py` in a directory containing the script and installed dependencies.

The result is restricted to odd sizes, ideal projective resets, independent exponential cycle times, the stated detuning sequences, and a first-switch observable. The provenance of the underlying renewal probability belongs to the cited original publications; independent validation of the new asymptotic analysis has not been performed.
