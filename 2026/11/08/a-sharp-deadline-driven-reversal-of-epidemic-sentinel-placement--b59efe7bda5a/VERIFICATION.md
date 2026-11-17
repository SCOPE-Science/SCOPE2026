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

A finite transient CTMC indexed by unobserved infected counts i,j has absorption-inclusive diagonal -[j(3-i)+i(4-j)], and transition rates j(3-a-i), i(1+a-j). Its exact four survival exponential-polynomial formulas follow from triangular linear ODEs. Independent 15-state individual-subset generator matches 20 Taylor derivatives for each placement, and Cayley-Hamilton makes this an exact identity check rather than numerical fitting. S2-S3 positive by a cubic sign bound, S1-S3 positive using -log x>=1-x and positive-discriminant-free quadratic, and S0-S3=x^3(1-x)R(x)/280 with R strictly concave and a unique zero. Direct exponential integration gives ET3=4/(21lambda), ET0=139/(630lambda). No claim for nonuniform seeds, recovery, or heterogeneous hazards.

## originality

PASS

PASS best knowledge for the exact finite-network K3,4 three-sentinel reversal, unique polynomial threshold and exclusion of both mixed allocations. The general SI hitting-time Markov-chain framework can evaluate each placement but does not supply this strict global comparison and phase diagram; matched Resultary entry is the same finding, not independent earlier coverage.

## value

PASS

A mathematically motivated counterexample to the rule that highest-degree sentinels or mean-time optimizers are always best: the risk objective changes the unique placement at a computable deadline with two rigorously excluded mixed alternatives. Small graph size does not invalidate the sharp decision boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
