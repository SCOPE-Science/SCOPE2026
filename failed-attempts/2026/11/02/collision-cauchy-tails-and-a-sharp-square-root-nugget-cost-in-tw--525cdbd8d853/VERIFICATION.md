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

The midpoint u and signed separation d have unit joint density on |d| < 2 min(u,1-u). Diagonalizing the Gram matrix in sum and difference directions yields the stated weight formulas. At zero nugget the difference of the two weights is m'(u)/(alpha d)+O(d) uniformly, and their sum is bounded. An independent tail derivation conditions on the nodes: the noise contribution is centered Gaussian with standard deviation sigma times the weight norm. Set d=x/t in the one-sided tail integral. The limiting integrand is the standard-normal upper tail at sqrt(2) alpha |x|/(sigma |m'(u)|), with zero contribution when m'(u)=0 and x is nonzero. The bound on the weight norm by a constant over |d| gives an integrable Gaussian-tail bound in x. Integration over positive and negative x gives sigma/(alpha sqrt(pi)) times the integral of |m'|. The other tail has the same coefficient by conditional symmetry; the tail-integral identity gives the moment cutoff at 1. A Lipschitz integrand cancels the inverse separation in the antisymmetric contribution, so the noiseless error is bounded and cannot alter the tails. For the nugget, set d=sqrt(eta/alpha) z. After multiplying by sqrt(eta), the difference mode converges to (m')^2 z^2/(2 alpha^(3/2)(1+z^2)^2), dominated by a constant times z^2/(1+c z^2)^2. Its integral gives the factor pi/4. The sum mode is bounded, and conditional noise variance is sigma^2 times the squared weight norm, giving the stated MSE at eta=sigma^2 and zero integrand. Direct Gaussian integration agrees with both derivative-integral evaluations.

## originality

FAIL

A distinct indexed Resultary result gives a stronger power-exponential theorem whose endpoint at kernel exponent 2 covers the entire substantive Gaussian finding for every kernel scale, including both exact coefficients, the cutoff and the Lipschitz cancellation. This is a verified coverage decision, not an assertion that the overlapping record was published first. Both carry the same date, and the broader record itself describes the Gaussian formulas at unit scale as already known without assigning a specific source or relative posting order.

## value

FAIL

The pathology is scientifically useful: arbitrarily small Gaussian measurement noise destroys the first absolute moment, although Lipschitz signal errors stay bounded. But this record supplies no additional scientifically distinct exact result beyond the verified stronger coverage; the explicit Gaussian integral evaluations and matched-noise substitution do not create an additional mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
