# Scientific review: eight projective types of \(\mathbb F_2\)-smooth cubic nets

## Correctness — PASS

The finite claim has a closed and reproducible computation. For characteristic-two cubics, Euler's formula makes simultaneous vanishing of the three partial derivatives equivalent to singularity; exact Gröbner zero-dimensionality tests establish geometric smoothness, not merely smoothness over \(\mathbb F_2\). Exhaustive enumeration of all \(1023\) nonzero forms gives \(336\) smooth forms, then canonical coset extension enumerates \(5544\) two-dimensional vector subspaces and \(864\) three-dimensional vector subspaces whose nonzero forms are all smooth. All \(168\) invertible binary coordinate matrices are expanded on the ten cubic monomials. The resulting eight disjoint projective orbits have sizes \(8,8,8,168,168,168,168,168\), summing to \(864\). The standalone verifier, run on its packaged path, completed with `SMOOTH_NET_CLASSIFICATION_PASS 336 5544 864 8`. Independent bounded-field derivative scans match the singular-mask set, but the exact algebraic test supplies the geometric proof.

## Originality — PASS, with residual priority risk

The closest directly examined source is Asgarli–Ghioca–Reichstein's maximal smooth-family theorem, arXiv:2207.00918: it already proves that such nets **exist** and no dimension-greater-than-two projective smooth system exists. Neither point is newly claimed. The later Asgarli–Ghioca article arXiv:2407.18104 recalls that theorem and studies *geometric irreducibility*, a weaker property, in larger systems. Berg's characteristic-two enumerative paper concerns incidence characteristic numbers, not the exact number of smooth nets and their rational projective equivalence classes. Actual record searches for the 864 and eight orbit counts, binary smooth ternary cubic subspaces, and discriminant-avoiding nets located no dominating result. This is a best-knowledge self-review, not proof against all unindexed historical tables. Berg's later sections were not all read; see structured residual risks.

## Mathematical value — PASS

The complete classification addresses prevalence and symmetry types of *maximal* smooth linear systems in the smallest characteristic-two field, precisely the natural objects supplied by the motivating existence theorem. It distinguishes three high-symmetry classes with stabilizer \(21\) from five with trivial stabilizer and shows that some inequivalent nets share the seven-member rational-point profile. These invariants do not follow from the earlier existence or maximum-dimension statement. The conclusion is limited to one field and degree and does not extend to systems all of whose geometric members are smooth.

Self-review: passed. Independent audit: not yet performed.
