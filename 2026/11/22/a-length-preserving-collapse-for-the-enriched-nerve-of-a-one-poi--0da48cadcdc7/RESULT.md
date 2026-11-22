# A length-preserving collapse for the enriched nerve of a one-point metric gluing

## Finding

**Theorem.** Let \((X_i,d_i,o)\), for \(1\le i\le t\) and finite \(t\ge2\), be finite pointed strict quasi-metric spaces, with finite nonnegative (possibly asymmetric) distances, \(d_i(x,x)=0\), \(d_i(x,y)>0\) for distinct points, and the directed triangle inequality. Assume their underlying sets are disjoint except for the common marked point \(o\). Define \(X=\bigvee_oX_i\) with inherited within-summand distances and, for \(x\in X_i\setminus\{o\}\), \(y\in X_j\setminus\{o\}\) and \(i\ne j\),

\[
d_X(x,y)=d_i(x,o)+d_j(o,y).
\]

For each real \(r\ge0\), let \(N_r(Z)\) be the **length-filtered enriched nerve**: its \(q\)-simplices are ordered \((q+1)\)-tuples \((z_0,\ldots,z_q)\) with \(\sum_{k=1}^q d_Z(z_{k-1},z_k)\le r\), and faces and degeneracies delete and repeat entries. Then the canonical simplicial-set inclusion

\[
\bigvee_{i=1}^tN_r(X_i)\ \longrightarrow\ N_r(X)
\]

induces a homotopy equivalence on geometric realizations **at every scale**. More precisely, the normalized CW cells outside the wedge admit an explicit acyclic matching, all matched pairs having **exactly equal total length**. Therefore the inclusion is a natural levelwise homotopy equivalence of the entire persistence simplicial-set filtration. For every commutative coefficient ring \(R\) and every homological degree \(q\ge1\), it induces a natural persistence-module isomorphism

\[
\widetilde H_q(N_\bullet(X);R)\cong
\bigoplus_{i=1}^t\widetilde H_q(N_\bullet(X_i);R).
\]

Positive-degree cohomology classes supported on distinct factors have zero pairwise cup product, and restriction identifies the reduced positive-degree cohomology algebra with the wedge/direct-product algebra of the factors.

## Assumptions and scope

A strict quasi-metric here has finite directed distances and strictly positive off-diagonal distances; symmetry is **not** assumed. The displayed cross-distance is essential: without the condition that every cross-summand distance factors through the marked point, the conclusion can fail. This construction respects triangle inequalities because a path between different summands through \(o\) realizes the stipulated cross-distance, while every other detour has length no shorter by the triangle inequalities in the factors. The boundary is substantive: on three points \(o,a,b\) with symmetric distances \(d(o,a)=d(o,b)=2\) and \(d(a,b)=1\), the scale-one length nerve has an edge from \(a\) to \(b\), whereas the wedge of the two two-point scale-one nerves consists of three isolated vertices. Thus allowing a cross-summand shortcut invalidates even the degree-zero conclusion. The definition uses **simplicial sets of ordered paths**, not ordinary unordered diameter-controlled Vietoris–Rips complexes. The two common persistence conventions, \(\le r\) and \(<r\), both satisfy the theorem, since every matching preserves the exact length.

Every nondegenerate \(q\)-simplex is a tuple with consecutive entries unequal. Since \(X\) is finite and strict, the minimum positive off-diagonal distance \(\delta\) is positive. A nondegenerate simplex in \(N_r(X)\) has \(q\delta\le r\), so every level is a finite-dimensional finite CW realization.

## Proof

**Step 1 (the matching).** Call a nondegenerate tuple *pure* when all its nonbasepoint entries lie in a single factor, and *mixed* otherwise. Its first nonbasepoint entry belongs to a unique factor \(X_a\). For a mixed tuple \(\sigma=(x_0,\ldots,x_q)\), let \(j\) be the first index whose nonbasepoint entry belongs to a factor other than \(X_a\). Such a \(j\) is strictly after the first nonbasepoint index. All nonbasepoint entries preceding \(j\) lie in \(X_a\).

If \(x_{j-1}\ne o\), match \(\sigma\) as the **lower** cell with \(\tau\) obtained by inserting \(o\) immediately before \(x_j\). If \(x_{j-1}=o\), match \(\sigma\) as the **upper** cell with the lower cell obtained by removing this particular \(o\). In the latter case \(x_{j-2}\in X_a\setminus\{o\}\), because the original tuple is nondegenerate and \(j\) is the first factor switch. The resulting tuple is still nondegenerate. These two operations invert one another, so each mixed cell belongs to exactly one pair and pure cells are the only critical cells.

**Step 2 (length and regularity).** At a first switch from \(x\in X_a\setminus\{o\}\) to \(y\in X_b\setminus\{o\}\), \(a\ne b\), the defining cross-distance satisfies

\[
d_X(x,y)=d_X(x,o)+d_X(o,y).
\]

Thus inserting or removing \(o\) at this switch preserves total path length exactly; both cells exist at precisely the same filtration thresholds. Deleting the inserted \(o\) is a regular face with incidence number \(\pm1\) in the normalized CW chain complex. In a nondegenerate tuple, no other face deletion can produce the same lower tuple: deleting a nonbasepoint leaves too many copies of \(o\), and deleting a different basepoint would require two adjacent equal entries for the resulting words to coincide.

**Step 3 (acyclicity).** Orient a matched incidence from lower to upper and all other face incidences from upper to lower. A matched move inserts only a copy of \(o\), preserving the number \(b(\sigma)\) of nonbasepoint entries. Suppose an upper matched cell is followed by an **unmatched** downward face which is a lower matched cell. Deleting a basepoint distinct from the inserted one leaves the first factor switch immediately preceded by the inserted \(o\), so the resulting cell is still an **upper** matched cell. Deleting the inserted basepoint gives the matched downward face, which is excluded. Consequently the unmatched downward face of a matched upper cell that can lead to another matched lower cell must delete a nonbasepoint entry, strictly decreasing \(b\). No closed gradient path exists. There are finitely many cells at every \(r\), so the resulting acyclic partial matching is a legitimate finite discrete-Morse matching. Because all critical cells form the full simplicial-set subcomplex \(\bigvee_iN_r(X_i)\), the geometric realization collapses up to homotopy onto that subcomplex by its matching.

**Step 4 (persistence and products).** The inclusion is literally the same simplicial map at every scale. The length-preserving pairing proves it is a homotopy equivalence at each \(r\), hence naturally identifies all persistence structure maps on homology. The realization of the simplicial-set wedge is a topological wedge because the factors intersect only in the shared vertex \(o\). Reduced homology of finite wedges splits in every positive degree over any coefficient ring; pullback in cohomology preserves cup products. On a wedge, cross-factor products of positive-degree cohomology classes vanish, proving the final assertion.

## Verification

A dependency-free Python checker enumerates the nondegenerate length-filtered nerves and the stated matching. For each test it checks pair involution, equal length, distinct pairs, exact identification of pure critical cells, and acyclicity of the **full directed face-incidence graph**. It also compares direct mod-two homology with the pure wedge subcomplex whenever requested. The checker passed \(76\) complete finite parameter instances and \(2{,}521\) enumerated cells. Cases include asymmetric shortest-path quasi-metrics, three summands, randomized integer-weight quasi-metrics, and two four-cycles joined at one vertex. For the last example, at integer thresholds \(r=1,2,3\) its nonzero positive-degree mod-two Betti ranks are respectively \(\beta_1=10\), \(\beta_2=14\), and \(\beta_3=18\); in each case these are exactly twice the one-cycle ranks. Run `python3 check_glued_nerve.py` to reproduce all listed tests. The computation checks finite instances; the unrestricted assertion follows from the preceding proof, not from extrapolation.

## Relationship to prior work

Bi–Feng–Li–Wu (first publicly posted **7 January 2026**) develops persistence for **fixed-length magnitude homology along isometric inclusions of finite metric spaces**; it does not provide the length-cutoff enriched-nerve wedge theorem proved here. Ivanov–Xu identify length-controlled simplicial sets with blurred magnitude homology and study stability, nerves, completion, and filtered colimits. Their filtered-colimit result does not imply preservation under a finite one-point pushout. Adamaszek et al. prove wedge decompositions for **ordinary unordered diameter-controlled** Vietoris–Rips and Čech complexes, whose simplices and filtration are different. Hepworth–Willerton's magnitude-homology Mayer–Vietoris theory, discussed by Roff, concerns the associated fixed-length homology and does not by itself give a simultaneous levelwise homotopy equivalence of the ordered-path enriched nerves. Livernet–Roff–Whitehouse develop Mayer–Vietoris for pages of the magnitude-path spectral sequence; this is not a realization-level collapse of the entire length-filtered nerve.

The new statement is the **length-preserving matching and levelwise simplicial-set realization homotopy equivalence** for all finite strict directed metric wedges, not the already-known ordinary Vietoris–Rips wedge theorem or the graded magnitude-homology decomposition.

## Limitations

The proof assumes finite positive off-diagonal distances, finitely many summands, and exact directed factorization of all cross distances through the common basepoint. It does **not** extend automatically to non-strict pseudometrics, infinite graphs, nontrivial overlap subspaces, or metrics with shortcuts across different factors. It does not claim a pointwise simplicial retraction or a canonical choice of inverse compatible with every parameter; naturality is supplied by the inclusion maps, which are levelwise equivalences. Historical priority cannot be guaranteed against unindexed equivalent gluing results; independent mathematical audit has not been performed.

## References

- W. Bi, H. Feng, J. Li, J. Wu, *Persistent magnitude homology on finite metric spaces*, arXiv:2601.03685v1 (7 January 2026), https://arxiv.org/html/2601.03685v1.
- S. O. Ivanov, X. Xu, *On \(\ell_p\)-Vietoris–Rips complexes*, arXiv:2411.01857v1 (4 November 2024); open-access publication https://link.springer.com/article/10.1007/s41468-026-00247-x.
- M. Adamaszek et al., *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI 10.4230/LIPIcs.SoCG.2018.3; https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2018.3.
- E. Roff, *Magnitude, homology, and the Whitney twist*, arXiv:2211.02520v1, https://arxiv.org/abs/2211.02520.
- M. Livernet, E. Roff, S. Whitehouse, *Homotopy theories via the magnitude-path spectral sequence*, arXiv:2606.09747v1 (8 June 2026), https://arxiv.org/html/2606.09747v1.
