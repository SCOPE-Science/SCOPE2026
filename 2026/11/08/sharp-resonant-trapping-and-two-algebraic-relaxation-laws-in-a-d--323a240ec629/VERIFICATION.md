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

# Reproducibility and scientific limits

Run `python verify.py` with Python 3, `sympy`, and `mpmath`. It computes the scalar reduction's trigonometric identity, jets at all four fixed phases, the unique critical extremum and leakage coefficient, three local leakage intervals, 5,988 test points for sector trapping, and long numerical trajectories from four distinct basins. The success line reads `VERIFY_OK harmonics=1 fixed_phase_zeros=4 exact_jets=8 sharp_threshold=1 leak_onset_cases=3 branch_samples=5988 orbit_classes=4`.

The universal phase classification follows from the exact max-ratio and monotonicity proof, not the finite grid. The \(n^{-1}\) and \(n^{-1/3}\) laws follow from reciprocal-power increments. Numerical root evaluation does not replace uniqueness of the trigonometric root; that uniqueness is analytical. The leakage expansion uses the nondegenerate maximum and Taylor's theorem. The code does not establish global behavior above the frontier, an independent audit, or definitive literature priority.
