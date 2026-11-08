# Scientific review: contact-refined cusp and fat-line Hilbert series

## Correctness — PASS

The statement is in \(K_0(\operatorname{Var}_k)[z][[Q]]\), for arbitrary fields \(k\) and all \(u,n,j\ge0\). The proof uses the exact inclusion \(t^{d+2}k[[t]]\subset I\) for any cusp ideal whose least valuation is \(d\), giving a uniform projective-line classification of reduced punctual Hilbert loci in every colength at least two. Direct reduction modulo \(x=t^2\) yields the two affine-line contact-one strata at colength two and three and the stable contact-two locus from colength four onward. The resulting \(G_g^x\) specializes to the independently published unrefined cusp Hilbert zeta function. The full fat-branch formula is then an exact application of Corollary 6.8 of arXiv:2610.34676v1, not an extrapolation from examples. Independent row-echelon enumerations over two finite fields confirm the first four colengths and the initial plane agreement for one attached branch. They are checks, not substitutes for the complete proof.

## Originality — PASS (best-knowledge, not priority certification)

The 2026 motivating paper, Section 6.4 and Question 11.4, specifically asks for contact-refined input for unibranch singularities, including \(y^p=x^q\). It proves the general substitution formula for adding a fat branch but neither states the explicit cusp contact coefficients nor this instantiated family. The closely related 2023 paper (arXiv:2305.06411), Section 7.2, supplies only the contact-forgetting identity \((1+\mathbb LQ^2)/(1-Q)\); that identity does not determine the contact statistic, and substituting it alone cannot determine the family with attached fat line. General reduced-curve rationality theorems give neither coefficients nor contact refinements. Searches for the cusp formula, equivalent \(A_2\) presentations, added-branch equivalents, and prior exact claims found no stronger statement that implies the entire claim. Uninspected implicit consequences of older semigroup or knot-homology work remain a residual historical-priority risk.

## Mathematical value — PASS

The explicit \(A_2\) cusp is the first singular unibranch instance of the concrete computation requested in Question 11.4. The answer identifies both exceptional low-colength contact strata, their dimensions, and the stable stratum, providing the missing input needed for a closed rational series for every multiplicity \(u\) of the added branch. This is an infinite, naturally defined, nonreduced curve family, with all contacts and lengths determined rather than a one-off exercise or numerical sample. The previously known unrefined cusp series alone cannot recover these data.

## Closest sources and limitations

Huang--Jiang--Oblomkov, *Sheaves on nodal singularities I*, arXiv:2610.34676v1, Sections 4, 6.4, 11.2; Huang--Jiang, *Punctual Quot schemes and Cohen--Lenstra series of the cusp singularity*, arXiv:2305.06411, Section 7.2; Bejleri--Ranganathan--Vakil, *Motivic Hilbert zeta functions of curves are rational* (2020). Scope is punctual motives of the specific cusp and its fat-line additions, not all unibranch germs, independently thickened tangent branches, full Hilbert scheme structures, or independent validation. External historical coverage cannot be exhaustively excluded.

Self-review: passed. Independent audit: not yet performed.
