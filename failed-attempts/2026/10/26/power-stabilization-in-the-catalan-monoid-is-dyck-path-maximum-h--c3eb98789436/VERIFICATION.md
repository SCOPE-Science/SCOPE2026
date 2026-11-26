---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Between two successive fixed points (or the final endpoint), monotonicity and regressiveness force all nonroots to have a smaller parent in the same interval. As parent labels are nondecreasing, visiting vertices in a queue produces exactly the consecutive labels within each component. Conversely componentwise breadth-first labelling of any plane forest gives a nondecreasing regressive map, including across component boundaries. Each vertex takes exactly its edge-depth many iterates to reach its fixed root. Equality of two successive powers is equivalent to every orbit having reached its root, and depth-first parenthesis nesting is edge-depth plus one for a nonempty forest. The empty map is counted separately with depth zero. A depth-k forest is a sequence of roots with child forests of depth at most k-1, giving the stated formal-series recurrence with F_0=1/(1-z). Its first three iterates give the displayed coefficient formulas. A chain of k+1 vertices and n-k-1 singletons realizes each k, and at k=n-1 only the chain occurs. For fixed k the even-step path-graph walk counts give the stated squared spectral radius, with positive endpoint projection and no cancellation on even powers.

## originality

FAIL

The claimed novelty of the stabilization-depth distribution and its ordered-tree identification is not established. Substantive pre-2026 author-abstract evidence already connects the bounded-potency one-fixed-point class of order-preserving maps to bounded-depth ordered trees and reports generating functions. The one-fixed-point class with root 1 is exactly the one-component Catalan class before imposing the potency bound. The general forest claim reduces to those components, with the standard parentheses encoding and classical bounded-height enumeration. A distinct indexed finding directly gives the same breadth-first forest identification and a stronger joint rank/depth census whose marginal is the frozen census. This comparison demonstrates mathematical coverage and strong prior-work overlap, but does not prove that the older full text literally states the precise breadth-first algorithm or the Dyck formulation, and the later indexed finding is not evidence of earlier public priority.

## value

FAIL

The invariant is natural and the proof is readable. The bounded-height recurrence, closed forms and transfer-matrix rate are classical after the tree-depth correspondence. Against the ordered-tree potency precedent and the exact indexed census and construction, no independent gain beyond a standard forest-to-parentheses re-encoding was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
