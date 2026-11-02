# Mathematical review

## Correctness
PASS. In the standard simplex-sum realization of the star graph associahedron, the total coordinate sum is \(M=2^n-1\). Every singleton facet has zero offset and projected normal norm \(\sqrt{n/(n+1)}\). Summing the singleton-ball constraints gives the globally sharp radius \(M/\sqrt{n(n+1)}\) and forces the unique uniform center. For every center-containing proper tube of size \(k\), the exact support offset is \(2^{k-1}-1\). The monotonicity of \(F(j)=(2^{j-1}-1)/(j(j-1))\) proves all other tube facets lie at least as far away. Equality at a larger tube occurs precisely when \(n=2,k=2\). Symbolic reasoning proves the all-dimensional result; exact rational computations in dimensions 2 through 80 independently corroborate it.

## Originality
FAIL. The separate published mathematical result *Singleton facets determine the inball of every genuine complete-bipartite graph associahedron* proves the coordinatewise nondecreasing density
\[
F(r,s)=\frac{(2^r-1)(2^s-1)}{(r+s)(r+s-1)}\qquad(r,s\ge1)
\]
and uses that lemma to establish an exact sharp singleton-facet inball. Its stated main theorem restricts to \(p,q\ge2\) and expressly excludes stars, so the headline theorem alone cannot be specialized to \(p=1\). However, its proved density lemma applies at \(p=1,q=n\) and yields exactly the star tube comparison and global radius. For \(n\ge3\) all non-singleton facets are strictly inactive. For \(n=2\), its exceptional equality \(F(1,1)=F(1,2)\) gives the two additional tangent facets. The previous statement is therefore mathematically covered by the prior proof's general lemma and standard support formulas, notwithstanding different headline hypotheses.

The earlier partial-permutohedron inradius result concerns a different metric realization and is not used as a false implication. The primary papers on stellohedron facets and star Minkowski sums supply definitions and facet premises rather than an independent exact inradius result.

## Mathematical value
FAIL. The standard stellohedron is a natural object, but this particular all-dimensional invariant and its low-dimensional exception require only the published general density lemma, singleton inball argument and a short substitution. They supply no independent additional structural finding beyond that implication.

## Sources and limits
- Baralić, Ivanović and Petrić, *Chromatic numbers for facet colouring of some generalised associahedra*, arXiv:2311.05901v3, §6 (facet indexing).
- Behrend, *Ehrhart polynomials of partial permutohedra*, arXiv:2403.06975v1, §3(v) (exact standard simplex-sum realization).
- *Singleton facets determine the inball of every genuine complete-bipartite graph associahedron*, publicly available 11 October 2026, equations (7)–(18): https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-singleton-facets-determine-the-inball-of-every-genuine-complete--472aa0e35fff/RESULT.md.
- *Exact Euclidean inradius of partial permutohedra*, public mathematical result dated 4 October 2026: https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-exact-euclidean-inradius-of-partial-permutohedra--df8bf5a2a297/RESULT.md.

The two mathematical records covering the stellohedron and the biclique calculation are each dated 11 October 2026; their order within that day was not established. This assessment concerns implication of mathematical content, not personal priority or authorship. No claim is made about unpublished literature, other Euclidean realizations, a formal proof-assistant certificate or expert attestation.
