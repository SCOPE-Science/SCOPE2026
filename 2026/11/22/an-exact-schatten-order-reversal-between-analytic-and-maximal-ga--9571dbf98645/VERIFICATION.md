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

PASS on repairs/3/RESULT.md. The frozen Verification paragraph gave the two example operator norms in reverse order relative to the named analytic/maximal pair. The corrected complete file explicitly gives analytic 1 and maximal 5/4, as the frozen checker already does. The theorem itself recomputes correctly: normalized source coefficient vectors are orthogonal by angular frequency, with squared norm α n!/(2t−α)^{n+1} before normalization; the target monomial norm squared is n!/β^n. This gives Cr^{n+1}. Gaussian unweighting and separate two-dimensional unitary dilations supply the kernel (2Cr/π)exp(−|x|²−|y|²+2r x·y); the Mehler ground Gaussian and complete Hermite tensor basis give 2Cq^{j+k+1}. The two geometric sums yield the stated ratio. The repaired proof verifies the central-interval mean inequality by writing a central uniform variable as aU+b(1−U), applying strict convexity or concavity pointwise, and integrating. This works also for the integrable singularity when p<1 and gives equality exactly at p=1,2. In the example the trace norms are 5 and the squared Hilbert–Schmidt norms are 25/9. At the critical limit the maximal shell m has multiplicity m+1, so m=√(2N)+O(1); -log r and -log q have leading terms δ/(2t²) and √δ/t, giving the distinct profiles. At equality δ=0 the analytic decomposition remains a bounded scalar partial isometry and has infinite rank; the positive modulus of the maximal operator is unitarily equivalent to the multiplier 2C exp(−|ξ|²/4), whose essential range is [0,2C] and whose level sets have measure zero. The supplied diagnostics were inspected, not executed.

## originality

PASS

Credit the established operators and compactness region, the analytic singular multiset and its critical specialization, classical Mehler diagonalization, and the elementary equality of Hilbert–Schmidt norms for kernels of equal modulus. The repaired finding's distinct focus is the exact strict comparison across all real Schatten exponents and the comparison to the maximal rank profile and boundary spectral type. The strongest inspected same-object and analogous results do not already supply those comparisons.

## value

PASS

The exact exponent classification answers a natural question that positivity, equality of Hilbert–Schmidt norms and pointwise kernel dominance do not answer. In particular the dominating kernel gives larger operator norm yet strictly smaller Schatten norm throughout (1,2), not just at one test value. The distinct critical rank profiles quantify the effect of multiplicities at a common compactness boundary and separate the infinite-rank partial isometry from the continuous positive modulus. These are useful comparisons independently of the already known analytic spectrum and compactness criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
