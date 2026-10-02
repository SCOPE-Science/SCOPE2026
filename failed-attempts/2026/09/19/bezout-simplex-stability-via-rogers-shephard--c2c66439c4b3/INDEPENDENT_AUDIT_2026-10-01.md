# Independent mathematical audit — SCOPE-20260919-c2c66439c4b3

Final disposition: **FAILED**.

## Correctness
**PASS** — The special-test proof was reconstructed. Mixed-volume monotonicity plus K_v^s+[0,sv] subset K yields the projected estimate; Minkowski and layer-cake integration give the lambda_n(c) chord bound. The covariogram identity g_K(-tv)=integral_t^ell P_s ds and polar integration give the difference-body inequality, with n B(n+1,n)=1/binom(2n,n). Applying the quoted Rogers-Shephard stability theorem then gives the displayed Banach-Mazur bound. No computational certificate is required.

## Originality
**FAIL** — A September 18 published result was inspected in full. Its stated theorem uses the full two-body Bezout coefficient beta(K), but the proof of its longest-chord and difference-body steps uses only the exact special tests A=K intersect (K-sv), B=[0,v]. Therefore the same proof already establishes a Banach-Mazur stability theorem under the restricted chord-test coefficient after replacing beta by that restricted supremum. Indeed its retained covariogram bound gives a stronger numerical lower bound than the simplified c^{-(n-1)} lambda_n(c)^n bound in the assigned record. The assigned theorem is thus mechanically contained in the earlier proof despite the weaker hypothesis not being named in its statement.

### Equivalent formulations
The assigned hypothesis is the load-bearing subfamily already sufficient for the earlier proof.

### Broader coverage
The earlier proof dominates the final assigned conclusion once its actually used hypothesis is stated explicitly.

### Exact database or table
The implication from the full earlier proof is decisive regardless of exact-title database hits.

### Claim versus prior implication
The assigned result is a direct corollary of the published proof, not merely similar in topic.

## Value
**FAIL** — Because the earlier published proof already works verbatim with the restricted test constant and yields at least as strong a quantitative conclusion, this record adds only a repackaging of which hypothesis the existing proof actually uses, plus a weaker simplification of the bound. That does not constitute an independently worthwhile new stability theorem under the stated value bar.

## Source inspections
- **Explicit Banach--Mazur stability from the Bézout mixed-volume coefficient** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-bezout-coefficient-banach-mazur-stability--fed154962a93): complete RESULT.md, especially longest-chord and difference-body Steps 2-3 Assessment: PRIOR_PROOF_MECHANICALLY_COVERS_ASSIGNED_RESTRICTED_TEST_RESULT. Evidence: The proof invokes the Bezout inequality only for K^s and [0,v] before applying the same Rogers-Shephard stability theorem.
- **The Bézout inequality for mixed volumes characterizes simplices** (https://arxiv.org/abs/2609.20380): primary abstract; arXiv HTML and authorized full-text retrieval failed to produce a verified PDF Assessment: PRIMARY_CONTEXT_WITH_ACCESS_LIMITATION. Evidence: The abstract states the all-dimensional characterization and longest-chord/relative-inradius characterizations.

## Residual risks
- No correctness defect is asserted; rejection rests on prior-proof implication.
- The primary Langharst-Wang full text was not available in this run, but that does not affect the decisive September 18 published-proof comparison.
