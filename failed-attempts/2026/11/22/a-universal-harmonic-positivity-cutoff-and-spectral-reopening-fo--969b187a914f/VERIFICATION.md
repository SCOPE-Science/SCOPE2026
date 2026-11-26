---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Summability of the Hausdorff moments gives the continuous Fourier expansion with coefficients a_|n|+(b/2)(a_|n−k|+a_|n+k|). The ratio of the shifted sum to a_n is strictly smaller than at k for 0≤n<k by decrease and log-convexity. For n≥k it is the expectation of the decreasing function r^(−k)+r^k under the r^n tilt, decreasing strictly in n except for a point mass. This proves the sharp bound and exact vanishing patterns. Consecutive positive high frequencies imply full rank on every set of distinct sites by Vandermonde; the pure critical kernel instead has the 2k−1 consecutive frequencies |n|<k. For n>k, multiply the critical coefficient by a_0+a_2k: the result is the integral over r<s against dμ(r)dμ(s) of (s^k−r^k)(1−(rs)^k)(s^(n−k)−r^(n−k)), by symmetrizing the product of moments. This yields exactly the stated two-rate identity, with a_0=1 by normalization. The supplied exact-rational script was inspected, not run; the decision uses the all-measure proof, not finite tests.

## originality

FAIL

Distinct catalogue records cover the underlying support and positivity problem in substance: d53f1b363054 gives an all-mask theorem and proof for non-point Poisson mixtures and 2dc7842600c0 gives the corresponding single-radius cone and ranks. The only additional support range here is handled by the same inverse-convolution proof through Wiener's lemma, as detailed below; the two-rate expression is direct moment expansion in a case already covered. The short moment proof is valid, but the claimed theorem and reopening are not established as a distinct mathematical finding. This is a statement/implication decision, not an assertion of chronological priority among same-date records.

## value

FAIL

The rank transition is a meaningful structural question, but the separate contribution left after the all-mask and pure-radius comparisons is an alternate short proof, a routine loss of a compact-support restriction under Wiener summability, and the factored two-rate coefficient in a covered case. The residue does not establish a distinct structural or independently needed exact finding beyond those results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
