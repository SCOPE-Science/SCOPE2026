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

For every integer k>=2 and lambda strictly between 0 and 1, the 2k-point matching-contracted equilateral metric has range <=1. Strict convexity of the uniform variance on potentials modulo constants forces each maximizer to a tight-edge-connected polytope vertex. Every such vertex has six possible states per matched pair and both a lower/upper anchor. An opposite split-pair replacement raises variance by 2 lambda(1-lambda)/(2k); a same-side two-split randomized replacement raises expected variance by (k-1)lambda(1-lambda)/k^2. Hence at most one split pair maximizes. Pure states have variance a(k-a)/k^2. The one-split finite difference (k-2a-lambda-1)/k^2 is maximized at a=(k-1)/2 for odd k, with difference from the best pure state lambda[(2k-1)lambda-2(k-1)]/(4k^2). This yields precisely the stated parity law and transition lambda=2(k-1)/(2k-1), with both classes at the transition. Endpoints lambda=0,1 are intentionally excluded. Independent direct enumeration at 12 rational k/lambda instances corroborated but does not prove the infinite theorem.

## originality

PASS

The earlier complete six-state vertex/facet theorem for arbitrary independent pair contractions covers an important geometric prerequisite but does not optimize the uniform centered L2 variance, prove one-split localization, or identify the sharp odd-parity threshold. Classical graph spread and generic Lipschitz polytope work do not supply the same model-specific sharp norm. No mathematically dominating formula was found in indexed results; historical priority is qualified.

## value

PASS

The sharp Lipschitz-to-centered-L2 norm is a natural metric invariant. Equal contraction of disjoint pairs leads to a genuinely nontrivial parity obstruction and a sharp one-defect optimizer transition, distinguishing values continuously between equilateral and matched metrics. The one-split localization lemma and equality family are reusable structural facts, not merely a finite numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
