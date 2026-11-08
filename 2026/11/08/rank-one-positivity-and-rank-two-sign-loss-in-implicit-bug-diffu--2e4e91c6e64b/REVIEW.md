# Scientific assessment: implicit BUG graph-diffusion positivity

## Correctness — PASS

The claim has two separately checked parts. The universal rank-one proof reduces both subspace solves to resolvents of irreducible nonsingular \(M\)-matrices, then proves positivity of the projected scalar and its denominator for every positive timestep. The rank-two counterexample is specified by integer generator and factor matrices; its exact Galerkin K/L/S systems are solved over rational numbers by `verify.py`. The strictly negative third diagonal entry is enclosed between \(-9/100\) and \(-8/100\), while the exact full-rank backward-Euler solution is strictly positive. The Galerkin equations are basis invariant, so using unnormalized rational bases does not change the QR-based algorithm. Finite numerical demonstrations have not been substituted for an infinite-domain argument.

## Originality — PASS, with residual priority risk

The nearest primary article, Saha–Yang–Yin, arXiv:2610.18419, establishes the implicit BUG equations and \(L^2\)-stability, but not a componentwise positivity classification. Relevant prior literature discusses general positivity correction, often after SVD truncation, which does not imply this exact untruncated rank-one/rank-two boundary. Searches for the claim, its graph-diffusion and \(M\)-matrix formulations, and rank-two sign loss in published mathematical records found no implication-equivalent or dominating result. Novelty is a best-knowledge assessment, not a uniqueness certificate; older nonindexed or inaccessible full-text results remain possible.

## Value — PASS

Implicit matrix diffusion naturally preserves nonnegativity, and nonnegative concentrations are important in reaction–diffusion applications. Low-rank Galerkin methods do not automatically inherit that property. The two-part theorem identifies a guaranteed safe rank-one regime and proves that merely increasing retained rank to two can lose positivity even when no rank truncation occurs. This directly informs when additional positivity controls may be needed, separate from norm stability. The claim does not pretend to classify all higher ranks, all finite-element stiffness operators, or sharp step restrictions.

## Closest sources and limitations

- J. Saha, J. Yang, P. Yin, arXiv:2610.18419, original implicit BUG/KLS equations and well-posedness/energy stability. Full relevant HTML sections were examined.
- G. Ceruti, C. Lubich, arXiv:2010.02022, earlier forward-time BUG framework. Relevant full HTML sections inspected: its algorithm and exact-rank trajectory theorems do not imply sign preservation of the later implicit backward-Euler BUG substeps.
- K. Kormann, M. Nazarov, J. Wen, arXiv:2606.31662, low-rank positivity corrections for Vlasov systems. Available abstract and introductory excerpts examined.
- Y. Wu, S. Becker, J. Qiu, X. Zhang, arXiv:2607.26272, nonnegative correction for low-rank Vlasov simulations. Abstract and indexed excerpts inspected; full document inaccessible.

Self-review: passed. Independent audit: not yet performed.
