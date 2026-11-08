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

# Reproducibility checks

Run `python verify_enumeration.py` and `python verify_linear.py` using standard Python 3, with no third-party dependencies.

The exhaustive routine checks every recurrent code for each integer k from 1 through 9, comparing actual stabilization against the closed forms and the maximizing last-two-block condition. It additionally iterates all stable height assignments through k=5, using the burning test to rule out overlooked recurrent configurations.

The separate reduced-Laplacian routine directly checks the maximal integer odometer and uniform-stationary Green function through k=50, solves the associated rational linear systems through k=12, and tests independent randomly chosen recurrent states for k=2 through 50. Both programs executed without assertion failures on the packaged source bytes.

For arbitrary k, correctness rests on the written burning, uniqueness, monotonicity and Laplacian arguments; finite computations are not an all-k certificate. Novelty assessment is limited to accessible primary sources and indexed prior claims. The model is restricted to the single-root fixed-distal-source graph family; no external independent audit has been performed.
