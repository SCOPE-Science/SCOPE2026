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

Run `python3 checker.py` with Python 3.10 or newer from this package. The checker needs only the standard library and uses `fractions.Fraction` throughout. It confirms the piecewise-affine image proportions and common transition matrix independently for each map, the invariant vector, the first nine covariance values and eleven exact finite variance identities. Direct integration of preimage intervals, explicitly subdividing both domain-branch boundaries and target-atom boundaries, checks all \(16\) length-four switching words and all \(243\) coarse-state histories of length five: \(3888\) exact rational probability comparisons. The checker prints `PASS` when all assertions hold.

The main argument in RESULT.md establishes uniform conditional distributions, the full Markov cylinder law for every finite word, and the standard finite-state central limit theorem for every predetermined infinite switching sequence. Finite checking does not independently certify the theorem for arbitrary lengths or all real initial conditions. Endpoints and their iterated preimages are excluded as sets of measure zero; independence from the switching path is distributional, not pointwise. No independent mathematical audit has been performed.
