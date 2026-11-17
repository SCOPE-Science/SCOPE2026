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

From conditional independence P(T>t)=exp(-gt) B_{n,k}(exp(-(e-g)t)). Telescoping uB'_{n,k}=k*binom(n,k)*u^k*(1-u)^(n-k) yields elasticity R(u) strictly decreasing from k to 0 for k<n, and constant n for k=n. For g2>g1, t^-1 log(S_g2/S_g1)=integral_{e-g2}^{e-g1} (R(exp(-st))-1)ds, strictly increasing from -(g2-g1) to (k-1)(g2-g1) for interior k. This proves one crossing, including g2=e boundary; k=1 or k=n has uniform strict sign. Exact n=3,k=2 survival 3exp(-(2e-g)t)-2exp(-(3e-2g)t) integrates to mean (5e-4g)/((2e-g)(3e-2g)); derivative numerator 8x^2-20x+11 gives sole maximum x=(5-sqrt3)/4 and value (8-4sqrt3)/e. Independent exact algebraic binomial derivative and mean check plus inspected uniformization code corroborated; numerical grid alone not proof.

## originality

PASS

Best-of-knowledge original final claim after direct statement/implication comparison; earlier general frameworks, alternative rules or smaller families are credited, with access and historical priority risks explicitly retained.

## value

PASS

For a natural ecological k-of-n resilience threshold while holding every marginal extinction rate constant, a universal strict horizon-dependent reversal and exact sharp non-endpoint mean-optimal synchrony identify a genuine structural tradeoff, not the routine common-shock survival formula. The 3-patch interior quorum is the smallest natural example, and the result covers all n,k and real rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
