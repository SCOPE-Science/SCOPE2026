# Independent mathematical audit — SCOPE-20260919-9406e4d724a9

Final disposition: **FAILED**.

## Correctness
**PASS** — For the symmetric normalized body, the Mielke-Sulz profile inequality gives the full profile moment and their mixed identity gives the first moment. Dividing the projection-volume inequality by the volume term therefore yields exactly the normalized moment ratio. Writing that ratio as an order-\(n-1\) Rényi divergence is algebraically correct; the Blaschke factorization for nonsymmetric bodies, Rényi monotonicity, the variance identity, Pinsker bound, and the cylinder calculation are also correct.

## Originality
**FAIL** — The central theorem is mechanically implied by the primary proof already published by Mielke-Sulz. Their profile functional inequality and mixed identity combine to give exactly \(Q(K)/Q(B)\ge \mathbb E[X^{n-1}]/(\mathbb E X)^{n-1}\); normalizing \(Y=X/\mathbb E X\) and naming \(\log \mathbb E[Y^{n-1}]/(n-2)\) a Rényi divergence is a change of notation. The lower-order divergence, variance, and total-variation statements then follow from standard monotonicity, the \(D_2\) identity, and Pinsker. The cylinder equality is a correct direct substitution but does not make the composite stability theorem original.

### Equivalent formulations
The claimed deficit is the same inequality expressed in normalized-probability notation, not a distinct implication.

### Broader coverage
The source machinery dominates the main claim even though it does not use the words Rényi, variance, or Pinsker.

### Exact database or table
Specific inapplicability: the decisive comparison is theorem implication, not a finite computed invariant.

### Claim versus prior implication
The primary source mechanically implies the headline theorem.

## Value
**FAIL** — Because the advertised quantitative stability mechanism is already encoded explicitly in the source moment inequality and mixed identity, the final package is primarily a repackaging with standard information-theoretic inequalities. The cylinder check is useful exposition but is too small and mechanically attached to rescue the package as a separate mathematical contribution.

## Source inspections
- **The Petty Conjecture for Convex Bodies of Revolution** (https://arxiv.org/abs/2609.13517): complete 21-page primary preprint, including the profile-transform definition, the multilinear estimate, the mixed identity, and the Hölder step on the proof pages Assessment: STRONGER_PRIMARY_IMPLICATION. Evidence: The displayed profile functional and mixed identity give the normalized high-moment ratio used verbatim by the assigned proof.

## Residual risks
- The cylinder equality appears to be an extra direct computation rather than a statement highlighted in the source, but it does not overcome coverage of the central theorem.
- No correctness defect is asserted.
