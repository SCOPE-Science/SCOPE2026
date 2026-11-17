# Review — Delayed complete-Pick failure in two-root fractional Schur products

## Correctness (PASS)

The domain is the open unit disk, with fixed \(0<a<1\), \(0<b<1\). The factors are complete Pick by positive-coefficient feature representations; the first factor makes the product radial kernel irreducible with strictly positive coefficients. The normalized complete-Pick criterion reduces the decision to the coefficients of \(1-(1-t)^a(1-t^2)^b\). The nonstandard step is uniform transfer from the two fixed unit-circle singularities \(t=1,-1\), including a factor \(b\) in the remainder from \(t=-1\). The argument explicitly derives this factor from reciprocal-Gamma zeros, supplies both error exponents, and handles the potential integer exponent at \(t=1\) in the fixed-parameter assertion. Taking \(bn^a\to x\) proves the signed parity limit; a small-index compactness argument and uniform tail margin prove the first-negative-index equivalent. The Hardy endpoint is separately checked by a three-term expansion. The extracted exact-arithmetic checker passes 2,551 checks and is not confused with proof of the infinite statement.

## Originality (PASS, best-knowledge)

The primary 2026-05-20 source's Section 3 characterizes multiplicative functionals for Schur products of two complete Pick kernels (Theorem 3.2); it does not determine whether the products are themselves complete Pick, nor a first negative reciprocal coefficient. The 2018 factorization literature supplies function-space structure rather than a finite-test obstruction scale. The close public monomial-defect classification is for \((1-st^m)(1-t)^{-\gamma}\); a separate inspected historical claim is for a finite rational pole \([(1-t)^a(1-\tau t^m)]^{-1}\) and has a positive small-amplitude complete-Pick interval. Neither contains the present fractional branch point at \(t=-1\), and neither implies the \(b^{-1/a}\) delayed detection law. Exact-formula and equivalent-asymptotic searches of indexed sources and primary literature produced no covering statement. Residual risk: the coefficient asymptotics may have appeared in older unindexed analytic-combinatorics or kernel sources; search noncoverage is not proof of universal priority.

## Mathematical value (PASS)

This addresses a natural obstruction to permanence of complete Pick interpolation under Schur products, precisely the class singled out in the 2026 motivating paper. It goes beyond the elementary qualitative failure: every fixed finite Pick-coefficient check is eventually inconclusive at small perturbation, and the theorem computes the sharp polynomial degree of the first witness, including its constant and parity profile. The contrast with positive stability for small finite monomial poles identifies the mathematically responsible change: a new singularity exactly on the boundary. The problem's object and invariant are canonical, not an arbitrary finite instance or unsupported downstream application.

## Closest literature and limitations

Bhattacharyya–Jaikishan–Kumar (arXiv:2605.21808v1), Section 3, is the most relevant motivating primary text. Aleman–Hartz–McCarthy–Richter (2018) provides complete-Pick factorization background. Agler–McCarthy (2000) supplies the established coefficient criterion. The published monomial-defect classification is a close but non-dominating explicit specialization in a different family. No uniform claim at the endpoint \(a\to1\) is made, and the exact finite first-negative index is not closed-form. There has been no independent verification or universal priority proof.

Self-review: passed. Independent audit: not yet performed.
