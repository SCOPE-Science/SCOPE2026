# Scientific review: fixed-rank Volterra singular-value hierarchy

## Correctness

**PASS.** The claim fixes the singular-value rank before taking the large integration-order limit. The factorial normalization and the output/input coordinate Jacobians are explicit, leaving the self-adjoint Hankel kernel (3). On the ordered exterior-power domain its kernel is the determinant without an extraneous factorial. The mixed analytic coefficient argument identifies the Vandermonde leading term, and the exponential-tail bound promotes local convergence to Hilbert–Schmidt convergence. Andréief's identity and scaled Laguerre monic norms give the exact coefficient. Dividing consecutive exterior norms is valid because their positive limiting constants are nonzero. Exact-rational moment determinant tests and finite Nyström diagnostics support, but do not substitute for, those steps. No variable-rank conclusion is claimed.

## Originality

**PASS, with historical-priority qualification.** Eveson's 2003/2004 full texts address leading rank-one behavior; Ransford–Walsh (2022) addresses polynomial norms. The closest published finding, *Sharp second singular asymptotics and rank-two collapse for high Volterra powers*, proves the second-rank coefficient and only a rank-two Hilbert–Schmidt approximation bound; its published limitations explicitly leave the third and later fixed-rank constants uncomputed. This finding makes the new assertion only for the exact coefficients at every fixed rank at least three, which are neither stated nor implied by that upper-bound result. Fixed-order high-index Weyl estimates are not the same asymptotic regime. The 2001 Dostanić article was available only as an abstract; equivalence to unindexed historical results remains a residual risk.

## Mathematical value

**PASS.** Sharp approximation numbers of powers of Volterra integration are natural conditioning and low-rank approximation invariants. The known first two ranks leave open how rapidly every further optimal approximation rank collapses. The exact hierarchy gives the first sharp third-rank coefficient and all successive factorial constants, revealing a nontrivial exterior-power/Laguerre structure rather than a routine numerical improvement or arbitrary parameter slice. It answers a coherent family of rank-approximation questions in one theorem.

## Scientific limitations

No estimates uniform in ranks increasing with order, no exact finite-order singular spectrum, and no independently conducted audit. A historical source unavailable in full remains a bibliographic-priority qualification.

Self-review: passed. Independent audit: not yet performed.
