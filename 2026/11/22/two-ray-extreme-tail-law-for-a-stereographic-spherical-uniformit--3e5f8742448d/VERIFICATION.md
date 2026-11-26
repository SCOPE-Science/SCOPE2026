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

For each pair the dot product is uniform on [-1,1], so Z and 1/Z have the same survival 1/(1+z^2) and mean π/2. On Z≥1 the reciprocating term is bounded and the rescaled density converges to 2r^-3 along the collision ray; on Z<1 exchange Z and 1/Z to get the antipodal ray (zero if the parameter vector vanishes). Distinct pair kernels are independent in pairs, including edges sharing one point by conditioning on that point and rotational invariance. With finitely many edges, two contributions above a fixed fraction of x have probability O(x^-4). For a test function supported away from zero, a nonzero test contribution forces some edge to exceed a fixed positive fraction of x; a uniform continuity bound on the event only that edge exceeds a much smaller fraction proves additivity as the latter fraction tends to zero. Multiplication by 2/n yields binom(n,2)(2/n)^2=c_n; the deterministic centering is irrelevant to the limit. For unbounded tail sets, the union bound gives uniform x^2-scaled mass O(M^-2) outside radius M, so vague convergence can be applied to the two scalar tails with boundary of measure zero. This yields c_n(1+a_+^2) and c_n a_-^2; integration and inversion then give the moment threshold, 2c_n(1+a^2) log x, and upper quantile constant. Covers n=2, negative and zero a, and coincident or absent rays. The supplied numerical checker was read, not run; its finite scalar checks do not certify the finite-sum theorem.

## originality

PASS

Bounded searches and statement comparisons support the fixed-sample two-ray measure and explicit extreme constants as distinct; neither the underlying statistic nor its infinite variance is the new finding.

## value

PASS

For an existing test whose untruncated S² version has no variance, the constants give exact fixed-n rare-significance calibration and explain which geometric events make different parameter choices fail together. For negative a the two events drive opposite signed tails, and the ray statement adds joint information not supplied by a scalar infinite-variance assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
