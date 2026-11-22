# Scientific review

## Correctness — PASS
The positive baseline and fixed budget imply positive definiteness and a compact feasible simplex. The Rayleigh-quotient argument proves that every asymmetric leaf allocation strictly worsens the bottom eigenvalue after symmetrization (with the top eigenvalue weakly worsening), so reducing to equal leaf loadings loses no optimizers. The full spectrum then separates into the \(m-1\) leaf-difference modes and the two quotient eigenvalues, which strictly straddle the former. Their ratio is minimized by a rational function whose derivative has exactly one real zero on the positive line. Clipping at the budget bound yields a unique global optimizer; the support boundary is the unique positive root of the displayed quadratic. Independently implemented rational and full-matrix checks passed 8,962 assertions. The finite checker is not offered as a proof of the universal claim.

## Originality — PASS, subject to publication-priority risk
Greif–Varah (2006) treat free low-rank perturbations, Lu–Pong (2011) provide general convex-program machinery for conditioning and a separate multiplicative diagonal preconditioning framework, and Kurras–von Luxburg–Blanchard (2014) treat a normalized graph-Laplacian construction. The inspected full texts contain no formula for the unique budgeted additive vertex loading of every unit star or its hub-activation threshold. Related archived spectral-gap and diagonal scaling records were compared by their mathematical hypotheses and conclusions, not just titles. Generic solvability as an SDP does not logically deliver the explicit optimizer, support threshold, or strict unrestricted uniqueness. Published and indexed coverage is not exhaustive; an unindexed equivalent specialization remains possible.

## Value — PASS
An exact fixed-cost diagonal stabilization rule for a class of ill-conditioned sparse SPD systems is a motivated numerical linear algebra design problem. The theorem resolves the whole star family, proves strong uniqueness without symmetry assumptions, and identifies the exact budget at which the hub activates. The location and existence of the threshold are not immediate from a generic conditioning SDP or from edge-conductance spectral-gap optimization; the result is useful as a structural benchmark for diagonal regularization methods.

## Scope and limits
All edge weights are one; \(m\ge2\), \(a>0\), and \(B\ge0\). The claim does not extend to all trees, arbitrary edge prices or other conditioning functionals. No exhaustive public-literature priority guarantee or independent proof audit is claimed.

Self-review: passed. Independent audit: not yet performed.
