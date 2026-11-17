---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Rockett finite identity f(n)=(n+1)2^{−n−1}Σ_{j=1}^{n+1}2^j/j follows from verified first-order recurrence. In Q2 the convergent Σ_{j≥1}2^j/j=−log(−1)=0 (torsion −1), giving exact tail f(n)=−(n+1)Σ_{i≥1}2^i/(n+1+i). Subtraction yields −hΣ_{i≥1} i2^i/((n+i+1)(n+h+i+1)). For nonnegative u and v≥1, trailing binary ones prove ν2(u+v)≤s2(u)+s2(v−1); also 2s2(i)≤i+1. Each summand has valuation at least ν2(h)−s2(n)−s2(n+h)−1, inherited by convergent sum. Set h=2^e, 0≤k<2^e to obtain Davis conjecture since s2(k+h)=s2(k)+1. Proof is infinite analytic, not extrapolated from examples; independent Fraction check passed all 6400 n,h pairs tested.

## originality

PASS

Best-of-knowledge proof of explicitly open Davis 2013 Conjecture 1.2 via a stronger arbitrary-shift 2-adic tail inequality, with exact primary comparison; chronological novelty remains subject to unindexed later proofs.

## value

PASS

Solving a named 2013 conjecture on 2-adic inverse-binomial sums is a substantive number-theoretic advance. The general-shift inequality and removal of a conditional 2-adic definability hypothesis give meaningful new structure, not a routine finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
