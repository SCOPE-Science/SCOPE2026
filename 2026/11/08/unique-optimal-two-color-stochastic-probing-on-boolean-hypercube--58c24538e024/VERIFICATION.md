---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The product formula for cube heat kernels makes B(x,y)=b(x xor y). The squared entrywise kernel W has Walsh eigenvalues Lambda_r given by double integral A(s,t)^{d-r}D(s,t)^r, where A=(1+e^{-2(s+t)})/2, D=(e^{-2s}+e^{-2t})/2 and A-D=(1-e^{-2s})(1-e^{-2t})/2. Since the finite positive mixing measure gives positive mass to (0,infty), Lambda_0>...>Lambda_d>0. Independence and Rademacher fourth moment produce Var=N(Lambda_0-2w(0))+sigma^T W sigma. Walsh Parseval then gives the exact nonnegative excess sum and unique equality when sigma is ± top-degree parity character. Independently constructed rational Green kernel for d=3,B=(I+L)^-1 and enumerated all 256 sign maps, finding optimum 1024/3675 attained exactly twice. This finite check corroborates, but does not replace, the all-d/full-measure proof.

## originality

PASS

Best-of-knowledge: the Frommer–Rinelli–Schweitzer general variance identity for any fixed coloring and distance-color bounds supply the framework but not the globally optimal parity partition among all (even improper/unbalanced) partitions of the cube or the strict Walsh spectral identity. Published screened-cycle checkerboard and complete-bipartite stochastic probing classifications treat different graph kernels; neither logically supplies this all-dimensional heat-mixture result.

## value

PASS

A unique globally minimum-variance partition is a natural optimization invariant for the widely used stochastic trace estimator on the hypercube, not a relabeling of a generic formula. The all-positive-heat-mixture assertion and exact spectral gap quantify robustness to every competing two-coloring and are useful for designing stochastic probes, including resolvent kernels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
