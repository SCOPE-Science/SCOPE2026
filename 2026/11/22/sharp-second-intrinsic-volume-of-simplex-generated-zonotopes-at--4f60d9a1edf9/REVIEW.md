# Mathematical review

## Correctness — PASS

The proof first uses the published intrinsic-volume identity \(V_2(Z)=\sum_{i<j}\lVert p_i\wedge p_j\rVert\). Separating segment lengths from directions, weighted Cauchy–Schwarz gives \(S^2\le AB\). The exact length identity \(A=A_*-Q/2\) and trace-of-frame-operator identity \(B=B_*-E/2\) provide both sharp bounds. All constants and dimensions agree with regular-simplex equality; the equality classification follows from the rank-\(d\) Gram projection on \(d+1\) columns, rather than assuming equiangularity. The exact deficit identity and two coercive inequalities are checked algebraically. The verifier passed 11 rational/simplex checks and 900 independent random configurations, including degeneracies. The latter do not prove the general theorem.

## Originality — PASS (with residual priority risk)

The strongest directly relevant source, Joós–Lángi (arXiv:2206.03204), proves the equilateral case in Theorem 6 and asks the unrestricted case in Problem 3; neither their formulation nor their inspected proofs contain the weighted length/frame isotropy inequality. Brazitikos–McIntyre (arXiv:2102.05900) compares different normalizations and proves its \(p=1\) result for \(d\) vectors, not the sharp fixed-sum \(d+1\) case. Ivanov (arXiv:1804.10055) optimizes cube projections with a Parseval-frame condition, not arbitrary weighted generators at fixed mean width. Relevant results in the indexed research collection treat circumradius, inradius, volume fractions, or width variance; no implication to the present sharp \(V_2\) law was established. Exact/alias/stronger coverage searches are recorded in the structured audit. Unindexed equivalent work remains possible.

## Mathematical value — PASS

The result fills a specifically named gap in the geometry of zonotopes: the \(k=2\) instance of Joós–Lángi's fixed-mean-width Problem 3 in all \(d\ge3\). The unrestricted variation in generator lengths matters; the published theorem assumes equal lengths. The identity exhibits a structural and quantitative rigidity mechanism linking angular scatter, segment-length imbalance and the frame operator. No claim is made for other \(k\).

## Scope and outstanding limits

The result is a self-review only. The proof is self-contained conditional on the explicitly credited classical intrinsic-volume formula. The tests are finite corroboration. The originality review cannot exclude obscure equivalent statements, and no independent mathematical audit is available.

Self-review: passed. Independent audit: not yet performed.
