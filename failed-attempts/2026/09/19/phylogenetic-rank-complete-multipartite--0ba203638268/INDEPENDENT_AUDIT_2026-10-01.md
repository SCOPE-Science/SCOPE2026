# Independent audit — 2026-10-01

## Final claim

The phylogenetic rank of a connected complete multipartite graph is the number of non-singleton parts plus one exactly when at least two singleton parts occur, with the stated full fixed-order rank spectrum.

## Correctness — PASS

The star-coordinate construction realizes the complete-multipartite graph metric with q+1_{s>=2} tree factors. For the lower bound, a distance-two pair chosen in each non-singleton part requires a realizing coordinate, and two such pairs cannot share one because that would create a unique largest four-point sum. If at least two singleton parts occur, their unit-distance pair cannot be realized in a coordinate already realizing a non-singleton distance-two pair, again by the four-point condition. A fresh independent replay checked explicit tree pseudometrics and four-point certificates on all 128 connected complete-multipartite types through order 10.

## Originality — FAIL

Originality fails decisively because an earlier published finding from 2026-09-18 gives the exact same formula, the same star construction, the same four-point lower bound, and matching-deleted complete-graph consequences. The current fixed-order spectrum is an immediate arithmetic corollary of that formula.

### Equivalent formulations

Searches: Published-record semantic search for phylogenetic rank of complete multipartite graphs

Evidence: The earlier 2026-09-18 result and the assigned result were the top two exact hits; the earlier full RESULT was inspected.

Reasoning: The formulas are mathematically identical, including the all-singleton complete-graph endpoint.

### Broader coverage

Searches: Earlier exact complete-multipartite rank theorem

Evidence: The prior theorem covers all connected complete multipartite graphs and arbitrary numbers of singleton parts.

Reasoning: It fully dominates the current central claim.

### Exact database or table

Searches: Exact rank formula and matching-deletion consequences

Evidence: The prior finding gives the same formula and arbitrary matching-deleted complete-graph specialization.

Reasoning: The spectrum follows mechanically from feasible counts of non-singleton parts.

### Claim versus prior implication

Searches: Full prior RESULT comparison

Evidence: Same construction and four-point obstruction are already present.

Reasoning: No independent new claim survives the implication comparison.

### Source inspections

- **Exact phylogenetic rank of complete multipartite graphs** — Decisive exact coverage. Material read: Complete RESULT.md. Evidence: It states pr(G)=max{1,q+1_{s>=2}} and proves it with the same tree-factor construction and four-point obstruction.

Checked sources: Earlier published finding: Exact phylogenetic rank of complete multipartite graphs (2026-09-18), full RESULT inspected; Ashworth et al., The phylogenetic rank of a graph, arXiv:2609.19372v1 (2026); Assigned verifier plus fresh independent small-order reconstruction through order 10; Published-record semantic search for complete-multipartite phylogenetic rank

Residual risks: No correctness defect was found; the scientific rejection is exact prior coverage.

## Scientific value — FAIL

A complete classification of this natural graph family would be valuable if open, but the exact classification was already published. The remaining spectrum statement is a routine consequence of the known formula, so no independent worthwhile gap remains.

## Conclusion

The finding is scientifically rejected because all three axes must pass; correctness evidence is preserved, but originality and value fail under the implication-based comparison.
