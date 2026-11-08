# Scientific review: cross-polytope affine projection and cube duality gap

## Correctness — PASS

For normalized real volume measure on the cross-polytope, sign/permutation symmetry and a beta marginal give covariance \(2I_d/((d+1)(d+2))\). Thus the affine \(L^2\) projector kernel is exactly \(1+\frac{(d+1)(d+2)}2 x\cdot y\). Convexity reduces the norm to vertices, and a positive-measure sign-disagreement argument makes the reduction strict at every nonvertex. The beta integral evaluates the sharp norm and the negative kernel mass. A differential inequality shows strict dimension growth; a Taylor expansion gives the asymptotic. For the cube comparison, the Cauchy--Schwarz bound handles all \(d\ge8\); an exact Irwin--Hall rational calculation handles \(d\le7\). The adjacent reproducibility script independently checks both families of formulas and the exact positive gaps in the finite base range. No claim of proving infinitely many cases by enumeration is made.

## Originality — PASS, qualified

Hangelbroek–Narcowich–Sun–Ward (arXiv:1005.2424, Introduction, Section 4 and Theorem 5.1) give \(L^\infty\) stability bounds for least-squares projections in localized kernel spaces on manifolds, not exact continuous-volume affine cross-polytope norms. Białas-Cież–Kenne–Sommariva–Vianello (arXiv:2311.18656, Introduction and relevant portions of Sections 2 and 3) construct polynomial-mesh procedures for estimating Lebesgue constants on cubes, simplices and Euclidean balls, but do not supply the new identity or duality comparison. Available related mathematical claims cover cubes, simplices, isotropic constants or nearest-point metric projections and do not imply the specified projector formula. The cross-polytope is not an affine image of a cube when \(d\ge3\). Search and comparison cannot exclude unindexed equivalent calculations; no priority beyond accessible evidence is claimed.

## Mathematical value — PASS

The sharp Lebesgue constant measures worst-case uniform amplification and directly controls near-best approximation bounds. The exact all-dimensional \(\ell_1\)-ball constant, exclusive vertex normers and sharp positivity defect completely resolve a canonical volume-orthogonal affine projection problem. The strict comparison with the polar cube for every \(d\ge3\), and the linear-versus-square-root growth contrast, are structural and dimension-uniform rather than an isolated numerical benchmark. The proof's finite-versus-infinite split provides an explicit explanation of why the gap holds throughout all dimensions.

## Closest literature and scientific limitations

Sources: arXiv:1005.2424 (2010-05-13); arXiv:2311.18656 (2023-11-30). Related exact claims for cube and simplex projectors concern different domains and cannot be transferred to the full cross-polytope by affine equivalence or per-simplex localization. Searches do not constitute mathematical proof of novelty. This result is for real coefficients, normalized continuous volume, degree-one polynomials and this specific dual pair; it does not compare all polar bodies, all Hanner polytopes or arbitrary measures.

Self-review: passed. Independent audit: not yet performed.
