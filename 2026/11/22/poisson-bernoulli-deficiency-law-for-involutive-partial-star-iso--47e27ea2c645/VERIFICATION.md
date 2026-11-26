---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Self-inverse means a common domain/image carrying an involutive permutation. If the hub moves to a leaf, it swaps with that leaf, and any other included leaf would violate distance preservation. Otherwise arbitrary leaf partial involutions combine with either hub omission or hub fixity and extend by identity on the missing vertices. This proves the polynomial, exact exceptions, and the finite deficiency mixture, with exceptional mass at most m/(2·2^m+m). Direct counting at m=2 gives 1+3z+6z²+2z³. For the analytic step, let r²+2r=m and use independent Poisson variables of means r,r,r²/2; after conditioning on total weight m, the r powers cancel giving exactly the labelled component counts. For W=Y+2Z and T=X+W, Fourier inversion has a central arc |t|≤r^(-3/4), cubic error O(r^(-1/4)), and variance of order r². The arcs near ±π are exponentially suppressed by the remaining singleton mean, and outside those and the central arc the pair term gives exp(-Ω(sqrt(r))) or better. Thus the stated local probabilities at displacement O(r^(2/3)) agree to relative o(1); the variances have ratio tending to one. The conditional likelihood ratio tends to one on a Poisson-high-probability window, and normalization bounds the conditional mass off that window. Convolution and the exceptional mass estimate give TV convergence. Since r=√m+O(1) and √r∼m^(1/4), the Poisson CLT gives the final normalization.

## originality

PASS

The supported distinct result is the TV deficiency theorem with an exact star-mixture bridge. The star monoid decomposition, conditioned Poisson framework for labelled assemblies, and conditional likelihood-ratio identity are established tools, not independently original here. The passages checked do not give the uniform lattice estimate for this two-singleton-color statistic, nor the assembled star deficiency approximation. The symmetry and finite exceptional term give the Bernoulli interpretation, not an asymptotically identifiable correction by itself.

## value

PASS

The exact bridge explains how the star center and the exceptional nonextendible involutions affect the rank, while the TV estimate gives a discrete distributional approximation for the omitted-leaf statistic stronger than a CLT. The need to smooth a parity constraint in the pairing contribution is a genuine feature of this natural inverse monoid model. The scientific value is the rank-law package, not the finite structural specialization alone or just adding an asymptotically negligible Bernoulli shift.

The dated certificate retains the supplied scientific assessment, sources and limitations.
