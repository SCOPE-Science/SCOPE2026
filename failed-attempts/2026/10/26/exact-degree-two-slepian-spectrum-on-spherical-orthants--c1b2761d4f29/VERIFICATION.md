---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For probability-normalized sphere measure, squared coordinates are Dirichlet with all parameters 1/2 and the independent signs give an orthant factor 2^-n. On the full-sphere orthonormal traceless diagonal and off-diagonal bases, the rescaled diagonal block is identity. For edge pairs the moments give 1, s, s² for equal, adjacent and disjoint pairs, hence B=(1−s)²I+s(1−s)R*R+s²J with unsigned incidence R. In the mixed moment the terms with a diagonal index on the edge have twice the generic moment; after summing the generic part against the traceless coefficients, the cross block is (s/√2)R*. Since RR*=(n−2)I+J_n, constants give T and ker R gives e with the stated dimension (zero at n=3). On the sum-zero image normalization of R* supplies √(n−2), giving n−1 identical 2-by-2 blocks with entries 1,b,b,a. The dimensions exhaust the complex harmonic space. Both T−1 and T−a exceed b; the shifted determinant at e is (n−2)s²(2s²−6s+3)/2<0 at s=2/π. Thus the top mode is unique up to scalar, and the spectral gap controls the orthogonal component sharply, with equality on any second-branch vector. The expansion T=(s²/2)n²+O(n), a=ns(1−s)+O(1), b=O(√n), gives r_+=ns(1−s)+O(1) from the quadratic eigenvalue formula for large n. It yields both stated limits, including s/[2(1−s)]=1/(π−2) for the top-to-second coefficient.

## originality

FAIL

A distinct indexed Resultary record supplies exactly the same complete spectrum, strict ordering and top eigenspace on the same exact-degree-two orthant problem. The claimed stability constant and both limits are direct consequences of that explicit spectrum. Its explicitly stated condition-number asymptotic compares top and bottom instead of top and second, but the data for the frozen ratio is already present. No substantive uncovered conclusion was identified. The later date on the matching catalog path is not evidence of priority, dependence or earlier publication.

## value

FAIL

The exact spectrum is naturally motivated and mathematically useful, but the frozen record does not add an independently useful invariant to the matched calculation. Its extra gap and spectral-ratio statements are a standard spectral-theorem deduction and leading-term computation from explicitly known branches, not further orthant analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
