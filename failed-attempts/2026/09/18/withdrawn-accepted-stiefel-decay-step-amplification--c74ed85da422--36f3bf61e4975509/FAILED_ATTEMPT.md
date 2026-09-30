# FAILED ATTEMPT — NOT A VALIDATED FINDING

**Record:** `2026/09/18/stiefel-decay-step-amplification--c74ed85da422`  
**Independent audit date:** 2026-09-29 (UTC)  
**Task:** `606a6b7728282fb3bda8cdcceb11ddb5`

This package is retained for provenance, but the independent audit does **not** validate it as a publishable research finding.

## Correct mathematics retained

PASS. For tangent Delta, the cross term in (aW+Delta)^T(aW+Delta) vanishes, giving a^2 I+Delta^T Delta, the singular-value formula, unconditional full rank, and the conditioning formula. Positive homogeneity of the polar factor for a>0 gives P(aW+Delta)=P(W+Delta/a), hence eta_eff=eta/(1-eta lambda) for a fused AdamW radial term. The trace calculation yields the chordal-displacement formula, and the graph decomposition Delta=WA+B gives the principal-angle statement. An independent random-matrix check reproduced these identities to floating-point roundoff.

## Decisive originality finding

FAIL under the independent-research bar. The exact Stiefel formula was not located verbatim, but the central claimed mechanism is the immediate specialization of two established facts: polar/normalization maps are positively homogeneous, and decoupled weight decay is multiplicative radial shrinkage. The broader phenomenon that weight decay on scale-invariant or normalized parameters acts through effective step/learning-rate changes has been explicit in the literature since at least van Laarhoven's normalization analysis and later work. Guerrero's motivating paper already foregrounds the complementary one-line Stiefel fact that radial weight decay has zero Riemannian gradient. The submitted eta/(1-eta lambda) identity therefore does not constitute a sufficiently independent new mechanism rather than a direct algebraic corollary of standard ingredients.

## Decisive scientific-value finding

FAIL AS A VALIDATED NEW RESEARCH CONTRIBUTION. The formulas are correct and useful as an implementation note warning that 'project then decay' and 'fuse decay then project' are different, but the principal theorem is obtained in one line from positive homogeneity, and the Gram, displacement, conditioning, and angle consequences are routine matrix-algebra elaborations. Existing normalized/scale-invariant optimization literature already treats weight decay primarily as an effective-learning-rate control. The package is therefore pedagogically useful but does not clear this audit's scientific-value threshold for a standalone finding.

## Preservation note

The complete original package should be relocated atomically to the assigned failed-attempt destination. No evidence file should be selectively deleted. A future submission would need a substantively stronger result beyond the direct positive-homogeneity/effective-step corollary to qualify as a new finding.
