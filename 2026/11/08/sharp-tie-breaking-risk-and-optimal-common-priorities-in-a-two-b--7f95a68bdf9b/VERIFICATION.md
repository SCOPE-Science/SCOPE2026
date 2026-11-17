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

For two workers/two firms every complete DA matching has exactly one alternative; original weak Pareto domination must use the alternative and requires at least two tied agents (one across each alternative pair), while four ties eliminate strict gain. Independent exhaustive enumeration of all 16 deterministic tie policies and 3^4=81 weak-order profiles gives coefficient pairs (c2,c3)=(1,2) for 10, (2,3) for 4, (3,4) for 2. Every fixed policy has risk c2*t²(1-t)²/4+c3*t³(1-t)/2; convex mixing cannot beat the first class. Equal worker-side priorities attain Pmin=t²(1-t)(3t+1)/4, while independent fair four-agent tie breaks give Pind=t²(1-t)(7t+3)/8. Independently reimplemented complete DA and Pareto test for all 1296 inputs, reproducing exact classes. Polynomial coefficient expression establishes all real 0<=t<=1.

## originality

PASS

Best-of-knowledge: core original contribution is not established as a corollary or stronger prior result by the materially inspected sources and searches. Theorem 4 supporting a Pareto-efficient outcome by some tie break after observing preferences does not imply a single report-independent vector or lottery minimizes unconditional failure. Existence after observing profiles and ex-ante stochastic risk are mathematically different optimization orders. Residual priority risks remain; a failed search is not an originality proof.

## value

PASS

The fully optimized stochastic tie-breaking failure probability quantifies a concrete Pareto-efficiency cost of independent random refinement and identifies a simple jointly coordinated design that improves it. A smallest balanced market exact risk classification is a natural benchmark for mechanism design, not simply an implementation example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
