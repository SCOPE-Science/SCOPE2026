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

# Mathematical verification

The proof's defining assumptions are: real pointwise Jordan-BV inputs; \(n\ge2\); positive integer iteration \(r\); uniform Lebesgue integration; the ordinary binomial Bernstein kernel. The claim is proved for all such inputs and parameters, not inferred from a finite grid sweep.

Reproduction: run `python checker.py`. It uses exact Python rational arithmetic, with no third-party packages. It verifies mass and mean conservation for every row of the finite transition matrix, the decomposition into intermediate-state weights, pointwise endpoint-step domination at 31 rational inputs for each degree 2 through 9 and each iterate 1 through 8, and the exact first-iterate formula. Expected outcome: `PASS exact rational pointwise tests 10912 for n=2..9,r=1..8,31 rational x; mass/mean and first-iterate constants`.

The all-degree inequality is proved using positive intermediate-state probabilities and comparisons of \(k/n\) with \(1-k/n\). Exact integration uses the beta integral. Strict decrease follows from positive one-step absorption. The fixed-degree Perron asymptotic follows from the exact binomial second moment and the polynomial-eigenvalue list.

No independent mathematical audit has been performed. The full historical-priority comparison remains subject to undiscovered literature.
