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

# Reproducibility notes

Run `python CHECK.py` in an environment with NumPy and SciPy. The companion `CHECK_OUTPUT.txt` contains the captured output of this same code, using a deterministic four-dimensional Sobol point set. The assertions verify the exact area at \(p=1,2\), the two special fixed-\(p\) constants, the disk crossover constant, the angular entropy maximum, monotonicity of the calculated crossover at four tested values, and six approximate scaled near-diameter probabilities from exact finite-\(\varepsilon\) constraints.

The probabilistic limits are analytic results, not extrapolations or certifications from the finite numerical sample. The proof depends on compact localization at the four fixed-\(p\) axial diameter pairs, uniformly differentiable polar boundary radii for \(p\) near two, dominated-convergence scaling of the corresponding sets, and the exact three-dimensional parabolic-section volume. All claims are restricted to the explicit parameter domains in `RESULT.md`. Complete historical priority and independent auditing remain unperformed.
