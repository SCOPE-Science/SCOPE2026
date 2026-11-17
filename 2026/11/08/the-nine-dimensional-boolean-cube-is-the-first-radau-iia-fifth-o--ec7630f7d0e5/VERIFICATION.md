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

Walsh diagonalization gives exact Krawtchouk shell sum. Positive cubic denominator factors reduce each d,k entry to an integer polynomial numerator. Independent reconstruction computed all 44 d<=8 numerator polynomials; 43 are nonnegative-coefficient, with first positive term at h^k; exceptional P_8,1 has nonnegative-coefficient transforms (1+t)^24P(t/(1+t)) and P(1+t), covering 0<h<1 and h>=1. Exact independent spectral and common-denominator rational checks give the displayed negative Q9 witness. This is a complete finite polynomial certificate of infinitely many real timesteps for eight fixed dimensions, not a grid scan.

## originality

PASS

Prior Radau hypercube theorems apply the different two-stage third-order propagator; general SSP barriers and fifth-order path theorems do not establish a fifth-order cube d=9 endpoint threshold. Best-of-knowledge comparison supports a distinct statement.

## value

PASS

Sharp first failure dimension for a standard high-order time integrator on a canonical family of graph heat semigroups, with globally valid all-step positivity certificates, is a motivated numerical-analysis boundary rather than an arbitrary single-step witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
