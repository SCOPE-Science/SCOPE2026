# Complete shattering profiles for cyclic king neighborhoods

## Finding
Let \(m,n\ge3\) and let \(G_{m,n}\) be the king graph on the finite torus \(\mathbb Z_m\times\mathbb Z_n\): two distinct vertices are adjacent if their cyclic distance is at most one in each coordinate. Let \(\mathcal K_{m,n}\) be the family of **closed vertex neighborhoods** of \(G_{m,n}\). A support is shattered if every Boolean membership assignment on its vertices is the trace of some member of \(\mathcal K_{m,n}\). Define \(\Phi_{m,n}(z)=\sum_{S\text{ shattered}}z^{|S|}\), and write \(a=\min\{m,n\}\), \(b=\max\{m,n\}\). Then the **complete, all-parameter polynomial** is
\[
\boxed{\Phi_{m,n}(z)=\begin{cases}
1,&a=b=3,\\
1+12z,&a=3,\ b=4,\\
1+15z+45z^2,&a=3,\ b=5,\\
1+3bz+18bz^2,&a=3,\ b\ge6,\\
1+16z+120z^2+288z^3,&a=b=4,\\
1+4bz+38bz^2+84bz^3,&a=4,\ b\ge5,\\
1+mnz+12mnz^2+12mnz^3,&m,n\ge5.
\end{cases}}
\]
In particular, \(\operatorname{VCdim}(\mathcal K_{m,n})\) is zero on the \(3\times3\) torus, one on \(3\times4\), two on \(3\times b\) for \(b\ge5\), and three when both side lengths are at least four.

On every torus with \(m,n\ge5\), all shattered triples are precisely the translates and coordinate-dihedral images of the following three local patterns:
\[
\{(0,0),(0,2),(1,1)\},\quad
\{(0,0),(0,2),(2,1)\},\quad
\{(0,1),(1,0),(2,2)\}.
\]
Their distinct translates form twelve full translation orbits. Moreover, precisely \(4mn\) shattered pairs are **inclusion-maximal** rather than lying in a shattered triple. Their translated difference classes are the two axial classes \((1,0),(0,1)\) and the two diagonal classes \((2,2),(2,-2)\), up to sign of the whole difference. Consequently the shattered-support simplicial complex is nonpure for all \(m,n\ge5\), having \(4mn\) maximal two-element faces and \(12mn\) maximal three-element faces.

## Assumptions and scope
Coordinates are residues, with all arithmetic modulo the respective side length. The cyclic distance in \(\mathbb Z_3\) is one for every distinct pair. The center is **included** in its own closed neighborhood; the neighborhood at \((u,v)\) is exactly
\[
B_{u,v}=\{u-1,u,u+1\}\times\{v-1,v,v+1\}.
\]
No empty or universal hypotheses are artificially adjoined; for \(3\times3\), every member of the actual concept family is universal. Supports are sets of distinct actual vertices, not unlabeled shape classes. The empty support is shattered by convention and contributes the constant term one. The result concerns ordinary static VC shattering of the actual finite neighborhood family, not the graph's Lovász neighborhood complex, online dimensions or all cyclic rectangles of arbitrary widths.

## Proof
**1. Finite-template reduction.** Shattering of a nonempty support \(S\) requires realization of its all-one trace. Thus \(S\subseteq B_{u,v}\) for some center, and translating the torus puts it inside \(W=\{0,1,2\}^2\). There are exactly \(2^9=512\) subsets of this template, including the empty set. For any \(S\subseteq W\), identify the nine template positions by bits and compute all trace masks \(B_{u,v}\cap S\). The explicit standard-library program `VERIFY.py` enumerates the 512 templates and all actual translates, without sampling. A template is shattered precisely when the collection of masks has cardinality \(2^{|S|}\). This is an exact decision test, not a necessary-condition heuristic.

**2. Why the finite certificate applies to *all* periods.** On the one-dimensional three-position window \(I=\{0,1,2\}\), the distinct intersections with a translated cyclic three-position window are exactly:

- when the period is three: \(\{0,1,2\}\);
- when the period is four: \(\{0,1,2\},\{0,1\},\{1,2\},\{0,2\}\);
- when the period is at least five, ignoring possible empty intersections: \(\{0,1,2\},\{0,1\},\{1,2\},\{0\},\{2\}\).

For period five every center has a nonempty overlap; for greater periods additional centers may contribute an empty overlap, but no new nonempty overlap. Each two-dimensional trace mask on \(S\) is obtained by intersecting \(S\) with one overlap from each coordinate, so the **collection of nonempty trace masks is invariant** throughout any of the regimes \((3,b\ge6)\), \((4,b\ge5)\), and \((m,n\ge5)\), when comparing the same anchored template \(S\). The only possible change would be acquisition of the empty trace. The checker independently exhausts all 512 anchored templates for the boundary representatives \((3,6),(4,5),(5,5)\) and finds **no nonempty template for which all nonempty Boolean traces occur but the empty trace is missing**. Hence no new shattered template can arise by acquiring an empty trace, even after a period grows without bound. This proves rigorously that the finite template census determines shattering throughout each infinite parameter regime. The exceptional dimensions \((3,3),(3,4),(3,5),(4,4)\) are tested directly.

**3. Exact counts by translation orbits.** The checker builds all candidate supports from every translated three-by-three window, tests their traces against the actual neighborhood family, and constructs each complete translation orbit (deduplicating repeated supports). The exhaustive base-case orbit tables are:

| Grid | Counts by support size, starting at size zero | Translation orbit sizes and multiplicities for nonempty supports |
|---|---|---|
| \(3\times3\) | \((1)\) | none |
| \(3\times4\) | \((1,12)\) | one size-12 singleton orbit |
| \(3\times5\) | \((1,15,45)\) | one size-15 singleton orbit; three size-15 pair orbits |
| \(3\times6\) | \((1,18,108)\) | one size-18 singleton orbit; six size-18 pair orbits |
| \(4\times4\) | \((1,16,120,288)\) | one size-16 singleton orbit; three size-8 and six size-16 pair orbits; eighteen size-16 triple orbits |
| \(4\times5\) | \((1,20,190,420)\) | one size-20 singleton orbit; one size-10 and nine size-20 pair orbits; twenty-one size-20 triple orbits |
| \(5\times5\) | \((1,25,300,300)\) | one size-25 singleton orbit; twelve size-25 pair orbits; twelve size-25 triple orbits |

The exceptional short-period orbit stabilizers are completely accounted for: on the \(4\times b\) tori a pair of vertices in one column at opposite rows has an order-two translation stabilizer, yielding the unique half-sized pair orbit. No shattered triple on the listed stable regimes admits a nonidentity translational stabilizer. In the long-period regimes, every selected support sits inside three consecutive positions of each coordinate; any nontrivial translational stabilizer of a two- or three-point support would require an order-two antipodal pair or an order-three evenly spaced triple. Such a support cannot fit inside three consecutive positions if that coordinate period is at least five. If one coordinate period is four, the antipodal-pair exception is exactly the one tabulated. Period three is separately treated; there are no shattered triples in that regime. The local relative patterns, hence their orbit multiplicities, cannot change as a period grows, by step 2. Multiplying the stable numbers of orbits by their orbit sizes gives the piecewise polynomial exactly.

**4. Stable-range face structure.** On the \(7\times7\) representative, the checker forms the union of translations and all eight planar dihedral images of each of the three displayed motifs. This union consists of exactly \(12\cdot49=588\) distinct triples and agrees *setwise* with the exhaustive shattered triple set. Because each template and its rotation/reflection lies inside a three-by-three window and the overlap-profile argument of step 2 preserves its shattering status on every larger torus, these are all shattered triples for \(m,n\ge5\). The remaining shattered pairs on \(7\times7\) not contained in any such triple are precisely the four stated translation-difference classes, giving \(4\cdot49=196\) maximal pairs. Both the pair-membership test and local motif characterization depend only on the same three-by-three overlap types and cannot change for periods at least five; the four full orbits therefore give \(4mn\) maximal pairs universally. Every shattered triple is maximal, since the local census has no shattered four-element support. This proves the nonpurity statement.

## Verification
Run `python3 VERIFY.py` with Python 3 and its standard library only. The program exhaustively computes support traces and translation-orbit sizes for seven base grids, compares **all 512 anchored templates** across seven representative enlargement pairs, excludes the unique possible empty-trace obstruction at three boundary representatives, tests the exact dihedral triple motif classification and maximal pairs at \(7\times7\), and cross-checks nine additional torus sizes from \(3\times7\) to \(7\times7\). The recorded final marker is `ALL_CYCLIC_KING_SHATTERING_CHECKS_PASS`. No large random search or external library is needed. The finite computation is part of a proof by exhaustive finite reduction justified in step 2; without that reduction, a collection of finite observations would not imply the theorem.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1] analyze VC-dimension bounds and densities for open neighborhood systems of Johnson and Hamming graphs, but Cartesian products of complete graphs and open neighborhoods are not the cyclic king strong products with inclusive three-by-three neighborhoods used here. Gillibert, Lachmann and Müllner [2] analyze axis-parallel boxes on the continuous torus; their factors have variable cyclic-interval lengths, rather than the fixed three-position windows and discrete translations here. Coudert and collaborators [3] study algorithms for computing closed-neighborhood VC dimensions on graphs, not an exact two-parameter shattering polynomial for this family.

The published finite-cyclic-rectangle classification [4] concerns **all** cyclic intervals on each factor; its unrestricted VC dimensions can reach six, and its result explicitly does not count shattered supports. The published exact cycle-ball counting result [5] uses one-dimensional graph balls with radii ranging from zero to a cutoff, not products of radius-one windows. The published rook-graph neighborhood census [6] concerns the Cartesian rook graph rather than the king strong product. Neither the published statements nor inspected relevant proofs imply this fixed-width, two-dimensional parameter classification. In the small \(4\times4\) case, numerical polynomial coincidences with other graph families are not asserted to be new. The assessed contribution is the full cyclic-king family classification and its stable-range facet structure.

## Limitations
The theorem applies only to closed vertex neighborhoods of undirected cyclic king graphs with both side lengths at least three and graph distances measured separately in each coordinate for the king move. It does not determine online dimensions, more general radii or arbitrary rectangular windows. The all-parameter proof uses a deterministic 512-template computational certificate, not an independent formal proof assistant. Historical originality remains qualified because an equivalent profile might appear in unindexed literature under fixed-size toroidal box, translated-shape or Moore-neighborhood terminology. Independent mathematical validation has not been performed.

## References
1. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1 (first public 2020-07-31), https://arxiv.org/abs/2007.16042.
2. P. Gillibert, T. Lachmann and C. Müllner, *The VC-Dimension of Axis-Parallel Boxes on the Torus*, arXiv:2004.13861v1 (first public 2020-04-28), https://arxiv.org/abs/2004.13861.
3. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1 (first public 2024-05-13), https://arxiv.org/abs/2405.07588.
4. *Exact VC dimensions of finite cyclic rectangles on two-dimensional tori*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-vc-dimensions-of-finite-cyclic-rectangles-on-two-dimension--810fee39077c.
5. *Radius-filtered graph balls on cycles: exact shattering polynomials and a two-phase density law*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-radius-filtered-graph-balls-on-cycles-exact-shattering-polynomia--da8d9213216f.
6. *Exact open-neighborhood shattering polynomials of rectangular rook graphs*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-open-neighborhood-shattering-polynomials-of-rectangular-ro--ffaa2f7a2b1d.
