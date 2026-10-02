# Mathematical audit — 2026-10-01

## Final claim assessed

Exact zero forcing polynomial of complete multipartite graphs

## Correctness — PASS

PASS. If at least one part is non-singleton, three or more white vertices cannot be completely forced, while leaving one white vertex in each of two distinct parts is forceable; hence the zero forcing number is \(N-2\). The general size-\(N-2\) forcing criterion specializes to exactly the pairs in distinct parts, except a pair consisting of two singleton parts, giving coefficient \(\sum_{i<j}n_i n_j-\binom{s}{2}\). Every \(N-1\) subset is forcing in a connected graph, and the full set is forcing, yielding the stated polynomial. The complete-graph case gives \(Nx^{N-1}+x^N\). Repository enumeration agrees on all tested multipartite types.

## Originality — FAIL

FAIL. Boyer et al.'s full primary paper already proves a general theorem for every graph giving \(z(G;N)=1\), \(z(G;N-1)\), and, crucially, an exact neighborhood criterion for \(z(G;N-2)\). The same paper explicitly discusses complete multipartite graphs in its zero-forcing-polynomial context. For a complete multipartite graph, substituting its neighborhood classes into that theorem gives exactly the assigned coefficient: cross-part pairs qualify except pairs of singleton parts. The fact that no smaller set can force when a non-singleton part is present is the standard elementary computation \(Z(G)=N-2\) for this class. Thus the entire polynomial is mechanically determined by established theory.

### equivalent_formulations

Searches: Boyer et al. zero forcing polynomial complete multipartite; complete multipartite zero forcing number \(N-2\)

Evidence: Boyer et al. Theorem 1 gives the exact \(N-2\) coefficient for every graph via neighborhoods. For complete multipartite graphs the theorem's condition reduces immediately to the assigned cross-part count with the singleton correction.

Reasoning: The complement-of-two-vertices formulation in the package is exactly the specialization of the prior general coefficient criterion.
### broader_coverage

Searches: arXiv:1801.08910 full HTML Theorem 1; standard zero forcing number complete multipartite literature

Evidence: The prior graph-polynomial theorem supplies all top coefficients; the minimum forcing size eliminates every lower coefficient.

Reasoning: These prior ingredients mechanically determine the whole polynomial.
### exact_database_or_table

Searches: Resultary semantic search for complete multipartite zero forcing polynomial

Evidence: No earlier verbatim formula was found, but exact-text absence is irrelevant because the general theorem specializes directly.

Reasoning: This is implication coverage, not a database novelty question.
### claim_vs_prior_implication

Searches: Boyer et al. Theorem 1, especially \(z(G;N-2)\); complete multipartite neighborhood structure

Evidence: Two vertices in the same non-singleton part are twins and fail the prior criterion; two singleton vertices also fail after deleting each other; every other cross-part pair passes.

Reasoning: Substitution into the established criterion yields the exact coefficient without a new structural lemma.

## Scientific value — FAIL

FAIL. Once the general \(N-2\) coefficient theorem and the elementary complete-multipartite zero-forcing number are in hand, the claimed polynomial is a one-line specialization and bookkeeping count. It is useful as an example but does not clear the stated value bar against routine deductions from an existing graph-polynomial theorem.

## Source inspections

- **The zero forcing polynomial of a graph** — https://arxiv.org/abs/1801.08910. Material read: Complete primary HTML, especially Theorem 1 and the discussion of complete multipartite graphs. Assessment: DECISIVE_GENERAL_PRIOR_THEOREM. Evidence: Theorem 1 gives \(z(G;N-2)\) exactly from vertex-neighborhood comparison for every graph, and also gives the \(N-1\) and \(N\) coefficients.
- **Published-record and literature search for complete multipartite zero forcing** — Resultary and targeted zero-forcing searches. Material read: Ranked published findings and indexed complete-multipartite zero-forcing material. Assessment: SUPPORTING_STANDARD_CONTEXT. Evidence: The exact assigned record is recent, but the class's minimum forcing behavior is standard and elementary.

## Limitations and residual risks

The formula is correct but is rejected as a new finding because the only nontrivial coefficient is already given by the general extremal-coefficient theorem for the zero forcing polynomial, while the lower-degree vanishing is the standard elementary zero-forcing number calculation for complete multipartite graphs.

- No access limitation changes the failure because the decisive general theorem was inspected in full text.

## Disposition

**failed**
