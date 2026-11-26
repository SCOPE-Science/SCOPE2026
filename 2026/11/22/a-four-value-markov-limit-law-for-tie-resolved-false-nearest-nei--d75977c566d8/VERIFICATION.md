---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Fix the first index J_s of each symbol and its successor A_s. Once both references are present, for every nonreference position the earliest eligible index has distance zero and is J_s; Definition 1.1 flags that position exactly when its successor disagrees with A_s. The difference from the resulting transition-count formula is at most 2/n, even if a symbol has only one occurrence in the finite sample. Apply the ergodic theorem on a single probability-one event to the four transition frequencies; their random selection by A_s then needs no independence from the empirical counts. Given X_0=s, the opposite hit T is almost surely finite and at least 1, so X_1 is measurable at T, including the case T=1. The strong Markov law of X_{T+1} is the fixed opposite row, while X_1 has row s. The conditional product law does not depend on s, proving independence unconditionally. Multiplication gives the displayed ordered weights (A_0,A_1)=(0,0),(0,1),(1,0),(1,1); summing row means and independent weighted variances gives both formulas and the unique zero-variance point. Independently expanded the four-point moments symbolically and checked the finite reduction on all 4,052 binary words of lengths n+1, 2<=n<=10, with both symbols in the first n positions: minimize (distance,index) over j!=i and compare with the first-occurrence rule. The finite check is not the a.s. proof. The nearest-neighbour definition only needs n>=2; ratios at duplicate points and positive amplitude thresholds cause no boundary issue. No frozen code was executed.

## originality

PASS

The closest exact published result retrieved is the Bernoulli subfamily, not a law for genuinely dependent chains. The primary smooth FNN and symbolic partition papers do not imply this tie-resolved law. Priority is best of knowledge, not certified.

## value

PASS

A complete natural two-parameter calibration of the simplest dependent binary sensor distinguishes serial persistence from stationary symbol imbalance. The fixed-marginal family yields a checkable change in mean and loss of self-averaging, attributable to the random choice of first-hit successors, not generic observation behavior or a numerical fit. The conclusion is useful for this specified tie rule and is not a claim about successful embedding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
