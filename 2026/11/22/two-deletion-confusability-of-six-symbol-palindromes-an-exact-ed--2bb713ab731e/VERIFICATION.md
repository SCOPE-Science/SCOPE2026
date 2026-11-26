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

The palindrome parametrization is injective, and length-four common subsequences are exactly common outputs after two deletions. Independently inverted the explicit four-position subsequence shadows over six symbols and counted unique pairs (replay: python /workspace/audit-evidence/frozen5.py); dividing the ordered-pair counts by the falling factorial for each support size gives 20, 37, 9 for supports 2, 3, 4 and zero otherwise. Six symbols suffice to realize every equality partition of the six input slots, so relabelling yields the all-q law, not a finite-alphabet extrapolation. For fixed source support r, at most one new symbol can appear in a neighbor: two distinct fresh symbols occupy at least two slots of the other triple and leave at most two positions with source letters in its palindrome. Each one-new-symbol template has q−r realizations. Independent degree counts at r and r+1 agree with the constants and slopes, including the missing all-distinct type at q=2. The abba output partitions the vertices into q² cliques. Randomly ordering vertices gives an independent set with expected size Σ1/(d+1)≥|V|²/(|V|+2|E|), giving the asserted ceiling after substitution. The maximal packing of alphabet triples works because sharing at most one letter leaves at most two symbols of a common subsequence counted with multiplicity, and a chosen triple rules out at most 3(q−2) triples including itself. This proves the constructive bound for q≥3. The two frozen checkers were inspected, not executed. The result gives only bounds and asymptotic order for A_q, not its exact value.

## originality

PASS

The supported distinct claim is the entire all-alphabet unordered edge polynomial and the five degree laws for the palindrome-induced graph, with quadratic bounds as consequences. The deletion hypergraph, independence bound and greedy packing method are not themselves new. Relevant finite unrestricted censuses overlap the alphabet-size 2 and balanced alphabet-size 3 subdomains, and one-deletion and reconstruction results use closely related machinery. None of the inspected statements or their justified implications determines this all-alphabet graph law.

## value

PASS

Even-length palindromes avoid ordinary one-deletion conflicts, making the transition to two deletions a natural structural boundary. The exact all-q density and equality-type degree heterogeneity identify which constrained source words produce many conflicts and provide exact inputs for finite-alphabet packing bounds. The uniform result is useful beyond a single small instance; the generic independent-set bound or the mere Θ(q²) construction alone would give less information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
