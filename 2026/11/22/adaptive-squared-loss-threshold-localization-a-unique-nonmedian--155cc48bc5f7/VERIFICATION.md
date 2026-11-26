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

After a positive midpoint bit the posterior densities on the two halves are 1−e and 1+e and the mean is 1/2+e/4. For a second bit the two centered first moments are ±e Cov(X,1_{X≥u}), giving the displayed conditional explained variance. For b=2d the right and left covariance numerators are (1±e)(1−b)(1+b∓e)/8 respectively. Factoring their probability denominators and independently checking the polynomial numerators as integer polynomials verifies the mirror-difference and derivative identities. All mirror-difference factors have the required strict sign in the interior; the endpoints give zero, and the right derivative at zero is positive. On 0≤b≤1 the cubic's Bernstein coefficients have exactly one sign change: the third is negative since its numerator increases to −1, the last is negative and the first positive. The fractional-linear change of variable reduces this to Descartes' rule, and opposite endpoint values give existence. Evaluation at the posterior median is e(e−1)/(1+e)^2<0, so its displacement exceeds the unique maximizing displacement. The implicit series gives d_e=e/4−e³/8+O(e⁴); the conditional covariance is 1/8−3e²/32+O(e³) and the variance denominator differs from 1 by O(e⁴). This gives the claimed adaptive coefficient after adding the first-query explained variance e²/16. For parallel queries, if a response pair has probability D/4 and centered moment N/4, its contribution is N²/(4D); the Taylor expansion is even and uniform on the full threshold square since near e=0 every response probability is bounded below. Its leading coefficient has the unique repeated-midpoint maximizer. Therefore all optimizer sequences tend there. Evaluating the continuous fourth-order coefficient there using e²/[8(1+e²)] bounds the optimal limsup by −1/8 after subtracting the leading maximum; the same repeated design gives the opposite bound. The explained-variance difference is the claimed risk difference with the stated positive sign.

## originality

PASS

The supported distinct claim is the exact response-conditioned unique nonmedian optimum under squared loss and the leading weak-channel separation from unrestricted nonadaptive pairs. The same prior, channel and loss already occur in parallel design, and the same-day staircase work is materially related on the parallel side. No precedence is inferred from same-day metadata and no claim of identifying the first nonadaptive weak-noise expansion is needed for the distinct adaptive comparison.

## value

PASS

Two queries are the minimal feedback horizon and the midpoint is a canonical first query under the prior. The theorem supplies a complete all-noise conditional policy and a sharp distinction between entropy and quadratic loss there. The fourth-order term establishes a strict separation even when all fixed threshold pairs are optimized; its small absolute size reflects weak per-bit information and still decides the first order at which this form of feedback beats the unrestricted parallel design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
