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

Independent all-n check: conditional on the maximum being at most x>0, the n observations are iid from the truncated exponential, so the expected unbiased sample variance is its population variance, lambda^(-2) - x^2 e^(-lambda x)/(1-e^(-lambda x))^2. Integrating the centered sample variance against the survival indicator of the maximum gives the covariance integral of x^2 e^(-lambda x)(1-e^(-lambda x))^(n-2) over x>0. With u=e^(-lambda x), the integral is lambda^(-3) times the second derivative in a of B(a,n-1) at a=1. The product B(a,n-1)=(n-2)!/[a(a+1)...(a+n-2)] yields (H_{n-1}^2+H_{n-1}^{(2)})/(n-1), exactly (1) after restoring the scale. This covers n=2 as well and proves strict positivity. Independent exponential spacings give Var(M_n)=H_n^{(2)}/lambda^2; the unbiased-variance identity with central fourth moment 9/lambda^4 gives (3). The correlation and both asymptotic constants then follow. Decoupling is interpreted as vanishing Pearson correlation, not as a joint-limit assertion. Packaged rational replay was inspected, not needed for the proof.

## originality

FAIL

A distinct indexed theorem gives the identical covariance by adding an independent sample minimum to the range. It also already gives the asymptotic correlation, and the only finite-n change in the exact correlation is a known marginal-variance factor. This is demonstrated coverage, not inferred merely from title similarity or publication ordering.

## value

FAIL

Exact dependence of an extreme and dispersion is a natural invariant, but this record contributes no new invariant beyond the range theorem: adding the independent minimum supplies only the already-known marginal variance correction. The frozen proof repeats essentially the same spacing calculation. There is no surviving substantive remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
