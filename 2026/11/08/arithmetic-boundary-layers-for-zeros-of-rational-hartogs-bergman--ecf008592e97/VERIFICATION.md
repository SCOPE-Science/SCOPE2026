---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The fixed-k exact centered coefficient sum c_(k+r)=sum_A W_m(A) W_m(mr-kA), with m=n+k, is the coefficient of the frozen reciprocal degree-2k polynomial. The compact piecewise-quadratic trapezoidal estimate gives normalized coefficient and derivative error O_k(m^-2) against (s^2+4s+1)(1+...+s^(k-1))^2. The exact Fejér value at theta_j=2pi j/k is m sin^2(pi j/k)/sin^2(pi h_j(m)/k), with mh congruent j mod k. Scaling theta=theta_j+u/m yields a_kj u^2+6k^2 sin^2(pi j/k)/sin^2(pi h/k) with distinct imaginary roots, giving the displayed delta and O_k(m^-2) complex error via Rouché. A negative real simple root and k-1 interior/outer splits account for all 2k roots. Finite independent k=5,n=201 tent/Fejér/root checks corroborate but do not establish uniform infinite asymptotics. The result fixes k; it does not cover growing k or all two-variable zeros.

## originality

PASS

A previously published universal fixed-gap theorem has the identical limiting polynomial and O_k(m^-2) coefficient estimate, and the gap-three theorem has the special sqrt(6) radial coefficient. Those earlier premises do not state nor, without the additional root-of-unity Fejér evaluation and local quadratic scaling, directly imply the all-gap modular-inverse-dependent first-order coefficient. The full Deng–Fu all-gap count and kernel formulas likewise do not establish it. Novelty is assessed only for the sharp residue-dependent rates, not the prior limit or root count.

## value

PASS

Rational Hartogs Bergman-kernel zeros are a natural analytic invariant; root localization alone leaves unanswered how boundary-approaching zeros decay. The explicit residue-sensitive escape rate for all fixed gaps, including two distinct gap-five rates, exposes arithmetic dependence of a geometrically motivated asymptotic that the earlier coarse limit misses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
