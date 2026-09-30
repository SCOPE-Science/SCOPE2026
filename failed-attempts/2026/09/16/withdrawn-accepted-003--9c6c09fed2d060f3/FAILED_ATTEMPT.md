# FAILED ATTEMPT — NOT A VALIDATED FINDING

## Claimed goal

The package attempted to solve Argyros–Beanland–Motakis Problem 2(iii): prove that on the dual \(X_{0,1}^{n*}\), every product of \(n+1\) strictly singular operators is compact.

## Fatal gap

The proof reduces the problem to a proposed general lemma:

> If X is reflexive with an unconditional basis and T* is strictly singular, then T is strictly singular.

The contrapositive argument assumes that from a subspace on which T is bounded below one can pass, by gliding hump and small perturbation, to block subspaces \(E''\) and \(F''=T(E'')\) that are both complemented. The draft states that block subspaces of an unconditional basis are complemented. That assertion is false in general. An unconditional ambient basis makes coordinate subspaces complemented; it does not supply bounded projections onto arbitrary block-subspace spans.

The missing projection is essential. Without a bounded projection \(Q:X\to F''\), the identity
\[
A_0^*=i_{E''}^*T^*Q^*
\]
used to obtain a lower bound for \(T^*\) on \(Q^*(F''^*)\) is unavailable.

## Why this is exactly the known obstacle

The original ABM paper itself leaves the dual statement as Problem 2(iii) and observes that an affirmative answer would follow if every subspace of \(X_{0,1}^n\) contained a further subspace complemented in \(X_{0,1}^n\), adding that this “seems possible.” In other words, the filed proof assumes the very extra complementation phenomenon that the source identified as unproved.

## What remains potentially useful

The adjoint-order bookkeeping and Schauder compactness step are fine **conditional on** a valid mechanism proving that each preadjoint \(T_i\) is strictly singular. A future attempt would need either:

1. a theorem establishing the required hereditary complemented-subspace property for \(X_{0,1}^n\), or
2. a different dual-ideal argument specific to these spaces that avoids complementing the image of a block sequence.

Until such an input is supplied, the affirmative solution is not proved.

## Audit disposition

Relocate the complete package to the designated failed-attempt path and preserve the draft as a documented failed route. Do not state that ABM Problem 2(iii) has been solved.
