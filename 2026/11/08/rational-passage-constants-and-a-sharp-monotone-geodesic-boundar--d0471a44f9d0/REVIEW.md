# Scientific review

## Correctness

PASS. The complete-graph geometry is reduced to increasing paths by a valid local-extremum shortcut when all weights belong to \([a,2a]\). The exact four-state increment transition matrix and its invariant vector follow from independent entering-edge pairs. The fixed-parameter finite-state ergodic theorem and Poisson-equation martingale CLT yield the stated speed, variance and normal limit. `verify.py` confirms the displayed rational identities by exact symbolic algebra and tests the path recursion against an independent shortest-path algorithm. The scope excludes parameter sequences and weight ratios above two.

## Originality

PASS within the consulted published record, with residual historical risk. Dey–Kim prove non-explicit general microscopic time-constant and CLT statements for the same underlying spread-out line graph, but the exact two-point drift and asymptotic variance are not supplied in the inspected results. Ahlberg gives broad one-dimensional theory; Schlemm and Flaxman–Gamarnik–Sorkin study a different (three-degree) ladder, the latter already providing rational Bernoulli speeds. A targeted search of mathematical records and existing claims did not recover the four-state reduction or displayed two rational invariants for the second power of the integer line. The ladder paper's full text was not obtained, and an implicit reduction or unindexed exact formula cannot be ruled out solely by negative searches.

## Mathematical value

PASS. The explicit time constant and fluctuation variance are central, model-defining invariants for the fixed-range FPP family, not an arbitrary finite statistic. Their rational dependence on the Bernoulli parameter supplies precise quantitative transport information where the motivating 2026 general limit theorem supplies existence and implicit regenerative formulas. The sharp support-ratio bound clarifies exactly when genuinely undirected geodesics reduce to a simple one-sided recursion; this is why these constants become tractable. The result is a specialized, self-contained exact determination, not a new general FPP universality theorem.

Self-review: passed. Independent audit: not yet performed.
