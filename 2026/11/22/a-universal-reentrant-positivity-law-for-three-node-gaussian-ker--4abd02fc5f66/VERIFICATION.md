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

# Verification and limitations

The exact symbolic proof is in `RESULT.md`: Gaussian convolution and a two-by-two linear solve yield the weights, an integral derivative inequality yields a unique maximum, and a comparison with \(2q-1-q^4\) gives the sharp universal nugget. A strictly negative second derivative yields the fold expansion. No approximate computations are needed for the infinite-family statements.

`verify.py` is a self-contained Python 3 standard-library checker. Run `python verify.py` and expect a `PASS` line reporting 7,203 tests and the universal bound. It compares independently solved three-by-three systems against analytic weights for 6,000 randomized finite Gaussian mixtures and checks global-one-peak and sharpness patterns in 1,203 additional cases. It does not exhaust parameter space; the printed numbers are reproducibility checks, not an independent mathematical audit.

The kernel amplitude is one; changing it scales the physical noise variance. The result concerns prescribed symmetric locations, and it does not establish minimum integration error, global optimal location design, stable floating-point inversion at near-coincident sites, or that noisy measurements are nonnegative. Independent review remains unperformed.
