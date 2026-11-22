# Scientific review: finite-time zero dichotomy for inverse-age quantum resetting

## Correctness — PASS

The exact age distribution follows from renewal generating functions and equals the beta-binomial polynomial. Differentiating its generating function gives a three-term recurrence. On the unit circle, a symmetric Jacobi tridiagonal matrix plus a strictly sign-definite imaginary diagonal yields a nonvanishing determinant whenever the reset strength differs from one half. Continuous polynomial-root motion and reciprocal symmetry rigorously place every root inside or outside; the balanced case reduces to the standard Legendre recurrence. Crucial scope restrictions include strictly positive complementary shape parameters and the exact inverse-age hazard. A separately implemented finite checker passed 835 exact-rational or numerical assertions; the infinite claim rests on the determinant argument, not those tests.

## Originality — PASS, with a bounded literature risk

The 2024-10-15 primary preprint by Wald and collaborators provides the reset dynamics, exact age recursion and inverse-age hazard but not finite-horizon coherence zero locations. The previously published Legendre entanglement-node result fully covers the balanced case, which is **not** claimed as new. The previously published half-index quantum coherence result establishes asymptotic modes for a distinct survival clock; it does not imply the all-finite-degree root dichotomy. An asymmetric continuous Beta Fourier transform is known to have no real zeros, but this is a different analytic transform; its limit does not certify finite-polynomial zero avoidance. Searches for beta-binomial generating-function zeros, Jacobi or Legendre zero equivalences, and quantum-reset finite-time cancellation did not uncover an explicit stronger statement. Residual risk: classical special-function literature or unindexed discrete beta-binomial polynomial theorems could contain an equivalent root-location classification. No claim of definitive global novelty is made.

## Mathematical value — PASS

The statement is a complete sharp, all-degree phase classification of a physically measurable cancellation phenomenon, not a particular numerical example. Exactly balancing the two renewal exponents permits isolated *exact* finite-time coherence cancellations, while any asymmetric perturbation forbids them at every gate phase and every positive integer time. The inside/outside root migration is a structural stability boundary not deducible from the known balanced Legendre formula or large-time coherence decay alone. The determinant proof identifies a positive-definite mechanism relevant to spectral analysis of renewal coherences. Neither a general downstream theorem nor an arbitrary invariant is needed for this precise natural observable.

## Literature comparison and limitations

Primary material inspected: Wald et al., arXiv:2410.11497, sections 2, 4, and appendix, https://ar5iv.labs.arxiv.org/html/2410.11497 . Full published RESULT.md files inspected: *Exact Legendre entanglement nodes and Bessel scaling under a critical discrete reset clock*; *Half-index interference threshold for coherence under infinite-mean renewal resetting of a quantum gate*; *Phase rigidity and complex-zero escape for asymmetric Beta Fourier transforms*. The theorem is limited to one fixed phase gate, a full coherent reset and the inverse-age hazard. The 835 finite checks are not an infinite proof. The root-dichotomy priority comparison remains subject to unindexed prior literature.

Self-review: passed. Independent audit: not yet performed.
