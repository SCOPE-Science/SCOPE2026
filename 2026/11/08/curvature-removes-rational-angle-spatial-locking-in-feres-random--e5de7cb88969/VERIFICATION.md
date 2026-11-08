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

# Verification and limits

The finite-state argument uses an irreducible stochastic matrix, so the spectral-radius bound follows from equality in the triangle inequality along two different positive return loops. The needed loop probabilities were checked directly against the normalized branch probabilities in the 2020/2022 originating papers. The spherical and hyperbolic jump formulas were independently derived from the right-triangle laws, with quadrant choice fixed by the positive boundary orientation. Their extreme-radius limits were compared with the Euclidean limit \(\Gamma_{0,r}(v)=2v\), proving that the return-phase difference cannot be constant on either admissible radius interval.

The embedded script `check_curved_billiards.py` was run with Python, NumPy and standard-library `math`: **966 supporting finite checks passed**. It constructs angle classes and transition matrices for \(N=7,8,9,10,11,13\), three interior incoming-angle ratios and both curvature signs, confirms Markov row sums and positive two-step loops, checks the radius-zero angular formula, and estimates spectral radii of representative nonzero Fourier twists. Such calculations do not certify the irrationality of a phase at any given numerical radius; the theorem excludes a countable analytically defined set instead.

The law at each finite time is a finite atomic measure, so total-variation convergence to Haar is false. The proof yields a separate exponential estimate for each fixed nonzero Fourier mode and weak convergence after Fourier approximation, not a uniform rate over modes. The exceptional resonance sets are sufficient exclusions, not an exact classification of bad radii. Independent audit has not been performed.
