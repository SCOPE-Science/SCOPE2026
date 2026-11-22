# Self-review of common terminal-sibling persistence

## Correctness — PASS

The two-tree coupled parent kernel is explicit, and the exact probability of simultaneous parent equality at birth labels \(i<j\) is a finite sum over matching diagonal and off-diagonal parent pairs. Independent intermediate and later attachment avoidance yields exact products. The universal bound \(U_{ij}V_j\le (i-1)(j-1)/((n-1)(n-2))\) controls the triangular Riemann sums, including the vanishing-copying regime and the bounded different-parent law. The packaged `verify.py` independently exhausts small paired recursive trees and passes 78 grouped assertions. No finite enumeration is substituted for an infinite proof.

## Originality — PASS, with residual priority uncertainty

The closest prior literature includes Janson's one-tree degree-count laws, Gopaladesikan–Mahmoud–Ward's one-tree fringe-motif work, and Bäumler–Rácz–Ross–Sridhar's correlated attachment model. Public one-tree terminal-sibling results already imply the exact zero- and full-coupling endpoints; those endpoints are credited rather than treated as novel. A published full degree-profile cross-tree covariance kernel in the same coupling was read and does not record label-pair sibling intersections, so it does not imply the new kernel or crossover. The original 2026 correlated-tree paper's full text and a 2013 primary motif text were not fully inspectable here; an unlocated stronger pair-motif theorem could imply the result. This is best-knowledge originality, not independent priority certification.

## Value — PASS

A correlated pair of growing trees can have a linear expected number of identical terminal-sibling label pairs even though its expected pairs with *different* parent labels stay bounded. As copying decreases, the expected shared-pair count changes from the independent accidental baseline \(1/12\) at the sharp \(n^{-1/2}\) mean crossover. These are structural motif-level facts not conveyed by individual tree degree counts, and address persistence of local genealogical information under noisy copying. They do not, by themselves, establish a hypothesis-testing threshold or distributional convergence.

## Sources and limitations

See `RESULT.md` references and the structured comparison in `AUDIT.json` for primary-source and public prior-result IDs, actual query terms, broader-coverage comparisons, material inspected and residual access risks. Exact formulas are restricted to uniform parent choices and aligned birth labels; the asymptotic claims are for expectations only.

Self-review: passed. Independent audit: not yet performed.
