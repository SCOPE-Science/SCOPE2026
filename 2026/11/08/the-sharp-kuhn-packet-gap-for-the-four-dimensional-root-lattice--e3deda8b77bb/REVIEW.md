# Scientific review

## Correctness (PASS)

The result concerns the original common-frame definition: a single ordered independent lattice frame generates all 24 permutation simplices, and each simplex may have its own translate of the radius ball. For arbitrary points, the parity-aware nearest-integer argument establishes the exact ordinary covering radius one. For every independent frame, the diameter of a permutation simplex bounds each nonempty subset sum by twice the fitting radius. Squared norms in \(D_4\) are even, so any hypothetical radius strictly less than \(\sqrt{3/2}\) forces all generators and nonempty subset sums to have squared norms at most four. The 48-vector search enumerates **all** such independent candidate frames; exact Gram determinants and complete branching leave zero candidates at rank four. For the matching explicit basis, determinant two and all 24 midpoint-ball inequalities have been checked with integers. This proves matching bounds without extrapolation beyond the enumerated finite reduction.

The only computation-dependent lemma is the complete finite count \((1,48,816,1728,0)\); its verifier is standalone, deterministic, and standard-library-only. A complete list of independently replayable upper-bound midpoint witnesses is given in the result itself.

## Originality (PASS, provisional)

Xue, arXiv:2610.39034v1, Section 1, defines the invariant; Section 2 establishes general comparisons; Section 5 uses subset-sum diameter bounds to exhibit an asymptotic \(\sqrt d\) gap; Section 6 proves equality for a *relaxed* triangulation invariant on ellipsoids. The paper's specific general statements do not imply the exact \(D_4\) value or provide a \(D_4\) optimal packet. The dimension-four calculation, sharp 48-vector obstruction, and 24-ball basis certificate are additional. The older Lian--Xue paper treats Kuhn triangulation and a three-dimensional criterion, but only its abstract and references were accessible for this comparison; this is a historical-priority risk. Nebe--Sloane's D4 catalogue gives standard lattice facts, not the new packet optimization. The closest mathematical-record search matches concerning a D4 root 24-cell address lattice completeness and reduction, not the present packet invariant. No claim is made that absence from a search proves absolute novelty.

## Mathematical value (PASS)

The source explicitly asks how costly one common Kuhn frame is compared with ordinary lattice covering, and obtains the gap only asymptotically over high-dimensional unspecified lattices. An exact, well-known, highly symmetric low-dimensional lattice gives an interpretable strict gap of \(\sqrt{3/2}\), separating the original invariant from the relaxed version at a natural object. The strong all-frame subset-sum obstruction is useful for future exact searches on root lattices and distinguishes genuine packet geometry from classical Voronoi covering geometry. The result is a complete exact natural-instance computation, not an arbitrary parameter slice or routine substitution.

## Limits and nearest literature

The result does not compute all projection-indexed minima, characterize every optimal frame, or settle the optimal ratio over all four-dimensional lattices. Its finite search is an exact exhaustive certificate under a proved reduction, not a symbolic classification of all Euclidean frames. Priority remains provisional and independent review remains unperformed.

Self-review: passed. Independent audit: not yet performed.
