# Self-review

## Correctness — PASS
The graph Laplacian is explicitly diagonalized into constant, within-part, and block-constant eigenspaces with exact projection weights. The resolvent diagonals have a sign-definite difference formula ordered by part size; the smallest diagonal has one quadratic positive zero. Positivity off diagonal follows from the inverse of the irreducible M-matrix. Two symbolic identities and 1,230 exact full-matrix checks over 246 profiles were replayed; finite tests do not prove the all-size statement.

## Originality — PASS, bounded published comparison
The 2014 invariance-threshold paper gives broad rational-method sufficient bounds, not a complete-multipartite closed classification. The published general reversible Crank–Nicolson resolvent-return criterion supplies prior matrix identities and spectral crossing facts, but does not evaluate multipartite diagonal weights, prove the sharp minimum-part selector, the partition-independent two-parameter threshold, or fixed-order extremal characterization. Extensive analogous searches in published-finding corpus and literature found no dominating explicit classification; the possibility of unindexed specialist results remains.

The closest publication is [A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains](https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a), which already supplies the general Cayley/resolvent diagonal criterion and the complete-graph threshold. The 2014 Horváth–Song–Terlaky paper provides the broader rational-discretization framework. The present finding claims only the explicit complete-multipartite threshold, critical-size ordering, and sharp partition-extremal law. The risk of unindexed overlapping formulae is real.

## Mathematical value — PASS
The exact full classification replaces graph-size matrix resolvent tests by a closed quadratic in total order and minimum part size for arbitrarily many unequal parts. It identifies which vertices lose positivity, proves strict no-recovery, and characterizes sharp extremizers under fixed graph order and part count. These are motivated natural parameter effects for positivity-preserving implicit graph heat timestepping, not a chosen finite table.

## Scientific limitations
Finite exact checks are supplementary to a symbolic proof. The scope excludes weighted graphs and solver-stage nonnegativity. Specialist literature priority and independent validation remain unresolved.

Self-review: passed. Independent audit: not yet performed.
