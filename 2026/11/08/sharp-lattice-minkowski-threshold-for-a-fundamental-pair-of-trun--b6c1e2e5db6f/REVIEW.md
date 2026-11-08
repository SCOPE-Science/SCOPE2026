# Self-review

## Correctness — PASS
The proof reduces the decomposition problem to a height-two comparability graph, then uses Mirsky, König, and Dilworth to show that any failure in the six-point boundary must be a connected bipartite double star. For the only cases in which this finite boundary matters, a complete six-subset enumeration establishes precisely zero such graphs in the \(4\times4\) grid and one in the \(5\times4\) grid. The bundled exact verifier tests the witness inequalities and nondecomposability, and independently constructs the comparability graph for each enumerated subset. The large-parameter strictness follows from embedding that one explicit six-point support; it is not inferred from finite experimentation.

## Originality — PASS, subject to historical priority review
Feigin and Makhlin (arXiv:2610.40891v1, Sections 3–4) define the objects and give a nonadditivity example only at \((d,n)=(6,12)\); the inspected material gives no sharp threshold or count of missing points. Their first/last-weight Minkowski result does not cover \(e_2\) when \(d\ge4\). Makhlin's earlier marked chain-order construction and the closest accessible published Grassmannian-polytope research results concern different polytopes or different invariants. Claim-level literature and research-record searches did not identify a statement implying this exact threshold. Absence from search results is not a proof of global priority; unstated consequences in specialized literature remain a residual risk.

## Mathematical value — PASS
The theorem provides a natural, all-parameter boundary for lattice-point additivity exactly in the new polyhedral family used to index monomial bases for truncated Grassmannian representations. It improves the size of the known counterexample from a \(6\times6\) grid to the minimal \(5\times4\) grid and establishes a unique, explicit smallest obstruction. This is a structural boundary rather than a routine numerical restatement.

## Scope and limitations
Only the pair \(e_2,e_d\) is classified. The exact minimal-grid enumerations are finite proofs via transparent integer code; they do not independently establish the infinite claim. The latter is proved combinatorially. Independent review and exhaustive priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
