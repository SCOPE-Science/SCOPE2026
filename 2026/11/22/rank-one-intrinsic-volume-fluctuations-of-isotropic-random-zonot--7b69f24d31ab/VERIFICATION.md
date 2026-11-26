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

The repaired result keeps the fixed-d joint law and exact regressions. The Steiner Gram-determinant sum has constant first projection. The squared height off the j-plane is Beta((d-j)/2,j/2), giving a telescoping conditional mean c_{d,k} times the two-vector area. Summing the canonical pair projection gives the binomial multiplicity and the exact covariance. Higher canonical kernels are orthogonal, including across orders; the variance of the order-j contribution is O(n^{2k-j}), proving the residual and correlation rate. For the negative centered sine-of-angle kernel, the Bernstein representation is positive on mean-zero modes: the tensor kernel of degree 2m has a positive quadratic form on each nonzero harmonic of that degree, since its tensor moment contracted with the harmonic's coefficient tensor is the squared L2 norm. Odd and constant modes vanish. Mercer on the diagonal and the Hilbert–Schmidt identity give the trace s_d and squared trace v_d. The finite harmonic CLT uses the truncated kernel; the tail has variance at most half its squared Hilbert–Schmidt norm uniformly in n. A small finite chi-square prefix and an independent small nonnegative tail give the sharp upper endpoint; the first mode makes the lower tail unbounded. The original line 92 falsely said the correlation equals one when one index is two. For k>2 the continuous residual at coincident inputs is c_{d,k}s_d binom(n,k)(binom(k,2)-1)>0; full support and zero mean imply strictly positive residual variance. The repair replaces the false equality and explicitly restricts the fixed-cutoff display to the truncated statistic. The main asymptotic and exact mean/covariance claims are unchanged.

## originality

PASS

Pass for the common fixed-dimensional joint fluctuation and quantitative cross-intrinsic-volume result. Existing means, the d=3 volume marginal and standard harmonic/U-statistic machinery are not new contributions.

## value

PASS

First-order Gaussian theory misses exactly this isotropic fixed-length model. The result explains why all higher intrinsic-volume fluctuations become collinear, supplies the finite-sample coefficient and an error rate, and identifies a common non-Gaussian law with sharp one-sided bound. These are consequences about dependence, not a recomputation of the known means or a single marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
