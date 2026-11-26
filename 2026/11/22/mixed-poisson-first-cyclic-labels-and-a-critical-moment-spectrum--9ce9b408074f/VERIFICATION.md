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

For a specified cyclic k-set, the cyclic permutation and rooted forest count gives k!·k·n^{n−k−1}, also n! when k=n. Thus p(k)=(k/n)Q_{n,k}, with conditionally uniform labels. The log-product estimate on bounded k/√n ranges and a Gaussian tail bound give the Rayleigh limit. For the Cox claim, expand the conditional Laplace functional for any nonnegative continuous compactly supported f in elementary symmetric sums of b_v=1−exp(−f(v/√n)), weighted in order ℓ by (k)_ℓ/(n)_ℓ. On bounded k/√n ranges the absolute terms are bounded by C^ℓ/ℓ!; Riemann sums and omission of repeated indices give exp(−r∫(1−exp(−f))) for k/√n→r, including r=0. Mixing then gives the asserted vague limit. The conditional no-hit probability is hypergeometric, giving E exp(−tR), and scaling the Rayleigh integral shows the t^{−2} tail. Independently, the k+1 gaps around the ordered sample are a uniform weak composition of n−k; M−1 is the first gap. Weighting that gap j by s!·binom(j+s,s) gives s!·binom(n+s,k+s)/binom(n,k) by convolution, the claimed conditional rising moment even when k=n or s>n. The mean follows by Gaussian Riemann summation. For s=2, the sum of kQ_{n,k}/[(k+1)(k+2)] up to √n differs from the harmonic sum by O(1) using 1−Q≤k(k−1)/(2n); the tail contributes O(1). The prefactor is 2n+O(1), so the variance has coefficient one. For s>2, fixed-k dominated convergence is justified by k^{1−s}; summing via the beta integral yields s/[(s−1)(s−2)]. Lower-order terms in the rising polynomial have strictly smaller scale, including n log n for order two.

## originality

PASS

The classical distribution and Rayleigh limit for the core count and exchangeability of the core labels are not new. The supported claim is their use in a single-map fixed-label point-process and minimum-label theorem, particularly the exact critical variance and higher-moment spectrum. The strongest inspected comparisons do not supply that statistic and spectrum together or cover the asymptotic content by specialization.

## value

PASS

The earliest cyclic vertex in a deterministic ordering is a natural statistic for scanning a random functional graph. The result separates the typical √n label scale from a finite variance dominated by a logarithmic range of core sizes and higher moments dominated by rare small cores. The coefficient of the logarithm and the full fixed-integer moment constants quantify this distinction; neither reporting a weak limit alone nor restating the cyclic-core distribution does so.

The dated certificate retains the supplied scientific assessment, sources and limitations.
