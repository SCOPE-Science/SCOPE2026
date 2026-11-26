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

induces a homotopy equivalence on geometric realizations **at every scale**. More precisely, the nondegenerate CW cells outside the wedge admit an explicit acyclic matching, all matched pairs having **exactly equal total length**. The matched pairs can be removed by relative collapses: for each finite cutoff the resulting strong deformation retraction preserves every lower sublevel and fixes the wedge. In particular, the inclusion is a natural levelwise homotopy equivalence of the entire persistence simplicial-set filtration. For every commutative coefficient ring \(R\) and every homological degree \(q\ge1\), it induces a natural persistence-module isomorphism

\[
\widetilde H_q(N_\bullet(X);R)\cong
\bigoplus_{i=1}^t\widetilde H_q(N_\bullet(X_i);R).
\]

Positive-degree cohomology classes supported on distinct factors have zero pairwise cup product, and restriction identifies the reduced positive-degree cohomology algebra with the wedge/direct-product algebra of the factors.

## Assumptions and scope

A strict quasi-metric here has finite directed distances and strictly positive off-diagonal distances; symmetry is **not** assumed. The displayed cross-distance is essential: without the condition that every cross-summand distance factors through the marked point, the conclusion can fail. This construction respects triangle inequalities because a path between different summands through \(o\) realizes the stipulated cross-distance, while every other detour has length no shorter by the triangle inequalities in the factors. The boundary is substantive: on three points \(o,a,b\) with symmetric distances \(d(o,a)=d(o,b)=2\) and \(d(a,b)=1\), the scale-one length nerve has an edge from \(a\) to \(b\), whereas the wedge of the two two-point scale-one nerves consists of three isolated vertices. Thus allowing a cross-summand shortcut invalidates even the degree-zero conclusion. The definition uses **simplicial sets of ordered paths**, not ordinary unordered diameter-controlled Vietoris–Rips complexes. The same result holds under the strict convention \(<r\) for positive cutoffs \(r\), since every matching preserves the exact length. At strict cutoff zero the sublevel is empty and is not regarded as a pointed nerve.

If \(X=\{o\}\), the inclusion is the identity. Otherwise every nondegenerate \(q\)-simplex is a tuple with consecutive entries unequal and the finite space has a positive minimum off-diagonal distance \(\delta\). A nondegenerate simplex in \(N_r(X)\) has \(q\delta\le r\), so every level has a finite CW realization.

## Proof

**Step 1 (the matching).** Call a nondegenerate tuple *pure* when all its nonbasepoint entries lie in a single factor, and *mixed* otherwise. Its first nonbasepoint entry belongs to a unique factor \(X_a\). For a mixed tuple \(\sigma=(x_0,\ldots,x_q)\), let \(j\) be the first index whose nonbasepoint entry belongs to a factor other than \(X_a\). Such a \(j\) is strictly after the first nonbasepoint index. All nonbasepoint entries preceding \(j\) lie in \(X_a\).

If \(x_{j-1}\ne o\), match \(\sigma\) as the **lower** cell with \(\tau\) obtained by inserting \(o\) immediately before \(x_j\). If \(x_{j-1}=o\), match \(\sigma\) as the **upper** cell with the lower cell obtained by removing this particular \(o\). In the latter case \(x_{j-2}\in X_a\setminus\{o\}\), because the original tuple is nondegenerate and \(j\) is the first factor switch. The resulting tuple is still nondegenerate. These two operations invert one another, so each mixed cell belongs to exactly one pair and pure cells are the only critical cells.

**Step 2 (length and unique facet).** At a first switch from \(x\in X_a\setminus\{o\}\) to \(y\in X_b\setminus\{o\}\), \(a\ne b\), the defining cross-distance satisfies

\[
d_X(x,y)=d_X(x,o)+d_X(o,y).
\]

Thus inserting or removing \(o\) at this switch preserves total path length exactly; both cells exist at precisely the same filtration thresholds. The interior of the facet obtained by deleting the inserted \(o\) maps homeomorphically to the open lower cell, giving incidence number \(\pm1\) in the normalized CW chain complex. No other facet reaches that open cell: a degenerate facet has lower-dimensional image, deleting a nonbasepoint leaves too many copies of \(o\), and deleting a different basepoint would require adjacent equal entries for the resulting words to coincide. The lower cell itself need not have an embedded closed characteristic simplex.

**Step 3 (acyclicity and actual removal).** Orient a matched incidence from lower to upper and all other face incidences from upper to lower. A cycle would have to alternate between matched upward moves and codimension-one unmatched downward moves: there cannot be consecutive upward moves, each upward move increases dimension by one, and each downward move decreases dimension by at least one. A matched move inserts only a copy of \(o\), preserving the number \(b(\sigma)\) of nonbasepoint entries. Suppose an upper matched cell is followed by an **unmatched** downward face which is a lower matched cell. Deleting a basepoint distinct from the inserted one leaves the first factor switch immediately preceded by the inserted \(o\), so if the result is nondegenerate it is still an **upper** matched cell. Deleting the inserted basepoint gives the matched face, which is excluded. Consequently such an unmatched codimension-one descent must delete a nonbasepoint entry, strictly decreasing \(b\). No closed gradient path exists.

For an explicit relative collapse, at a fixed finite cutoff choose a remaining matched pair \((\sigma,\tau)\) with \((\dim\tau,b(\tau))\) lexicographically maximal. Pure cells cannot have a mixed face. All other remaining mixed cells have dimension at most \(\dim\tau\), so \(\tau\) has no coface and any other coface of \(\sigma\) would be a matched upper cell of the same dimension as \(\tau\). Its descent to \(\sigma\) would be unmatched and strictly decrease \(b\), implying that this other coface had larger \(b\) than \(\tau\). Thus \(\sigma\) is a free facet and is hit by just one facet of the characteristic simplex of \(\tau\), as in Step 2. In the standard simplex, take the elementary deformation retract onto the union of all facets other than this free facet, fixing that union pointwise. In the realization it descends relative to all retained cells: the only removed open cells are \(\tau\) and the free facet \(\sigma\), each parametrized injectively in its interior, and every boundary identification that remains lies in the fixed union of facets. This argument permits repeated nonconsecutive vertices and degenerate faces without applying a regular-CW theorem to a nonregular CW complex.

Continue for the finitely many pairs. At any lower cutoff, a removal fixes that sublevel pointwise if the pair lies above it; otherwise the sublevel contains the entire closed pair by the triangle inequality, and the removal maps the sublevel to itself. Thus the concatenated deformation fixes the pure wedge and preserves every lower sublevel. The remaining simplicial subset is precisely \(\bigvee_iN_r(X_i)\).

**Step 4 (persistence and products).** The inclusion is literally the same simplicial map at every scale. The length-preserving pairing proves it is a homotopy equivalence at each \(r\), hence naturally identifies all persistence structure maps on homology. The realization of the simplicial-set wedge is a topological wedge because the factors intersect only in the shared vertex \(o\). Reduced homology of finite wedges splits in every positive degree over any coefficient ring; pullback in cohomology preserves cup products. On a wedge, cross-factor products of positive-degree cohomology classes vanish, proving the final assertion.

## Verification

A dependency-free Python checker enumerates the nondegenerate length-filtered nerves and the stated matching. For each test it checks pair involution, equal length, distinct pairs, exact identification of pure critical cells, and acyclicity of the directed nondegenerate codimension-one face graph. It also compares direct mod-two homology with the pure wedge subcomplex whenever requested. The accompanying output records \(76\) complete finite parameter instances and \(2{,}521\) enumerated cells. Cases include asymmetric shortest-path quasi-metrics, three summands, randomized integer-weight quasi-metrics, and two four-cycles joined at one vertex. For the last example, at integer thresholds \(r=1,2,3\) its nonzero positive-degree mod-two Betti ranks are respectively \(\beta_1=10\), \(\beta_2=14\), and \(\beta_3=18\); in each case these are exactly twice the corresponding ranks for one four-cycle. Run `python3 check_glued_nerve.py` to reproduce all listed tests. The computation checks finite instances; the general collapse and its preservation of sublevels follow from the preceding proof, not from extrapolation.

## Relationship to prior work

Bi–Feng–Li–Wu (first publicly posted **7 January 2026**) develops persistence for **fixed-length magnitude homology along isometric inclusions of finite metric spaces**; it does not provide the length-cutoff enriched-nerve wedge theorem proved here. Ivanov–Xu identify length-controlled simplicial sets with blurred magnitude homology and study stability, nerves, completion, and filtered colimits. Their filtered-colimit result does not imply preservation under a finite one-point pushout. Adamaszek et al. prove wedge decompositions for **ordinary unordered diameter-controlled** Vietoris–Rips and Čech complexes, whose simplices and filtration are different. Hepworth–Willerton's magnitude-homology Mayer–Vietoris theory, discussed by Roff, concerns the associated fixed-length homology and does not by itself give a simultaneous levelwise homotopy equivalence of the ordered-path enriched nerves. Livernet–Roff–Whitehouse develop Mayer–Vietoris for pages of the magnitude-path spectral sequence; this is not a realization-level collapse of the entire length-filtered nerve.

More closely, Tajima–Yoshinaga's projecting matching (Definition 5.8, Proposition 5.9) inserts or removes gate points in a causal order complex, with a fixed-length magnitude-homotopy gluing theorem (Theorem 5.14 and Corollary 5.16). For symmetric two-factor point gluings, the gate insertion or deletion is the same combinatorial mechanism on the fixed-length paths. This is not a new gate-matching idea. Their statement concerns a quotient that collapses shorter-length data. The all-cutoff realization statement needs the matching on the non-quotiented ordered simplicial set, where shorter faces and nonregular cell closures must be handled. Similarly, the symmetric finite-space integral homology wedge splitting alone can be recovered by applying fixed-length magnitude excision (Hepworth–Willerton for graphs, Bottinelli–Kaiser for metrics) on each associated graded piece and using the long exact sequences through the finitely many lengths below each cutoff. This argument does not itself furnish the relative realization collapses and does not supply the directed case.

The contribution is the **relative realization collapse preserving all sublevels of each bounded filtration**, directly for finite strict directed one-point gluings. The homology and cup-product statements are consequences, rather than claims of independent priority.

## Limitations

The proof assumes finite positive off-diagonal distances, finitely many summands, and exact directed factorization of all cross distances through the common basepoint. It does **not** extend automatically to non-strict pseudometrics, infinite graphs, nontrivial overlap subspaces, or metrics with shortcuts across different factors. The relative deformation is on realizations, not a simplicial retraction; the theorem does not specify a canonical choice of inverse on the entire unbounded filtration. The priority comparison is limited to inspected works.

## References

- W. Bi, H. Feng, J. Li, J. Wu, *Persistent magnitude homology on finite metric spaces*, arXiv:2601.03685v1 (7 January 2026), https://arxiv.org/html/2601.03685v1.
- S. O. Ivanov, X. Xu, *On \(\ell_p\)-Vietoris–Rips complexes*, arXiv:2411.01857v1 (4 November 2024); open-access publication https://link.springer.com/article/10.1007/s41468-026-00247-x.
- M. Adamaszek et al., *Vietoris–Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI 10.4230/LIPIcs.SoCG.2018.3; https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2018.3.
- E. Roff, *Magnitude, homology, and the Whitney twist*, arXiv:2211.02520v1, https://arxiv.org/abs/2211.02520.
- M. Livernet, E. Roff, S. Whitehouse, *Homotopy theories via the magnitude-path spectral sequence*, arXiv:2606.09747v1 (8 June 2026), https://arxiv.org/html/2606.09747v1.
- R. Hepworth and S. Willerton, *Categorifying the magnitude of a graph*, arXiv:1505.04125, §6 and §8–9, https://arxiv.org/abs/1505.04125.
- R. Bottinelli and T. Kaiser, *Magnitude homology, diagonality, and median spaces*, §4.2, https://intlpress.com/site/pub/files/_fulltext/journals/hha/2021/0023/0002/HHA-2021-0023-0002-a007.pdf.
- Y. Tajima and M. Yoshinaga, *Causal Order Complex and Magnitude Homotopy Type of Metric Spaces*, arXiv:2302.09752, §5.2–5.3, https://arxiv.org/abs/2302.09752.
