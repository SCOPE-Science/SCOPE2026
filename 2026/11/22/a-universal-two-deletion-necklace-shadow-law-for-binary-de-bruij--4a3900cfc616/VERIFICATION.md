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

Reconstructed the collision classification for exactly two deleted positions, quotienting by rotations only. Each represented deletion creates at most two shortcut edges, so two equal circular outputs aligned at any rotation have at least 2^n−4n+2 common untouched length-n windows for n≥4. Unique occurrence of any such source factor gives a common retained anchor. Cut immediately before this anchor: the two masks now embed the same linear output into the same linear source. Every embedding can be moved to the leftmost greedy embedding by replacing each matched position in order by its earliest available equal symbol, keeping the anchor. Any such position change crosses at most two gaps, because all intervening unmatched sites plus the replacement site were deleted and only two sites are deleted. At distance one, or distance two with all symbols equal, the run choice is unchanged. At distance two with different middle symbol, the middle position is a deleted singleton and the deleted endpoint changes between its adjacent opposite-color runs. This proves necessity of the local moves even with consecutive deletions or two disappearing runs; each move visibly preserves the output. Each color has m=N/4 runs and s=N/8 singleton runs from the counts of 01/10 and 010/101, respectively. Thus same-color choices give binom(m,2)+(m−s)=m²/2. The mixed-choice graph has m² vertices and precisely 2s edges, a proper subgraph of the cycle of adjacent opposite-color pairs (there is a non-singleton run), with nonadjacent choices isolated. It is a forest, so exactly m²−m mixed outputs. Different compositions cannot collide because their output weights differ. The independent boundary replay `python3 /workspace/branches/independent_necklace_boundary.py` enumerated all 256 literal length-eight words, found exactly the two necklace representatives 00010111 and 00011101 satisfying the order-three condition, and yielded (2,2,2) in both cases. The supplied verification source was read, not executed; its order-six census is only a sample. The proof does not extrapolate from any census.

## originality

PASS

The strongest retrieved same-operation comparator gives the complete composition-resolved invariant on a disjoint elongated-run family. The general linear Sloane–Rains theorem does not settle cyclic alignment or composition, and no inspected broader circular result implies this de Bruijn theorem. This is a best-of-knowledge assessment, not a global priority claim.

## value

PASS

Cyclic de Bruijn sequences are a canonical complete-factor family, and the number of distinguishable two-deletion outputs is a natural circular-channel invariant. Its exact independence of the cycle, even after composition refinement, is informative: the collision count is not deducible just by knowing the number of deletion masks or the single-deletion spectrum. The common-factor anchor and local singleton-move forest explain why the invariant survives both local run coalescence and rotation ambiguities. No claim is made about deletion probabilities or more than two deletions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
