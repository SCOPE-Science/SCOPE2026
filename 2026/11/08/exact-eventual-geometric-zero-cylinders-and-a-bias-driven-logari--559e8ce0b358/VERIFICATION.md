---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

On a zero run the map doubles x, and the conditional zero-digit selector is g(x)=1 on |x|<a/2, p or q on the flanking subintervals and 0 beyond |x|>1/2. Original Dajani–Kalle–Maggioni Lemma 3.8/3.9 gives stationary density 1/(1+a) on |x|<=a at strong matching parameters; their Lemma 3.11 proof gives local L1 continuity, extending plateau to every 1<alpha<3/2, while alpha>=3/2 is explicit. When n>=J, |x|<=2^-n<=a; scaling u=2^(n-1)x makes all selector terms with j>=J equal 1, so exact P(0^n)=2^-n C(a,p). Finite geometric summation yields balanced a(J+2/theta)/(1+a), and biased a^delta F_s(theta)+O_p(a) with nonconstant log-periodic F_s.

## originality

PASS

Primary density/one-digit paper does not imply the explicit n-step geometric cylinder and bias-sensitive edge prefactor.

## value

PASS

Zero-run length cylinders in stationary random signed-expansion dynamics are natural observables beyond the studied single-digit marginal. The exact onset of geometric continuation and the sharp balanced-versus-biased singular behavior constitute a useful new renewal-like structural boundary, with log-periodic prefactors not mechanically implied by known one-digit frequency bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
