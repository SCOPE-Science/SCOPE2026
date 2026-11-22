# Scientific review: universal affine gap profiles

## Correctness — PASS

The quotient is integral for coprime multipliers because primitive roots are permuted. Exact coefficient extraction yields \(\varphi(m)\) periodic words, and their nonvanishing follows from the minimal polynomial of a primitive root. Period insertion adds a whole cyclic gap histogram to each block; the sole short final-block case is explicitly resolved using reciprocity and the leading coefficient of the inverse cyclotomic polynomial. A separate truncation argument proves the sharp gap bound \(\varphi(m)\). The verifier reproduces 631 distinct quotient instances by direct integer polynomial division and confirms the stated tables. Finite tests do not prove the infinite theorem; the written lemmas do.

## Originality — PASS (qualified)

Cafure–Cesaratto's binary second-gap results and restricted full distributions do not cover arbitrary fixed moduli or composite substitution quotients. Al-Kateeb–Dagher's general prime-parameter block and linear Hamming-weight results imply total support sizes, not length-by-length gap counts. Benoist–Perucca's ternary coefficient patterns and \(\Phi_{15p}\) tables make the finite example computationally accessible, and Zheng's general maximum-gap theorem controls only the extremal length; neither inspected work states the universal affine full-gap law. A significant residual risk is that the law might be implicit in earlier block formulas or appear without this terminology elsewhere. The contribution is the uniform cyclic-gap aggregation theorem including the composite quotient, not re-discovery of the coefficient formula or maximum-gap count.

## Mathematical value — PASS

A full gap histogram is a natural refinement of both the Hamming-weight statistic and maximum-gap studies. The theorem gives every length's exact frequency with only finite computations at one representative per residue class, for arbitrary cyclotomic modulus, and proves the all-length affine structure and sharp degree-mass identity. The extension from prime to composite multipliers addresses the natural integral substitution quotient rather than a contrived restricted sample. The \(m=15\) second-gap four-case law illustrates information absent from one-point sparsity and extremal-gap counts.

## Limitations and nearest literature

The theorem is restricted to coprime multipliers greater than the modulus. The prior block formulas determine all coefficients and are powerful antecedents, so an equivalent earlier aggregation is a priority risk; a full independent literature review remains outstanding. No general analytic formula simplifies the coefficient profiles uniformly over all moduli. Relevant primary texts are the four items in RESULT.md; the author preprint of Benoist–Perucca was materially read for its introduction, maximum-gap argument and \(\Phi_{15p}\) tables.

Self-review: passed. Independent audit: not yet performed.
