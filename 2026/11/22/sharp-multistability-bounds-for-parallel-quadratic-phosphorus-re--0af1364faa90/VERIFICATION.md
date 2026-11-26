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

The product of the positive denominators is positive for all real P and monic of degree 2m (the empty product is 1). Clearing it leaves a polynomial of degree 2m+1 with leading coefficient -a: all recycling contributions have degree at most 2m. Multiplicity of a root is preserved because its denominator is nonzero. An attracting isolated positive root must have positive field immediately to its left and negative immediately to its right, since otherwise a solution on that side cannot approach it; thus any two attracting roots enclose a different root. This includes nonhyperbolic roots. For simultaneous sharpness start at m=0 with the two witnesses 0 and 1. Adding (K,3K) contributes at each old witness at most 3P^2/K, so all prior strict signs persist for sufficiently large K. At the new witness K the field is at least L+K/2; at 4K it is below L+sum(old r)-K, made negative by the same large-K choice. These are ordered after the last prior witness and add two sign changes. The resulting distinct positive roots saturate the degree bound and must all be simple, with alternating stability. The argument uses finite K at every fixed stage and proves all-m attainability, not a numerical cutoff. Independently evaluated the six stated two-channel witnesses with integer-safe rational substitution: 1/10, -906517/32500520, 9499/100040, -13/626, 7199/117290, -50783079899/252501010. Positive loading keeps the half-line forward invariant and the linear-loss upper bound gives global boundedness. The uploaded script was inspected, not executed.

## originality

PASS

Credit is restricted to the simultaneous sharp arbitrary-m equilibrium and stability counts for positive quadratic Hill terms driven by a single concentration. The closest indexed independent record already exhibits five distinct equilibria and three attracting states in a two-threshold phosphorus family; neither that phenomenon nor scalar bistability is credited as new. Available broader switching-network and feedback results do not supply the arbitrary-m finite-steepness conclusion under the same quadratic restriction. The full equations of the same-day comparison are unresolved, but two-channel overlap, even if exact for that subcase, does not cover the unbounded family.

## value

PASS

An exact simultaneous upper bound and realization settle whether a fixed shallow Hill nonlinearity intrinsically caps the number of stable scalar regimes independently of how many feedback pathways are included. The construction answers no without replacing the nonlinearities by step functions, using negative feedback gains, or adding state variables. This is a structural distinction between a one-channel textbook example and the unbounded number of regimes attainable with finite positive channels.

The dated certificate retains the supplied scientific assessment, sources and limitations.
