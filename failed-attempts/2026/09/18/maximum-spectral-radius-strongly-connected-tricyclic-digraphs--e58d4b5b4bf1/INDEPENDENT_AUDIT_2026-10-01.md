# Independent mathematical audit — SCOPE-20260918-e58d4b5b4bf1

Final disposition: **FAILED**.

## Correctness
**PASS** — The proof is sound. Arc excess two forces either one outdegree-3 branch vertex or two outdegree-2 branch vertices. Eliminating deterministic chains gives exact first-return Perron equations. In the one-branch case, exponent transfer maximizes the return sum at \(1,2,m-1\) with loops and \(2,2,m-2\) without loops, with equality forcing internally disjoint covering excursions. The three irreducible endpoint patterns for two branch vertices yield strict inequalities at the candidate roots, so no two-branch graph attains the bound.

## Originality
**FAIL** — The assigned theorem is already published in an earlier September 17 SCOPE record, 'Maximum spectral radius for strongly connected digraphs with n+2 arcs'. Its complete RESULT.md states exactly the same loop-allowed and loopless formulas, the same unique three-petal extremizers, and the same branching/first-return proof strategy. This is decisive exact prior coverage.

### Equivalent formulations
There is no formulation gap between the earlier SCOPE theorem and the assigned result.

### Broader coverage
The earlier published SCOPE theorem strictly settles the exact assigned statement.

### Exact database or table
The exact hit is decisive; no negative-search inference is needed.

### Claim versus prior implication
The assigned final claim is fully covered, not merely a special case.

## Value
**FAIL** — As a mathematical theorem the result is worthwhile, but this assigned September 18 record is a duplicate of an already published September 17 finding. Re-publishing the same theorem and proof adds no independent scientific value.

## Source inspections
- **Maximum spectral radius for strongly connected digraphs with n+2 arcs** (Resultary 2026/9/17 SCOPE012): complete RESULT.md Assessment: EXACT_PRIOR_COVERAGE. Evidence: It states the identical loop-allowed and loopless maxima and equality cases and sketches the same two-branch elimination.
- **Generating Functions and the Minimum Spectral Radius in Strongly Connected Digraphs with m+2 Edges** (arXiv:2609.18367): primary abstract and current bibliographic record Assessment: SOURCE_CONTEXT. Evidence: The abstract proves the minimum-spectral-radius problem on the same class; the assigned package identifies its Conjecture 5.15 as the maximum problem.

## Residual risks
- No correctness defect was found; rejection is due to exact prior SCOPE coverage.
