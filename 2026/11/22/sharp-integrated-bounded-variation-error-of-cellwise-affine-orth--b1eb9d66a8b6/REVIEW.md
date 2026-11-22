# Review of the affine-projection integrated BV error law

## Correctness — PASS
The local operator is defined by the two exact \(L^2\) moment equations and acts on one-dimensional \(BV\) functions because they admit bounded representatives modulo constants. For a one-sided jump \(H_t\), its local projection is \(g_t(x)=1-t+6t(1-t)(x-1/2)\). Direct integration with the correct sign-change intervals gives the two rational branches (1) and (2) in `RESULT.md`. The first derivative has precisely one zero on \((0,1/3)\), because its cubic factor increases through zero; the second branch decreases strictly via the negative polynomial \(Q\). Reflection yields only two maximizing jump fractions. A signed-measure step representation and the triangle inequality extend the bound to all real distributional BV functions; a unit step on a longest cell attains the coefficient. The included rational checker passed all identity and finite-superposition checks. These tests supplement, but do not replace, the complete analytic argument.

## Originality — PASS, with residual historical risk
The actual prior comparisons are statements, not titles. The 2011 Angermann–Henke preprint, relevant Section 3, defines local \(L^2\) projection and estimates errors under Sobolev–Slobodecki smoothness assumptions, but does not in the inspected result state the exact \(BV\)-to-\(L^1\) norm of \(I-P\) or location of worst jumps. The 2012 Kristensen–Rindler preprint proves adaptive piecewise-affine approximation and strict approximation in BV rather than a fixed orthogonal projection's optimal integral error. A separately recorded exact result for this same cellwise projector concerns \(\operatorname{Var}(Pf)\), not \(\|f-Pf\|_1\); its cell-count-dependent coefficients do not imply the present cell-length law. Other exact results on Sobolev widths and \(L^\infty\) norms of continuous spline projectors concern different maps and domains. The scoped mathematical-search and full-text comparisons did not establish a prior implication, but historical priority has not been exhaustively certified.

## Value — PASS
The \(BV\to L^1\) norm of \(I-P\) is a natural, concrete shock/error calibration when cellwise local polynomial projection is used on possibly discontinuous signals. The finding determines a sharp *all-mesh* coefficient rather than a generic regularity-dependent inequality, identifies two off-centre extremizing jump phases, and proves that only the longest cell controls the worst-case error. The phase location matters for grid alignment; the magnitude \(\kappa\approx0.2514977\) is about half the sharp \(1/2\) error coefficient of cellwise constant \(L^2\) projection. The answer is not a direct reformulation of a prior output-variation norm or a general Sobolev estimate.

## Sources and limits
- Angermann–Henke, arXiv:1102.3100, first version 2011-02-15, relevant local orthogonal projection definition and Section 3 projection estimates.
- Kristensen–Rindler, arXiv:1211.1792, first version 2012-11-08, relevant Theorem 1 and Introduction on BV approximation.
- A prior exact result on the same cellwise affine projector's total-variation amplification, with a different norm and a different mesh law, was compared specifically for implications.
- Residual risks: unindexed exact historical formulas; possible stronger estimates in uninspected specialist sources; extension beyond unweighted one-dimensional degree one not established.

Self-review: passed. Independent audit: not yet performed.
