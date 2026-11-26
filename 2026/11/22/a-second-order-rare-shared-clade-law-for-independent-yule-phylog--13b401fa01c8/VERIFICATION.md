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

The event is the union over proper common clades of size at least three in two independent rooted labeled YHK trees; a prescribed joint probability in one tree must therefore be squared. Recomputing the size-three and size-four first moments gives 1/(6n)+(1/2+6/25)/n². Two distinct triples must be disjoint, and their unordered-pair correction is 1/(72n²). A prescribed nested triple has conditional probability 1/6 given its four-clade in one tree; the four possible triples contribute the pair correction 2/(75n²). For a compatible intersection with disjoint maximal clades of sizes k_i, conditional group elimination bounds the one-tree probability by a product of O(n^{1-k_i}) terms. Squaring and summing over labels gives O(n^{sum_i(2-k_i)}). This bounds all compatible three-event patterns by O(n^-3), including a four-clade containing a triple plus a disjoint triple; no four-clade can contain two distinct triples. The same bound makes the disjoint triple/four and distinct-four pair terms negligible. For 5≤k≤n−5, sum the exact means using binom(n,k)≥binom(n,5) and the summability of 1/[k²(k+1)²]; k=n−j for 1≤j≤4 has mean O(n^-2-j). These bounds justify Bonferroni and give 1259/1800. They also bound the non-unique-triple alternatives by O(n^-2); division by the leading probability and label exchangeability give the conditional statements.

## originality

PASS

The inspected exact one-tree calculus is credited in full. The contribution is the second-order probability of a size-restricted overlap in two independent samples, not a new clade marginal, an expectation of shared clades, or a general Poisson approximation. The nested and unordered double-triple corrections distinguish it from those statements. Bounded comparison only; the 1993 full text could not be checked.

## value

PASS

Cherries have order-one expected overlap, so the first agreement larger than a cherry is a motivated, much rarer benchmark. The second coefficient measures a real distinction between single-clade frequency and the union probability: both nesting and two disjoint triple collisions affect it at the same order. The conditional uniform unique-triple description identifies the typical agreeing structure rather than only its rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
