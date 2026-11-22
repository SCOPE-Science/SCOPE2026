# Review: three-scale optimal free-energy stability in the square-gap shift

## Correctness — PASS

The claimed constant is defined as a supremum over **all** invariant probability measures, including the zero fixed-point atom. Kac--Abramov inducing plus the one-coordinate entropy inequality produces the exact maximal-entropy envelope at fixed marker density. The pressure root, strict concavity, and Bregman identity reduce the problem to a one-dimensional quotient. The local coefficient is the exact inverse curvature of this envelope. The global maximizing-density concentration is proved uniformly, and its stationary-point equation forces an intermediate \(e^{-3L/2}\) scale. The second correction follows from the two shortest returns; long returns contribute smaller-order terms. The supplied numerical verifier reproduced pressure roots, the local variance and the scaled global stationary-point calculation, but infinite conclusions rely on the written analytic bounds.

## Originality — PASS within inspected evidence

The 2026 renewal-type effective intrinsic ergodicity theorem of Haydarov, Kadyrov, Makhmudov and Mamayusupov guarantees a square-root free-energy comparison with an unspecified potential-dependent constant; it does not optimize the constant for the marker observable or analyze strong marker penalties. The separately published square-gap theta-cubic calculation gives the maximum entropy at each fixed marker density and its near-zero expansion. That is a substantial prior ingredient, explicitly credited, but it does **not** state the present global-versus-local constant, the globally maximizing density's intermediate exponent, or the nonzero \(e^{-3L/2}/L^2\) sharp correction. The new work analyzes a global singular maximization problem across the entire entropy curve; merely repeating the known pressure and entropy equations is not asserted as novelty. Search coverage includes semantically similar terminology, generic pressure-gap estimates, and prior research ledgers. Remaining risks: unindexed optimal-constant literature and an unpublished equivalent saddle analysis.

## Value — PASS

The measured object is the *best possible coefficient* in a published quantitative uniqueness paradigm, for its simplest natural marker observable. The leading global bound differs by an exponential factor from its infinitesimal susceptibility; the maximizing densities occupy a third asymptotic scale, distinct from both the equilibrium marker density and the limiting periodic marker density. The explicit secondary term and extremizer location distinguish this calculation from a routine asymptotic of the previously known constrained entropy. This is a motivated sharp boundary of applicability, not an arbitrary parameter slice.

## Limitations

This review is internal-to-the-work scientific checking only. No independent proof certification has been performed. The theorem addresses one family of scalar observables; it neither provides a sharp all-observable Hölder constant nor proves finite-field uniqueness of the maximizing density. Historical priority is conditional on the inspected accessible sources.

Self-review: passed. Independent audit: not yet performed.
